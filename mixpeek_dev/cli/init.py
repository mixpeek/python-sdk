"""Init command for creating new plugins from templates.

This module implements the `mixpeek init` command which scaffolds new plugin projects.

**Self-Documenting Design:**

The init command:
- Creates all necessary files from templates
- Includes extensive inline documentation
- Provides working examples out of the box
- Suggests next steps after creation

**Example:**

```bash
$ mixpeek init fashion_extractor --template=basic_text

Creating plugin: fashion_extractor
✓ Created manifest.py
✓ Created pipeline.py
✓ Created realtime.py
✓ Created README.md

Next steps:
1. cd fashion_extractor
2. Edit pipeline.py to implement your extraction logic
3. Test: mixpeek test --mock
4. Deploy: mixpeek push
```
"""

import re
from pathlib import Path

try:
    import click
    from jinja2 import Environment, FileSystemLoader
except ImportError as e:
    raise ImportError(
        f"{str(e)}\n"
        "jinja2 is required for mixpeek init.\n"
        "Install with: pip install 'mixpeek[dev]'"
    )

from mixpeek_dev.utils import get_logger


@click.command()
@click.argument("plugin_name")
@click.option(
    "--template",
    type=click.Choice(["basic_text"], case_sensitive=False),
    default="basic_text",
    help="Plugin template to use (default: basic_text)",
)
@click.option(
    "--description",
    type=str,
    help="Plugin description (will be prompted if not provided)",
)
@click.option(
    "--output-dir",
    type=click.Path(file_okay=False, dir_okay=True, path_type=Path),
    default=Path.cwd(),
    help="Directory to create plugin in (default: current directory)",
)
def init(plugin_name: str, template: str, description: str, output_dir: Path):
    """Create a new plugin from a template.

    **Examples:**

    \b
    # Create a text embedding plugin
    $ mixpeek init my_embedder --template=basic_text

    \b
    # Create with custom description
    $ mixpeek init fashion_extractor \\
        --description="Extract fashion attributes from product descriptions"

    \b
    # Create in specific directory
    $ mixpeek init my_plugin --output-dir=~/plugins/

    **Templates:**

    \b
    basic_text:
      Perfect for: Text embeddings, NLP tasks, text classification
      Includes: Hash-based embedding example, fully documented
      Use when: Working with text data

    **After Creation:**

    \b
    1. Navigate to plugin directory: cd {plugin_name}
    2. Review manifest.py (plugin metadata)
    3. Implement pipeline.py (batch processing logic)
    4. Implement realtime.py (realtime inference logic)
    5. Test locally: mixpeek test --mock
    6. Deploy: mixpeek push

    **Self-Documenting:**

    Generated files include extensive documentation:
    - What each file does and why
    - How to modify for your use case
    - Examples of common patterns
    - Tips for AI assistants
    """
    logger = get_logger()

    # Validate plugin name
    if not _is_valid_plugin_name(plugin_name):
        logger.error(
            f"Invalid plugin name: '{plugin_name}'\n\n"
            f"Plugin names must:\n"
            f"  - Start with a lowercase letter\n"
            f"  - Contain only lowercase letters, numbers, and underscores\n"
            f"  - Use snake_case (e.g., 'my_plugin', 'fashion_extractor')\n\n"
            f"Examples:\n"
            f"  ✓ fashion_extractor\n"
            f"  ✓ sentiment_v2\n"
            f"  ✓ brand_detector\n"
            f"  ✗ FashionExtractor (use lowercase)\n"
            f"  ✗ fashion-extractor (use underscores)\n"
            f"  ✗ 123plugin (must start with letter)"
        )
        return

    # Prompt for description if not provided
    if not description:
        description = click.prompt(
            "Plugin description",
            default=f"Custom {plugin_name} feature extractor",
            type=str,
        )

    # Create plugin directory
    plugin_dir = output_dir / plugin_name
    if plugin_dir.exists():
        if not click.confirm(
            f"Directory '{plugin_dir}' already exists. Overwrite?",
            default=False,
        ):
            logger.info("Cancelled.")
            return

    plugin_dir.mkdir(parents=True, exist_ok=True)

    # Generate plugin files from template
    logger.info(f"\nCreating plugin: {plugin_name}")
    logger.info(f"Template: {template}")
    logger.info(f"Output directory: {plugin_dir}\n")

    try:
        _generate_plugin_from_template(
            plugin_name=plugin_name,
            description=description,
            template=template,
            output_dir=plugin_dir,
            logger=logger,
        )
    except Exception as e:
        logger.error(f"Failed to create plugin: {str(e)}")
        import traceback

        logger.error(traceback.format_exc())
        return

    # Show next steps
    logger.info(f"\n{'='*60}")
    logger.success(f"Plugin '{plugin_name}' created successfully!")
    logger.info(f"{'='*60}\n")

    logger.info("Next steps:\n")
    logger.info(f"  1. cd {plugin_name}")
    logger.info(f"  2. Review manifest.py (plugin metadata)")
    logger.info(f"  3. Edit pipeline.py (implement your extraction logic)")
    logger.info(f"  4. Edit realtime.py (implement realtime inference)")
    logger.info(f"  5. Test locally: mixpeek test --mock")
    logger.info(f"  6. Validate: mixpeek validate")
    logger.info(f"  7. Deploy: mixpeek push\n")


def _is_valid_plugin_name(name: str) -> bool:
    """Check if plugin name is valid.

    Rules:
    - Must start with lowercase letter
    - Can contain lowercase letters, numbers, underscores
    - Must use snake_case

    Args:
        name: Plugin name to validate

    Returns:
        True if valid, False otherwise

    Examples:
        >>> _is_valid_plugin_name("my_plugin")
        True
        >>> _is_valid_plugin_name("MyPlugin")
        False
        >>> _is_valid_plugin_name("123plugin")
        False
    """
    return bool(re.match(r"^[a-z][a-z0-9_]*$", name))


def _generate_plugin_from_template(
    plugin_name: str,
    description: str,
    template: str,
    output_dir: Path,
    logger,
):
    """Generate plugin files from Jinja2 templates.

    Args:
        plugin_name: Name of the plugin (snake_case)
        description: Plugin description
        template: Template name (e.g., "basic_text")
        output_dir: Directory to create files in
        logger: Logger instance
    """
    # Setup Jinja2 environment
    import mixpeek_dev.templates

    templates_dir = Path(mixpeek_dev.templates.__file__).parent / template
    if not templates_dir.exists():
        raise ValueError(f"Template '{template}' not found at {templates_dir}")

    env = Environment(loader=FileSystemLoader(str(templates_dir)))

    # Template context
    context = {
        "plugin_name": plugin_name,
        "plugin_class_name": _snake_to_pascal(plugin_name) + "InferenceService",
        "description": description,
    }

    # Generate files from templates
    template_files = {
        "manifest.py.j2": "manifest.py",
        "pipeline.py.j2": "pipeline.py",
        "realtime.py.j2": "realtime.py",
        "LLM_GUIDE.md.j2": "LLM_GUIDE.md",  # For AI assistants
    }

    for template_file, output_file in template_files.items():
        template_path = templates_dir / template_file
        if not template_path.exists():
            logger.warning(f"Template file not found: {template_file}")
            continue

        # Render template
        template_obj = env.get_template(template_file)
        rendered = template_obj.render(**context)

        # Write to output
        output_path = output_dir / output_file
        with open(output_path, "w") as f:
            f.write(rendered)

        logger.success(f"Created {output_file}")

    # Create README
    _create_readme(plugin_name, description, output_dir, logger)

    # Create models directory (for custom models)
    models_dir = output_dir / "models"
    models_dir.mkdir(exist_ok=True)
    (models_dir / ".gitkeep").touch()
    logger.success("Created models/ directory")

    # Create tests directory
    tests_dir = output_dir / "tests"
    tests_dir.mkdir(exist_ok=True)
    _create_test_file(plugin_name, tests_dir, logger)


def _snake_to_pascal(snake_str: str) -> str:
    """Convert snake_case to PascalCase.

    Args:
        snake_str: String in snake_case

    Returns:
        String in PascalCase

    Examples:
        >>> _snake_to_pascal("my_plugin")
        'MyPlugin'
        >>> _snake_to_pascal("fashion_extractor")
        'FashionExtractor'
    """
    return "".join(word.capitalize() for word in snake_str.split("_"))


def _create_readme(plugin_name: str, description: str, output_dir: Path, logger):
    """Create README.md with plugin documentation.

    Args:
        plugin_name: Plugin name
        description: Plugin description
        output_dir: Directory to create README in
        logger: Logger instance
    """
    readme_content = f"""# {plugin_name}

{description}

## 🤖 For AI Assistants

**If you're an LLM helping a user with this plugin:**
1. **READ** [LLM_GUIDE.md](LLM_GUIDE.md) first - it has everything you need
2. **UNDERSTAND** the structure before making changes
3. **TEST** after every change: `mixpeek test --mock`
4. **EXPLAIN** what you're doing and why

The LLM_GUIDE.md contains:
- Complete file structure explanation
- Common customization patterns
- Debugging guides
- Example conversations
- Quick reference

## Quick Start

```bash
# Test locally with mock services
mixpeek test --mock

# Test with verbose output
mixpeek test --mock --verbose

# Validate before deployment
mixpeek validate

# Deploy to production
mixpeek push
```

## Structure

- **manifest.py**: Plugin metadata and configuration
- **pipeline.py**: Batch processing pipeline
- **realtime.py**: Realtime inference service
- **models/**: Directory for custom model files
- **tests/**: Unit tests for your plugin

## Development Workflow

1. **Implement**: Edit pipeline.py and realtime.py
2. **Test**: Run `mixpeek test --mock` for fast iteration
3. **Validate**: Run `mixpeek validate` to check for issues
4. **Deploy**: Run `mixpeek push` to deploy to production

## Customization

### Using Custom Models

1. Add your model file to the `models/` directory:
   ```bash
   cp my_model.safetensors models/
   ```

2. Load in realtime.py:
   ```python
   from mixpeek_dev.models import load_custom_model

   def __init__(self):
       super().__init__()
       self.model = load_custom_model("./models/my_model.safetensors")
   ```

3. Test:
   ```bash
   mixpeek test --mock
   ```

### Using Mixpeek Services

Access builtin services (E5, Whisper, etc.) in pipeline.py:

```python
def build_steps(extractor_request, container=None, ...):
    # Get E5 embedding service
    e5 = container.inference.get("intfloat/e5-large")

    # Get Whisper transcription service
    whisper = container.inference.get("openai/whisper")

    # Add to pipeline
    steps = [whisper, e5]
    return {{"steps": steps, "prepare": lambda ds: ds}}
```

## Testing

Run tests with different modes:

```bash
# Mock mode (fast, no dependencies)
mixpeek test --mock

# Local stack mode (full E2E with Docker)
mixpeek test --local-stack

# Production mode (test deployed plugin)
mixpeek test --environment=production
```

## Documentation

All generated files include extensive inline documentation:
- What each component does
- How to customize for your use case
- Examples of common patterns
- Tips for AI assistants

## Support

- Documentation: https://docs.mixpeek.com/plugins
- Support: support@mixpeek.com
"""

    readme_path = output_dir / "README.md"
    with open(readme_path, "w") as f:
        f.write(readme_content)

    logger.success("Created README.md")


def _create_test_file(plugin_name: str, tests_dir: Path, logger):
    """Create basic test file.

    Args:
        plugin_name: Plugin name
        tests_dir: Tests directory
        logger: Logger instance
    """
    test_content = f'''"""Tests for {plugin_name} plugin."""

import pytest


def test_placeholder():
    """Placeholder test.

    Replace with actual tests for your plugin.

    Example:
    ```python
    from mixpeek_dev.testing import LocalTestRunner

    @pytest.mark.asyncio
    async def test_batch_processing():
        runner = LocalTestRunner("../", mode="mock")
        results = await runner.test_batch([{{"text": "test"}}])
        assert len(results) == 1
        assert "{plugin_name}_v1_embedding" in results[0]
    ```
    """
    assert True
'''

    test_path = tests_dir / "test_plugin.py"
    with open(test_path, "w") as f:
        f.write(test_content)

    logger.success("Created tests/test_plugin.py")
