"""Local plugin testing framework.

This module provides the core testing infrastructure for running Mixpeek plugins
locally without requiring cloud services.

**Key Classes:**

- `LocalTestRunner`: Main test execution engine
- `MockServiceContainer`: Deterministic mock services for fast testing
- `ManifestValidator`: Validate plugin definition
- `SecurityValidator`: Scan for security issues
- `SchemaValidator`: Validate input/output schemas

**Testing Modes:**

1. **Mock mode** (`--mock`): Fast, deterministic, no dependencies
   - Uses MockServiceContainer
   - Perfect for unit tests and rapid iteration
   - Runs in <1 second

2. **Local stack mode** (`--local-stack`): Real services locally
   - Uses Docker containers (Ray + Qdrant)
   - Full E2E testing: extract → index → search
   - Runs in ~5 seconds

3. **Production mode** (`--environment=production`): Test deployed plugins
   - Calls production APIs
   - Validates deployment worked correctly
   - Smoke testing after deployment
"""

from mixpeek_dev.testing.mock_services import MockServiceContainer
from mixpeek_dev.testing.production_runner import ProductionTestRunner
from mixpeek_dev.testing.runner import LocalTestRunner
from mixpeek_dev.testing.validators import (
    ManifestValidator,
    SchemaValidator,
    SecurityValidator,
    ValidationResult,
)

__all__ = [
    "LocalTestRunner",
    "ProductionTestRunner",
    "MockServiceContainer",
    "ManifestValidator",
    "SecurityValidator",
    "SchemaValidator",
    "ValidationResult",
]
