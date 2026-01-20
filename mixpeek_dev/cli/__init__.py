"""CLI commands for Mixpeek development tools.

This module provides the command-line interface for local plugin development.

**Commands:**

- `mixpeek test`: Test plugins locally
- `mixpeek init`: Create new plugin from template
- `mixpeek validate`: Validate plugin before deployment
- `mixpeek push`: Deploy plugin to production

**Example:**

```bash
# Initialize new plugin
mixpeek init my_plugin --template=basic_text

# Test locally with mocks
cd my_plugin
mixpeek test --mock

# Validate before deployment
mixpeek validate

# Deploy to production
mixpeek push
```
"""

__all__ = ["cli"]
