# StorageConnectionListResponse

Response envelope for listing storage connections.  Contains paginated results and metadata about the listing operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[StorageConnectionModel]**](StorageConnectionModel.md) | List of storage connections matching the request filters. Results are paginated according to the pagination parameters. SECURITY: Sensitive credential fields are automatically redacted. | 
**pagination** | [**PaginationResponse**](PaginationResponse.md) | Pagination metadata including total count, page number, page size, and navigation links for next/previous pages. | 
**total** | **int** | Total number of connections matching the filters (before pagination). Use this to calculate total pages and display pagination controls. | 

## Example

```python
from mixpeek.models.storage_connection_list_response import StorageConnectionListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StorageConnectionListResponse from a JSON string
storage_connection_list_response_instance = StorageConnectionListResponse.from_json(json)
# print the JSON string representation of the object
print(StorageConnectionListResponse.to_json())

# convert the object into a dict
storage_connection_list_response_dict = storage_connection_list_response_instance.to_dict()
# create an instance of StorageConnectionListResponse from a dict
storage_connection_list_response_from_dict = StorageConnectionListResponse.from_dict(storage_connection_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


