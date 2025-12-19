# SourceCollectionOutput

A source collection for a flat taxonomy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_id** | **str** | The ID of the source collection for the taxonomy. | 
**enrichment_fields** | [**List[EnrichmentField]**](EnrichmentField.md) | Fields to copy from matched taxonomy node when enriching (append/replace semantics). If omitted, the full payload is copied. | [optional] 

## Example

```python
from mixpeek.models.source_collection_output import SourceCollectionOutput

# TODO update the JSON string below
json = "{}"
# create an instance of SourceCollectionOutput from a JSON string
source_collection_output_instance = SourceCollectionOutput.from_json(json)
# print the JSON string representation of the object
print(SourceCollectionOutput.to_json())

# convert the object into a dict
source_collection_output_dict = source_collection_output_instance.to_dict()
# create an instance of SourceCollectionOutput from a dict
source_collection_output_from_dict = SourceCollectionOutput.from_dict(source_collection_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


