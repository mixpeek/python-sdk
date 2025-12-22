#!/usr/bin/env python3
"""
Auto-increment the patch version in setup.py
Outputs the new version to GitHub Actions output
"""

import re
import sys
from pathlib import Path


def get_current_version(setup_file: Path) -> str:
    """Extract current version from setup.py"""
    content = setup_file.read_text()
    match = re.search(r"version=['\"]([^'\"]+)['\"]", content)
    if not match:
        raise ValueError("Could not find version in setup.py")
    return match.group(1)


def increment_patch_version(version: str) -> str:
    """Increment the patch version (e.g., 0.11.2 -> 0.11.3)"""
    parts = version.split(".")
    if len(parts) != 3:
        raise ValueError(f"Invalid version format: {version}. Expected X.Y.Z")

    major, minor, patch = parts
    new_patch = int(patch) + 1
    return f"{major}.{minor}.{new_patch}"


def update_setup_file(setup_file: Path, old_version: str, new_version: str):
    """Update version in setup.py"""
    content = setup_file.read_text()
    updated_content = re.sub(
        rf"version=['\"]({re.escape(old_version)})['\"]",
        f'version="{new_version}"',
        content,
    )
    setup_file.write_text(updated_content)


def main():
    repo_root = Path(__file__).parent.parent
    setup_file = repo_root / "setup.py"

    if not setup_file.exists():
        print("Error: setup.py not found", file=sys.stderr)
        sys.exit(1)

    try:
        # Get current version
        current_version = get_current_version(setup_file)
        print(f"Current version: {current_version}", file=sys.stderr)

        # Increment version
        new_version = increment_patch_version(current_version)
        print(f"New version: {new_version}", file=sys.stderr)

        # Update setup.py
        update_setup_file(setup_file, current_version, new_version)
        print(f"Updated setup.py with version {new_version}", file=sys.stderr)

        # Output for GitHub Actions
        print(f"new_version={new_version}")
        print(f"old_version={current_version}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
