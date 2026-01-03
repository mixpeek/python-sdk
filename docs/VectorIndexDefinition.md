# VectorIndexDefinition

Complete vector index definition that can be either single or multi-vector.  This is the USER-FACING representation that appears in feature extractor definitions and API responses. It wraps a VectorIndex (or MultiVectorIndex) and adds metadata.  Key Concepts - Two-Name System:     - VectorIndexDefinition.name: SHORT user-facing name (e.g., \"embedding\")       Used in feature URIs: mixpeek://text_extractor@v1/multilingual_e5_large_instruct_v1                                                         ^^^^^^^^^^      - VectorIndex.name: FULL storage name (e.g., \"text_extractor_v1_embedding\")       Used as Qdrant collection name for namespace isolation  This two-level naming allows clean URIs while preventing storage collisions.  Use Cases:     - Define extractor outputs in feature extractor definitions     - Expose available vector indexes in collection metadata     - Enable feature URI resolution (short name → full storage name)  Requirements:     - name: REQUIRED - Short output name for feature URIs     - description: REQUIRED - Explain what this output produces     - type: REQUIRED - \"single\" (most common) or \"multi\" (rare)     - index: REQUIRED - Nested VectorIndex or MultiVectorIndex     - feature_uri: OPTIONAL - Populated at collection creation time

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_uri** | **str** | Full feature URI for this vector index. Format: mixpeek://{extractor}@{version}/{output_name}. Populated at collection creation time. Use this URI in retriever feature_filter stages. | [optional] 
**name** | **str** | REQUIRED. Short user-facing output name used in feature URIs. This is NOT the Qdrant collection name - it&#39;s the clean identifier for this output. Format: Simple snake_case name (e.g., &#39;embedding&#39;, &#39;video_embedding&#39;, &#39;sparse_embedding&#39;). Used in feature URIs: mixpeek://{extractor}@{version}/{THIS_NAME}. Must be unique within this extractor&#39;s outputs. | 
**description** | **str** | REQUIRED. Human-readable description of this vector output. Explain what content this output embeds and when to use it. Appears in API documentation and helps users choose the right feature URI. Be specific about the embedding type and use cases. | 
**type** | **str** | REQUIRED. Index type - &#39;single&#39; or &#39;multi&#39;. &#39;single&#39;: One vector per document (most common). Use for standard embeddings. &#39;multi&#39;: Multiple named vectors per document (rare). Use for hybrid/ensemble. Determines whether &#39;index&#39; field contains VectorIndex or MultiVectorIndex. | 
**index** | [**Index**](Index.md) |  | 

## Example

```python
from mixpeek.models.vector_index_definition import VectorIndexDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of VectorIndexDefinition from a JSON string
vector_index_definition_instance = VectorIndexDefinition.from_json(json)
# print the JSON string representation of the object
print(VectorIndexDefinition.to_json())

# convert the object into a dict
vector_index_definition_dict = vector_index_definition_instance.to_dict()
# create an instance of VectorIndexDefinition from a dict
vector_index_definition_from_dict = VectorIndexDefinition.from_dict(vector_index_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


