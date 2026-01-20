"""Test command for local plugin testing.

This module implements the `mixpeek test` command which runs plugin tests locally.

**Command Modes:**

1. **Mock mode** (default): Fast, deterministic testing with mock services
   ```bash
   mixpeek test --mock
   ```

2. **Local stack mode**: Full E2E testing with Docker containers
   ```bash
   mixpeek test --local-stack
   ```

3. **Production mode**: Test deployed plugins
   ```bash
   mixpeek test --environment=production
   ```

**Self-Documenting Design:**

The test command provides rich, formatted output showing:
- Plugin metadata
- Test progress with spinners
- Results table with pass/fail status
- Clear error messages with suggestions

**Example Output:**

```
Testing Plugin: text_echo v1
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✓ Plugin loaded successfully
✓ Manifest valid
✓ Batch pipeline: 5/5 items processed
✓ Output schema validation passed
✓ All tests passed (0.3s)
```
"""

import asyncio
import json
import sys
from pathlib import Path
from typing import Optional

try:
    import click
except ImportError:
    raise ImportError(
        "click is required for the Mixpeek CLI.\n"
        "Install with: pip install 'mixpeek[dev]'"
    )

from mixpeek_dev.testing import (
    LocalTestRunner,
    ManifestValidator,
    ProductionTestRunner,
    SecurityValidator,
)
from mixpeek_dev.utils import get_logger


@click.command()
@click.option(
    "--plugin",
    type=click.Path(exists=True, file_okay=False, dir_okay=True, path_type=Path),
    default=Path.cwd(),
    help="Path to plugin directory (default: current directory)",
)
@click.option(
    "--mock",
    is_flag=True,
    default=True,
    help="Use mock services for fast testing (default)",
)
@click.option(
    "--local-stack",
    is_flag=True,
    help="Use local Docker stack (Ray + Qdrant) for E2E testing",
)
@click.option(
    "--environment",
    type=click.Choice(["production"], case_sensitive=False),
    help="Test deployed plugin in production",
)
@click.option(
    "--input",
    "input_file",
    type=click.Path(exists=True, file_okay=True, dir_okay=False, path_type=Path),
    help="JSON file with test input data",
)
@click.option(
    "--verbose",
    "-v",
    is_flag=True,
    help="Show detailed output",
)
@click.option(
    "--namespace-id",
    type=str,
    envvar="MIXPEEK_NAMESPACE_ID",
    help="Namespace ID for production testing (can also set MIXPEEK_NAMESPACE_ID env var)",
)
@click.option(
    "--api-key",
    type=str,
    envvar="MIXPEEK_API_KEY",
    help="Mixpeek API key for production testing (can also set MIXPEEK_API_KEY env var)",
)
@click.option(
    "--api-url",
    type=str,
    default="https://api.mixpeek.com",
    envvar="MIXPEEK_API_URL",
    help="Mixpeek API base URL (default: https://api.mixpeek.com)",
)
def test(
    plugin: Path,
    mock: bool,
    local_stack: bool,
    environment: Optional[str],
    input_file: Optional[Path],
    verbose: bool,
    namespace_id: Optional[str],
    api_key: Optional[str],
    api_url: str,
):
    """Test plugin locally with mock or real services.

    **Examples:**

    \b
    # Test with mock services (fast, default)
    $ mixpeek test --mock

    \b
    # Test with local Docker stack (E2E)
    $ mixpeek test --local-stack

    \b
    # Test with custom input data
    $ mixpeek test --input test_data.json

    \b
    # Test deployed plugin in production
    $ mixpeek test --environment=production

    **Test Modes:**

    \b
    --mock (default)
      Fast, deterministic testing with mock services
      - No external dependencies
      - Runs in <1 second
      - Perfect for unit tests and rapid iteration

    \b
    --local-stack
      Full E2E testing with real services in Docker
      - Requires Docker
      - Runs in ~5 seconds
      - Tests complete extract → index → search workflow

    \b
    --environment=production
      Test deployed plugin via production API
      - Requires API key
      - Tests live deployment
      - Smoke testing after deployment

    **Self-Documenting:**

    This command provides rich output with:
    - Clear success/error indicators
    - Formatted results table
    - Helpful error messages with solutions
    - Performance metrics
    """
    logger = get_logger()

    # Determine test mode
    if local_stack:
        mode = "local-stack"
    elif environment:
        mode = "production"
    else:
        mode = "mock"

    # Show test header
    logger.info(f"\n{'='*50}")
    logger.info(f"Mixpeek Plugin Test - Mode: {mode}")
    logger.info(f"Plugin path: {plugin}")
    logger.info(f"{'='*50}\n")

    # Run async test
    exit_code = asyncio.run(
        _run_test(
            logger,
            plugin,
            mode,
            input_file,
            verbose,
            namespace_id,
            api_key,
            api_url,
        )
    )
    sys.exit(exit_code)


async def _run_test(
    logger,
    plugin_path: Path,
    mode: str,
    input_file: Optional[Path],
    verbose: bool,
    namespace_id: Optional[str] = None,
    api_key: Optional[str] = None,
    api_url: str = "https://api.mixpeek.com",
) -> int:
    """Run plugin test asynchronously.

    Args:
        logger: Logger instance
        plugin_path: Path to plugin directory
        mode: Test mode ("mock", "local-stack", "production")
        input_file: Optional path to test data JSON file
        verbose: Show detailed output

    Returns:
        Exit code (0 = success, 1 = failure)
    """
    try:
        # Step 1: Validate manifest
        logger.info("Step 1: Validating manifest...")
        manifest_validator = ManifestValidator()
        manifest_result = manifest_validator.validate(plugin_path)

        if not manifest_result.is_valid:
            logger.error("Manifest validation failed:")
            for error in manifest_result.errors:
                logger.error(f"  {error}")
            return 1

        logger.success("Manifest valid")

        # Show warnings if any
        if manifest_result.warnings:
            for warning in manifest_result.warnings:
                logger.warning(f"  {warning}")

        # Step 2: Security scan
        logger.info("\nStep 2: Running security scan...")
        security_validator = SecurityValidator()
        security_result = security_validator.validate(plugin_path)

        if not security_result.is_valid:
            logger.error("Security scan failed:")
            for error in security_result.errors:
                logger.error(f"  {error}")
            return 1

        logger.success("Security scan passed")

        # Step 3: Load test runner
        logger.info(f"\nStep 3: Initializing test runner (mode: {mode})...")
        try:
            if mode == "production":
                # Production mode - test deployed plugin
                runner = ProductionTestRunner(
                    plugin_path=plugin_path,
                    namespace_id=namespace_id,
                    api_key=api_key,
                    api_url=api_url,
                )

                # Verify deployment first
                logger.info("Verifying plugin deployment...")
                deployment_status = await runner.verify_deployment()

                if deployment_status.get("status") != "deployed":
                    logger.error(
                        f"Plugin is not deployed. Status: {deployment_status.get('status')}\n"
                        f"Deploy first with: mixpeek push"
                    )
                    return 1

                logger.success("Plugin deployed and accessible")
            else:
                # Local mode - test using local files
                runner = LocalTestRunner(plugin_path=plugin_path, mode=mode)

        except Exception as e:
            logger.error(f"Failed to initialize test runner: {str(e)}")
            if verbose:
                import traceback
                logger.error(traceback.format_exc())
            return 1

        logger.success(f"Plugin loaded: {runner.manifest.get('feature_extractor_name')} v{runner.manifest.get('version')}")

        # Step 4: Prepare test data
        logger.info("\nStep 4: Preparing test data...")
        if input_file:
            # Load from file
            with open(input_file, "r") as f:
                test_data = json.load(f)

            if not isinstance(test_data, list):
                logger.error("Test data must be a JSON array of input objects")
                return 1
        else:
            # Use default test data
            test_data = _get_default_test_data(runner)

        logger.info(f"Test data: {len(test_data)} items")

        # Step 5: Run batch test
        logger.info("\nStep 5: Running batch pipeline test...")
        try:
            results = await runner.test_batch(test_data)
        except Exception as e:
            logger.error(f"Batch test failed: {str(e)}")
            if verbose:
                import traceback
                logger.error(traceback.format_exc())
            return 1

        logger.success(f"Batch pipeline: {len(results)}/{len(test_data)} items processed")

        # Step 6: Validate output
        logger.info("\nStep 6: Validating output...")
        # Check that results have expected fields
        expected_features = [f["name"] for f in runner.manifest.get("features", [])]
        for i, result in enumerate(results):
            for feature in expected_features:
                if feature not in result:
                    logger.warning(f"Result {i} missing expected feature: {feature}")

        logger.success("Output schema validation passed")

        # Step 7: Show results
        if verbose and results:
            logger.info("\nSample Results:")
            logger.info(f"First result: {json.dumps(results[0], indent=2)[:500]}...")

        # Summary
        logger.info(f"\n{'='*50}")
        logger.success("All tests passed!")
        logger.info(f"{'='*50}\n")

        return 0

    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        if verbose:
            import traceback
            logger.error(traceback.format_exc())
        return 1


def _get_default_test_data(runner: LocalTestRunner) -> list:
    """Generate default test data based on plugin type.

    Args:
        runner: LocalTestRunner instance with loaded manifest

    Returns:
        List of test input dicts

    **Smart Test Data Generation:**

    The test data is generated based on the plugin's input_mappings:
    - If input has "text" field → Generate text samples
    - If input has "image" field → Generate dummy image URLs
    - If input has "audio" field → Generate dummy audio URLs

    This makes the CLI self-sufficient for basic testing.
    """
    # Get input mappings from manifest
    input_mappings = runner.manifest.get("input_mappings", {})

    # Generate test data based on input type
    test_data = []

    if "text" in input_mappings:
        # Text-based plugin
        test_data = [
            {"text": "Sample document 1 for testing"},
            {"text": "Another test document with different content"},
            {"text": "Third test item to verify batch processing"},
            {"text": "Fourth document for comprehensive testing"},
            {"text": "Final test document to complete the batch"},
        ]
    elif "image" in input_mappings:
        # Image-based plugin
        test_data = [
            {"image": "https://example.com/image1.jpg"},
            {"image": "https://example.com/image2.jpg"},
            {"image": "https://example.com/image3.jpg"},
        ]
    elif "audio" in input_mappings:
        # Audio-based plugin
        test_data = [
            {"audio": "https://example.com/audio1.mp3"},
            {"audio": "https://example.com/audio2.mp3"},
        ]
    else:
        # Default: empty dict
        test_data = [{"data": f"test_item_{i}"} for i in range(5)]

    return test_data
