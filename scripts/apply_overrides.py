#!/usr/bin/env python3
"""
Apply method name overrides and exclusions from sdk-config.yml
Modifies generated Python SDK code based on configuration
"""

import re
import yaml
from pathlib import Path
from typing import Dict, List, Set


def load_config(config_file: Path) -> dict:
    """Load SDK configuration from YAML file"""
    with open(config_file, 'r') as f:
        return yaml.safe_load(f)


def find_python_files(directory: Path) -> List[Path]:
    """Recursively find all Python files in directory"""
    return list(directory.rglob("*.py"))


def apply_method_renames(file_path: Path, overrides: Dict[str, str]):
    """Apply method name overrides to a Python file"""
    if not overrides:
        return

    content = file_path.read_text()
    modified = False

    for old_name, new_name in overrides.items():
        # Pattern to match function/method definitions
        def_pattern = rf"\bdef {re.escape(old_name)}\("
        new_def = f"def {new_name}("

        if re.search(def_pattern, content):
            content = re.sub(def_pattern, new_def, content)
            modified = True
            print(f"  Renamed method: {old_name} -> {new_name} in {file_path.name}")

    if modified:
        file_path.write_text(content)


def should_exclude_file(file_path: Path, exclude_operations: List[str]) -> bool:
    """Check if a file should be excluded based on operation names"""
    if not exclude_operations:
        return False

    file_name = file_path.stem

    # Check if file name matches any excluded operation
    for excluded_op in exclude_operations:
        # Convert camelCase to snake_case for comparison
        snake_case_op = re.sub(r'(?<!^)(?=[A-Z])', '_', excluded_op).lower()
        if snake_case_op in file_name.lower():
            return True

    return False


def remove_excluded_operations(api_dir: Path, exclude_operations: List[str], exclude_tags: List[str]):
    """Remove excluded operations and tags from generated code"""
    if not api_dir.exists():
        print("Warning: API directory not found, skipping exclusions")
        return

    if not exclude_operations and not exclude_tags:
        return

    print(f"\nApplying exclusions:")
    print(f"  Excluded operations: {exclude_operations or 'none'}")
    print(f"  Excluded tags: {exclude_tags or 'none'}")

    # Remove excluded operation files
    for python_file in find_python_files(api_dir):
        if should_exclude_file(python_file, exclude_operations):
            print(f"  Excluding: {python_file.relative_to(api_dir)}")
            python_file.unlink()

    # Remove excluded tag directories
    for tag in exclude_tags:
        tag_dir = api_dir / tag.lower().replace(" ", "_").replace("/", "_")
        if tag_dir.exists() and tag_dir.is_dir():
            print(f"  Excluding tag directory: {tag_dir.name}")
            import shutil
            shutil.rmtree(tag_dir)


def update_imports(package_dir: Path, overrides: Dict[str, str]):
    """Update __init__.py files to reflect renamed methods"""
    if not overrides:
        return

    init_files = [f for f in package_dir.rglob("__init__.py")]

    for init_file in init_files:
        content = init_file.read_text()
        modified = False

        for old_name, new_name in overrides.items():
            # Update imports like: from .module import old_name
            import_pattern = rf"\bfrom\s+\.\S+\s+import\s+([^,\n]*\b{re.escape(old_name)}\b[^,\n]*)"
            if re.search(import_pattern, content):
                content = re.sub(
                    rf"\b{re.escape(old_name)}\b",
                    new_name,
                    content
                )
                modified = True

        if modified:
            init_file.write_text(content)
            print(f"  Updated imports in: {init_file.relative_to(package_dir)}")


def main():
    repo_root = Path(__file__).parent.parent
    config_file = repo_root / "sdk-config.yml"
    package_dir = repo_root / "mixpeek"

    if not config_file.exists():
        print("Warning: sdk-config.yml not found, skipping overrides")
        return

    print("Applying SDK configuration overrides...")

    # Load configuration
    config = load_config(config_file)

    # Extract configuration sections
    method_overrides = config.get('method_overrides') or {}
    exclude_operations = config.get('exclude_operations') or []
    exclude_tags = config.get('exclude_tags') or []

    # Apply method renames
    if method_overrides:
        print(f"\nApplying method renames: {len(method_overrides)} override(s)")
        for python_file in find_python_files(package_dir):
            apply_method_renames(python_file, method_overrides)

        # Update imports to reflect renames
        update_imports(package_dir, method_overrides)

    # Remove excluded operations
    api_dir = package_dir / "api"
    remove_excluded_operations(api_dir, exclude_operations, exclude_tags)

    print("\nOverrides applied successfully!")


if __name__ == "__main__":
    main()
