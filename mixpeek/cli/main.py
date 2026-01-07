"""Main CLI entry point for Mixpeek."""

import click

from mixpeek.cli.plugin import plugin


@click.group()
@click.version_option(package_name="mixpeek")
@click.option(
    "--api-key",
    envvar="MIXPEEK_API_KEY",
    help="Mixpeek API key (or set MIXPEEK_API_KEY env var)",
)
@click.option(
    "--base-url",
    envvar="MIXPEEK_BASE_URL",
    default="https://api.mixpeek.com",
    help="Mixpeek API base URL",
)
@click.pass_context
def cli(ctx: click.Context, api_key: str | None, base_url: str) -> None:
    """Mixpeek CLI - Build, test, and publish custom extractors.

    \b
    Examples:
        mixpeek plugin init my_extractor     Create new plugin
        mixpeek plugin test                  Test locally
        mixpeek plugin publish               Publish to your namespace
    """
    ctx.ensure_object(dict)
    ctx.obj["api_key"] = api_key
    ctx.obj["base_url"] = base_url


# Register command groups
cli.add_command(plugin)


def main() -> None:
    """Entry point for the CLI."""
    cli()


if __name__ == "__main__":
    main()
