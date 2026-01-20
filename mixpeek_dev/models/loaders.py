"""Model loading utilities for custom models.

Supports loading models in various formats:
- .safetensors (recommended for security and speed)
- .pt / .pth (PyTorch native format)
- .onnx (ONNX Runtime for cross-platform inference)

Example usage in pipeline.py:
```python
from mixpeek_dev.models import load_custom_model

class MyExtractor:
    def __init__(self):
        self.model = load_custom_model("./models/my_model.safetensors")

    def __call__(self, batch):
        # Use self.model for inference
        embeddings = self.model.encode(batch["text"].tolist())
        batch["embedding"] = embeddings
        return batch
```
"""

from pathlib import Path
from typing import Any, Union


def load_custom_model(model_path: Union[str, Path]) -> Any:
    """Load a custom model from file.

    Automatically detects format based on file extension and loads appropriately.

    Args:
        model_path: Path to model file (.safetensors, .pt, .pth, or .onnx)

    Returns:
        Loaded model object (format depends on file type)

    Raises:
        FileNotFoundError: If model file doesn't exist
        ValueError: If file format is unsupported
        ImportError: If required library not installed

    Example:
        ```python
        # Load SafeTensors model (recommended)
        model = load_custom_model("./models/my_model.safetensors")

        # Load PyTorch model
        model = load_custom_model("./models/my_model.pt")

        # Load ONNX model
        model = load_custom_model("./models/my_model.onnx")
        ```
    """
    model_path = Path(model_path)

    if not model_path.exists():
        raise FileNotFoundError(
            f"Model file not found: {model_path}\n\n"
            f"Make sure you've placed your model file in the correct location.\n"
            f"For plugins, models should be in the models/ directory:\n"
            f"  my_plugin/models/my_model.safetensors\n\n"
            f"Supported formats: .safetensors, .pt, .pth, .onnx"
        )

    suffix = model_path.suffix.lower()

    if suffix == ".safetensors":
        return _load_safetensors(model_path)
    elif suffix in [".pt", ".pth"]:
        return _load_pytorch(model_path)
    elif suffix == ".onnx":
        return _load_onnx(model_path)
    else:
        raise ValueError(
            f"Unsupported model format: {suffix}\n\n"
            f"Supported formats:\n"
            f"  - .safetensors (recommended)\n"
            f"  - .pt or .pth (PyTorch)\n"
            f"  - .onnx (ONNX Runtime)\n\n"
            f"Convert your model to one of these formats first."
        )


def _load_safetensors(model_path: Path) -> Any:
    """Load SafeTensors format model.

    SafeTensors is the recommended format because:
    - Fast loading
    - Memory efficient
    - Secure (no arbitrary code execution)
    - Cross-framework compatible

    Args:
        model_path: Path to .safetensors file

    Returns:
        Dict of tensor name -> tensor value

    Raises:
        ImportError: If safetensors not installed
    """
    try:
        from safetensors import safe_open
    except ImportError:
        raise ImportError(
            "safetensors library required to load .safetensors models.\n\n"
            "Install with: pip install 'mixpeek[dev]'\n"
            "Or manually: pip install safetensors>=0.4.0"
        )

    # Load tensors
    tensors = {}
    with safe_open(model_path, framework="pt", device="cpu") as f:
        for key in f.keys():
            tensors[key] = f.get_tensor(key)

    # Return a simple wrapper that provides common interface
    return SafeTensorsModel(tensors, model_path)


def _load_pytorch(model_path: Path) -> Any:
    """Load PyTorch format model (.pt or .pth).

    Args:
        model_path: Path to .pt or .pth file

    Returns:
        Loaded PyTorch model

    Raises:
        ImportError: If torch not installed
    """
    try:
        import torch
    except ImportError:
        raise ImportError(
            "PyTorch required to load .pt/.pth models.\n\n"
            "Install with: pip install torch\n"
            "See: https://pytorch.org/get-started/locally/"
        )

    # Load model (map to CPU by default for compatibility)
    model = torch.load(model_path, map_location="cpu")

    # If it's a state dict, wrap it
    if isinstance(model, dict):
        return PyTorchStateDictModel(model, model_path)

    # Otherwise return the model directly
    if hasattr(model, "eval"):
        model.eval()  # Set to evaluation mode

    return model


def _load_onnx(model_path: Path) -> Any:
    """Load ONNX format model.

    ONNX is good for:
    - Cross-platform deployment
    - Optimized inference
    - Framework independence

    Args:
        model_path: Path to .onnx file

    Returns:
        ONNX InferenceSession

    Raises:
        ImportError: If onnxruntime not installed
    """
    try:
        import onnxruntime as ort
    except ImportError:
        raise ImportError(
            "ONNX Runtime required to load .onnx models.\n\n"
            "Install with: pip install 'mixpeek[dev]'\n"
            "Or manually: pip install onnxruntime>=1.16.0"
        )

    # Create inference session
    session = ort.InferenceSession(str(model_path))

    return ONNXModel(session, model_path)


# Model wrapper classes to provide consistent interface


class SafeTensorsModel:
    """Wrapper for SafeTensors models providing common interface."""

    def __init__(self, tensors: dict, path: Path):
        self.tensors = tensors
        self.path = path

    def __repr__(self):
        return f"SafeTensorsModel(path={self.path}, tensors={len(self.tensors)})"

    def get_tensor(self, name: str):
        """Get a specific tensor by name."""
        if name not in self.tensors:
            available = list(self.tensors.keys())
            raise KeyError(
                f"Tensor '{name}' not found in model.\n"
                f"Available tensors: {available}"
            )
        return self.tensors[name]

    def keys(self):
        """Get all tensor names."""
        return self.tensors.keys()


class PyTorchStateDictModel:
    """Wrapper for PyTorch state dict providing common interface."""

    def __init__(self, state_dict: dict, path: Path):
        self.state_dict = state_dict
        self.path = path

    def __repr__(self):
        return f"PyTorchStateDictModel(path={self.path}, params={len(self.state_dict)})"

    def get_param(self, name: str):
        """Get a specific parameter by name."""
        if name not in self.state_dict:
            available = list(self.state_dict.keys())
            raise KeyError(
                f"Parameter '{name}' not found in state dict.\n"
                f"Available params: {available[:10]}..."
            )
        return self.state_dict[name]

    def keys(self):
        """Get all parameter names."""
        return self.state_dict.keys()


class ONNXModel:
    """Wrapper for ONNX models providing common interface."""

    def __init__(self, session, path: Path):
        self.session = session
        self.path = path
        self._input_names = [i.name for i in session.get_inputs()]
        self._output_names = [o.name for o in session.get_outputs()]

    def __repr__(self):
        return f"ONNXModel(path={self.path}, inputs={self._input_names}, outputs={self._output_names})"

    def run(self, inputs: dict):
        """Run inference with ONNX model.

        Args:
            inputs: Dict of input_name -> numpy array

        Returns:
            List of output tensors

        Example:
            ```python
            model = load_custom_model("model.onnx")
            outputs = model.run({"input": input_array})
            ```
        """
        # Convert dict to list in correct order
        input_list = [inputs[name] for name in self._input_names]
        return self.session.run(self._output_names, dict(zip(self._input_names, input_list)))

    @property
    def input_names(self):
        """Get model input names."""
        return self._input_names

    @property
    def output_names(self):
        """Get model output names."""
        return self._output_names
