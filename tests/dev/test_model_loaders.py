"""Tests for custom model loading functionality."""

import tempfile
from pathlib import Path
import pytest
import numpy as np

from mixpeek_dev.models import load_custom_model


class TestModelLoaders:
    """Test suite for model loading utilities."""

    def test_load_safetensors_model(self):
        """Test loading a SafeTensors model."""
        # Create a temporary .safetensors file
        from safetensors.torch import save_file
        import torch

        with tempfile.NamedTemporaryFile(suffix=".safetensors", delete=False) as f:
            model_path = f.name
            # Create dummy tensors
            tensors = {
                "weight1": torch.randn(10, 20),
                "weight2": torch.randn(20, 30),
                "bias": torch.randn(30),
            }
            save_file(tensors, model_path)

        try:
            # Load the model
            model = load_custom_model(model_path)

            # Verify it loaded correctly
            assert hasattr(model, "tensors")
            assert hasattr(model, "get_tensor")
            assert "weight1" in model.keys()
            assert "weight2" in model.keys()
            assert "bias" in model.keys()

            # Verify we can get a tensor
            weight1 = model.get_tensor("weight1")
            assert weight1.shape == (10, 20)

            print("✓ SafeTensors model loaded successfully")

        finally:
            # Cleanup
            Path(model_path).unlink()

    def test_load_pytorch_state_dict(self):
        """Test loading a PyTorch state dict."""
        import torch

        with tempfile.NamedTemporaryFile(suffix=".pt", delete=False) as f:
            model_path = f.name
            # Create dummy state dict
            state_dict = {
                "layer1.weight": torch.randn(10, 20),
                "layer1.bias": torch.randn(10),
                "layer2.weight": torch.randn(10, 5),
            }
            torch.save(state_dict, model_path)

        try:
            # Load the model
            model = load_custom_model(model_path)

            # Verify it loaded correctly
            assert hasattr(model, "state_dict")
            assert hasattr(model, "get_param")
            assert "layer1.weight" in model.keys()
            assert "layer2.weight" in model.keys()

            # Verify we can get a parameter
            weight = model.get_param("layer1.weight")
            assert weight.shape == (10, 20)

            print("✓ PyTorch state dict loaded successfully")

        finally:
            # Cleanup
            Path(model_path).unlink()

    def test_load_onnx_model(self):
        """Test loading an ONNX model."""
        import torch
        import torch.nn as nn

        # Create a simple PyTorch model
        class SimpleModel(nn.Module):
            def __init__(self):
                super().__init__()
                self.linear = nn.Linear(10, 5)

            def forward(self, x):
                return self.linear(x)

        model = SimpleModel()
        model.eval()

        with tempfile.NamedTemporaryFile(suffix=".onnx", delete=False) as f:
            onnx_path = f.name

            # Export to ONNX
            dummy_input = torch.randn(1, 10)
            torch.onnx.export(
                model,
                dummy_input,
                onnx_path,
                input_names=["input"],
                output_names=["output"],
                dynamic_axes={"input": {0: "batch_size"}, "output": {0: "batch_size"}},
            )

        try:
            # Load the ONNX model
            onnx_model = load_custom_model(onnx_path)

            # Verify it loaded correctly
            assert hasattr(onnx_model, "session")
            assert hasattr(onnx_model, "run")
            assert hasattr(onnx_model, "input_names")
            assert hasattr(onnx_model, "output_names")

            # Verify input/output names
            assert "input" in onnx_model.input_names
            assert "output" in onnx_model.output_names

            # Test inference
            test_input = np.random.randn(1, 10).astype(np.float32)
            outputs = onnx_model.run({"input": test_input})
            assert len(outputs) > 0
            assert outputs[0].shape == (1, 5)

            print("✓ ONNX model loaded and inference successful")

        finally:
            # Cleanup
            Path(onnx_path).unlink()

    def test_unsupported_format(self):
        """Test that unsupported formats raise ValueError."""
        with tempfile.NamedTemporaryFile(suffix=".pkl", delete=False) as f:
            model_path = f.name

        try:
            with pytest.raises(ValueError, match="Unsupported model format"):
                load_custom_model(model_path)

            print("✓ Unsupported format correctly rejected")

        finally:
            # Cleanup
            Path(model_path).unlink()

    def test_file_not_found(self):
        """Test that missing files raise FileNotFoundError."""
        with pytest.raises(FileNotFoundError, match="Model file not found"):
            load_custom_model("/nonexistent/model.safetensors")

        print("✓ File not found correctly detected")


if __name__ == "__main__":
    # Run tests manually
    test_suite = TestModelLoaders()

    print("\n=== Testing Custom Model Loaders ===\n")

    try:
        test_suite.test_load_safetensors_model()
    except Exception as e:
        print(f"✗ SafeTensors test failed: {e}")

    try:
        test_suite.test_load_pytorch_state_dict()
    except Exception as e:
        print(f"✗ PyTorch test failed: {e}")

    try:
        test_suite.test_load_onnx_model()
    except Exception as e:
        print(f"✗ ONNX test failed: {e}")

    try:
        test_suite.test_unsupported_format()
    except Exception as e:
        print(f"✗ Unsupported format test failed: {e}")

    try:
        test_suite.test_file_not_found()
    except Exception as e:
        print(f"✗ File not found test failed: {e}")

    print("\n=== Model Loader Tests Complete ===\n")
