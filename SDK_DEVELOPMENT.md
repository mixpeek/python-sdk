# Mixpeek Python SDK Development Guide

This document explains how the Python SDK is automatically generated from the OpenAPI specification and kept in sync with API changes.

## Overview

The Python SDK is automatically generated from the OpenAPI specification located at the root of the server repository. Any changes to the API models or endpoints will automatically trigger SDK regeneration via pre-commit hooks.

## Directory Structure

```
server/
├── openapi.json                          # Source of truth - OpenAPI spec
├── sdk/python-client/
│   ├── mixpeek/                          # Generated SDK package
│   │   └── mixpeek/                      # Auto-generated client code
│   │       ├── api/                      # API endpoint modules
│   │       ├── models/                   # Pydantic models
│   │       └── client.py                 # Client classes
│   ├── scripts/
│   │   ├── generate_sdk.sh               # SDK generation script
│   │   └── apply_overrides.py            # Post-generation customizations
│   ├── openapi-config.yml                # Generator configuration
│   ├── sdk-config.yml                    # SDK customization config
│   ├── test_e2e.py                       # E2E tests against local API
│   └── README.md                         # SDK usage documentation
```

## Automatic SDK Regeneration

### GitHub Action Workflow

When `openapi.json` changes are pushed to the server repo, a GitHub Action automatically:

1. Detects changes to `openapi.json` on the main branch
2. Checks out the python-sdk repository
3. Copies the updated OpenAPI spec
4. Runs the SDK generator script
5. Commits and pushes changes to the python-sdk repo

**GitHub Action location:** `.github/workflows/sync-python-sdk.yml`

**Required Setup:**
- Create a Personal Access Token (PAT) with `repo` scope
- Add it as a repository secret named `PYTHON_SDK_PAT`
- The workflow will automatically sync changes between repos

### Manual Regeneration

To manually regenerate the SDK:

```bash
cd sdk/python-client
bash scripts/generate_sdk.sh
```

This will:
- Read the OpenAPI spec from `../../openapi.json`
- Generate the client using `openapi-python-client`
- Apply custom method overrides from `sdk-config.yml`
- Create a backup of the existing SDK before regeneration

## Testing

### Running E2E Tests

The SDK includes end-to-end tests that run against your local API:

```bash
cd sdk/python-client

# Using default local API (http://localhost:8000)
python test_e2e.py

# Using custom API URL
MIXPEEK_API_URL=http://localhost:3000 python test_e2e.py

# Using custom API key
MIXPEEK_API_KEY=your-key-here python test_e2e.py
```

### Test Coverage

Current tests:
- ✓ Client initialization
- ✓ Health check endpoint
- ✓ Collections listing (requires auth)

### Running Original Tests

The legacy test file is still available:

```bash
cd sdk/python-client
python test.py
```

## Configuration

### OpenAPI Generator Config (`openapi-config.yml`)

```yaml
project_name_override: mixpeek
package_name_override: mixpeek
```

### SDK Customization Config (`sdk-config.yml`)

Configure method name overrides, excluded operations, and excluded tags:

```yaml
method_overrides:
  # Example: override verbose names with shorter ones
  # "createCollectionDocument": "create_document"

exclude_operations:
  # Example: exclude admin-only operations
  # - "adminDeleteOrganization"

exclude_tags:
  # Example: exclude private/admin endpoints
  # - "Organizations (Private/Admin)"
```

## Publishing

The SDK can be published to PyPI:

```bash
cd sdk/python-client

# Build the package
python setup.py sdist bdist_wheel

# Publish to PyPI (requires credentials)
twine upload dist/*
```

## Troubleshooting

### OpenAPI Spec Warnings

During generation, you may see warnings about missing schema references. These are informational and don't prevent generation:

```
WARNING: Cannot parse response for status code 200
Reference(ref='#/components/schemas/SomeModel')
```

To fix these:
1. Ensure all referenced schemas exist in `openapi.json`
2. Check that schema names match exactly (case-sensitive)
3. Verify schema definitions are in `/components/schemas/`

### GitHub Action Not Triggering

If the GitHub Action doesn't run automatically:

1. **Check workflow file syntax:**
   ```bash
   # Validate YAML syntax
   yamllint .github/workflows/sync-python-sdk.yml
   ```

2. **Verify secrets are configured:**
   - Go to Settings → Secrets and variables → Actions
   - Ensure `PYTHON_SDK_PAT` is set with a valid PAT

3. **Check action logs:**
   - Go to Actions tab in GitHub
   - Look for "Sync Python SDK" workflow runs

4. **Manually trigger:**
   - Go to Actions → Sync Python SDK → Run workflow

### Generated Client Structure

The generated client uses the standard `openapi-python-client` structure:

```python
from mixpeek.client import AuthenticatedClient
from mixpeek.api.health.healthcheck_v1_health_get import sync_detailed

# Initialize client
client = AuthenticatedClient(
    base_url="http://localhost:8000",
    token="your-api-key",
    timeout=30.0
)

# Make API calls
response = sync_detailed(client=client)
```

## Development Workflow

### Server Repo (mixpeek/showcase)
1. **Make API Changes**: Modify your FastAPI endpoints or Pydantic models
2. **Generate OpenAPI Spec**: Your API framework generates `openapi.json`
3. **Commit & Push**: Push changes to main branch
4. **GitHub Action Triggers**: Automatically regenerates SDK in python-sdk repo

### Python SDK Repo (mixpeek/python-sdk)
1. **Review Auto-Generated Changes**: Check the PR or commit from GitHub Actions
2. **Run Tests Locally** (optional):
   ```bash
   cd /path/to/python-sdk
   python test_e2e.py
   ```
3. **Publish**: Update version in `setup.py` and publish to PyPI
   ```bash
   python setup.py sdist bdist_wheel
   twine upload dist/*
   ```

## Resources

- [openapi-python-client Documentation](https://github.com/openapi-generators/openapi-python-client)
- [OpenAPI Specification](https://swagger.io/specification/)
- [Mixpeek API Documentation](https://api.mixpeek.com/docs)
