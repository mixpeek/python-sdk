"""Mock service container for local plugin testing.

This module provides deterministic mock implementations of Mixpeek services
for fast, offline plugin testing.

**Philosophy:**

Mock services are designed to be:
1. **Deterministic**: Same input always produces same output (critical for testing)
2. **Fast**: No model loading, no network calls (runs in milliseconds)
3. **Zero dependencies**: No model files, no external services
4. **Drop-in compatible**: Same interface as real ServiceContainer

**Key Classes:**

- `MockServiceContainer`: Drop-in replacement for engine ServiceContainer
- `MockE5Embedding`: Hash-based deterministic embeddings (mimics intfloat/e5-large)
- `MockWhisper`: Dummy transcription service (mimics openai/whisper)
- `MockQdrant`: In-memory vector storage (mimics Qdrant)

**Example Usage:**

```python
from mixpeek_dev.testing import MockServiceContainer

# Create mock container (drop-in replacement for real container)
container = MockServiceContainer()

# Get mock E5 service (deterministic embeddings)
e5 = container.inference.get("intfloat/e5-large")
embeddings = e5.embed_batch(["text1", "text2"])  # Hash-based, deterministic

# Get mock Whisper service (dummy transcription)
whisper = container.inference.get("openai/whisper")
transcription = whisper.transcribe("audio.mp3")  # Returns dummy text
```

**Deterministic Embeddings:**

The mock E5 service uses SHA-256 hashing to generate embeddings:
- Same text always produces same embedding
- Perfect for unit tests (no randomness)
- Normalized vectors (unit length)
- Configurable dimensions (default: 1024 to match E5-Large)

**How It Works:**

```python
# Input text
text = "Hello world"

# Generate deterministic seed from SHA-256 hash
hash_bytes = hashlib.sha256(text.encode()).digest()
seed = int.from_bytes(hash_bytes[:4], byteorder="big")

# Use seed to generate reproducible random vector
rng = np.random.default_rng(seed)
embedding = rng.standard_normal(1024)

# Normalize to unit length
embedding = embedding / np.linalg.norm(embedding)
```

This ensures:
- "Hello world" always gets the same embedding
- Different texts get different embeddings
- Embeddings are properly normalized

**Testing Strategy:**

Use mocks for:
- ✓ Unit tests (fast, no deps)
- ✓ Schema validation (check output structure)
- ✓ Pipeline logic (test step order, data flow)
- ✓ Error handling (test failure cases)

Don't use mocks for:
- ✗ Semantic search quality (mock embeddings aren't semantic)
- ✗ Model accuracy (mock models return dummy data)
- ✗ Performance benchmarking (mocks are artificially fast)

For these, use --local-stack or --environment=production mode.
"""

import hashlib
from typing import Any, Dict, List, Optional

import numpy as np


class MockInferenceAccessor:
    """Mock inference service accessor.

    Provides the same .get(service_name) interface as the real
    InferenceServiceAccessor but returns mock services.

    **Supported Services:**

    - intfloat/e5-large: MockE5Embedding (1024-dim hash embeddings)
    - intfloat/e5-*: MockE5Embedding (any E5 variant)
    - intfloat/multilingual-e5-large-instruct: MockE5Embedding
    - openai/whisper-*: MockWhisper (dummy transcription)
    - openai/whisper: MockWhisper

    **Error Handling:**

    If you request an unsupported service:
    ```python
    container.inference.get("unknown/service")
    # Raises: ValueError with list of supported services
    ```

    Example:
        ```python
        accessor = MockInferenceAccessor()

        # Get E5 embedding service
        e5 = accessor.get("intfloat/e5-large")
        assert isinstance(e5, MockE5Embedding)

        # Get Whisper service
        whisper = accessor.get("openai/whisper")
        assert isinstance(whisper, MockWhisper)
        ```
    """

    def __init__(self):
        """Initialize mock inference accessor."""
        self._services: Dict[str, Any] = {}

    def get(self, service_name: str) -> Any:
        """Get a mock inference service by name.

        Args:
            service_name: Service identifier (e.g., "intfloat/e5-large")

        Returns:
            Mock service instance

        Raises:
            ValueError: If service_name is not supported

        Example:
            ```python
            accessor = MockInferenceAccessor()
            e5 = accessor.get("intfloat/e5-large")
            embeddings = await e5.embed_batch(["text1", "text2"])
            ```
        """
        # Return cached service if already created
        if service_name in self._services:
            return self._services[service_name]

        # Create appropriate mock service
        if "e5" in service_name.lower():
            # All E5 variants use MockE5Embedding
            service = MockE5Embedding(service_name=service_name)
        elif "whisper" in service_name.lower():
            # All Whisper variants use MockWhisper
            service = MockWhisper(service_name=service_name)
        else:
            # Unsupported service
            supported = [
                "intfloat/e5-large",
                "intfloat/e5-base",
                "intfloat/multilingual-e5-large-instruct",
                "openai/whisper",
                "openai/whisper-large-v3",
            ]
            raise ValueError(
                f"Unsupported service: {service_name}\n\n"
                f"MockServiceContainer supports:\n"
                + "\n".join(f"  - {s}" for s in supported)
                + "\n\n"
                f"Add support for '{service_name}' to mock_services.py or use --local-stack mode."
            )

        # Cache and return
        self._services[service_name] = service
        return service


class MockModelsAccessor:
    """Mock models accessor.

    Provides access to custom models loaded from local files.
    In mock mode, this returns dummy models.

    TODO Phase 3: Implement custom model loading
    """

    def __init__(self):
        """Initialize mock models accessor."""
        self._models: Dict[str, Any] = {}

    def get(self, model_name: str) -> Any:
        """Get a mock model by name.

        Args:
            model_name: Model identifier

        Returns:
            Mock model instance

        Raises:
            NotImplementedError: Custom models not yet supported in mock mode
        """
        raise NotImplementedError(
            f"Custom models not yet supported in mock mode.\n\n"
            f"Use --local-stack mode to test with custom models."
        )


class MockServiceContainer:
    """Mock service container - drop-in replacement for engine ServiceContainer.

    This container provides the same interface as the production ServiceContainer
    but returns mock services for fast, deterministic testing.

    **Attributes:**
        inference: MockInferenceAccessor for getting inference services
        models: MockModelsAccessor for getting custom models

    **Interface Compatibility:**

    Real ServiceContainer:
    ```python
    from engine.services.container import ServiceContainer
    container = ServiceContainer.create(namespace_id="org_123")
    e5 = container.inference.get("intfloat/e5-large")
    ```

    MockServiceContainer:
    ```python
    from mixpeek_dev.testing import MockServiceContainer
    container = MockServiceContainer()
    e5 = container.inference.get("intfloat/e5-large")
    ```

    Both provide the same interface, so plugins work unchanged.

    Example:
        ```python
        # Plugin code (works with both real and mock container)
        def build_pipeline(container):
            e5 = container.inference.get("intfloat/e5-large")
            whisper = container.inference.get("openai/whisper")
            return [whisper, e5]

        # Testing with mock
        container = MockServiceContainer()
        pipeline = build_pipeline(container)
        # Uses MockWhisper and MockE5Embedding

        # Production with real container
        container = ServiceContainer.create(namespace_id="org_123")
        pipeline = build_pipeline(container)
        # Uses real Whisper and E5 models
        ```
    """

    def __init__(self):
        """Initialize mock service container.

        Creates inference and models accessors.
        """
        self.inference = MockInferenceAccessor()
        self.models = MockModelsAccessor()


class MockE5Embedding:
    """Mock E5 embedding service with deterministic hash-based embeddings.

    This service mimics the behavior of intfloat/e5-large and other E5 variants
    but generates embeddings using SHA-256 hashing instead of a neural network.

    **Key Properties:**

    - **Deterministic**: Same text always produces same embedding
    - **Fast**: No model loading or GPU inference
    - **Normalized**: All embeddings have unit length
    - **Configurable dimensions**: Default 1024 (matches E5-Large)

    **Example:**

    ```python
    mock_e5 = MockE5Embedding()

    # Generate embeddings
    texts = ["Hello world", "Another text"]
    embeddings = mock_e5.embed_batch(texts)

    # embeddings[0] is always the same for "Hello world"
    # embeddings[1] is always the same for "Another text"

    assert len(embeddings) == 2
    assert len(embeddings[0]) == 1024
    assert np.allclose(np.linalg.norm(embeddings[0]), 1.0)  # Normalized
    ```

    **Limitations:**

    Mock embeddings are NOT semantically meaningful:
    - Similar texts don't necessarily have similar embeddings
    - Cosine similarity is essentially random
    - Don't use for testing search quality

    For semantic search testing, use --local-stack or --environment=production mode.

    **Algorithm:**

    ```python
    def text_to_embedding(text: str, dim: int) -> List[float]:
        # 1. Hash text to get deterministic seed
        hash_bytes = hashlib.sha256(text.encode()).digest()
        seed = int.from_bytes(hash_bytes[:4], byteorder="big")

        # 2. Generate random vector from seed
        rng = np.random.default_rng(seed)
        embedding = rng.standard_normal(dim)

        # 3. Normalize to unit length
        embedding = embedding / np.linalg.norm(embedding)

        return embedding.tolist()
    ```
    """

    def __init__(self, service_name: str = "intfloat/e5-large", embedding_dim: int = 1024):
        """Initialize mock E5 embedding service.

        Args:
            service_name: Service identifier (for logging/debugging)
            embedding_dim: Embedding dimension (default 1024 for E5-Large)

        Example:
            ```python
            # Default (E5-Large, 1024 dimensions)
            e5 = MockE5Embedding()

            # Custom dimensions
            e5_small = MockE5Embedding(
                service_name="intfloat/e5-small",
                embedding_dim=384
            )
            ```
        """
        self.service_name = service_name
        self.embedding_dim = embedding_dim

    def text_to_embedding(self, text: str) -> List[float]:
        """Generate deterministic embedding from text using SHA-256 hash.

        Args:
            text: Input text

        Returns:
            List of floats (normalized embedding)

        Example:
            ```python
            e5 = MockE5Embedding()
            emb = e5.text_to_embedding("Hello world")
            assert len(emb) == 1024
            assert abs(np.linalg.norm(emb) - 1.0) < 1e-6  # Unit length
            ```
        """
        # Use SHA-256 hash for deterministic output
        hash_bytes = hashlib.sha256(text.encode("utf-8")).digest()

        # Create seed from hash
        seed = int.from_bytes(hash_bytes[:4], byteorder="big")
        rng = np.random.default_rng(seed)

        # Generate embedding and normalize
        embedding = rng.standard_normal(self.embedding_dim).astype(np.float32)
        norm = np.linalg.norm(embedding)
        if norm > 0:
            embedding = embedding / norm

        return embedding.tolist()

    def embed_batch(self, texts: List[str]) -> List[List[float]]:
        """Generate embeddings for a batch of texts.

        Args:
            texts: List of input texts

        Returns:
            List of embeddings (one per text)

        Example:
            ```python
            e5 = MockE5Embedding()
            embeddings = e5.embed_batch(["text1", "text2", "text3"])
            assert len(embeddings) == 3
            assert all(len(emb) == 1024 for emb in embeddings)
            ```
        """
        return [self.text_to_embedding(text) for text in texts]


class MockWhisper:
    """Mock Whisper transcription service.

    Returns dummy transcription for testing purposes.

    **Behavior:**

    - Always returns the same dummy transcription
    - No actual audio processing
    - Instant execution (no model loading)

    **Example:**

    ```python
    whisper = MockWhisper()
    result = whisper.transcribe("audio.mp3")
    # result = {"text": "Mock transcription of audio file."}
    ```

    **Use Cases:**

    Use MockWhisper for:
    - ✓ Testing pipeline structure (Whisper → E5 flow)
    - ✓ Testing error handling
    - ✓ Testing data transformations after transcription

    Don't use for:
    - ✗ Testing transcription quality
    - ✗ Testing language detection
    - ✗ Testing timestamp accuracy

    For real transcription testing, use --local-stack or --environment=production mode.
    """

    def __init__(self, service_name: str = "openai/whisper"):
        """Initialize mock Whisper service.

        Args:
            service_name: Service identifier (for logging/debugging)
        """
        self.service_name = service_name

    def transcribe(self, audio_path: str, **kwargs) -> Dict[str, Any]:
        """Mock transcription (returns dummy text).

        Args:
            audio_path: Path to audio file (unused in mock)
            **kwargs: Additional parameters (unused in mock)

        Returns:
            Dict with 'text' key containing dummy transcription

        Example:
            ```python
            whisper = MockWhisper()
            result = whisper.transcribe("audio.mp3")
            assert result["text"] == "Mock transcription of audio file."
            ```
        """
        return {
            "text": "Mock transcription of audio file.",
            "language": "en",
            "duration": 10.0,
            "segments": [],
        }


class MockQdrant:
    """Mock Qdrant vector database - in-memory storage.

    Provides basic vector storage for testing but does NOT support
    semantic search (no similarity computation).

    **Supported Operations:**

    - ✓ Store vectors (in-memory dict)
    - ✓ Retrieve by ID
    - ✗ Semantic search (not supported in mock mode)

    **Example:**

    ```python
    qdrant = MockQdrant()

    # Store vectors
    qdrant.upsert(collection="my_collection", points=[
        {"id": "1", "vector": [0.1, 0.2, ...], "payload": {"text": "doc1"}},
        {"id": "2", "vector": [0.3, 0.4, ...], "payload": {"text": "doc2"}},
    ])

    # Retrieve by ID
    point = qdrant.retrieve(collection="my_collection", ids=["1"])
    assert point[0]["payload"]["text"] == "doc1"

    # Search (not supported)
    qdrant.search(collection="my_collection", vector=[0.5, 0.6, ...])
    # Raises: NotImplementedError
    ```

    **Limitations:**

    MockQdrant does NOT support semantic search because:
    - Mock embeddings aren't semantically meaningful
    - No vector similarity computation
    - Would give misleading results

    For E2E testing with search, use --local-stack mode which runs
    real Qdrant in Docker.

    TODO Phase 4: Implement local-stack mode with real Qdrant
    """

    def __init__(self):
        """Initialize mock Qdrant with in-memory storage."""
        self._collections: Dict[str, Dict[str, Any]] = {}

    def create_collection(self, collection: str, **kwargs):
        """Create a collection.

        Args:
            collection: Collection name
            **kwargs: Collection parameters (unused in mock)
        """
        if collection not in self._collections:
            self._collections[collection] = {}

    def upsert(self, collection: str, points: List[Dict[str, Any]]):
        """Store vectors in collection.

        Args:
            collection: Collection name
            points: List of point dicts with id, vector, payload

        Example:
            ```python
            qdrant.upsert("my_collection", [
                {"id": "1", "vector": [0.1, 0.2], "payload": {"text": "doc1"}},
            ])
            ```
        """
        if collection not in self._collections:
            self.create_collection(collection)

        for point in points:
            self._collections[collection][point["id"]] = point

    def retrieve(self, collection: str, ids: List[str]) -> List[Dict[str, Any]]:
        """Retrieve points by ID.

        Args:
            collection: Collection name
            ids: List of point IDs

        Returns:
            List of point dicts

        Example:
            ```python
            points = qdrant.retrieve("my_collection", ["1", "2"])
            ```
        """
        if collection not in self._collections:
            return []

        return [
            self._collections[collection][id]
            for id in ids
            if id in self._collections[collection]
        ]

    def search(self, collection: str, vector: List[float], limit: int = 5):
        """Search for similar vectors (NOT SUPPORTED in mock mode).

        Args:
            collection: Collection name
            vector: Query vector
            limit: Number of results

        Raises:
            NotImplementedError: Semantic search not supported in mock mode

        Example:
            ```python
            # This raises NotImplementedError
            qdrant.search("my_collection", [0.1, 0.2, ...])
            ```

        **Why Not Supported:**

        Mock embeddings are hash-based and not semantically meaningful.
        Providing search results would be misleading.

        **Solution:**

        Use --local-stack mode for E2E testing with real Qdrant:
        ```bash
        mixpeek test --local-stack
        ```
        """
        raise NotImplementedError(
            f"Semantic search not supported in mock mode.\n\n"
            f"Mock embeddings are hash-based and not semantically meaningful.\n"
            f"For E2E testing with search, use --local-stack mode:\n\n"
            f"  mixpeek test --local-stack\n\n"
            f"This will start real Qdrant in Docker for semantic search testing."
        )
