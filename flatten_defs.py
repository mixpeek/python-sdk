#!/usr/bin/env python3
"""
Flatten nested $defs into components/schemas for OpenAPI Generator compatibility.

The OpenAPI Generator for Python doesn't support references to nested $defs,
so we need to move all $defs definitions to the top-level components/schemas.
"""

import json
import sys
from typing import Any, Dict


def collect_defs(obj: Any, collected: Dict[str, Any], path: str = "") -> None:
    """Recursively collect all $defs from the schema."""
    if isinstance(obj, dict):
        if '$defs' in obj:
            for name, definition in obj['$defs'].items():
                # Create unique name if needed (avoid collisions)
                unique_name = name
                counter = 1
                while unique_name in collected:
                    unique_name = f"{name}_{counter}"
                    counter += 1

                collected[unique_name] = definition

                # Recursively collect from nested defs
                collect_defs(definition, collected, f"{path}.$defs.{name}")

        for key, value in obj.items():
            if key != '$defs':  # Don't recurse into $defs we just processed
                collect_defs(value, collected, f"{path}.{key}")

    if isinstance(obj, list):
        for i, item in enumerate(obj):
            collect_defs(item, collected, f"{path}[{i}]")


def update_refs(obj: Any) -> Any:
    """Update all $ref references from #/$defs/X to #/components/schemas/X."""
    if isinstance(obj, dict):
        new_obj = {}
        for key, value in obj.items():
            if key == '$ref' and isinstance(value, str) and '/$defs/' in value:
                # Update the reference
                # #/$defs/TextQueryInput -> #/components/schemas/TextQueryInput
                new_ref = value.replace('/$defs/', '/components/schemas/')
                new_obj[key] = new_ref
            if isinstance(value, str) and '/$defs/' in value:
                # Also update any other string values containing /$defs/ (like discriminator mappings)
                new_obj[key] = value.replace('/$defs/', '/components/schemas/')
            else:
                new_obj[key] = update_refs(value)
        return new_obj

    if isinstance(obj, list):
        return [update_refs(item) for item in obj]

    return obj


def remove_defs(obj: Any) -> Any:
    """Remove all $defs from the schema."""
    if isinstance(obj, dict):
        new_obj = {}
        for key, value in obj.items():
            if key != '$defs':
                new_obj[key] = remove_defs(value)
        return new_obj

    if isinstance(obj, list):
        return [remove_defs(item) for item in obj]

    return obj


def flatten_openapi_defs(openapi_spec: Dict[str, Any]) -> Dict[str, Any]:
    """
    Flatten all nested $defs into components/schemas.

    Steps:
    1. Collect all $defs from all schemas
    2. Add them to components/schemas
    3. Update all $ref references
    4. Remove all $defs
    """
    # Ensure components/schemas exists
    if 'components' not in openapi_spec:
        openapi_spec['components'] = {}
    if 'schemas' not in openapi_spec['components']:
        openapi_spec['components']['schemas'] = {}

    # Step 1: Collect all defs
    collected_defs = {}
    collect_defs(openapi_spec['components']['schemas'], collected_defs)

    print(f"📦 Collected {len(collected_defs)} definitions from $defs")

    # Step 2: Add to components/schemas
    for name, definition in collected_defs.items():
        if name not in openapi_spec['components']['schemas']:
            openapi_spec['components']['schemas'][name] = definition
        else:
            print(f"⚠️  Skipping {name} (already exists in components/schemas)")

    # Step 3: Update all references
    openapi_spec = update_refs(openapi_spec)
    print("✅ Updated all $ref references")

    # Step 4: Remove all $defs
    openapi_spec['components']['schemas'] = remove_defs(openapi_spec['components']['schemas'])
    print("✅ Removed all $defs from schemas")

    return openapi_spec


if __name__ == '__main__':
    input_file = sys.argv[1] if len(sys.argv) > 1 else 'openapi.json'
    output_file = sys.argv[2] if len(sys.argv) > 2 else 'openapi-flattened.json'

    print(f"🔧 Flattening $defs in {input_file}")

    with open(input_file, 'r', encoding='utf-8') as f:
        spec = json.load(f)

    spec = flatten_openapi_defs(spec)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(spec, f, indent=2)

    print(f"✅ Wrote flattened spec to {output_file}")
