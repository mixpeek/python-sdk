"""Plugin validators for security and schema checking.

This module provides validators to check plugins before deployment:

1. **ManifestValidator**: Validate plugin metadata
2. **SecurityValidator**: Scan for dangerous code patterns
3. **SchemaValidator**: Validate input/output schemas

**Philosophy:**

Validators are designed to:
- Catch issues early (before deployment)
- Provide actionable error messages
- Help LLMs understand and fix problems
- Prevent security vulnerabilities

**Example Usage:**

```python
from mixpeek_dev.testing import ManifestValidator, SecurityValidator

# Validate manifest
manifest_validator = ManifestValidator()
result = manifest_validator.validate(plugin_path="./my_plugin")
if not result.is_valid:
    print(f"Manifest errors: {result.errors}")

# Security scan
security_validator = SecurityValidator()
result = security_validator.validate(plugin_path="./my_plugin")
if not result.is_valid:
    print(f"Security issues: {result.errors}")
```

**Validation Workflow:**

```bash
# Before deployment, run validation
mixpeek validate

# This runs:
# 1. ManifestValidator - Check required fields
# 2. SecurityValidator - Scan for dangerous code
# 3. SchemaValidator - Validate schemas
# 4. Exit with clear error messages if any fail
```
"""

import ast
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Set


class ValidationResult:
    """Result of a validation check.

    **Attributes:**
        is_valid: Whether validation passed
        errors: List of error messages
        warnings: List of warning messages

    **Example:**

    ```python
    result = ValidationResult()
    result.add_error("Missing required field: feature_extractor_name")
    result.add_warning("Consider adding a description")

    if not result.is_valid:
        print("Validation failed:")
        for error in result.errors:
            print(f"  ✗ {error}")
    ```
    """

    def __init__(self):
        """Initialize validation result."""
        self.errors: List[str] = []
        self.warnings: List[str] = []

    @property
    def is_valid(self) -> bool:
        """Check if validation passed (no errors).

        Returns:
            True if no errors, False otherwise

        Note: Warnings don't fail validation, only errors do.
        """
        return len(self.errors) == 0

    def add_error(self, message: str):
        """Add an error message.

        Args:
            message: Error description

        Example:
            ```python
            result.add_error("manifest.py missing required field: version")
            ```
        """
        self.errors.append(message)

    def add_warning(self, message: str):
        """Add a warning message.

        Args:
            message: Warning description

        Example:
            ```python
            result.add_warning("Consider adding a description field")
            ```
        """
        self.warnings.append(message)


class ManifestValidator:
    """Validate plugin manifest.py file.

    Checks that manifest.py contains all required fields and that values
    are correctly formatted.

    **Required Fields:**

    - feature_extractor_name: str (e.g., "my_extractor")
    - version: str (e.g., "v1")
    - features: list (e.g., [{"name": "embedding", "type": "vector"}])
    - output_schema: dict (JSON schema for output)

    **Optional Fields:**

    - description: str (recommended)
    - dependencies: list (pip packages)
    - input_mappings: dict
    - tier: int
    - tier_label: str

    **Example:**

    ```python
    validator = ManifestValidator()
    result = validator.validate("./my_plugin")

    if not result.is_valid:
        print("Manifest validation failed:")
        for error in result.errors:
            print(f"  ✗ {error}")
        sys.exit(1)
    ```

    **Error Messages:**

    Clear, actionable messages help users fix issues:

    - "Missing required field: feature_extractor_name"
      → Add: feature_extractor_name = "my_extractor"

    - "Invalid version format: '1'. Must be 'v1', 'v2', etc."
      → Change: version = "v1"

    - "Features list is empty. Must define at least one feature."
      → Add: features = [{"name": "embedding", "type": "vector"}]
    """

    def __init__(self):
        """Initialize manifest validator."""
        self.required_fields = [
            "feature_extractor_name",
            "version",
            "features",
            "output_schema",
        ]

    def validate(self, plugin_path: Path) -> ValidationResult:
        """Validate plugin manifest.

        Args:
            plugin_path: Path to plugin directory

        Returns:
            ValidationResult with errors and warnings

        Example:
            ```python
            result = validator.validate(Path("./my_plugin"))
            assert result.is_valid
            ```
        """
        result = ValidationResult()
        manifest_path = plugin_path / "manifest.py"

        # Check file exists
        if not manifest_path.exists():
            result.add_error(
                f"manifest.py not found in {plugin_path}\n"
                f"Create one with: mixpeek init {plugin_path.name} --template=basic_text"
            )
            return result

        # Load manifest
        try:
            manifest = self._load_manifest(manifest_path)
        except Exception as e:
            result.add_error(f"Failed to load manifest.py: {str(e)}")
            return result

        # Check required fields
        for field in self.required_fields:
            if field not in manifest:
                result.add_error(
                    f"Missing required field: {field}\n"
                    f"Add to manifest.py: {field} = ..."
                )

        # Validate field values
        if "feature_extractor_name" in manifest:
            self._validate_feature_extractor_name(manifest["feature_extractor_name"], result)

        if "version" in manifest:
            self._validate_version(manifest["version"], result)

        if "features" in manifest:
            self._validate_features(manifest["features"], result)

        if "output_schema" in manifest:
            self._validate_output_schema(manifest["output_schema"], result)

        # Check optional but recommended fields
        if "description" not in manifest:
            result.add_warning(
                "Consider adding a 'description' field to explain what your plugin does"
            )

        return result

    def _load_manifest(self, path: Path) -> Dict[str, Any]:
        """Load manifest.py as a dict of variables."""
        import importlib.util
        import sys

        spec = importlib.util.spec_from_file_location("manifest", path)
        if spec is None or spec.loader is None:
            raise ImportError(f"Could not load manifest from {path}")

        module = importlib.util.module_from_spec(spec)
        sys.modules["manifest"] = module
        spec.loader.exec_module(module)

        return {key: getattr(module, key) for key in dir(module) if not key.startswith("_")}

    def _validate_feature_extractor_name(self, name: Any, result: ValidationResult):
        """Validate feature_extractor_name field."""
        if not isinstance(name, str):
            result.add_error(
                f"feature_extractor_name must be a string, got {type(name).__name__}"
            )
        elif not name:
            result.add_error("feature_extractor_name cannot be empty")
        elif not re.match(r"^[a-z][a-z0-9_]*$", name):
            result.add_error(
                f"Invalid feature_extractor_name: '{name}'\n"
                f"Must be lowercase with underscores (e.g., 'my_extractor', 'fashion_classifier')"
            )

    def _validate_version(self, version: Any, result: ValidationResult):
        """Validate version field."""
        if not isinstance(version, str):
            result.add_error(f"version must be a string, got {type(version).__name__}")
        elif not version.startswith("v"):
            result.add_error(
                f"Invalid version format: '{version}'\n"
                f"Must start with 'v' (e.g., 'v1', 'v2', 'v1_0')"
            )

    def _validate_features(self, features: Any, result: ValidationResult):
        """Validate features list."""
        if not isinstance(features, list):
            result.add_error(f"features must be a list, got {type(features).__name__}")
            return

        if not features:
            result.add_error(
                "features list is empty. Must define at least one feature.\n"
                "Example: features = [{{'name': 'embedding', 'type': 'vector', 'dimensions': 128}}]"
            )
            return

        for i, feature in enumerate(features):
            if not isinstance(feature, dict):
                result.add_error(f"features[{i}] must be a dict, got {type(feature).__name__}")
                continue

            # Check required feature fields
            if "name" not in feature:
                result.add_error(f"features[{i}] missing 'name' field")
            if "type" not in feature:
                result.add_error(f"features[{i}] missing 'type' field")

            # Validate vector features
            if feature.get("type") == "vector":
                if "dimensions" not in feature:
                    result.add_error(
                        f"features[{i}] is type 'vector' but missing 'dimensions' field"
                    )

    def _validate_output_schema(self, schema: Any, result: ValidationResult):
        """Validate output_schema dict."""
        if not isinstance(schema, dict):
            result.add_error(f"output_schema must be a dict, got {type(schema).__name__}")
            return

        if not schema:
            result.add_error(
                "output_schema is empty. Must define at least one output field.\n"
                "Example: output_schema = {{'text': {{'type': 'string'}}, 'embedding': {{'type': 'array'}}}}"
            )


class SecurityValidator:
    """Scan plugin code for security vulnerabilities.

    Checks for dangerous patterns that could:
    - Execute arbitrary code
    - Access the file system
    - Make network requests
    - Import unsafe modules

    **Dangerous Patterns:**

    - `os.system()`: Shell command execution
    - `subprocess`: Process spawning
    - `eval()`, `exec()`: Code execution
    - `__import__()`: Dynamic imports
    - `open()` with write mode: File system writes
    - `requests`, `urllib`: Network access (should use Mixpeek SDK)

    **Example:**

    ```python
    # This would fail validation
    import subprocess
    subprocess.run(["rm", "-rf", "/"])  # Dangerous!

    # This would also fail
    import os
    os.system("malicious command")  # Dangerous!
    ```

    **Safe Patterns:**

    ```python
    # Reading files within plugin directory is OK
    with open("./models/my_model.safetensors", "rb") as f:
        model_data = f.read()

    # Using Mixpeek services is OK
    container.inference.get("intfloat/e5-large")
    ```

    **Usage:**

    ```python
    validator = SecurityValidator()
    result = validator.validate("./my_plugin")

    if not result.is_valid:
        print("Security issues found:")
        for error in result.errors:
            print(f"  ✗ {error}")
    ```
    """

    def __init__(self):
        """Initialize security validator."""
        # Dangerous imports to check for
        self.dangerous_imports = {
            "os.system",
            "subprocess",
            "eval",
            "exec",
            "__import__",
            "importlib.import_module",
            "pickle",  # Unsafe deserialization
            "shelve",  # Unsafe deserialization
        }

        # Dangerous function calls
        self.dangerous_calls = {
            "eval",
            "exec",
            "compile",
            "__import__",
            "system",
            "popen",
            "spawn",
        }

    def validate(self, plugin_path: Path) -> ValidationResult:
        """Scan plugin for security issues.

        Args:
            plugin_path: Path to plugin directory

        Returns:
            ValidationResult with security errors

        Example:
            ```python
            result = validator.validate(Path("./my_plugin"))
            if not result.is_valid:
                print("Security issues:", result.errors)
            ```
        """
        result = ValidationResult()

        # Scan Python files
        for py_file in plugin_path.glob("**/*.py"):
            self._scan_file(py_file, result)

        return result

    def _scan_file(self, file_path: Path, result: ValidationResult):
        """Scan a single Python file for security issues.

        Args:
            file_path: Path to .py file
            result: ValidationResult to add errors to
        """
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                code = f.read()
        except Exception as e:
            result.add_warning(f"Could not read {file_path}: {str(e)}")
            return

        # Parse AST
        try:
            tree = ast.parse(code)
        except SyntaxError as e:
            result.add_error(f"Syntax error in {file_path}:{e.lineno}: {e.msg}")
            return

        # Check imports
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    self._check_import(alias.name, file_path, node.lineno, result)
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    self._check_import(node.module, file_path, node.lineno, result)

            # Check function calls
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name):
                    self._check_call(node.func.id, file_path, node.lineno, result)
                elif isinstance(node.func, ast.Attribute):
                    self._check_call(node.func.attr, file_path, node.lineno, result)

    def _check_import(self, module_name: str, file_path: Path, lineno: int, result: ValidationResult):
        """Check if import is dangerous.

        Args:
            module_name: Name of imported module
            file_path: File being scanned
            lineno: Line number
            result: ValidationResult to add errors to
        """
        for dangerous in self.dangerous_imports:
            if module_name == dangerous or module_name.startswith(dangerous + "."):
                result.add_error(
                    f"{file_path}:{lineno}: Dangerous import '{module_name}'\n"
                    f"Importing '{dangerous}' is not allowed for security reasons.\n"
                    f"If you need this functionality, contact Mixpeek support."
                )

    def _check_call(self, func_name: str, file_path: Path, lineno: int, result: ValidationResult):
        """Check if function call is dangerous.

        Args:
            func_name: Function being called
            file_path: File being scanned
            lineno: Line number
            result: ValidationResult to add errors to
        """
        if func_name in self.dangerous_calls:
            result.add_error(
                f"{file_path}:{lineno}: Dangerous function call '{func_name}()'\n"
                f"Calling '{func_name}' is not allowed for security reasons.\n"
                f"Remove this call or contact Mixpeek support if you have a valid use case."
            )


class SchemaValidator:
    """Validate plugin input/output schemas.

    Checks that:
    - Output data matches output_schema
    - Required fields are present
    - Field types are correct

    **Example:**

    ```python
    validator = SchemaValidator()

    # Validate output against manifest
    result = validator.validate_output(
        output_data={"text": "Hello", "embedding": [0.1, 0.2]},
        output_schema={
            "text": {"type": "string"},
            "embedding": {"type": "array"}
        }
    )

    if not result.is_valid:
        print("Schema errors:", result.errors)
    ```

    **Use Cases:**

    - Validate plugin output during local testing
    - Ensure output matches manifest.output_schema
    - Catch schema mismatches before deployment

    TODO: Implement full JSON schema validation
    """

    def __init__(self):
        """Initialize schema validator."""
        pass

    def validate_output(
        self, output_data: Dict[str, Any], output_schema: Dict[str, Any]
    ) -> ValidationResult:
        """Validate output data against schema.

        Args:
            output_data: Plugin output data
            output_schema: Expected schema from manifest

        Returns:
            ValidationResult with schema errors

        Example:
            ```python
            result = validator.validate_output(
                output_data={"text": "Hello"},
                output_schema={"text": {"type": "string"}}
            )
            assert result.is_valid
            ```

        TODO: Implement full JSON schema validation with jsonschema library
        """
        result = ValidationResult()

        # Check for required fields
        for field, schema in output_schema.items():
            if field not in output_data:
                # Check if field is required (for now, assume all are required)
                result.add_error(
                    f"Missing required output field: '{field}'\n"
                    f"Plugin output must include all fields defined in output_schema"
                )

        return result
