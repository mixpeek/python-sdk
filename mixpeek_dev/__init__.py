"""Mixpeek Development Tools - Local Plugin Testing Framework.

This package provides tools for developing, testing, and deploying custom Mixpeek plugins
entirely from your local environment.

**Quick Start:**

1. Install development tools:
   ```bash
   pip install mixpeek[dev]
   ```

2. Create a new plugin:
   ```bash
   mixpeek init my_plugin --template=basic_text
   ```

3. Test locally with mock services (fast iteration):
   ```bash
   cd my_plugin
   mixpeek test --mock
   ```

4. Deploy to production:
   ```bash
   mixpeek push
   ```

**Core Components:**

- `LocalTestRunner`: Execute plugins locally without cloud infrastructure
- `MockServiceContainer`: Drop-in replacement for production services (fast, deterministic)
- `Validators`: Security scanning and schema validation before deployment
- `Model Loaders`: Load custom models (.safetensors, .pt, .onnx)

**Philosophy:**

This framework is designed to be **self-documenting** and **LLM-friendly**. Every template,
error message, and docstring is written to help AI assistants generate correct code.

**Example Use Case:**

E-commerce company wants to extract fashion attributes (brand, color, material) from
product descriptions and make them searchable using semantic search.

```python
# Create plugin
mixpeek init fashion_extractor --template=basic_text

# Add custom model
cp fashion_model.safetensors fashion_extractor/models/

# Test locally
cd fashion_extractor
mixpeek test --mock  # Fast iteration with mocks
mixpeek test --local-stack  # Full E2E with Ray + Qdrant

# Deploy
mixpeek validate  # Security scan
mixpeek push  # Deploy to production
```
"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("mixpeek")
except PackageNotFoundError:
    __version__ = "unknown"

__all__ = ["__version__"]
