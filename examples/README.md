# Mixpeek SDK Examples

This directory contains example scripts demonstrating how to use the Mixpeek Python SDK.

## Prerequisites

1. Install the SDK:
   ```bash
   pip install mixpeek
   ```

2. Get your API key from [mixpeek.com](https://mixpeek.com)

3. Set your API key as an environment variable:
   ```bash
   export MIXPEEK_API_KEY="your_api_key_here"
   ```

## Running Examples

### Quick Start

The quickstart example demonstrates basic SDK usage:

```bash
python examples/quickstart.py
```

This example covers:
- Listing collections
- Creating a new collection
- Adding documents
- Listing documents
- Checking retrievers

## Example Topics

Each example focuses on a specific aspect of the Mixpeek platform:

- **quickstart.py** - Basic SDK usage and collection management
- (More examples coming soon!)

## Creating Your Own Examples

Here's a minimal template:

```python
import os
import mixpeek
from mixpeek.api import collections_api

# Configure
api_key = os.environ.get('MIXPEEK_API_KEY')
configuration = mixpeek.Configuration(
    host="https://api.mixpeek.com",
    api_key={'ApiKeyAuth': api_key}
)

# Use the SDK
with mixpeek.ApiClient(configuration) as api_client:
    collections = collections_api.CollectionsApi(api_client)
    result = collections.list_collections()
    print(f"Found {len(result.collections)} collections")
```

## Need Help?

- **Documentation**: [docs.mixpeek.com](https://docs.mixpeek.com)
- **Issues**: [github.com/mixpeek/python-sdk/issues](https://github.com/mixpeek/python-sdk/issues)
- **Support**: [info@mixpeek.com](mailto:info@mixpeek.com)

