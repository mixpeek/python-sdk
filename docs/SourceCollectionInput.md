# SourceCollectionInput

A source collection for a flat taxonomy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_id** | **str** | The ID of the source collection for the taxonomy. | 
**enrichment_fields** | [**List[EnrichmentField]**](EnrichmentField.md) | Fields to copy from matched taxonomy node when enriching (append/replace semantics). If omitted, the full payload is copied. | [optional] 

## Example

```python
from mixpeek.models.source_collection_input import SourceCollectionInput

# TODO update the JSON string below
json = "{}"
# create an instance of SourceCollectionInput from a JSON string
source_collection_input_instance = SourceCollectionInput.from_json(json)
# print the JSON string representation of the object
print(SourceCollectionInput.to_json())

# convert the object into a dict
source_collection_input_dict = source_collection_input_instance.to_dict()
# create an instance of SourceCollectionInput from a dict
source_collection_input_from_dict = SourceCollectionInput.from_dict(source_collection_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


