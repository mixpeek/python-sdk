# CursorPaginationParams

Cursor-based pagination referencing last seen position.  Best for: Infinite scroll UIs, mobile apps, real-time feeds  How it works: - First request: cursor=null - Response includes next cursor token - Next request: pass cursor from previous response - Stateless: no server-side state - Consistent: no duplicates/gaps even with concurrent writes  Use when: - Building infinite scroll interfaces - Users scroll through results sequentially - You need consistency across pages - You don't need to jump to arbitrary pages  Example flow: 1. Request: {\"method\": \"cursor\", \"limit\": 20, \"cursor\": null} 2. Response: {\"documents\": [...], \"pagination\": {\"cursor\": \"abc123\", \"has_next\": true}} 3. Request: {\"method\": \"cursor\", \"limit\": 20, \"cursor\": \"abc123\"}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | [**PaginationMethod**](PaginationMethod.md) | Constant identifying cursor pagination (REQUIRED). | [optional] 
**limit** | **int** | Maximum number of documents to return per page (REQUIRED). Default: 10. | [optional] [default to 10]
**cursor** | **str** | Opaque base64 cursor from previous response (OPTIONAL). null for first page, then use cursor from response.pagination.cursor | [optional] 

## Example

```python
from mixpeek.models.cursor_pagination_params import CursorPaginationParams

# TODO update the JSON string below
json = "{}"
# create an instance of CursorPaginationParams from a JSON string
cursor_pagination_params_instance = CursorPaginationParams.from_json(json)
# print the JSON string representation of the object
print(CursorPaginationParams.to_json())

# convert the object into a dict
cursor_pagination_params_dict = cursor_pagination_params_instance.to_dict()
# create an instance of CursorPaginationParams from a dict
cursor_pagination_params_from_dict = CursorPaginationParams.from_dict(cursor_pagination_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


