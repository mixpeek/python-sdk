"""Main CLI entry point for Mixpeek development tools.

This module provides the `mixpeek` command-line interface.

**Self-Documenting Design:**

The CLI is designed to be self-documenting:
- Clear help messages for every command
- Examples in command descriptions
- Helpful error messages that suggest solutions
- Rich formatted output when available

**Example Usage:**

```bash
# Show help
mixpeek --help

# Test plugin
mixpeek test --mock

# Create new plugin
mixpeek init my_plugin --template=basic_text

# Validate plugin
mixpeek validate

# Deploy plugin
mixpeek push
```
"""

try:
    import click
except ImportError:
    raise ImportError(
        "click is required for the Mixpeek CLI.\n"
        "Install with: pip install 'mixpeek[dev]'"
    )

from mixpeek_dev import __version__


@click.group()
@click.version_option(version=__version__, prog_name="mixpeek")
def cli():
    """Mixpeek Development Tools - Build, test, and deploy custom plugins.

    **Quick Start:**

    \b
    1. Create a new plugin:
       $ mixpeek init my_plugin --template=basic_text

    \b
    2. Test locally with mock services:
       $ cd my_plugin
       $ mixpeek test --mock

    \b
    3. Validate before deployment:
       $ mixpeek validate

    \b
    4. Deploy to production:
       $ mixpeek push

    **Philosophy:**

    This CLI is designed to be self-documenting and LLM-friendly.
    Every command provides clear help messages and examples.

    **Getting Help:**

    \b
    - Command help: mixpeek <command> --help
    - Documentation: https://docs.mixpeek.com/plugins
    - Support: support@mixpeek.com
    """
    pass


# Import commands after defining the group to avoid circular imports
from mixpeek_dev.cli.init import init
from mixpeek_dev.cli.push import push
from mixpeek_dev.cli.test import test

cli.add_command(init)
cli.add_command(test)
cli.add_command(push)


if __name__ == "__main__":
    cli()
