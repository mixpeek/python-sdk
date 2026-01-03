# PaginationResponse

PaginationResponse.  Cursor-based pagination response: - Use next_cursor for navigation - Total count fields only populated when include_total=true

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**page** | **int** |  | [optional] 
**page_size** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**next_cursor** | **str** |  | [optional] 

## Example

```python
from mixpeek.models.pagination_response import PaginationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationResponse from a JSON string
pagination_response_instance = PaginationResponse.from_json(json)
# print the JSON string representation of the object
print(PaginationResponse.to_json())

# convert the object into a dict
pagination_response_dict = pagination_response_instance.to_dict()
# create an instance of PaginationResponse from a dict
pagination_response_from_dict = PaginationResponse.from_dict(pagination_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


