# Mixpeek Python SDK

The official Python SDK for the [Mixpeek API](https://mixpeek.com) - a multimodal search and data processing platform.

## Installation

```bash
pip install mixpeek
```

## Quick Start

```python
from mixpeek import Mixpeek

# Initialize client (reads MIXPEEK_API_KEY from environment)
client = Mixpeek()

# Or pass the API key directly
client = Mixpeek(api_key="your_api_key")

# List collections
collections = client.collections.list()
for c in collections.collections:
    print(f"{c.alias}: {c.collection_id}")

# Create a collection
collection = client.collections.create(
    alias="my_collection",
    description="My data collection"
)

# Add documents
doc = client.documents.create(
    collection="my_collection",
    metadata={"title": "Hello", "content": "World"}
)

# Search with retrievers
results = client.retrievers.query(
    retriever="my_retriever",
    queries=[{"text": "search query"}],
    limit=10
)
```

## Features

- **Simple API**: Clean, intuitive interface following Stripe/OpenAI SDK patterns
- **Type Safe**: Full type hints and Pydantic models for IDE support
- **Auto-configured**: Reads `MIXPEEK_API_KEY` from environment automatically

## Resources

| Resource | Description |
|----------|-------------|
| `client.collections` | Manage document collections |
| `client.documents` | CRUD operations on documents |
| `client.retrievers` | Search and retrieval operations |
| `client.buckets` | Manage storage buckets |
| `client.objects` | Manage objects in buckets |
| `client.namespaces` | Data isolation namespaces |
| `client.tasks` | Monitor async operations |
| `client.taxonomies` | Classification and categorization |
| `client.clusters` | Data clustering operations |
| `client.feature_extractors` | Embedding models |

## Configuration

```python
from mixpeek import Mixpeek

client = Mixpeek(
    api_key="your_api_key",           # Or set MIXPEEK_API_KEY env var
    base_url="https://api.mixpeek.com", # Default API URL
    namespace="production",            # Default namespace for requests
    timeout=30.0,                      # Request timeout in seconds
)
```

## Error Handling

```python
from mixpeek import Mixpeek, ApiException

client = Mixpeek()

try:
    collection = client.collections.get("non_existent")
except ApiException as e:
    print(f"Error {e.status}: {e.reason}")
```

## Examples

See the [examples/](examples/) directory for more detailed usage:
- [quickstart.py](examples/quickstart.py) - Basic SDK usage

## Requirements

- Python 3.9+
- Dependencies: `pydantic>=2`, `urllib3>=1.25.3`, `python-dateutil>=2.8.2`

## Documentation

- [API Reference](https://docs.mixpeek.com)
- [Full API Docs](docs/)

## License

MIT

---

*This SDK is auto-generated from the [OpenAPI specification](https://api.mixpeek.com/docs/openapi.json) with a modern client wrapper.*
