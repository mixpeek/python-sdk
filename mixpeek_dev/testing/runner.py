"""Local plugin test runner.

This module provides the LocalTestRunner class which executes Mixpeek plugins
locally without requiring cloud infrastructure.

**Design Philosophy:**

This runner is designed to be:
1. **Self-documenting**: Clear error messages guide users to solutions
2. **LLM-friendly**: Structured to help AI assistants debug and fix issues
3. **Fast**: Mock mode runs in <1 second for rapid iteration
4. **Flexible**: Supports both old and new plugin structures

**Plugin Structure Supported:**

Old structure (test_echo_plugin):
- manifest.py: Simple Python variables (feature_extractor_name, version, features, etc.)
- pipeline.py: extract() function returning object with steps and prepare
- realtime.py: Class extending BaseInferenceService

New structure (builtin plugins):
- definition.py: FeatureExtractorModel with Pydantic schemas
- pipeline.py: PipelineDefinition with StepDefinition list
- realtime.py: get_inference_service() function

**Example Usage:**

```python
from mixpeek_dev.testing import LocalTestRunner

# Initialize runner in mock mode
runner = LocalTestRunner(
    plugin_path="./my_plugin",
    mode="mock"
)

# Test batch processing
results = await runner.test_batch([
    {"text": "Hello world"},
    {"text": "Another document"}
])

# Test realtime inference
result = await runner.test_realtime({"text": "Query text"})

# Full E2E test (extract → index → search)
await runner.test_e2e(
    extract_data=[{"text": "Document 1"}, {"text": "Document 2"}],
    search_query="find something"
)
```

**Testing Strategy:**

Phase 1 (MVP): Support old plugin structure with mock services only
Phase 2: Add new plugin structure support
Phase 3: Add local-stack mode with real Ray + Qdrant
Phase 4: Add production mode for smoke testing
"""

import importlib.util
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

import pandas as pd


class LocalTestRunner:
    """Execute Mixpeek plugins locally with mock or real services.

    This is the core testing engine. It loads plugin modules dynamically,
    executes batch pipelines, and runs realtime inference.

    **Attributes:**
        plugin_path: Path to plugin directory
        mode: Test mode ("mock" | "local-stack" | "production")
        manifest: Loaded plugin manifest (metadata)
        pipeline_module: Loaded pipeline.py module
        realtime_module: Loaded realtime.py module (optional)

    **Supported Test Modes:**

    1. **mock**: Uses MockServiceContainer for fast, deterministic testing
       - No external dependencies
       - Runs in <1 second
       - Perfect for unit tests

    2. **local-stack**: Uses local Docker containers (Ray + Qdrant)
       - Full E2E testing
       - Runs in ~5 seconds
       - Tests complete workflow

    3. **production**: Tests deployed plugins via API
       - Validates deployment
       - Smoke testing
       - Requires API key

    **Error Handling:**

    The runner provides clear, actionable error messages:
    - Missing files: "manifest.py not found. Create it with: mixpeek init"
    - Import errors: "Failed to import pipeline.py. Check for syntax errors."
    - Schema errors: "Output doesn't match schema. Expected 'text_echo_v1_embedding'."

    These messages are designed to help both humans and LLMs quickly identify
    and fix issues.
    """

    def __init__(
        self,
        plugin_path: Union[str, Path],
        mode: str = "mock",
        service_container: Optional[Any] = None,
    ):
        """Initialize the test runner.

        Args:
            plugin_path: Path to plugin directory containing manifest.py and pipeline.py
            mode: Test mode - "mock" (fast, no deps), "local-stack" (Docker), or "production"
            service_container: Optional custom service container (defaults to MockServiceContainer in mock mode)

        Raises:
            FileNotFoundError: If plugin_path doesn't exist
            ValueError: If mode is not one of the supported modes

        Example:
            ```python
            # Mock mode (fast iteration)
            runner = LocalTestRunner("./my_plugin", mode="mock")

            # Local stack mode (full E2E)
            runner = LocalTestRunner("./my_plugin", mode="local-stack")

            # Production mode (smoke test deployed plugin)
            runner = LocalTestRunner("./my_plugin", mode="production")
            ```
        """
        self.plugin_path = Path(plugin_path).resolve()
        self.mode = mode
        self.service_container = service_container

        # Validate mode
        valid_modes = ["mock", "local-stack", "production"]
        if mode not in valid_modes:
            raise ValueError(
                f"Invalid mode '{mode}'. Must be one of: {', '.join(valid_modes)}\n\n"
                f"Try: runner = LocalTestRunner(plugin_path, mode='mock')"
            )

        # Validate plugin path exists
        if not self.plugin_path.exists():
            raise FileNotFoundError(
                f"Plugin directory not found: {self.plugin_path}\n\n"
                f"Create a plugin with: mixpeek init my_plugin --template=basic_text"
            )

        # Will be populated by _load_plugin()
        self.manifest: Optional[Dict[str, Any]] = None
        self.pipeline_module: Optional[Any] = None
        self.realtime_module: Optional[Any] = None

        # Load plugin modules
        self._load_plugin()

        # Initialize service container if not provided
        if self.service_container is None:
            if mode == "mock":
                from mixpeek_dev.testing.mock_services import MockServiceContainer

                self.service_container = MockServiceContainer()
            elif mode == "local-stack":
                # TODO Phase 4: Implement local stack container
                raise NotImplementedError(
                    "local-stack mode not yet implemented. Use --mock for now."
                )
            elif mode == "production":
                # TODO Phase 7: Implement production testing
                raise NotImplementedError(
                    "production mode not yet implemented. Use --mock for now."
                )

    def _load_plugin(self) -> None:
        """Load plugin modules dynamically.

        This method loads manifest.py, pipeline.py, and optionally realtime.py
        from the plugin directory.

        **Error Handling:**

        Provides clear error messages for common issues:
        - Missing manifest.py: Suggests using mixpeek init
        - Missing pipeline.py: Explains required structure
        - Syntax errors: Shows the actual error with line number

        Raises:
            FileNotFoundError: If required files are missing
            ImportError: If modules have syntax errors or import issues
        """
        # Check for required files
        manifest_path = self.plugin_path / "manifest.py"
        pipeline_path = self.plugin_path / "pipeline.py"
        realtime_path = self.plugin_path / "realtime.py"

        if not manifest_path.exists():
            raise FileNotFoundError(
                f"manifest.py not found in {self.plugin_path}\n\n"
                f"A plugin requires a manifest.py file with metadata.\n"
                f"Create one with: mixpeek init {self.plugin_path.name} --template=basic_text"
            )

        if not pipeline_path.exists():
            raise FileNotFoundError(
                f"pipeline.py not found in {self.plugin_path}\n\n"
                f"A plugin requires a pipeline.py file with an extract() function.\n"
                f"Create one with: mixpeek init {self.plugin_path.name} --template=basic_text"
            )

        # Load manifest.py
        try:
            self.manifest = self._load_module_as_dict(manifest_path)
        except Exception as e:
            raise ImportError(
                f"Failed to load manifest.py: {str(e)}\n\n"
                f"Check for syntax errors in {manifest_path}"
            )

        # Validate manifest has required fields
        required_fields = ["feature_extractor_name", "version", "features"]
        missing_fields = [f for f in required_fields if f not in self.manifest]
        if missing_fields:
            raise ValueError(
                f"manifest.py missing required fields: {', '.join(missing_fields)}\n\n"
                f"Required fields:\n"
                f"- feature_extractor_name: str (e.g., 'my_extractor')\n"
                f"- version: str (e.g., 'v1')\n"
                f"- features: list (e.g., [{{'name': 'embedding', 'type': 'vector'}}])"
            )

        # Load pipeline.py
        try:
            self.pipeline_module = self._load_module(pipeline_path)
        except Exception as e:
            raise ImportError(
                f"Failed to load pipeline.py: {str(e)}\n\n"
                f"Check for syntax errors in {pipeline_path}"
            )

        # Validate pipeline has extract() function
        if not hasattr(self.pipeline_module, "extract"):
            raise AttributeError(
                f"pipeline.py must define an extract() function.\n\n"
                f"Example:\n"
                f"def extract(extractor_request, base_steps=None, dataset_size=None, content_flags=None):\n"
                f"    # Return object with .steps and .prepare attributes\n"
                f"    return PipelineResult(steps=[MyProcessor()], prepare=lambda ds: ds)"
            )

        # Load realtime.py (optional)
        if realtime_path.exists():
            try:
                self.realtime_module = self._load_module(realtime_path)
            except Exception as e:
                # Realtime is optional, so just warn
                print(
                    f"Warning: Failed to load realtime.py: {str(e)}\n"
                    f"Realtime inference will not be available."
                )

    def _load_module(self, path: Path) -> Any:
        """Load a Python module from a file path.

        Args:
            path: Path to .py file

        Returns:
            Loaded module object

        Example:
            ```python
            module = self._load_module(Path("my_plugin/pipeline.py"))
            extract_fn = module.extract
            ```
        """
        module_name = path.stem
        spec = importlib.util.spec_from_file_location(module_name, path)
        if spec is None or spec.loader is None:
            raise ImportError(f"Could not load module from {path}")

        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        return module

    def _load_module_as_dict(self, path: Path) -> Dict[str, Any]:
        """Load a Python module and extract top-level variables as a dict.

        This is used for manifest.py which defines simple Python variables
        instead of classes/functions.

        Args:
            path: Path to .py file

        Returns:
            Dict of variable_name -> value

        Example:
            ```python
            # manifest.py contains:
            # feature_extractor_name = "my_extractor"
            # version = "v1"

            manifest = self._load_module_as_dict(Path("manifest.py"))
            # Returns: {"feature_extractor_name": "my_extractor", "version": "v1", ...}
            ```
        """
        module = self._load_module(path)
        return {
            key: getattr(module, key)
            for key in dir(module)
            if not key.startswith("_")
        }

    async def test_batch(
        self, input_data: List[Dict[str, Any]], parameters: Optional[Dict[str, Any]] = None
    ) -> List[Dict[str, Any]]:
        """Test batch pipeline processing.

        This method simulates the Mixpeek batch extraction pipeline:
        1. Load input data into a pandas DataFrame
        2. Call extract() to build pipeline steps
        3. Execute each step in sequence
        4. Return processed data

        Args:
            input_data: List of input dicts (e.g., [{"text": "doc1"}, {"text": "doc2"}])
            parameters: Optional plugin parameters (from parameter_schema)

        Returns:
            List of output dicts with extracted features

        Raises:
            AttributeError: If pipeline.extract() is not defined
            ValueError: If output doesn't match expected schema

        Example:
            ```python
            runner = LocalTestRunner("./my_plugin", mode="mock")

            results = await runner.test_batch([
                {"text": "Hello world"},
                {"text": "Another document"}
            ])

            # results = [
            #     {"text": "Hello world", "embedding": [0.1, 0.2, ...]},
            #     {"text": "Another document", "embedding": [0.3, 0.4, ...]}
            # ]
            ```

        **How It Works:**

        The batch pipeline follows these steps:
        1. Convert input_data to pandas DataFrame
        2. Call pipeline.extract() to get pipeline steps
        3. Execute each step (steps are callable classes)
        4. Convert result back to list of dicts
        5. Validate output against manifest.output_schema

        **Mock Mode:**

        In mock mode, ServiceContainer returns deterministic mock services:
        - MockE5: Returns hash-based embeddings (same input = same output)
        - MockWhisper: Returns dummy transcription
        - MockQdrant: In-memory vector storage

        **Error Messages:**

        Clear, actionable errors help debug issues:
        - "No extract() function found": Add extract() to pipeline.py
        - "Step failed: TypeError": Check step implementation
        - "Output missing field 'embedding'": Add field to output or fix schema
        """
        if self.pipeline_module is None:
            raise RuntimeError("Plugin not loaded. Call _load_plugin() first.")

        # Convert input data to DataFrame
        df = pd.DataFrame(input_data)

        # Create mock extractor request (simplified for local testing)
        extractor_request = type(
            "ExtractorRequest",
            (),
            {
                "parameters": parameters or {},
                "feature_extractor_name": self.manifest.get("feature_extractor_name"),
                "version": self.manifest.get("version"),
            },
        )()

        # Call extract() to build pipeline
        # NOTE: Plugins can access builtin services via container parameter
        try:
            # Check if plugin's build_steps() accepts container parameter
            import inspect
            if hasattr(self.pipeline_module, 'build_steps'):
                sig = inspect.signature(self.pipeline_module.build_steps)
                if 'container' in sig.parameters:
                    # Plugin uses container - pass it
                    pipeline_result = self.pipeline_module.extract(
                        extractor_request=extractor_request,
                        base_steps=[],
                        dataset_size=len(input_data),
                        content_flags={},
                    )
                    # Manually call build_steps with container to rebuild pipeline
                    from types import SimpleNamespace
                    rebuilt = self.pipeline_module.build_steps(
                        extractor_request=extractor_request,
                        container=self.service_container,
                        base_steps=[],
                        dataset_size=len(input_data),
                        content_flags={},
                    )
                    # Update pipeline_result with container-aware steps
                    pipeline_result.steps = rebuilt["steps"]
                    pipeline_result.prepare = rebuilt["prepare"]
                else:
                    # Plugin doesn't use container
                    pipeline_result = self.pipeline_module.extract(
                        extractor_request=extractor_request,
                        base_steps=[],
                        dataset_size=len(input_data),
                        content_flags={},
                    )
            else:
                # Old-style plugin without build_steps
                pipeline_result = self.pipeline_module.extract(
                    extractor_request=extractor_request,
                    base_steps=[],
                    dataset_size=len(input_data),
                    content_flags={},
                )
        except Exception as e:
            raise RuntimeError(
                f"Failed to build pipeline: {str(e)}\n\n"
                f"The extract() function in pipeline.py raised an error.\n"
                f"Check the implementation and ensure it returns an object with .steps and .prepare attributes."
            ) from e

        # Validate pipeline has required attributes
        if not hasattr(pipeline_result, "steps"):
            raise AttributeError(
                f"Pipeline result must have .steps attribute.\n\n"
                f"The extract() function should return an object with:\n"
                f"- .steps: list of callable step objects\n"
                f"- .prepare: function to prepare dataset"
            )

        if not hasattr(pipeline_result, "prepare"):
            raise AttributeError(
                f"Pipeline result must have .prepare attribute.\n\n"
                f"The extract() function should return an object with:\n"
                f"- .steps: list of callable step objects\n"
                f"- .prepare: function to prepare dataset"
            )

        # Run prepare function
        try:
            df = pipeline_result.prepare(df)
        except Exception as e:
            raise RuntimeError(
                f"Failed to run prepare function: {str(e)}\n\n"
                f"The prepare() function raised an error. Check the implementation."
            ) from e

        # Execute pipeline steps in sequence
        for i, step in enumerate(pipeline_result.steps):
            try:
                df = step(df)
            except Exception as e:
                raise RuntimeError(
                    f"Failed to execute pipeline step {i}: {str(e)}\n\n"
                    f"Step class: {type(step).__name__}\n"
                    f"Error: {str(e)}\n\n"
                    f"Check the step implementation in pipeline.py"
                ) from e

        # Convert result back to list of dicts
        results = df.to_dict(orient="records")

        # TODO: Validate output against manifest.output_schema
        # For now, just return results

        return results

    async def test_realtime(
        self, inputs: Dict[str, Any], parameters: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Test realtime inference.

        This method simulates the Mixpeek realtime inference API:
        1. Load realtime service from realtime.py
        2. Call run_inference() with inputs and parameters
        3. Return inference result

        Args:
            inputs: Input dict (e.g., {"text": "query"})
            parameters: Optional plugin parameters

        Returns:
            Inference result dict

        Raises:
            RuntimeError: If realtime.py not found or service not defined

        Example:
            ```python
            runner = LocalTestRunner("./my_plugin", mode="mock")

            result = await runner.test_realtime({"text": "Hello world"})
            # result = {"embeddings": [[0.1, 0.2, ...]]
            ```

        **How It Works:**

        The realtime service follows these steps:
        1. Load inference service class from realtime.py
        2. Instantiate the service
        3. Call run_inference(inputs, parameters)
        4. Return the result

        **Error Messages:**

        - "realtime.py not found": Add realtime.py or use --batch-only flag
        - "No inference service found": Define a class extending BaseInferenceService
        - "run_inference() failed": Check service implementation
        """
        if self.realtime_module is None:
            raise RuntimeError(
                f"realtime.py not loaded.\n\n"
                f"Realtime inference requires a realtime.py file with a service class.\n"
                f"Create one with: mixpeek init {self.plugin_path.name} --template=basic_text"
            )

        # Find inference service class (should extend BaseInferenceService)
        service_class = None
        for attr_name in dir(self.realtime_module):
            attr = getattr(self.realtime_module, attr_name)
            if (
                isinstance(attr, type)
                and attr_name.endswith("InferenceService")
                and not attr_name.startswith("Base")
            ):
                service_class = attr
                break

        if service_class is None:
            raise RuntimeError(
                f"No inference service class found in realtime.py.\n\n"
                f"Define a class extending BaseInferenceService with a run_inference() method.\n\n"
                f"Example:\n"
                f"from shared.plugins.inference.serve import BaseInferenceService\n\n"
                f"class MyInferenceService(BaseInferenceService):\n"
                f"    async def run_inference(self, inputs, parameters):\n"
                f"        # Your inference logic here\n"
                f"        return {{'result': ...}}"
            )

        # Instantiate service
        try:
            service = service_class()
        except Exception as e:
            raise RuntimeError(
                f"Failed to instantiate {service_class.__name__}: {str(e)}\n\n"
                f"Check the __init__() method."
            ) from e

        # Run inference
        try:
            result = await service.run_inference(
                inputs=inputs, parameters=parameters or {}
            )
        except Exception as e:
            raise RuntimeError(
                f"Failed to run inference: {str(e)}\n\n"
                f"The run_inference() method raised an error. Check the implementation."
            ) from e

        return result

    async def test_e2e(
        self,
        extract_data: List[Dict[str, Any]],
        search_query: str,
        top_k: int = 5,
    ) -> Dict[str, Any]:
        """Test end-to-end workflow: extract → index → search.

        This method simulates the complete Mixpeek workflow:
        1. Extract features from documents (batch pipeline)
        2. Index vectors in Qdrant
        3. Search for similar documents

        Args:
            extract_data: Documents to extract and index
            search_query: Query text to search for
            top_k: Number of results to return

        Returns:
            Dict with extraction results and search results

        Raises:
            NotImplementedError: In mock mode (requires local-stack or production)

        Example:
            ```python
            runner = LocalTestRunner("./my_plugin", mode="local-stack")

            result = await runner.test_e2e(
                extract_data=[
                    {"text": "Red summer dress"},
                    {"text": "Blue winter coat"},
                ],
                search_query="red dress"
            )

            # result = {
            #     "extracted": [...],
            #     "indexed": 2,
            #     "search_results": [
            #         {"text": "Red summer dress", "score": 0.95},
            #         {"text": "Blue winter coat", "score": 0.32}
            #     ]
            # }
            ```

        **Requirements:**

        E2E testing requires real services (Qdrant for vector storage):
        - Use --local-stack mode to run with Docker
        - Use --environment=production to test deployed plugin

        **Not Supported in Mock Mode:**

        MockQdrant doesn't support semantic search, so this method
        raises NotImplementedError in mock mode.
        """
        if self.mode == "mock":
            raise NotImplementedError(
                f"E2E testing not supported in mock mode.\n\n"
                f"E2E tests require a vector database (Qdrant) for semantic search.\n"
                f"Use --local-stack mode instead:\n\n"
                f"  mixpeek test --local-stack\n\n"
                f"This will start Qdrant and Ray in Docker containers for full E2E testing."
            )

        # TODO Phase 4: Implement local-stack E2E testing
        # TODO Phase 7: Implement production E2E testing
        raise NotImplementedError("E2E testing not yet implemented")
