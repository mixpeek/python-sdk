"""Production test runner for deployed plugins."""

import asyncio
import os
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

import httpx


class ProductionTestRunner:
    """Test runner for deployed plugins via production API.

    This runner tests plugins that have been deployed to Mixpeek by submitting
    real batch extraction requests and verifying the results.

    Example:
        ```python
        runner = ProductionTestRunner(
            plugin_path=Path("./my_plugin"),
            namespace_id="ns_xxx",
            api_key="pk_xxx",
            api_url="https://api.mixpeek.com",
        )

        # Test batch extraction
        results = await runner.test_batch([
            {"text": "Sample input 1"},
            {"text": "Sample input 2"},
        ])
        ```
    """

    def __init__(
        self,
        plugin_path: Path,
        namespace_id: Optional[str] = None,
        api_key: Optional[str] = None,
        api_url: str = "https://api.mixpeek.com",
    ):
        """Initialize production test runner.

        Args:
            plugin_path: Path to plugin directory (to load manifest)
            namespace_id: Mixpeek namespace ID (or set MIXPEEK_NAMESPACE_ID)
            api_key: Mixpeek API key (or set MIXPEEK_API_KEY)
            api_url: API base URL (default: https://api.mixpeek.com)
        """
        self.plugin_path = plugin_path
        self.namespace_id = namespace_id or os.environ.get("MIXPEEK_NAMESPACE_ID")
        self.api_key = api_key or os.environ.get("MIXPEEK_API_KEY")
        self.api_url = api_url

        # Validate credentials
        if not self.namespace_id:
            raise ValueError(
                "Namespace ID is required for production testing.\n\n"
                "Provide via:\n"
                "  --namespace-id=ns_xxx\n"
                "  OR set MIXPEEK_NAMESPACE_ID environment variable"
            )

        if not self.api_key:
            raise ValueError(
                "API key is required for production testing.\n\n"
                "Provide via:\n"
                "  --api-key=pk_xxx\n"
                "  OR set MIXPEEK_API_KEY environment variable"
            )

        # Load manifest from plugin directory
        self.manifest = self._load_manifest()
        self.plugin_id = f"{self.manifest['feature_extractor_name']}_{self.manifest['version'].replace('.', '_')}"
        self.feature_uri = f"mixpeek://{self.manifest['feature_extractor_name']}@{self.manifest['version']}"

    def _load_manifest(self) -> Dict[str, Any]:
        """Load plugin manifest from file."""
        import importlib.util
        import sys

        manifest_file = self.plugin_path / "manifest.py"

        if not manifest_file.exists():
            raise FileNotFoundError(
                f"manifest.py not found in {self.plugin_path}\n\n"
                "A plugin requires a manifest.py file with metadata."
            )

        spec = importlib.util.spec_from_file_location("manifest", manifest_file)
        if spec is None or spec.loader is None:
            raise ImportError(f"Failed to load manifest from {manifest_file}")

        manifest_module = importlib.util.module_from_spec(spec)
        sys.modules["manifest"] = manifest_module
        spec.loader.exec_module(manifest_module)

        return {
            "feature_extractor_name": manifest_module.feature_extractor_name,
            "version": manifest_module.version,
            "description": manifest_module.description,
            "features": manifest_module.features,
            "output_schema": manifest_module.output_schema,
            "input_mappings": manifest_module.input_mappings,
        }

    async def test_batch(
        self,
        input_data: List[Dict[str, Any]],
        parameters: Optional[Dict[str, Any]] = None,
    ) -> List[Dict[str, Any]]:
        """Test batch processing via production API.

        This submits a batch extraction request to the deployed plugin and
        returns the results.

        Args:
            input_data: List of input items to process
            parameters: Optional extraction parameters

        Returns:
            List of processed results

        Raises:
            httpx.HTTPStatusError: If API request fails
        """
        async with httpx.AsyncClient(timeout=60.0) as client:
            # Step 1: Submit batch extraction request
            extract_url = f"{self.api_url}/v1/namespaces/{self.namespace_id}/extract"
            headers = {"Authorization": f"Bearer {self.api_key}"}

            request_body = {
                "collection_id": f"test_collection_{int(time.time())}",
                "feature_uri": self.feature_uri,
                "data": input_data,
                "parameters": parameters or {},
            }

            response = await client.post(
                extract_url,
                json=request_body,
                headers=headers,
            )
            response.raise_for_status()

            extract_result = response.json()

            # For sync extraction, results are returned immediately
            if "results" in extract_result:
                return extract_result["results"]

            # For async extraction, we need to poll
            if "task_id" in extract_result:
                task_id = extract_result["task_id"]

                # Poll for completion
                status_url = f"{self.api_url}/v1/tasks/{task_id}"

                max_retries = 60  # 60 * 5s = 5 minutes max
                retry_delay = 5  # seconds

                for attempt in range(max_retries):
                    await asyncio.sleep(retry_delay)

                    status_response = await client.get(status_url, headers=headers)
                    status_response.raise_for_status()
                    status_data = status_response.json()

                    if status_data["status"] == "completed":
                        return status_data["results"]

                    if status_data["status"] == "failed":
                        raise Exception(
                            f"Batch extraction failed: {status_data.get('error', 'Unknown error')}"
                        )

                raise TimeoutError(
                    f"Batch extraction timed out after {max_retries * retry_delay} seconds"
                )

            # Fallback: return empty list if no results
            return []

    async def test_realtime(
        self,
        input_data: Dict[str, Any],
        parameters: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Test realtime inference via production API.

        This calls the deployed plugin's realtime endpoint and returns the result.

        Args:
            input_data: Single input item to process
            parameters: Optional inference parameters

        Returns:
            Inference result

        Raises:
            httpx.HTTPStatusError: If API request fails
        """
        async with httpx.AsyncClient(timeout=30.0) as client:
            # Realtime inference endpoint
            inference_url = (
                f"{self.api_url}/v1/inference/custom/"
                f"{self.manifest['feature_extractor_name']}"
            )
            headers = {"Authorization": f"Bearer {self.api_key}"}

            request_body = {
                "inputs": input_data,
                "parameters": parameters or {},
            }

            response = await client.post(
                inference_url,
                json=request_body,
                headers=headers,
            )
            response.raise_for_status()

            return response.json()

    async def verify_deployment(self) -> Dict[str, Any]:
        """Verify the plugin is deployed and accessible.

        Returns:
            Deployment status information

        Raises:
            httpx.HTTPStatusError: If plugin is not deployed
        """
        async with httpx.AsyncClient(timeout=30.0) as client:
            status_url = (
                f"{self.api_url}/v1/namespaces/{self.namespace_id}"
                f"/plugins/{self.plugin_id}/status"
            )
            headers = {"Authorization": f"Bearer {self.api_key}"}

            response = await client.get(status_url, headers=headers)
            response.raise_for_status()

            return response.json()
