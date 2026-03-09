# Pagination

Pagination strategy configuration. Defaults to cursor-based pagination with limit=20.   IMPORTANT: Pagination params do NOT support template variables ({{INPUT.x}} or {{DOCUMENT.x}}). Pagination is a request-level parameter for slicing results, separate from pipeline business logic. Pass cursor/limit values directly from your client code. Cursor values come from the previous response's pagination.cursor field.  Supported Methods: - CURSOR (default): Best for infinite scroll, stateless, opaque token - KEYSET: Most efficient, requires stable sort, stateless - OFFSET: Traditional page numbers, can have drift issues - SCROLL: Server-side state, best for bulk exports   Use CURSOR for: - Infinite scroll UIs (mobile apps, feeds, timelines) - Real-time updates where consistency matters - When you can't jump to arbitrary pages   Use KEYSET for: - Maximum performance with large result sets - Stable sort fields (e.g., score DESC, id ASC) - When you need truly stateless pagination   Use OFFSET for: - Traditional page UIs with page numbers - When users need to jump to specific pages - Smaller result sets where drift is acceptable   Use SCROLL for: - Bulk exports or processing large datasets - When you need to iterate through all results - Background jobs with progress tracking   Example (cursor - first page): {\"method\": \"cursor\", \"limit\": 20, \"cursor\": null}  Example (cursor - next page, using cursor from previous response): {\"method\": \"cursor\", \"limit\": 20, \"cursor\": \"eyJvZmZzZXQiOjIwfQ==\"}  Example (offset): {\"method\": \"offset\", \"page_size\": 25, \"page_number\": 2}  Example (keyset): {\"method\": \"keyset\", \"limit\": 20, \"after\": {\"score\": 0.73, \"id\": \"doc_20\"}} 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | [**PaginationMethod**](PaginationMethod.md) | Constant identifying keyset pagination (REQUIRED). | [optional] 
**page_size** | **int** | Number of documents per page (REQUIRED). Default: 10. | [optional] [default to 10]
**page_number** | **int** | 1-based page index to retrieve (REQUIRED). Default: 1. | [optional] [default to 1]
**limit** | **int** | Maximum number of documents to return per page (REQUIRED). Default: 10. | [optional] [default to 10]
**cursor** | **str** | Opaque base64 cursor from previous response (OPTIONAL). null for first page, then use cursor from response.pagination.cursor | [optional] 
**scroll_id** | **str** | Server-issued scroll session identifier (OPTIONAL). null for first request, then use scroll_id from response | [optional] 
**scroll_ttl** | **int** | Seconds to keep scroll context alive (REQUIRED). Default: 300 (5 minutes). | [optional] [default to 300]
**after** | **Dict[str, object]** | Last seen keyset marker from previous response (OPTIONAL). Must include all sort fields. Example: {&#39;score&#39;: 0.73, &#39;id&#39;: &#39;doc_20&#39;}. null for first page, then use next_cursor from response | [optional] 

## Example

```python
from mixpeek.models.pagination import Pagination

# TODO update the JSON string below
json = "{}"
# create an instance of Pagination from a JSON string
pagination_instance = Pagination.from_json(json)
# print the JSON string representation of the object
print(Pagination.to_json())

# convert the object into a dict
pagination_dict = pagination_instance.to_dict()
# create an instance of Pagination from a dict
pagination_from_dict = Pagination.from_dict(pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


