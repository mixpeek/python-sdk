# MultiVectorIndex

Configuration for multi-vector indexes.  Allows a single extractor to produce multiple named vector outputs in one index. Useful for hybrid search combining different embedding types or multiple models.  Use Cases:     - Hybrid dense + sparse embeddings in one index     - Multiple models for ensemble retrieval     - Different granularities (sentence + paragraph embeddings)  Requirements:     - name: REQUIRED - Full qualified name for the multi-vector index     - description: REQUIRED - Explain what vector combinations are included     - vectors: REQUIRED - Dictionary mapping output names to VectorIndex configs  Note: Currently less common than single VectorIndex. Most extractors use separate VectorIndexDefinitions for each output instead.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | REQUIRED. Fully-qualified name for the multi-vector index. Format: {extractor}_{version}_{output} (e.g., &#39;hybrid_extractor_v1_multi&#39;). Must be unique across namespace. | 
**description** | **str** | REQUIRED. Human-readable description of the multi-vector index. Explain what vector types are included and their purposes. Describe use cases for this multi-vector configuration. | 
**vectors** | [**Dict[str, VectorIndex]**](VectorIndex.md) | REQUIRED. Dictionary mapping vector output names to their VectorIndex configurations. Each key is a unique identifier for that vector type within this multi-index. Each value is a complete VectorIndex with its own dimensions, type, and inference service. Example keys: &#39;dense&#39;, &#39;sparse&#39;, &#39;primary&#39;, &#39;secondary&#39;. | 

## Example

```python
from mixpeek.models.multi_vector_index import MultiVectorIndex

# TODO update the JSON string below
json = "{}"
# create an instance of MultiVectorIndex from a JSON string
multi_vector_index_instance = MultiVectorIndex.from_json(json)
# print the JSON string representation of the object
print(MultiVectorIndex.to_json())

# convert the object into a dict
multi_vector_index_dict = multi_vector_index_instance.to_dict()
# create an instance of MultiVectorIndex from a dict
multi_vector_index_from_dict = MultiVectorIndex.from_dict(multi_vector_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


