"""Deploy plugin to Mixpeek production."""

import asyncio
import io
import os
import zipfile
from pathlib import Path
from typing import Optional

import click
import httpx
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn

from mixpeek_dev.testing.validators import ManifestValidator, SecurityValidator
from mixpeek_dev.utils.logger import get_logger

console = Console()
logger = get_logger()


@click.command()
@click.option(
    "--plugin",
    type=Path,
    default=Path.cwd(),
    help="Path to plugin directory (default: current directory)",
)
@click.option(
    "--namespace-id",
    type=str,
    envvar="MIXPEEK_NAMESPACE_ID",
    help="Namespace ID (can also set MIXPEEK_NAMESPACE_ID env var)",
)
@click.option(
    "--api-key",
    type=str,
    envvar="MIXPEEK_API_KEY",
    help="Mixpeek API key (can also set MIXPEEK_API_KEY env var)",
)
@click.option(
    "--api-url",
    type=str,
    default="https://api.mixpeek.com",
    envvar="MIXPEEK_API_URL",
    help="Mixpeek API base URL (default: https://api.mixpeek.com)",
)
@click.option(
    "--deploy/--no-deploy",
    default=True,
    help="Automatically deploy after upload (default: True)",
)
@click.option(
    "--description",
    type=str,
    help="Plugin description (optional)",
)
def push(
    plugin: Path,
    namespace_id: Optional[str],
    api_key: Optional[str],
    api_url: str,
    deploy: bool,
    description: Optional[str],
):
    """Deploy plugin to Mixpeek production.

    This command:
    1. Validates the plugin locally
    2. Packages it into a .zip archive
    3. Uploads to Mixpeek
    4. Optionally deploys for realtime inference

    \b
    Examples:
        # Deploy current directory plugin
        $ mixpeek push

        # Deploy specific plugin
        $ mixpeek push --plugin=./my_plugin

        # Upload without deploying
        $ mixpeek push --no-deploy

        # Specify namespace and API key inline
        $ mixpeek push --namespace-id=ns_xxx --api-key=pk_xxx

    \b
    Environment Variables:
        MIXPEEK_NAMESPACE_ID - Default namespace ID
        MIXPEEK_API_KEY      - API key for authentication
        MIXPEEK_API_URL      - API base URL (default: https://api.mixpeek.com)
    """
    asyncio.run(_push_async(plugin, namespace_id, api_key, api_url, deploy, description))


async def _push_async(
    plugin: Path,
    namespace_id: Optional[str],
    api_key: Optional[str],
    api_url: str,
    deploy: bool,
    description: Optional[str],
):
    """Async implementation of push command."""

    # Validate required parameters
    if not namespace_id:
        console.print(
            "[red]Error:[/red] Namespace ID is required.\n\n"
            "Provide it via:\n"
            "  --namespace-id=ns_xxx\n"
            "  OR set MIXPEEK_NAMESPACE_ID environment variable"
        )
        raise click.Abort()

    if not api_key:
        console.print(
            "[red]Error:[/red] API key is required.\n\n"
            "Provide it via:\n"
            "  --api-key=pk_xxx\n"
            "  OR set MIXPEEK_API_KEY environment variable"
        )
        raise click.Abort()

    # Resolve plugin path
    plugin_path = plugin.resolve()
    if not plugin_path.exists():
        console.print(f"[red]Error:[/red] Plugin directory not found: {plugin_path}")
        raise click.Abort()

    console.print(Panel(
        f"[bold]Deploying Plugin to Mixpeek[/bold]\n\n"
        f"Plugin: {plugin_path.name}\n"
        f"Namespace: {namespace_id}\n"
        f"API: {api_url}",
        border_style="blue",
    ))

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:

        # Step 1: Validate manifest
        task = progress.add_task("[cyan]Validating manifest...", total=None)
        manifest_validator = ManifestValidator(plugin_path)
        manifest_result = manifest_validator.validate()

        if not manifest_result.passed:
            progress.stop()
            console.print("\n[red]✗ Manifest validation failed:[/red]")
            for error in manifest_result.errors:
                console.print(f"  • {error}")
            raise click.Abort()

        progress.update(task, description="[green]✓ Manifest validated")

        # Step 2: Security scan
        task = progress.add_task("[cyan]Running security scan...", total=None)
        security_validator = SecurityValidator(plugin_path)
        security_result = security_validator.validate()

        if not security_result.passed:
            progress.stop()
            console.print("\n[red]✗ Security validation failed:[/red]")
            for error in security_result.errors:
                console.print(f"  • {error}")
            raise click.Abort()

        if security_result.warnings:
            progress.stop()
            console.print("\n[yellow]⚠ Security warnings:[/yellow]")
            for warning in security_result.warnings:
                console.print(f"  • {warning}")

            if not click.confirm("\nContinue with deployment?"):
                raise click.Abort()

            progress.start()

        progress.update(task, description="[green]✓ Security scan passed")

        # Step 3: Package plugin
        task = progress.add_task("[cyan]Packaging plugin...", total=None)

        # Load manifest to get name and version
        manifest_module = _load_manifest(plugin_path)
        plugin_name = manifest_module.feature_extractor_name
        plugin_version = manifest_module.version

        # Create zip archive in memory
        zip_buffer = io.BytesIO()
        _create_plugin_archive(plugin_path, zip_buffer)
        zip_size = len(zip_buffer.getvalue())

        progress.update(
            task,
            description=f"[green]✓ Plugin packaged ({zip_size / 1024:.1f} KB)",
        )

        # Step 4: Get presigned URL
        task = progress.add_task("[cyan]Getting upload URL...", total=None)

        async with httpx.AsyncClient(timeout=30.0) as client:
            # Request presigned URL
            upload_url = f"{api_url}/v1/namespaces/{namespace_id}/plugins/uploads"
            headers = {"Authorization": f"Bearer {api_key}"}

            upload_request = {
                "name": plugin_name,
                "version": plugin_version,
                "description": description or f"Custom plugin: {plugin_name}",
            }

            try:
                response = await client.post(
                    upload_url,
                    json=upload_request,
                    headers=headers,
                )
                response.raise_for_status()
                upload_data = response.json()

                presigned_url = upload_data["presigned_url"]
                upload_id = upload_data["upload_id"]

                progress.update(task, description="[green]✓ Upload URL obtained")

            except httpx.HTTPStatusError as e:
                progress.stop()
                console.print(f"\n[red]✗ Failed to get upload URL:[/red]")
                console.print(f"  Status: {e.response.status_code}")
                console.print(f"  Error: {e.response.text}")
                raise click.Abort()
            except Exception as e:
                progress.stop()
                console.print(f"\n[red]✗ Failed to get upload URL:[/red] {e}")
                raise click.Abort()

            # Step 5: Upload to S3
            task = progress.add_task(
                f"[cyan]Uploading plugin ({zip_size / 1024:.1f} KB)...",
                total=None,
            )

            try:
                zip_buffer.seek(0)
                response = await client.put(
                    presigned_url,
                    content=zip_buffer.getvalue(),
                    headers={"Content-Type": "application/zip"},
                )
                response.raise_for_status()

                # Get ETag from response headers
                etag = response.headers.get("ETag", "").strip('"')

                progress.update(task, description="[green]✓ Plugin uploaded to S3")

            except httpx.HTTPStatusError as e:
                progress.stop()
                console.print(f"\n[red]✗ Failed to upload plugin:[/red]")
                console.print(f"  Status: {e.response.status_code}")
                raise click.Abort()
            except Exception as e:
                progress.stop()
                console.print(f"\n[red]✗ Failed to upload plugin:[/red] {e}")
                raise click.Abort()

            # Step 6: Confirm upload
            task = progress.add_task("[cyan]Confirming upload...", total=None)

            confirm_url = (
                f"{api_url}/v1/namespaces/{namespace_id}"
                f"/plugins/uploads/{upload_id}/confirm"
            )

            confirm_request = {
                "etag": etag if etag else None,
                "file_size_bytes": zip_size,
            }

            try:
                response = await client.post(
                    confirm_url,
                    json=confirm_request,
                    headers=headers,
                )
                response.raise_for_status()
                confirm_data = response.json()

                plugin_id = confirm_data["plugin_id"]
                feature_uri = confirm_data["feature_uri"]
                validation_status = confirm_data["validation_status"]

                progress.update(task, description="[green]✓ Upload confirmed")

            except httpx.HTTPStatusError as e:
                progress.stop()
                console.print(f"\n[red]✗ Failed to confirm upload:[/red]")
                console.print(f"  Status: {e.response.status_code}")
                console.print(f"  Error: {e.response.text}")
                raise click.Abort()
            except Exception as e:
                progress.stop()
                console.print(f"\n[red]✗ Failed to confirm upload:[/red] {e}")
                raise click.Abort()

            # Step 7: Deploy (if requested)
            deployment_status = "uploaded"

            if deploy:
                task = progress.add_task("[cyan]Deploying plugin...", total=None)

                deploy_url = (
                    f"{api_url}/v1/namespaces/{namespace_id}"
                    f"/plugins/{plugin_id}/deploy"
                )

                try:
                    response = await client.post(
                        deploy_url,
                        headers=headers,
                    )
                    response.raise_for_status()
                    deploy_data = response.json()

                    deployment_status = deploy_data.get("status", "deployed")
                    deployment_type = deploy_data.get("deployment_type", "unknown")

                    if deployment_status == "queued":
                        progress.update(
                            task,
                            description="[yellow]⏳ Deployment queued (will complete in ~3-5 minutes)",
                        )
                    elif deployment_status == "deployed":
                        if deployment_type == "batch_only":
                            progress.update(
                                task,
                                description="[green]✓ Deployed for batch processing",
                            )
                        else:
                            progress.update(
                                task,
                                description="[green]✓ Plugin deployed",
                            )
                    else:
                        progress.update(
                            task,
                            description=f"[yellow]⚠ Deployment status: {deployment_status}",
                        )

                except httpx.HTTPStatusError as e:
                    progress.stop()
                    console.print(f"\n[yellow]⚠ Deployment request failed:[/yellow]")
                    console.print(f"  Status: {e.response.status_code}")
                    console.print(f"  Plugin uploaded but not deployed.")
                    console.print(f"  Deploy manually via: mixpeek push --plugin={plugin_path}")
                    deployment_status = "upload_only"
                except Exception as e:
                    progress.stop()
                    console.print(f"\n[yellow]⚠ Deployment failed:[/yellow] {e}")
                    console.print(f"  Plugin uploaded but not deployed.")
                    deployment_status = "upload_only"

    # Print success summary
    console.print("\n" + "=" * 60)
    console.print(Panel(
        f"[bold green]✓ Plugin Deployed Successfully![/bold green]\n\n"
        f"[cyan]Plugin ID:[/cyan] {plugin_id}\n"
        f"[cyan]Feature URI:[/cyan] {feature_uri}\n"
        f"[cyan]Validation:[/cyan] {validation_status}\n"
        f"[cyan]Deployment:[/cyan] {deployment_status}\n\n"
        f"[dim]Use this feature_uri when creating collections.[/dim]",
        border_style="green",
    ))

    # Print next steps
    if deployment_status == "queued":
        console.print("\n[bold]Next Steps:[/bold]")
        console.print(
            f"  • Check deployment status: "
            f"GET {api_url}/v1/namespaces/{namespace_id}/plugins/{plugin_id}/status"
        )
        console.print("  • Deployment typically completes in 3-5 minutes")

    if deployment_status == "deployed":
        console.print("\n[bold]Your plugin is ready to use![/bold]")
        console.print(f"  • Test with: mixpeek test --environment=production")


def _load_manifest(plugin_path: Path):
    """Load the manifest module from the plugin."""
    import importlib.util
    import sys

    manifest_file = plugin_path / "manifest.py"

    if not manifest_file.exists():
        raise FileNotFoundError(
            f"manifest.py not found in {plugin_path}\n\n"
            "A plugin requires a manifest.py file with metadata."
        )

    spec = importlib.util.spec_from_file_location("manifest", manifest_file)
    if spec is None or spec.loader is None:
        raise ImportError(f"Failed to load manifest from {manifest_file}")

    manifest_module = importlib.util.module_from_spec(spec)
    sys.modules["manifest"] = manifest_module
    spec.loader.exec_module(manifest_module)

    return manifest_module


def _create_plugin_archive(plugin_path: Path, output_buffer: io.BytesIO):
    """Create a zip archive of the plugin.

    Includes:
    - manifest.py (required)
    - pipeline.py (required)
    - realtime.py (optional)
    - models/ directory (optional)
    - Any other .py files
    """
    with zipfile.ZipFile(output_buffer, "w", zipfile.ZIP_DEFLATED) as zf:
        # Add required files
        _add_file_to_zip(zf, plugin_path, "manifest.py", required=True)
        _add_file_to_zip(zf, plugin_path, "pipeline.py", required=True)

        # Add optional files
        _add_file_to_zip(zf, plugin_path, "realtime.py", required=False)
        _add_file_to_zip(zf, plugin_path, "batch.py", required=False)

        # Add models directory if it exists
        models_dir = plugin_path / "models"
        if models_dir.exists() and models_dir.is_dir():
            for model_file in models_dir.rglob("*"):
                if model_file.is_file():
                    arcname = str(model_file.relative_to(plugin_path))
                    zf.write(model_file, arcname)

        # Add any other Python files in root
        for py_file in plugin_path.glob("*.py"):
            if py_file.name not in ["manifest.py", "pipeline.py", "realtime.py", "batch.py"]:
                _add_file_to_zip(zf, plugin_path, py_file.name, required=False)


def _add_file_to_zip(
    zf: zipfile.ZipFile,
    plugin_path: Path,
    filename: str,
    required: bool = False,
):
    """Add a file to the zip archive."""
    file_path = plugin_path / filename

    if not file_path.exists():
        if required:
            raise FileNotFoundError(
                f"Required file not found: {filename}\n\n"
                f"Plugin must contain {filename}"
            )
        return

    zf.write(file_path, filename)
