"""Plugin development commands for Mixpeek CLI.

Commands:
    init     - Create a new plugin from template
    test     - Test plugin locally with sample data
    validate - Validate plugin structure and schemas
    publish  - Publish plugin to your namespace
    list     - List plugins in your namespace
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

import click

# Plugin template structure
PLUGIN_TEMPLATE = {
    "manifest.py": '''"""Plugin manifest - defines metadata and schemas."""

from pydantic import BaseModel, Field
from typing import Optional


class {class_name}Input(BaseModel):
    """Input schema for {name}."""

    text: str = Field(..., description="Input text to process")


class {class_name}Output(BaseModel):
    """Output schema for {name}."""

    result: str = Field(..., description="Processed result")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Confidence score")


class {class_name}Params(BaseModel):
    """Parameters for {name}.

    These are configurable via the API when creating a collection.
    """

    threshold: float = Field(
        default=0.5,
        ge=0.0,
        le=1.0,
        description="Processing threshold",
    )
    text_column: str = Field(
        default="text",
        description="Name of the input text column",
    )
    output_column: str = Field(
        default="result",
        description="Name of the output column",
    )


# Plugin metadata (for plugin loader discovery)
metadata = {{
    "name": "{name}",
    "version": "v1",
    "description": "{description}",
    "category": "{category}",
    "icon": "sparkles",
    "author": "{author}",
}}

# Schema exports
input_schema = {class_name}Input
output_schema = {class_name}Output
parameter_schema = {class_name}Params

# Supported input types
supported_input_types = ["{category}"]  # Options: text, image, video, audio, pdf
''',
    "pipeline.py": '''"""Pipeline implementation for {name}.

This module defines how your plugin processes data using the declarative
pipeline system. The framework handles batching, concurrency, and resource
allocation automatically - you just define WHAT to do, not HOW to configure it.

Available ResourceTypes:
    - ResourceType.CPU: CPU-bound processing (embeddings, classification)
    - ResourceType.GPU: GPU-bound processing (local models requiring GPU)
    - ResourceType.API: External API calls (OpenAI, etc.)

Available RowConditions:
    - RowCondition.IS_TEXT: Process text content
    - RowCondition.IS_IMAGE: Process image content
    - RowCondition.IS_VIDEO: Process video content
    - RowCondition.IS_AUDIO: Process audio content
    - RowCondition.IS_PDF: Process PDF documents
    - RowCondition.ALWAYS: Process all rows (default)
"""

from typing import Any, Dict, Optional

from engine.plugins.extractors.pipeline import (
    PipelineDefinition,
    ResourceType,
    RowCondition,
    StepDefinition,
    build_pipeline_steps,
)
from shared.collection.features.extractors.models import ExtractorDefinition

from .manifest import {class_name}Params, metadata
from .processors.core import {class_name}Config, {class_name}Processor


def build_steps(
    extractor_request: Any,
    container: Optional[Any] = None,
    base_steps: Optional[list] = None,
    dataset_size: Optional[int] = None,
    content_flags: Optional[dict] = None,
) -> Dict[str, Any]:
    """Build the extraction pipeline.

    The framework automatically handles:
    - Actor configuration (num_cpus, num_gpus based on ResourceType)
    - Batch sizes (based on hardware config)
    - Concurrency (scaled based on dataset_size)
    - Row filtering (based on RowCondition)

    Args:
        extractor_request: Request context with config and parameters.
        container: Service container (optional, for accessing shared services).
        base_steps: Optional preprocessing steps to prepend.
        dataset_size: Size of dataset (used for intelligent concurrency scaling).
        content_flags: Content type flags for the dataset.

    Returns:
        Dict with 'steps' list and 'prepare' function.
    """
    # Extract and validate parameters from request
    params_dict = extractor_request.extractor_config.parameters or {{}}
    params = {class_name}Params(**params_dict)

    # Configure your processor
    processor_config = {class_name}Config(
        threshold=params.threshold,
        text_column=params.text_column,
        output_column=params.output_column,
    )

    # Define pipeline steps declaratively
    # The framework handles batching, concurrency, and resource allocation
    steps = [
        StepDefinition(
            service_class={class_name}Processor,
            resource_type=ResourceType.CPU,  # CPU, GPU, or API
            config=processor_config,
            condition=RowCondition.IS_TEXT,  # Only process text rows
            # Optional overrides (usually not needed):
            # concurrency=4,    # Override auto-calculated concurrency
            # batch_size=32,    # Override default batch size
        ),
    ]

    # Build pipeline definition
    pipeline = PipelineDefinition(
        name="{name}",
        version="v1",
        steps=steps,
    )

    # Convert to executable steps (framework handles all the config)
    pipeline_steps = build_pipeline_steps(pipeline, dataset_size=dataset_size)

    # Combine with any base preprocessing steps
    all_steps = (base_steps or []) + pipeline_steps

    def prepare(ds):
        """Prepare dataset before processing.

        Use this to filter, transform, or validate the dataset.
        """
        return ds

    return {{
        "steps": all_steps,
        "prepare": prepare,
    }}


# Extractor definition for engine discovery
extractor_definition = ExtractorDefinition(
    name=metadata["name"],
    version=metadata["version"],
    extractor_function_path=build_steps,
    requires_file_resolution=False,
)
''',
    "realtime.py": '''"""Real-time inference services for Ray Serve deployment.

This module is OPTIONAL. Include it if your plugin needs to expose
a real-time HTTP endpoint in addition to batch processing.

For BUILTIN plugins:
    Re-export shared services from engine/inference/ to avoid duplication.

For CUSTOM plugins:
    Define your own Ray Serve deployment class.
"""

from typing import Any, Dict

from shared.plugins.inference.serve import BaseInferenceService, ServeDeploymentConfig

from .processors.core import {class_name}Config, {class_name}Processor


class {class_name}RealtimeService(BaseInferenceService):
    """Real-time inference service for HTTP endpoints.

    This service is deployed as a Ray Serve deployment and handles
    individual inference requests via HTTP.

    The framework automatically handles:
    - Ray Serve deployment configuration
    - HTTP route registration (/inference/{{name}})
    - Request/response parsing
    - Error handling
    """

    # Optional: customize deployment (defaults work for most cases)
    serve_config = ServeDeploymentConfig(
        enabled=True,
        num_replicas=1,  # Auto-scaled in production
    )

    def __init__(self):
        super().__init__()
        self._processor = None

    def _load_processor(self):
        """Lazy load processor on first request."""
        if self._processor is None:
            config = {class_name}Config()
            self._processor = {class_name}Processor(config)
            self.logger.info("[{class_name}RealtimeService] Processor loaded")

    async def _process_single(self, inputs: Dict[str, Any], parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Process a single inference request.

        Args:
            inputs: Input data (e.g., {{"text": "Hello world"}})
            parameters: Optional parameters (e.g., {{"threshold": 0.7}})

        Returns:
            Inference result dict
        """
        self._load_processor()

        text = inputs.get("text", "")
        result, confidence = self._processor._process_single(text)

        return {{
            "result": result,
            "confidence": confidence,
        }}


# Export for Ray Serve deployment
__all__ = ["{class_name}RealtimeService"]
''',
    "processors/__init__.py": '''"""Custom processors for {name}.

Processors are the core processing units that handle batch data.
They are instantiated once per Ray actor and called repeatedly.
"""

from .core import {class_name}Config, {class_name}Processor

__all__ = ["{class_name}Config", "{class_name}Processor"]
''',
    "processors/core.py": '''"""Core processing logic for {name}.

Processors must be callable and accept a pandas DataFrame.
Use __init__ for expensive setup (loading models) and __call__ for processing.
"""

from dataclasses import dataclass
from typing import Tuple

import pandas as pd


@dataclass
class {class_name}Config:
    """Configuration for the processor.

    This is passed to the processor via StepDefinition.config.
    """

    threshold: float = 0.5
    text_column: str = "text"
    output_column: str = "result"


class {class_name}Processor:
    """Main batch processor for {name}.

    Processors are instantiated once per Ray actor and called repeatedly
    with batches of data. Use __init__ for expensive setup (loading models)
    and __call__ for batch processing.

    The framework handles:
    - Actor lifecycle management
    - Batch sizing and concurrency
    - Progress tracking (via progress_actor)
    - Error handling and retries
    """

    def __init__(self, config: {class_name}Config, progress_actor=None):
        """Initialize the processor.

        This is called once when the Ray actor starts.
        Load models and do expensive setup here.

        Args:
            config: Processor configuration.
            progress_actor: Optional Ray actor for progress tracking.
        """
        self.config = config
        self.progress_actor = progress_actor
        self._model = None  # Lazy load expensive resources

    def _load_model(self):
        """Lazy load model on first use.

        This pattern is useful for expensive resources that shouldn't
        be loaded until actually needed.
        """
        if self._model is None:
            # TODO: Load your model here
            # Example: self._model = transformers.AutoModel.from_pretrained("...")
            self._model = "loaded"

    def __call__(self, batch: pd.DataFrame) -> pd.DataFrame:
        """Process a batch of data.

        This is called repeatedly with batches of data.
        The batch size is configured by the framework based on hardware.

        Args:
            batch: Input DataFrame with data to process.

        Returns:
            DataFrame with added output columns.
        """
        self._load_model()

        text_col = self.config.text_column
        output_col = self.config.output_column

        # Handle missing column gracefully
        if text_col not in batch.columns:
            batch[output_col] = None
            batch["confidence"] = 0.0
            return batch

        # Process each row
        results = []
        confidences = []

        for text in batch[text_col].fillna(""):
            result, confidence = self._process_single(text)
            results.append(result)
            confidences.append(confidence)

        # Add results to DataFrame
        batch[output_col] = results
        batch["confidence"] = confidences

        return batch

    def _process_single(self, text: str) -> Tuple[str, float]:
        """Process a single text input.

        Args:
            text: Input text string.

        Returns:
            Tuple of (result, confidence).
        """
        if not text:
            return "", 0.0

        # TODO: Replace with your actual processing logic
        # Example: sentiment = self._model(text)
        processed = f"Processed: {{text[:100]}}"
        confidence = min(1.0, len(text) / 100 * self.config.threshold)

        return processed, confidence
''',
    "tests/__init__.py": '''"""Tests for {name}."""
''',
    "tests/test_plugin.py": '''"""Unit tests for {name}."""

import pandas as pd
import pytest

from ..manifest import {class_name}Input, {class_name}Output, {class_name}Params
from ..processors.core import {class_name}Config, {class_name}Processor


class TestSchemas:
    """Test input/output schemas."""

    def test_input_schema_valid(self):
        """Test valid input."""
        input_data = {class_name}Input(text="Hello world")
        assert input_data.text == "Hello world"

    def test_input_schema_required(self):
        """Test required fields."""
        with pytest.raises(Exception):
            {class_name}Input()

    def test_output_schema(self):
        """Test output schema."""
        output = {class_name}Output(result="test", confidence=0.95)
        assert output.result == "test"
        assert output.confidence == 0.95

    def test_params_defaults(self):
        """Test parameter defaults."""
        params = {class_name}Params()
        assert params.threshold == 0.5
        assert params.text_column == "text"
        assert params.output_column == "result"

    def test_params_custom(self):
        """Test custom parameters."""
        params = {class_name}Params(
            threshold=0.8,
            text_column="content",
            output_column="sentiment",
        )
        assert params.threshold == 0.8
        assert params.text_column == "content"


class TestProcessor:
    """Test the main processor."""

    @pytest.fixture
    def processor(self):
        """Create processor instance."""
        config = {class_name}Config(threshold=0.5)
        return {class_name}Processor(config)

    def test_process_batch(self, processor):
        """Test batch processing."""
        batch = pd.DataFrame({{"text": ["Hello world", "Test input"]}})
        result = processor(batch)

        assert "result" in result.columns
        assert "confidence" in result.columns
        assert len(result) == 2

    def test_process_empty_text(self, processor):
        """Test empty text handling."""
        batch = pd.DataFrame({{"text": [""]}})
        result = processor(batch)

        assert result["result"].iloc[0] == ""
        assert result["confidence"].iloc[0] == 0.0

    def test_process_missing_column(self, processor):
        """Test missing text column."""
        batch = pd.DataFrame({{"other": ["data"]}})
        result = processor(batch)

        assert "result" in result.columns
        assert result["confidence"].iloc[0] == 0.0

    def test_custom_columns(self):
        """Test custom column configuration."""
        config = {class_name}Config(
            text_column="content",
            output_column="output",
        )
        processor = {class_name}Processor(config)

        batch = pd.DataFrame({{"content": ["Hello"]}})
        result = processor(batch)

        assert "output" in result.columns
        assert "confidence" in result.columns
''',
    "README.md": '''# {name}

{description}

## Installation

This plugin is designed to work with the Mixpeek platform.

## Usage

### As a Collection Extractor

```python
from mixpeek import Mixpeek

client = Mixpeek(api_key="your_api_key")

# Create a collection with this extractor
collection = client.collections.create(
    collection_name="my_collection",
    feature_extractor={{
        "feature_extractor_name": "{name}",
        "version": "v1",
        "parameters": {{
            "threshold": 0.7,
            "text_column": "text",
            "output_column": "result"
        }}
    }}
)
```

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| threshold | float | 0.5 | Processing threshold (0.0-1.0) |
| text_column | str | "text" | Name of the input text column |
| output_column | str | "result" | Name of the output column |

## Input Schema

- `text` (required): Input text to process

## Output Schema

- `result`: Processed result string
- `confidence`: Confidence score (0.0-1.0)

## Plugin Structure

```
{name}/
├── manifest.py          # Metadata and schema definitions
├── pipeline.py          # build_steps() implementation (declarative)
├── realtime.py          # Ray Serve real-time endpoint (optional)
├── processors/
│   ├── __init__.py
│   └── core.py          # Processor class ({class_name}Processor)
└── tests/
    └── test_plugin.py   # Unit tests
```

## Development

### Testing

```bash
mixpeek plugin test
```

### Publishing

```bash
mixpeek plugin publish
```

## Framework Features

The plugin uses Mixpeek's declarative pipeline system which automatically handles:

- **Resource allocation**: CPU/GPU/API based on `ResourceType`
- **Batching**: Automatic batch sizing based on hardware
- **Concurrency**: Intelligent scaling based on dataset size
- **Row filtering**: Conditional processing via `RowCondition`
- **Real-time serving**: Ray Serve deployment via `realtime.py`

## Author

{author}
''',
    "pyproject.toml": '''[project]
name = "{name}"
version = "0.1.0"
description = "{description}"
authors = [{{ name = "{author}" }}]
requires-python = ">=3.10"

[project.optional-dependencies]
dev = ["pytest", "pandas"]

[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"
''',
}


def to_class_name(name: str) -> str:
    """Convert plugin name to class name (PascalCase)."""
    return "".join(word.capitalize() for word in name.replace("-", "_").split("_"))


@click.group()
def plugin() -> None:
    """Plugin development commands.

    \b
    Create, test, and publish custom extractors.
    """
    pass


@plugin.command()
@click.argument("name")
@click.option(
    "--description",
    "-d",
    default="A custom Mixpeek extractor",
    help="Plugin description",
)
@click.option(
    "--category",
    "-c",
    type=click.Choice(["text", "image", "video", "audio", "document", "multimodal"]),
    default="text",
    help="Plugin category",
)
@click.option(
    "--author",
    "-a",
    default=None,
    help="Author name (defaults to git user.name)",
)
@click.option(
    "--output",
    "-o",
    type=click.Path(),
    default=None,
    help="Output directory (defaults to current dir)",
)
def init(
    name: str,
    description: str,
    category: str,
    author: str | None,
    output: str | None,
) -> None:
    """Create a new plugin from template.

    \b
    Examples:
        mixpeek plugin init my_extractor
        mixpeek plugin init sentiment_analyzer -c text -d "Sentiment analysis"
    """
    # Validate name
    if not name.replace("_", "").replace("-", "").isalnum():
        raise click.ClickException(
            "Plugin name must contain only letters, numbers, underscores, and hyphens"
        )

    # Get author from git config if not provided
    if author is None:
        try:
            result = subprocess.run(
                ["git", "config", "user.name"],
                capture_output=True,
                text=True,
                check=True,
            )
            author = result.stdout.strip() or "Unknown"
        except (subprocess.CalledProcessError, FileNotFoundError):
            author = "Unknown"

    # Determine output directory
    output_dir = Path(output) if output else Path.cwd()
    plugin_dir = output_dir / name

    if plugin_dir.exists():
        raise click.ClickException(f"Directory already exists: {plugin_dir}")

    click.echo(f"Creating plugin: {name}")
    click.echo(f"  Category: {category}")
    click.echo(f"  Author: {author}")
    click.echo(f"  Location: {plugin_dir}")
    click.echo()

    # Create directory structure
    plugin_dir.mkdir(parents=True)
    (plugin_dir / "processors").mkdir()
    (plugin_dir / "tests").mkdir()

    # Template variables
    class_name = to_class_name(name)
    template_vars = {
        "name": name,
        "class_name": class_name,
        "description": description,
        "category": category,
        "author": author,
    }

    # Create files from template
    for filename, template in PLUGIN_TEMPLATE.items():
        filepath = plugin_dir / filename
        filepath.parent.mkdir(parents=True, exist_ok=True)
        content = template.format(**template_vars)
        filepath.write_text(content)
        click.echo(f"  Created: {filename}")

    # Create __init__.py
    init_content = f'''"""{name} - {description}

A Mixpeek custom plugin using the declarative pipeline system.
"""

from .manifest import (
    {class_name}Input,
    {class_name}Output,
    {class_name}Params,
    metadata,
)
from .pipeline import build_steps, extractor_definition
from .processors import {class_name}Config, {class_name}Processor
from .realtime import {class_name}RealtimeService

__all__ = [
    # Schemas
    "{class_name}Input",
    "{class_name}Output",
    "{class_name}Params",
    "metadata",
    # Pipeline
    "build_steps",
    "extractor_definition",
    # Processors
    "{class_name}Config",
    "{class_name}Processor",
    # Realtime
    "{class_name}RealtimeService",
]
'''
    (plugin_dir / "__init__.py").write_text(init_content)
    click.echo("  Created: __init__.py")

    click.echo()
    click.echo(click.style("Plugin created successfully!", fg="green"))
    click.echo()
    click.echo("Next steps:")
    click.echo(f"  1. cd {name}")
    click.echo("  2. Edit processors/core.py with your processing logic")
    click.echo("  3. Update pipeline.py if you need different ResourceType/RowCondition")
    click.echo("  4. Run: mixpeek plugin test")
    click.echo("  5. Run: mixpeek plugin publish")
    click.echo()
    click.echo("Files created:")
    click.echo("  - manifest.py      Schemas and metadata")
    click.echo("  - pipeline.py      Declarative pipeline (StepDefinition, ResourceType)")
    click.echo("  - realtime.py      Ray Serve endpoint (optional)")
    click.echo("  - processors/      Your processing logic")


@plugin.command()
@click.option(
    "--path",
    "-p",
    type=click.Path(exists=True),
    default=".",
    help="Plugin directory path",
)
@click.option(
    "--sample-data",
    "-s",
    type=click.Path(exists=True),
    default=None,
    help="Sample data file (JSON/CSV) for testing",
)
@click.option(
    "--verbose",
    "-v",
    is_flag=True,
    help="Verbose output",
)
def test(path: str, sample_data: str | None, verbose: bool) -> None:
    """Test plugin locally with sample data.

    \b
    Runs validation and unit tests for the plugin.

    \b
    Examples:
        mixpeek plugin test
        mixpeek plugin test -p ./my_extractor
        mixpeek plugin test -s sample_data.json
    """
    plugin_path = Path(path).resolve()

    click.echo(f"Testing plugin at: {plugin_path}")
    click.echo()

    # Check required files
    required_files = ["manifest.py", "pipeline.py", "__init__.py"]
    missing = [f for f in required_files if not (plugin_path / f).exists()]
    if missing:
        raise click.ClickException(
            f"Missing required files: {', '.join(missing)}\n"
            "Is this a valid plugin directory?"
        )

    click.echo(click.style("1. Validating structure...", bold=True))

    # Add plugin to path for imports
    sys.path.insert(0, str(plugin_path.parent))
    plugin_name = plugin_path.name

    try:
        # Import and validate manifest
        click.echo("   Importing manifest...")
        manifest = __import__(f"{plugin_name}.manifest", fromlist=["metadata"])

        if not hasattr(manifest, "metadata"):
            raise click.ClickException("manifest.py must define 'metadata' dict")
        if not hasattr(manifest, "input_schema"):
            raise click.ClickException("manifest.py must define 'input_schema'")
        if not hasattr(manifest, "output_schema"):
            raise click.ClickException("manifest.py must define 'output_schema'")

        metadata = manifest.metadata
        click.echo(f"   Plugin: {metadata.get('name', 'unknown')}")
        click.echo(f"   Version: {metadata.get('version', 'unknown')}")
        click.echo(f"   Category: {metadata.get('category', 'unknown')}")
        click.echo(click.style("   Structure: OK", fg="green"))

        # Import and validate pipeline
        click.echo()
        click.echo(click.style("2. Validating pipeline...", bold=True))
        click.echo("   Importing pipeline...")
        pipeline = __import__(f"{plugin_name}.pipeline", fromlist=["build_steps"])

        if not hasattr(pipeline, "build_steps"):
            raise click.ClickException("pipeline.py must define 'build_steps' function")
        if not callable(pipeline.build_steps):
            raise click.ClickException("'build_steps' must be a callable")

        click.echo(click.style("   Pipeline: OK", fg="green"))

        # Run pytest if tests exist
        click.echo()
        click.echo(click.style("3. Running tests...", bold=True))
        tests_dir = plugin_path / "tests"
        if tests_dir.exists() and any(tests_dir.glob("test_*.py")):
            try:
                result = subprocess.run(
                    [sys.executable, "-m", "pytest", str(tests_dir), "-v" if verbose else "-q"],
                    cwd=str(plugin_path.parent),
                    capture_output=not verbose,
                    text=True,
                )
                if result.returncode == 0:
                    click.echo(click.style("   Tests: PASSED", fg="green"))
                else:
                    click.echo(click.style("   Tests: FAILED", fg="red"))
                    if not verbose and result.stdout:
                        click.echo(result.stdout)
                    if not verbose and result.stderr:
                        click.echo(result.stderr)
            except FileNotFoundError:
                click.echo(click.style("   Tests: SKIPPED (pytest not installed)", fg="yellow"))
        else:
            click.echo(click.style("   Tests: SKIPPED (no test files)", fg="yellow"))

        # Test with sample data if provided
        if sample_data:
            click.echo()
            click.echo(click.style("4. Testing with sample data...", bold=True))
            import pandas as pd

            sample_path = Path(sample_data)
            if sample_path.suffix == ".json":
                with open(sample_path) as f:
                    data = json.load(f)
                df = pd.DataFrame(data if isinstance(data, list) else [data])
            elif sample_path.suffix == ".csv":
                df = pd.read_csv(sample_path)
            else:
                raise click.ClickException(f"Unsupported file type: {sample_path.suffix}")

            click.echo(f"   Loaded {len(df)} samples")

            # Create mock request
            class MockConfig:
                parameters = {}
                input_mappings = {}

            class MockRequest:
                extractor_config = MockConfig()

            # Build and run pipeline
            result = pipeline.build_steps(MockRequest())
            steps = result.get("steps", [])
            prepare = result.get("prepare", lambda x: x)

            # Process through pipeline
            processed = df
            for step in steps:
                if callable(step):
                    processed = step(processed)

            click.echo(f"   Output columns: {list(processed.columns)}")
            if verbose:
                click.echo(f"   Sample output:\n{processed.head()}")
            click.echo(click.style("   Sample data: OK", fg="green"))

        click.echo()
        click.echo(click.style("All validations passed!", fg="green", bold=True))

    except ImportError as e:
        raise click.ClickException(f"Import error: {e}")
    finally:
        sys.path.remove(str(plugin_path.parent))


@plugin.command()
@click.option(
    "--path",
    "-p",
    type=click.Path(exists=True),
    default=".",
    help="Plugin directory path",
)
def validate(path: str) -> None:
    """Validate plugin structure and schemas.

    \b
    Checks that the plugin has all required files and valid schemas.
    """
    # Reuse test command with no sample data
    ctx = click.get_current_context()
    ctx.invoke(test, path=path, sample_data=None, verbose=False)


@plugin.command()
@click.option(
    "--path",
    "-p",
    type=click.Path(exists=True),
    default=".",
    help="Plugin directory path",
)
@click.option(
    "--namespace",
    "-n",
    envvar="MIXPEEK_NAMESPACE",
    help="Target namespace ID (or set MIXPEEK_NAMESPACE)",
)
@click.option(
    "--dry-run",
    is_flag=True,
    help="Validate without actually publishing",
)
@click.pass_context
def publish(ctx: click.Context, path: str, namespace: str | None, dry_run: bool) -> None:
    """Publish plugin to your namespace.

    \b
    Uploads the plugin to Mixpeek for use in your namespace.
    Requires API key and namespace to be set.

    \b
    Examples:
        mixpeek plugin publish
        mixpeek plugin publish -n ns_abc123
        mixpeek plugin publish --dry-run
    """
    api_key = ctx.obj.get("api_key") if ctx.obj else None
    base_url = ctx.obj.get("base_url", "https://api.mixpeek.com") if ctx.obj else "https://api.mixpeek.com"

    if not api_key and not dry_run:
        raise click.ClickException(
            "API key required. Set MIXPEEK_API_KEY or use --api-key"
        )

    if not namespace and not dry_run:
        raise click.ClickException(
            "Namespace required. Set MIXPEEK_NAMESPACE or use --namespace"
        )

    plugin_path = Path(path).resolve()

    click.echo(f"Publishing plugin from: {plugin_path}")
    if dry_run:
        click.echo(click.style("(DRY RUN - no changes will be made)", fg="yellow"))
    click.echo()

    # Validate first
    click.echo(click.style("1. Validating plugin...", bold=True))
    ctx.invoke(validate, path=path)
    click.echo()

    # Load metadata
    sys.path.insert(0, str(plugin_path.parent))
    plugin_name = plugin_path.name

    try:
        manifest = __import__(f"{plugin_name}.manifest", fromlist=["metadata"])
        metadata = manifest.metadata

        click.echo(click.style("2. Preparing package...", bold=True))
        click.echo(f"   Name: {metadata.get('name')}")
        click.echo(f"   Version: {metadata.get('version')}")

        if dry_run:
            click.echo()
            click.echo(click.style("Dry run complete. Plugin is ready to publish.", fg="green"))
            return

        # Create tarball
        click.echo("   Creating archive...")
        with tempfile.TemporaryDirectory() as tmpdir:
            archive_base = Path(tmpdir) / plugin_name
            # make_archive returns the path with extension
            archive_path = shutil.make_archive(
                str(archive_base),
                "gztar",
                plugin_path.parent,
                plugin_name,
            )

            # Get archive size
            archive_size = os.path.getsize(archive_path)
            click.echo(f"   Archive size: {archive_size / 1024:.1f} KB")

            click.echo()
            click.echo(click.style("3. Uploading to Mixpeek (via presigned URL)...", bold=True))

            import httpx

            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            }

            # Convert version format: "v1" -> "1.0.0" or use as-is if already semver
            version = metadata.get("version", "1.0.0")
            if version.startswith("v") and "." not in version:
                # Simple version like "v1" -> "1.0.0"
                version = f"{version[1:]}.0.0"

            # Step 1: Get presigned URL
            click.echo("   Requesting upload URL...")
            presigned_response = httpx.post(
                f"{base_url}/v1/namespaces/{namespace}/plugins/uploads",
                json={
                    "name": metadata.get("name", plugin_name),
                    "version": version,
                    "description": metadata.get("description", ""),
                    "file_size_bytes": archive_size,
                },
                headers=headers,
                timeout=30.0,
            )

            if presigned_response.status_code != 200:
                click.echo(click.style(f"   Failed to get upload URL: {presigned_response.status_code}", fg="red"))
                click.echo(f"   Error: {presigned_response.text}")
                raise click.ClickException("Failed to get presigned URL")

            presigned_data = presigned_response.json()
            upload_id = presigned_data["upload_id"]
            presigned_url = presigned_data["presigned_url"]

            click.echo(f"   Upload ID: {upload_id}")

            # Step 2: Upload to S3 via presigned URL
            click.echo("   Uploading archive to S3...")
            with open(archive_path, "rb") as f:
                archive_content = f.read()

            upload_response = httpx.put(
                presigned_url,
                content=archive_content,
                headers={"Content-Type": "application/gzip"},
                timeout=120.0,  # 2 minute timeout for large files
            )

            if upload_response.status_code not in [200, 201, 204]:
                click.echo(click.style(f"   S3 upload failed: {upload_response.status_code}", fg="red"))
                click.echo(f"   Error: {upload_response.text}")
                raise click.ClickException("Failed to upload to S3")

            # Get ETag from S3 response for integrity check
            etag = upload_response.headers.get("ETag", "").strip('"')
            click.echo(f"   S3 upload complete (ETag: {etag[:8]}...)")

            # Step 3: Confirm upload
            click.echo("   Confirming upload...")
            confirm_response = httpx.post(
                f"{base_url}/v1/namespaces/{namespace}/plugins/uploads/{upload_id}/confirm",
                json={
                    "etag": etag,
                    "file_size_bytes": archive_size,
                },
                headers=headers,
                timeout=60.0,
            )

            if confirm_response.status_code == 200:
                result = confirm_response.json()
                if result.get("success"):
                    click.echo(click.style("   Validation: PASSED", fg="green"))
                    click.echo()
                    click.echo(click.style("Plugin published successfully!", fg="green", bold=True))
                    click.echo()
                    click.echo("Your plugin is now available as:")
                    click.echo(f"  Name: {metadata.get('name')}")
                    click.echo(f"  Version: {version}")
                    click.echo(f"  Namespace: {namespace}")
                    if result.get("plugin_id"):
                        click.echo(f"  Plugin ID: {result['plugin_id']}")
                    if result.get("feature_uri"):
                        click.echo(f"  Feature URI: {result['feature_uri']}")
                else:
                    click.echo(click.style("   Validation: FAILED", fg="red"))
                    if result.get("validation_errors"):
                        for error in result["validation_errors"]:
                            click.echo(f"   - {error}")
                    raise click.ClickException("Plugin validation failed")
            else:
                click.echo(click.style(f"   Confirm failed: {confirm_response.status_code}", fg="red"))
                click.echo(f"   Error: {confirm_response.text}")
                raise click.ClickException("Failed to confirm upload")

    finally:
        sys.path.remove(str(plugin_path.parent))


@plugin.command("list")
@click.option(
    "--namespace",
    "-n",
    envvar="MIXPEEK_NAMESPACE",
    help="Namespace ID (or set MIXPEEK_NAMESPACE)",
)
@click.option(
    "--source",
    "-s",
    type=click.Choice(["all", "builtin", "custom", "community"]),
    default="all",
    help="Filter by source type",
)
@click.pass_context
def list_plugins(ctx: click.Context, namespace: str | None, source: str) -> None:
    """List available plugins.

    \b
    Shows all extractors available in your namespace.

    \b
    Examples:
        mixpeek plugin list
        mixpeek plugin list -s builtin
        mixpeek plugin list -n ns_abc123
    """
    api_key = ctx.obj.get("api_key") if ctx.obj else None
    base_url = ctx.obj.get("base_url", "https://api.mixpeek.com") if ctx.obj else "https://api.mixpeek.com"

    if not api_key:
        raise click.ClickException(
            "API key required. Set MIXPEEK_API_KEY or use --api-key"
        )

    import httpx

    headers = {"Authorization": f"Bearer {api_key}"}
    if namespace:
        headers["X-Namespace"] = namespace

    response = httpx.get(
        f"{base_url}/v1/collections/features/extractors",
        headers=headers,
        timeout=30.0,
    )

    if response.status_code != 200:
        raise click.ClickException(f"API error: {response.status_code} - {response.text}")

    extractors = response.json()

    # Filter by source if specified
    if source != "all":
        extractors = [e for e in extractors if e.get("source", "builtin") == source]

    if not extractors:
        click.echo("No plugins found.")
        return

    click.echo(f"Found {len(extractors)} plugin(s):\n")

    for ext in extractors:
        source_badge = ext.get("source", "builtin").upper()
        source_color = {
            "builtin": "blue",
            "custom": "green",
            "community": "magenta",
        }.get(ext.get("source", "builtin"), "white")

        click.echo(
            f"  {click.style(ext['feature_extractor_name'], bold=True)} "
            f"({ext['version']}) "
            f"[{click.style(source_badge, fg=source_color)}]"
        )
        click.echo(f"    {ext.get('description', 'No description')[:60]}...")
        click.echo()
