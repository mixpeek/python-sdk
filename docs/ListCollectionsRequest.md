# ListCollectionsRequest

Request model for listing collections.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**LogicalOperatorInput**](LogicalOperatorInput.md) | Filters to apply when listing collections | [optional] 
**sort** | [**SortOption**](SortOption.md) | Sort options for the results | [optional] 
**search** | **str** | Search query for filtering collections | [optional] 
**case_sensitive** | **bool** | If True, filters and search will be case-sensitive | [optional] [default to False]

## Example

```python
from mixpeek.models.list_collections_request import ListCollectionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListCollectionsRequest from a JSON string
list_collections_request_instance = ListCollectionsRequest.from_json(json)
# print the JSON string representation of the object
print(ListCollectionsRequest.to_json())

# convert the object into a dict
list_collections_request_dict = list_collections_request_instance.to_dict()
# create an instance of ListCollectionsRequest from a dict
list_collections_request_from_dict = ListCollectionsRequest.from_dict(list_collections_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


