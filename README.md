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
- 🎨 **Clean API** - Stripe-like resource interfaces for common operations
- 🔧 **CLI Tools** - Build, test, and publish custom extractors

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

### Two Ways to Use the SDK

**Option 1: Clean Resource API (Recommended)**

```python
from mixpeek import AuthenticatedClient, Collections, Buckets, Retrievers

client = AuthenticatedClient(
    base_url="https://api.mixpeek.com",
    token="your_api_key",
    headers={"X-Namespace": "ns_your_namespace_id"}
)

# Use resource interfaces
collections = Collections(client)
response = collections.list(limit=10)

buckets = Buckets(client)
response = buckets.get("bucket_id")
```

**Option 2: Direct API Access (Full Control)**

```python
from mixpeek.api.collections.list_collections_v1_collections_list_post import sync_detailed

response = sync_detailed(client=client, limit=10)
if response.status_code == 200:
    collections = response.parsed
    print(f"Found {len(collections)} collections")
```

### List Collections

```python
from mixpeek import Collections

collections = Collections(client)
response = collections.list(limit=10, offset=0)
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

## CLI: Custom Plugin Development

The Mixpeek CLI enables you to build, test, and publish custom extractors.

### Quick Start

```bash
# Create a new plugin
mixpeek plugin init my_extractor --category text --description "My custom text processor"

# Navigate to plugin directory
cd my_extractor

# Test locally
mixpeek plugin test

# Publish to your namespace (Enterprise)
mixpeek plugin publish --namespace ns_your_namespace
```

### CLI Commands

#### `mixpeek plugin init <name>`

Create a new plugin from a template with all required files.

```bash
mixpeek plugin init sentiment_analyzer \
  --category text \
  --description "Custom sentiment analysis" \
  --author "Your Name"
```

**Options:**
| Option | Short | Description |
|--------|-------|-------------|
| `--description` | `-d` | Plugin description |
| `--category` | `-c` | Category: text, image, video, audio, document, multimodal |
| `--author` | `-a` | Author name (defaults to git user.name) |
| `--output` | `-o` | Output directory |

**Generated Structure:**
```
my_extractor/
├── __init__.py          # Package exports
├── manifest.py          # Metadata, input/output schemas
├── pipeline.py          # build_steps() implementation
├── processors/
│   ├── __init__.py
│   └── core.py          # Main processing logic
├── tests/
│   ├── __init__.py
│   └── test_plugin.py   # Unit tests (pytest)
├── README.md            # Documentation
└── pyproject.toml       # Package config
```

#### `mixpeek plugin test`

Validate plugin structure and run tests locally.

```bash
# Test current directory
mixpeek plugin test

# Test specific path
mixpeek plugin test --path ./my_extractor

# Test with sample data
mixpeek plugin test --sample-data test_data.json --verbose
```

**Options:**
| Option | Short | Description |
|--------|-------|-------------|
| `--path` | `-p` | Plugin directory path |
| `--sample-data` | `-s` | JSON/CSV file with test data |
| `--verbose` | `-v` | Show detailed output |

**What it validates:**
1. Required files exist (manifest.py, pipeline.py)
2. Schemas are valid (input, output, parameters)
3. Pipeline builds successfully
4. Unit tests pass (pytest)
5. Sample data processes correctly (if provided)

#### `mixpeek plugin validate`

Quick validation without running full tests.

```bash
mixpeek plugin validate --path ./my_extractor
```

#### `mixpeek plugin publish`

Upload plugin to your Mixpeek namespace (Enterprise feature).

```bash
# Publish with explicit credentials
mixpeek plugin publish \
  --namespace ns_abc123 \
  --api-key sk_your_key

# Using environment variables
export MIXPEEK_API_KEY=sk_your_key
export MIXPEEK_NAMESPACE=ns_abc123
mixpeek plugin publish

# Dry run (validate without publishing)
mixpeek plugin publish --dry-run
```

**Options:**
| Option | Short | Description |
|--------|-------|-------------|
| `--path` | `-p` | Plugin directory path |
| `--namespace` | `-n` | Target namespace ID |
| `--dry-run` | | Validate without publishing |

#### `mixpeek plugin list`

List available extractors in your namespace.

```bash
# List all extractors
mixpeek plugin list --api-key sk_your_key

# Filter by source
mixpeek plugin list --source builtin   # Mixpeek built-in
mixpeek plugin list --source custom    # Your custom plugins
mixpeek plugin list --source community # Community marketplace
```

**Options:**
| Option | Short | Description |
|--------|-------|-------------|
| `--namespace` | `-n` | Namespace ID |
| `--source` | `-s` | Filter: all, builtin, custom, community |

### Plugin Development Guide

#### 1. Define Your Schema (manifest.py)

```python
from pydantic import BaseModel, Field

class MyExtractorInput(BaseModel):
    """What your extractor accepts."""
    text: str = Field(..., description="Input text")

class MyExtractorOutput(BaseModel):
    """What your extractor produces."""
    sentiment: str = Field(..., description="Detected sentiment")
    confidence: float = Field(..., ge=0.0, le=1.0)

class MyExtractorParams(BaseModel):
    """User-configurable parameters."""
    threshold: float = Field(default=0.5, ge=0.0, le=1.0)
```

#### 2. Implement Processing Logic (processors/core.py)

```python
import pandas as pd
from dataclasses import dataclass

@dataclass
class MyProcessorConfig:
    threshold: float = 0.5
    text_column: str = "text"

class MyProcessor:
    def __init__(self, config: MyProcessorConfig, progress_actor=None):
        self.config = config
        self.progress_actor = progress_actor  # For Ray progress tracking

    def __call__(self, batch: pd.DataFrame) -> pd.DataFrame:
        """Process a batch of inputs."""
        results = []
        for text in batch[self.config.text_column]:
            # Your processing logic here
            sentiment, confidence = self.analyze(text)
            results.append({"sentiment": sentiment, "confidence": confidence})

        batch["sentiment"] = [r["sentiment"] for r in results]
        batch["confidence"] = [r["confidence"] for r in results]
        return batch

    def analyze(self, text: str) -> tuple[str, float]:
        # Implement your analysis
        return "positive", 0.95
```

#### 3. Wire Up the Pipeline (pipeline.py)

```python
from .processors.core import MyProcessor, MyProcessorConfig

def build_steps(extractor_request, container=None, base_steps=None, **kwargs):
    params = extractor_request.extractor_config.parameters or {}

    config = MyProcessorConfig(
        threshold=params.get("threshold", 0.5)
    )

    steps = base_steps or []
    steps.append(MyProcessor(config))

    return {
        "steps": steps,
        "prepare": lambda ds: ds,  # Dataset preparation
    }
```

#### 4. Write Tests (tests/test_plugin.py)

```python
import pandas as pd
import pytest
from ..processors.core import MyProcessor, MyProcessorConfig

def test_processor_basic():
    config = MyProcessorConfig(threshold=0.5)
    processor = MyProcessor(config)

    batch = pd.DataFrame({"text": ["I love this!", "This is terrible"]})
    result = processor(batch)

    assert "sentiment" in result.columns
    assert "confidence" in result.columns
    assert len(result) == 2
```

#### 5. Test and Publish

```bash
# Run local tests
mixpeek plugin test --verbose

# Publish when ready
mixpeek plugin publish --namespace ns_your_namespace
```

### Using Your Custom Plugin

After publishing, use your extractor in collections:

```python
from mixpeek import Mixpeek

client = Mixpeek(api_key="sk_your_key")

# Create collection with your custom extractor
collection = client.collections.create(
    collection_name="my_collection",
    source={"type": "bucket", "bucket_ids": ["bkt_abc123"]},
    feature_extractor={
        "feature_extractor_name": "my_extractor",
        "version": "v1",
        "parameters": {
            "threshold": 0.7
        }
    }
)
```

### Environment Variables

| Variable | Description |
|----------|-------------|
| `MIXPEEK_API_KEY` | Your API key |
| `MIXPEEK_NAMESPACE` | Default namespace ID |
| `MIXPEEK_BASE_URL` | API base URL (default: https://api.mixpeek.com) |

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
