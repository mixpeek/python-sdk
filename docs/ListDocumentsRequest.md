# ListDocumentsRequest

Request model for listing documents.  Supports two pagination strategies:  **Offset-based (default)**: Use query params `?page=2&page_size=10` - Simple and familiar - Works well for shallow pagination (first ~100 pages) - Less efficient for deep pagination with sorting  **Cursor-based (optional)**: Pass `cursor` from previous response's `next_cursor` - More efficient for deep pagination (page 100+) - Required for consistent results when sorting large datasets - When cursor is provided, offset is ignored

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**LogicalOperatorInput**](LogicalOperatorInput.md) | Filters to apply. | [optional] 
**sort** | [**SortOption**](SortOption.md) | Sort options. | [optional] 
**search** | **str** | Search term. | [optional] 
**cursor** | **str** | OPTIONAL cursor for efficient deep pagination. Pass the &#39;pagination.next_cursor&#39; value from a previous response to fetch the next page. When cursor is provided, the page/offset query params are ignored. Use cursor-based pagination when: (1) paginating beyond page ~100, (2) sorting large datasets, or (3) you need consistent iteration. Use offset-based pagination (default) for: simple use cases, random page access, or when page numbers are needed in the UI. | [optional] 
**return_url** | **bool** | Whether to return presigned URLs for object keys. | [optional] [default to False]
**return_vectors** | **bool** | Whether to return vector embeddings in the document results. | [optional] [default to False]
**group_by** | **str** | OPTIONAL. Field to group documents by. Supports dot notation for nested fields (e.g., &#39;metadata.category&#39;, &#39;source_type&#39;). When specified, documents are grouped by the field value and returned as grouped results. Requires a payload index on the field in Qdrant for optimal performance. If no index exists, the operation will fail with a validation error. Common groupable fields: &#39;source_object_id&#39;, &#39;root_object_id&#39;, &#39;collection_id&#39;, &#39;metadata.category&#39;. | [optional] 
**select** | **List[str]** | OPTIONAL. List of fields to include in the response. Supports dot notation for nested fields (e.g., &#39;metadata.title&#39;, &#39;content&#39;). When specified, only the selected fields will be returned in the document results, reducing response size. System fields like &#39;_id&#39; and &#39;document_id&#39; are always included. Use this to optimize response size when working with large documents. | [optional] 

## Example

```python
from mixpeek.models.list_documents_request import ListDocumentsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListDocumentsRequest from a JSON string
list_documents_request_instance = ListDocumentsRequest.from_json(json)
# print the JSON string representation of the object
print(ListDocumentsRequest.to_json())

# convert the object into a dict
list_documents_request_dict = list_documents_request_instance.to_dict()
# create an instance of ListDocumentsRequest from a dict
list_documents_request_from_dict = ListDocumentsRequest.from_dict(list_documents_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


