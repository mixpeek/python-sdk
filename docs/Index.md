# Index

REQUIRED. Nested index configuration. VectorIndex if type='single' (most common case). MultiVectorIndex if type='multi' (rare, for hybrid search). Contains the full storage configuration including Qdrant collection name, dimensions, distance metric, and inference service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | REQUIRED. Fully-qualified name for the multi-vector index. Format: {extractor}_{version}_{output} (e.g., &#39;hybrid_extractor_v1_multi&#39;). Must be unique across namespace. | 
**description** | **str** | REQUIRED. Human-readable description of the multi-vector index. Explain what vector types are included and their purposes. Describe use cases for this multi-vector configuration. | 
**dimensions** | **int** | Number of vector dimensions. REQUIRED for DENSE vectors (e.g., 1024 for E5-Large, 1408 for multimodal). NOT REQUIRED for SPARSE vectors (dimensions determined dynamically). Must match the output dimensions of the inference service. Cannot be changed after index creation without recreating the collection. | [optional] 
**type** | [**VectorType**](VectorType.md) | REQUIRED. Vector storage format type. Determines how vectors are stored and searched in Qdrant. Use DENSE for traditional embeddings (most common), SPARSE for keyword-based models like SPLADE, MULTI_DENSE for late-interaction models like ColBERT. Must match the output format of your inference service. | 
**distance** | **str** | Distance metric for similarity search. OPTIONAL - defaults to &#39;cosine&#39; (normalized dot product). Options: &#39;cosine&#39; (most common, normalized), &#39;dot&#39; (raw dot product), &#39;euclidean&#39; (L2 distance), &#39;manhattan&#39; (L1 distance). Cosine recommended for most embeddings as it&#39;s scale-invariant. Must match the metric your model was trained with. | [optional] [default to 'cosine']
**datatype** | [**VectorDataType**](VectorDataType.md) | Data type for storing vector values. OPTIONAL - defaults to FLOAT32 (standard precision). Use FLOAT32 for general use (4 bytes per dimension). Use FLOAT16 to save 50% storage with minimal quality loss. Use UINT8 for maximum compression (quantization, ~2% quality loss). Lower precision &#x3D; smaller storage + faster search, slightly lower accuracy. | [optional] 
**on_disk** | **bool** | OPTIONAL. If true, vectors stored on disk instead of RAM. Defaults to true for memory efficiency. Set to false for faster search with higher memory usage. Trade-off: on_disk&#x3D;true saves ~95% RAM but ~10x slower search. Recommended to keep default (true) unless RAM is abundant and low latency critical. | [optional] 
**supported_inputs** | [**List[BucketSchemaFieldType]**](BucketSchemaFieldType.md) | OPTIONAL. List of bucket schema field types this vector can process. Validates that input fields are compatible with this index. Examples: TEXT and STRING for text embeddings, VIDEO and IMAGE for multimodal embeddings, DOCUMENT for PDF extractors. Used for validation during collection creation. | [optional] 
**inference_name** | **str** | DEPRECATED: Use inference_service_id instead. Identifier of the inference service to generate embeddings. Must reference a valid inference service registered in the system. Examples: &#39;multilingual_e5_large_instruct_v1&#39; for text, &#39;vertex_multimodal_embedding&#39; for video, &#39;laion_clip_vit_l_14_v1&#39; for images. This determines which model creates the vectors during ingestion. Cannot be changed after collection creation. | [optional] 
**inference_service_id** | **str** | RECOMMENDED. Service ID in org/name format (e.g., &#39;intfloat/e5-large&#39;). When set, dimensions and distance are automatically derived from the registry. This is the canonical identifier for cross-plugin compatibility. Plugins using the same service_id can search across each other&#39;s vectors. Takes precedence over inference_name when both are set. | [optional] 
**purpose** | [**VectorPurpose**](VectorPurpose.md) | RECOMMENDED. Semantic purpose of this vector index. Enables pipelines to look up vector configs by purpose (text, code, image) without needing to know the specific inference_service_id. This provides automatic configuration - the pipeline just says &#39;give me the text vector&#39; and gets the correct column name. If not specified, pipeline must use inference_service_id lookup. | [optional] 
**vector_name_override** | **str** | OPTIONAL. Override for Qdrant named vector identifier. When set, this value is used as the Qdrant vector name instead of auto-deriving from inference_service_id. This enables multiple vectors from the same embedding model with different storage names. The inference_service_id is still used for cross-extractor compatibility checking, but storage uses this custom name. Use case: A single extractor producing N vectors (e.g., title_embedding, body_embedding) using the same model but needing separate storage. | [optional] 
**vectors** | [**Dict[str, VectorIndex]**](VectorIndex.md) | REQUIRED. Dictionary mapping vector output names to their VectorIndex configurations. Each key is a unique identifier for that vector type within this multi-index. Each value is a complete VectorIndex with its own dimensions, type, and inference service. Example keys: &#39;dense&#39;, &#39;sparse&#39;, &#39;primary&#39;, &#39;secondary&#39;. | 

## Example

```python
from mixpeek.models.index import Index

# TODO update the JSON string below
json = "{}"
# create an instance of Index from a JSON string
index_instance = Index.from_json(json)
# print the JSON string representation of the object
print(Index.to_json())

# convert the object into a dict
index_dict = index_instance.to_dict()
# create an instance of Index from a dict
index_from_dict = Index.from_dict(index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


