# ListDocumentsResponse

Response model for listing documents.  Supports both regular document lists and grouped results based on the group_by parameter. When group_by is specified, results are returned as groups instead of a flat list.  Pagination strategies: - **Offset-based (default)**: Use `pagination.page` and `pagination.page_size` - **Cursor-based (optional)**: Use `pagination.next_cursor` for efficient deep pagination

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[DocumentResponse]**](DocumentResponse.md) | List of documents when group_by is NOT specified. Contains flat list of documents with pagination applied. Mutually exclusive with &#39;groups&#39; field. | [optional] 
**groups** | [**List[DocumentGroup]**](DocumentGroup.md) | List of document groups when group_by IS specified. Each group contains documents sharing the same field value. Pagination applies to groups, not individual documents. Mutually exclusive with &#39;results&#39; field. | [optional] 
**pagination** | [**PaginationResponse**](PaginationResponse.md) | Pagination information. Includes next_cursor for cursor-based pagination. When group_by is used, pagination applies to groups (not individual documents). total_count reflects total number of groups, not total documents. | 
**stats** | [**DocumentListStats**](DocumentListStats.md) | Aggregate statistics across all documents in the result | [optional] 
**group_by_field** | **str** | The field that was used for grouping when group_by was specified. None for non-grouped results. Useful for clients to understand the grouping structure. | [optional] 

## Example

```python
from mixpeek.models.list_documents_response import ListDocumentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListDocumentsResponse from a JSON string
list_documents_response_instance = ListDocumentsResponse.from_json(json)
# print the JSON string representation of the object
print(ListDocumentsResponse.to_json())

# convert the object into a dict
list_documents_response_dict = list_documents_response_instance.to_dict()
# create an instance of ListDocumentsResponse from a dict
list_documents_response_from_dict = ListDocumentsResponse.from_dict(list_documents_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


