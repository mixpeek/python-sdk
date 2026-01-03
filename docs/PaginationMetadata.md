# PaginationMetadata

Pagination metadata envelope.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Total number of records | 
**limit** | **int** | Requested page size | 
**offset** | **int** | Offset applied to query | 
**has_next** | **bool** | Whether additional pages exist | 

## Example

```python
from mixpeek.models.pagination_metadata import PaginationMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationMetadata from a JSON string
pagination_metadata_instance = PaginationMetadata.from_json(json)
# print the JSON string representation of the object
print(PaginationMetadata.to_json())

# convert the object into a dict
pagination_metadata_dict = pagination_metadata_instance.to_dict()
# create an instance of PaginationMetadata from a dict
pagination_metadata_from_dict = PaginationMetadata.from_dict(pagination_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


