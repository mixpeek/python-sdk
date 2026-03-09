# EnrichmentInputMapping

Maps a document field or constant to a retriever input parameter.  Defines how to construct retriever inputs from the document being enriched.  Attributes:     input_key: The retriever input parameter name     source: Where to get the value from (document field or constant)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_key** | **str** | The retriever input parameter name | 
**source** | [**InputMappingSource**](InputMappingSource.md) | Where to get the value from (document field or constant) | 

## Example

```python
from mixpeek.models.enrichment_input_mapping import EnrichmentInputMapping

# TODO update the JSON string below
json = "{}"
# create an instance of EnrichmentInputMapping from a JSON string
enrichment_input_mapping_instance = EnrichmentInputMapping.from_json(json)
# print the JSON string representation of the object
print(EnrichmentInputMapping.to_json())

# convert the object into a dict
enrichment_input_mapping_dict = enrichment_input_mapping_instance.to_dict()
# create an instance of EnrichmentInputMapping from a dict
enrichment_input_mapping_from_dict = EnrichmentInputMapping.from_dict(enrichment_input_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


