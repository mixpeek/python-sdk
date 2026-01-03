# ListCollectionsResponse

Response model for listing collections.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[CollectionResponse]**](CollectionResponse.md) | List of collections | 
**pagination** | [**PaginationResponse**](PaginationResponse.md) | Pagination information | 
**total_count** | **int** | Total number of collections matching the query | 
**stats** | [**CollectionListStats**](CollectionListStats.md) | Aggregate statistics across all collections in the result | [optional] 

## Example

```python
from mixpeek.models.list_collections_response import ListCollectionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListCollectionsResponse from a JSON string
list_collections_response_instance = ListCollectionsResponse.from_json(json)
# print the JSON string representation of the object
print(ListCollectionsResponse.to_json())

# convert the object into a dict
list_collections_response_dict = list_collections_response_instance.to_dict()
# create an instance of ListCollectionsResponse from a dict
list_collections_response_from_dict = ListCollectionsResponse.from_dict(list_collections_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


