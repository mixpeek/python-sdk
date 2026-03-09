# ListPagesResponse

Paginated list of pages.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[PageResponse]**](PageResponse.md) |  | 
**total_count** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 

## Example

```python
from mixpeek.models.list_pages_response import ListPagesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListPagesResponse from a JSON string
list_pages_response_instance = ListPagesResponse.from_json(json)
# print the JSON string representation of the object
print(ListPagesResponse.to_json())

# convert the object into a dict
list_pages_response_dict = list_pages_response_instance.to_dict()
# create an instance of ListPagesResponse from a dict
list_pages_response_from_dict = ListPagesResponse.from_dict(list_pages_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


