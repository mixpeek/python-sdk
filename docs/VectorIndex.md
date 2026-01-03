# VectorIndex

Configuration for a single vector index in Qdrant.  Defines the fully-qualified vector index including storage name, dimensions, distance metric, and inference service. This is the actual index that gets created in Qdrant and used for vector similarity search.  Key Concepts:     - The `name` field is the FULL qualified name used as the Qdrant collection name     - Format: {extractor}_{version}_{output} (e.g., \"text_extractor_v1_embedding\")     - This ensures namespace isolation between extractors and versions     - Different from VectorIndexDefinition.name which is the short user-facing name  Use Cases:     - Define vector storage configuration for feature extractors     - Specify inference service and model parameters     - Configure distance metrics for similarity search     - Set storage optimization (on-disk for large vectors)  Requirements:     - name: REQUIRED - Must be unique across all extractors in namespace     - description: REQUIRED - Explain what this vector represents     - dimensions: REQUIRED for DENSE vectors, OPTIONAL for SPARSE     - type: REQUIRED - Must match VectorType enum     - inference_name: REQUIRED - Must reference a valid inference service

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | REQUIRED. Fully-qualified vector index name (Qdrant collection name). Format: {extractor}_{version}_{output} (e.g., &#39;text_extractor_v1_embedding&#39;). This is the STORAGE name used internally in Qdrant, NOT the user-facing short name. Must be unique across all extractors in the namespace to prevent collisions. Different versions of same extractor use different names for isolation. | 
**description** | **str** | REQUIRED. Human-readable description of what this vector index represents. Explain the content type, use cases, and search characteristics. Shown in API documentation and collection metadata. Be specific about what embeddings are stored here. | 
**dimensions** | **int** | Number of vector dimensions. REQUIRED for DENSE vectors (e.g., 1024 for E5-Large, 1408 for multimodal). NOT REQUIRED for SPARSE vectors (dimensions determined dynamically). Must match the output dimensions of the inference service. Cannot be changed after index creation without recreating the collection. | [optional] 
**type** | [**VectorType**](VectorType.md) | REQUIRED. Vector storage format type. Determines how vectors are stored and searched in Qdrant. Use DENSE for traditional embeddings (most common), SPARSE for keyword-based models like SPLADE, MULTI_DENSE for late-interaction models like ColBERT. Must match the output format of your inference service. | 
**distance** | **str** | Distance metric for similarity search. OPTIONAL - defaults to &#39;cosine&#39; (normalized dot product). Options: &#39;cosine&#39; (most common, normalized), &#39;dot&#39; (raw dot product), &#39;euclidean&#39; (L2 distance), &#39;manhattan&#39; (L1 distance). Cosine recommended for most embeddings as it&#39;s scale-invariant. Must match the metric your model was trained with. | [optional] [default to 'cosine']
**datatype** | [**VectorDataType**](VectorDataType.md) | Data type for storing vector values. OPTIONAL - defaults to FLOAT32 (standard precision). Use FLOAT32 for general use (4 bytes per dimension). Use FLOAT16 to save 50% storage with minimal quality loss. Use UINT8 for maximum compression (quantization, ~2% quality loss). Lower precision &#x3D; smaller storage + faster search, slightly lower accuracy. | [optional] 
**on_disk** | **bool** | OPTIONAL. If true, vectors stored on disk instead of RAM. Use for very large vectors (&gt;2GB total) to save memory. Trade-off: ~10x slower search, but unlimited capacity. Defaults to false (RAM storage) for fast search. Enable for: massive datasets, high-dimensional vectors (&gt;2048 dims), or when RAM is constrained. Recommended for ColBERT (500KB/doc). | [optional] 
**supported_inputs** | [**List[BucketSchemaFieldType]**](BucketSchemaFieldType.md) | OPTIONAL. List of bucket schema field types this vector can process. Validates that input fields are compatible with this index. Examples: TEXT and STRING for text embeddings, VIDEO and IMAGE for multimodal embeddings, DOCUMENT for PDF extractors. Used for validation during collection creation. | [optional] 
**inference_name** | **str** | REQUIRED. Identifier of the inference service to generate embeddings. Must reference a valid inference service registered in the system. Examples: &#39;multilingual_e5_large_instruct_v1&#39; for text, &#39;vertex_multimodal_embedding&#39; for video, &#39;laion_clip_vit_l_14_v1&#39; for images. This determines which model creates the vectors during ingestion. Cannot be changed after collection creation. | [optional] 

## Example

```python
from mixpeek.models.vector_index import VectorIndex

# TODO update the JSON string below
json = "{}"
# create an instance of VectorIndex from a JSON string
vector_index_instance = VectorIndex.from_json(json)
# print the JSON string representation of the object
print(VectorIndex.to_json())

# convert the object into a dict
vector_index_dict = vector_index_instance.to_dict()
# create an instance of VectorIndex from a dict
vector_index_from_dict = VectorIndex.from_dict(vector_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


