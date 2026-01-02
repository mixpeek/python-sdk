# Mixpeek Python SDK

[![PyPI version](https://badge.fury.io/py/mixpeek.svg)](https://badge.fury.io/py/mixpeek)
[![Python versions](https://img.shields.io/pypi/pyversions/mixpeek.svg)](https://pypi.org/project/mixpeek/)
[![License](https://img.shields.io/pypi/l/mixpeek.svg)](https://github.com/mixpeek/python-sdk/blob/main/LICENSE)

Official Python SDK for [Mixpeek](https://mixpeek.com) - Multimodal AI infrastructure for indexing, searching, and understanding your unstructured data.

This SDK is automatically generated from the [OpenAPI specification](https://api.mixpeek.com/docs) and provides type-safe access to all Mixpeek API endpoints.

## Features

- 🔄 **Auto-generated** - Always in sync with the latest API
- 📦 **Type-safe** - Full type hints with Pydantic models
- 🚀 **Async support** - Both sync and async client methods
- 🎯 **Complete coverage** - 200+ endpoints for all Mixpeek features
- ✅ **Well-tested** - Comprehensive test suite with 100% pass rate

## Installation

```bash
pip install mixpeek
```

Upgrade to the latest version:

```bash
pip install --upgrade mixpeek
```

## Quick Start

### Authentication

```python
from mixpeek import AuthenticatedClient

# Initialize the client
client = AuthenticatedClient(
    base_url="https://api.mixpeek.com",
    token="your_api_key_here",
    timeout=30.0
)
```

### Working with Namespaces

Most resource operations require a namespace. Set it via headers:

```python
from mixpeek import AuthenticatedClient

# Initialize with namespace header
client = AuthenticatedClient(
    base_url="https://api.mixpeek.com",
    token="your_api_key_here",
    headers={"X-Namespace": "ns_your_namespace_id"},
    timeout=30.0
)
```

## Usage Examples

### List Collections

```python
from mixpeek.api.collections.list_collections_v1_collections_list_post import sync_detailed

response = sync_detailed(client=client)
if response.status_code == 200:
    collections = response.parsed
    print(f"Found {len(collections)} collections")
```

### List Buckets

```python
from mixpeek.api.buckets.list_buckets_v1_buckets_list_post import sync_detailed

response = sync_detailed(client=client)
if response.status_code == 200:
    buckets = response.parsed
    print(f"Found {len(buckets)} buckets")
```

### List Retrievers

```python
from mixpeek.api.retrievers.list_retrievers_v1_retrievers_list_post import sync_detailed

response = sync_detailed(client=client)
if response.status_code == 200:
    retrievers = response.parsed
    print(f"Found {len(retrievers)} retrievers")
```

### Get Organization Details

```python
from mixpeek.api.organizations.get_organization_v1_organizations_get import sync_detailed

response = sync_detailed(client=client)
if response.status_code == 200:
    org = response.parsed
    print(f"Organization: {org.name}")
```

### Async Usage

All endpoints have async equivalents:

```python
from mixpeek.api.collections.list_collections_v1_collections_list_post import asyncio_detailed
import asyncio

async def main():
    response = await asyncio_detailed(client=client)
    if response.status_code == 200:
        collections = response.parsed
        print(f"Found {len(collections)} collections")

asyncio.run(main())
```

## Core Resources

The SDK provides complete coverage of all Mixpeek resources:

- **Namespaces** - Organize and isolate your resources
- **Buckets** - Store and manage your data
- **Objects** - Individual items in buckets
- **Uploads** - File upload management
- **Batches** - Batch processing operations
- **Collections** - Organize and search your indexed data
- **Documents** - Items within collections
- **Retrievers** - Configure and execute searches
- **Stages** - Build multi-stage retrieval pipelines
- **Taxonomies** - Classification and labeling
- **Clusters** - Group similar content
- **Feature Extractors** - Available AI models and processors

See the [API Coverage documentation](https://github.com/mixpeek/python-sdk/blob/main/API_COVERAGE.md) for a complete list of available methods.

## Error Handling

The SDK returns response objects with status codes and parsed data:

```python
response = sync_detailed(client=client)

if response.status_code == 200:
    # Success
    data = response.parsed
elif response.status_code == 403:
    print("Permission denied - check your API key and namespace")
elif response.status_code == 404:
    print("Resource not found")
else:
    print(f"Error: {response.status_code}")
```

## Response Format

All methods return a `Response` object with:

- `status_code` (int) - HTTP status code
- `parsed` (Pydantic model) - Parsed response data (if successful)
- `content` (bytes) - Raw response content
- `headers` (dict) - Response headers

## Requirements

- Python 3.7+
- `httpx` - HTTP client library
- `attrs` - Python classes without boilerplate
- `python-dateutil` - Date/time handling
- `pydantic` - Data validation using type hints

## Getting Your API Key

1. Sign up at [mixpeek.com](https://mixpeek.com)
2. Navigate to Settings → API Keys
3. Create a new API key
4. Copy your namespace ID from Settings → Namespaces

## Documentation

- **API Reference**: https://api.mixpeek.com/docs
- **API Coverage**: [API_COVERAGE.md](https://github.com/mixpeek/python-sdk/blob/main/API_COVERAGE.md)
- **Mixpeek Documentation**: https://docs.mixpeek.com
- **GitHub Repository**: https://github.com/mixpeek/python-sdk

## Support

- **Issues**: https://github.com/mixpeek/python-sdk/issues
- **Email**: support@mixpeek.com
- **Discord**: https://discord.gg/mixpeek

## Contributing

This SDK is auto-generated from the OpenAPI specification. To report bugs or request features:

1. **API Issues**: Report at the [main repository](https://github.com/mixpeek/showcase/issues)
2. **SDK Issues**: Report at the [SDK repository](https://github.com/mixpeek/python-sdk/issues)

## License

MIT License - see [LICENSE](https://github.com/mixpeek/python-sdk/blob/main/LICENSE) for details.

---

**Note**: This SDK is automatically generated and published. The code is synchronized with the latest API specification to ensure compatibility.
