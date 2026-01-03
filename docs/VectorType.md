# VectorType

Vector types supported by the Mixpeek system.  Defines the storage format and structure of embeddings in Qdrant.  Values:     DENSE: Traditional float array embeddings (e.g., [0.1, 0.2, 0.3]).            Most common format. Used by: text_extractor, multimodal_extractor, image_extractor.            Storage: ~4KB per 1024-dim vector. Fast cosine/dot similarity search.      SPARSE: Index-value pairs for sparse embeddings (e.g., SPLADE, BM25).             Only stores non-zero dimensions. Format: {indices: [1,5,9], values: [0.8,0.6,0.4]}.             Storage: ~20KB. Keyword-based semantic search.      MULTI_DENSE: List of dense vectors for late interaction models (e.g., ColBERT).                  Each document has multiple embeddings. Format: [[0.1,0.2], [0.3,0.4], ...].                  Storage: ~500KB. High-precision retrieval.  Examples:     - DENSE for general semantic search (text_extractor, multimodal_extractor)     - SPARSE for keyword expansion and explainability     - MULTI_DENSE for maximum precision retrieval

## Enum

* `DENSE` (value: `'dense'`)

* `SPARSE` (value: `'sparse'`)

* `MULTI_DENSE` (value: `'multi_dense'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


