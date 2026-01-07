"""Mixpeek CLI for plugin development.

Commands:
    mixpeek plugin init <name>    - Create a new plugin from template
    mixpeek plugin test           - Test plugin locally
    mixpeek plugin publish        - Publish plugin to namespace
    mixpeek plugin list           - List available plugins
"""

from mixpeek.cli.main import cli

__all__ = ["cli"]
