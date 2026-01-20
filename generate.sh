#!/bin/bash

# Script to generate Python SDK using OpenAPI Generator

set -e

echo "🔧 Generating Mixpeek Python SDK..."

# Check if openapi-generator-cli is available
if ! command -v openapi-generator-cli &> /dev/null; then
    echo "⚠️  openapi-generator-cli not found. Installing via npm..."
    npm install -g @openapitools/openapi-generator-cli
fi

# Use existing openapi.json (synced from server repo)
# Or download if it doesn't exist (for manual generation)
if [ ! -f "openapi.json" ]; then
    echo "📥 Downloading OpenAPI specification from production..."
    curl -s https://server-xb24.onrender.com/docs/openapi.json -o openapi.json
else
    echo "✅ Using existing openapi.json file"
fi

# Flatten nested $defs (OpenAPI Generator doesn't support them)
echo "🔄 Flattening nested \$defs..."
python3 flatten_defs.py openapi.json openapi-flattened-temp.json
mv openapi-flattened-temp.json openapi.json

# Clean the OpenAPI spec (remove anyOf with null types and simplify operation IDs)
echo "🧼 Cleaning OpenAPI specification..."
python3 << 'PYTHON_SCRIPT'
import json
import re

with open('openapi.json', 'r') as f:
    spec = json.load(f)

def clean_schema(schema):
    """Recursively clean anyOf/oneOf that include null type"""
    if isinstance(schema, dict):
        # Handle anyOf with null
        if 'anyOf' in schema and isinstance(schema['anyOf'], list):
            cleaned = [s for s in schema['anyOf'] if s.get('type') != 'null']
            if len(cleaned) == 1 and len(schema['anyOf']) > 1:
                for key, value in cleaned[0].items():
                    schema[key] = value
                del schema['anyOf']
                schema['nullable'] = True
            elif len(cleaned) < len(schema['anyOf']):
                schema['anyOf'] = cleaned
                schema['nullable'] = True
        
        # Handle oneOf with null
        if 'oneOf' in schema and isinstance(schema['oneOf'], list):
            cleaned = [s for s in schema['oneOf'] if s.get('type') != 'null']
            if len(cleaned) == 1 and len(schema['oneOf']) > 1:
                for key, value in cleaned[0].items():
                    schema[key] = value
                del schema['oneOf']
                schema['nullable'] = True
            elif len(cleaned) < len(schema['oneOf']):
                schema['oneOf'] = cleaned
                schema['nullable'] = True
        
        for key, value in list(schema.items()):
            if isinstance(value, (dict, list)):
                clean_schema(value)
    elif isinstance(schema, list):
        for item in schema:
            clean_schema(item)
    return schema

def simplify_operation_id(operation_id):
    """
    Simplify operation IDs to be more developer-friendly.
    Examples:
      - create_organization_private_v1_private_organizations_post -> create_private_organization
      - list_collections_v1_collections_list_post -> list_collections
      - get_collection_v1_collections_collection_identifier_get -> get_collection
    """
    if not operation_id:
        return operation_id
    
    # Remove version prefix (v1, v2, etc.)
    operation_id = re.sub(r'_v\d+_', '_', operation_id)
    
    # Remove HTTP method suffix (_post, _get, _put, _delete, _patch)
    operation_id = re.sub(r'_(post|get|put|delete|patch)$', '', operation_id)
    
    # Remove common path patterns
    operation_id = re.sub(r'_identifier_', '_', operation_id)
    operation_id = re.sub(r'__{1,}', '_', operation_id)
    
    # Split into parts
    parts = operation_id.split('_')
    
    # Extract action verb (usually at the start)
    action_verbs = ['create', 'get', 'list', 'update', 'delete', 'patch', 'execute', 
                    'upsert', 'describe', 'add', 'remove', 'set']
    
    action = None
    if parts and parts[0] in action_verbs:
        action = parts[0]
        parts = parts[1:]
    
    # Remove generic/redundant words
    skip_words = ['route', 'endpoint', 'api', 'private', 'public', 'v1', 'v2', 'v3']
    
    # Track singular/plural forms to avoid duplication
    seen_roots = set()
    cleaned_parts = []
    
    for part in parts:
        if part in skip_words:
            continue
        
        # Get root form (simple pluralization check)
        root = part.rstrip('s') if part.endswith('s') and len(part) > 3 else part
        
        # Skip if we've seen this root (or very similar)
        if root.lower() in seen_roots:
            continue
        
        cleaned_parts.append(part)
        seen_roots.add(root.lower())
    
    # Rebuild operation ID
    if action:
        result = action + ('_' + '_'.join(cleaned_parts) if cleaned_parts else '')
    else:
        result = '_'.join(cleaned_parts)
    
    # Final cleanup
    result = result.strip('_')
    
    # Remove action duplication at the end (e.g., "list_collections_list" -> "list_collections")
    for verb in action_verbs:
        pattern = f'_{verb}$'
        if result.startswith(verb + '_') and result.endswith(f'_{verb}'):
            result = re.sub(pattern, '', result)
    
    # Remove duplicate nouns (e.g., "get_document_collections_id" -> "get_document")
    # Keep only the meaningful parts
    parts_to_check = result.split('_')
    if len(parts_to_check) > 2:
        # If we have action + noun + extra, check if extra is generic
        generic_suffixes = ['collections', 'list', 'id', 'identifier', 'document', 'documents']
        while len(parts_to_check) > 2 and parts_to_check[-1] in generic_suffixes:
            parts_to_check = parts_to_check[:-1]
        result = '_'.join(parts_to_check)
    
    return result

def clean_operation_ids(spec):
    """Clean all operation IDs in the spec"""
    if 'paths' not in spec:
        return
    
    for path, path_item in spec['paths'].items():
        if not isinstance(path_item, dict):
            continue
        
        for method in ['get', 'post', 'put', 'delete', 'patch', 'options', 'head']:
            if method in path_item and isinstance(path_item[method], dict):
                operation = path_item[method]
                if 'operationId' in operation:
                    old_id = operation['operationId']
                    new_id = simplify_operation_id(old_id)
                    operation['operationId'] = new_id
                    print(f"  {old_id} -> {new_id}")

# Clean schemas
if 'components' in spec and 'schemas' in spec['components']:
    clean_schema(spec['components']['schemas'])
if 'paths' in spec:
    clean_schema(spec['paths'])

# Clean operation IDs
print("  Simplifying operation IDs:")
clean_operation_ids(spec)

with open('openapi-cleaned.json', 'w') as f:
    json.dump(spec, f, indent=2)
print("✅ Cleaned OpenAPI spec")
PYTHON_SCRIPT

# Clean previous generation (except important files)
echo "🧹 Cleaning previous generation..."
if [ -d "mixpeek" ]; then
    rm -rf mixpeek
fi
if [ -d "test" ]; then
    rm -rf test
fi
if [ -d "docs" ]; then
    rm -rf docs
fi
rm -f .openapi-generator-ignore
rm -f .gitlab-ci.yml
rm -f git_push.sh
rm -f tox.ini
rm -f test-requirements.txt

# Generate the SDK
echo "🚀 Generating SDK..."
openapi-generator-cli generate \
    -i openapi-cleaned.json \
    -g python \
    -o . \
    --skip-validate-spec \
    --package-name mixpeek \
    --additional-properties=projectName=mixpeek,packageVersion=0.81.0,packageUrl=https://github.com/mixpeek/python-sdk,library=urllib3

# Post-generation cleanup
echo "✨ Post-generation cleanup..."

# Remove unnecessary files
rm -f .travis.yml
rm -f git_push.sh
rm -f .gitlab-ci.yml

echo "✅ SDK generation complete!"
echo ""
echo "📦 To build and install locally:"
echo "   pip install -e ."
echo ""
echo "🚀 To publish to PyPI:"
echo "   python -m build"
echo "   twine upload dist/*"

