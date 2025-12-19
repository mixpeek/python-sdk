# SourceDetails

Generic source details for any Qdrant point/document.  Keep this intentionally minimal so specialized models (e.g., DocumentSourceDetails) can extend it with domain-specific fields.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**SourceType**](SourceType.md) | Immediate origin type from which this entity was derived. | 
**source_id** | **str** | Identifier of the immediate source entity (e.g., bucket_id, collection_id, taxonomy_id). | 

## Example

```python
from mixpeek.models.source_details import SourceDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SourceDetails from a JSON string
source_details_instance = SourceDetails.from_json(json)
# print the JSON string representation of the object
print(SourceDetails.to_json())

# convert the object into a dict
source_details_dict = source_details_instance.to_dict()
# create an instance of SourceDetails from a dict
source_details_from_dict = SourceDetails.from_dict(source_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


