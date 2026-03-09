# StageDefsVectorQueryInput

Raw embedding vector query input for direct vector similarity search.  Accepts a pre-computed embedding vector and uses it directly for similarity search without any inference. Useful for programmatic use cases such as taxonomy enrichment where embeddings are already available.  Use Cases:     - Taxonomy enrichment (passing pre-computed document embeddings)     - Programmatic similarity search with known vectors     - Cross-collection matching with pre-extracted features     - ColBERT/multi-vector search with pre-computed token embeddings  Examples:     Single dense vector:         ```json         {\"input_mode\": \"vector\", \"value\": [0.1, 0.2, 0.3, ...]}         ```      Multi-dense vector (ColBERT — list of token embeddings):         ```json         {\"input_mode\": \"vector\", \"value\": [[0.1, 0.2], [0.3, 0.4], ...]}         ```      Template-based (from taxonomy input mapping):         ```json         {\"input_mode\": \"vector\", \"value\": \"{{INPUT.query_image}}\"}         ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_mode** | **str** | Discriminator field. Always &#39;vector&#39; for raw embedding queries. | [optional] [default to 'vector']
**value** | [**Value2**](Value2.md) |  | [optional] 

## Example

```python
from mixpeek.models.stage_defs_vector_query_input import StageDefsVectorQueryInput

# TODO update the JSON string below
json = "{}"
# create an instance of StageDefsVectorQueryInput from a JSON string
stage_defs_vector_query_input_instance = StageDefsVectorQueryInput.from_json(json)
# print the JSON string representation of the object
print(StageDefsVectorQueryInput.to_json())

# convert the object into a dict
stage_defs_vector_query_input_dict = stage_defs_vector_query_input_instance.to_dict()
# create an instance of StageDefsVectorQueryInput from a dict
stage_defs_vector_query_input_from_dict = StageDefsVectorQueryInput.from_dict(stage_defs_vector_query_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


