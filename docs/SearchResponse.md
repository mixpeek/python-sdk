# SearchResponse

Response model for resource search results.  Contains paginated search results with metadata about total matches and pagination state. Results are sorted by relevance (exact matches first, then partial matches) and creation time (newest first).  Use Cases:     - Display search results to users     - Implement pagination UI     - Show total result counts     - Navigate through large result sets  Fields:     - results: List of matched resources     - total: Total number of matches (before pagination)     - limit: Results per page (from request)     - offset: Current pagination offset (from request)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[SearchResultItem]**](SearchResultItem.md) | List of matched resources. REQUIRED. May be empty if no matches found. Sorted by: 1) Exact matches first, 2) Partial matches, 3) Created timestamp descending. Length is min(total - offset, limit). Each result contains full resource metadata for display. | 
**total** | **int** | Total number of matches across all pages. REQUIRED. Count before pagination is applied. Use to calculate total pages: ceil(total / limit). May be 0 if no matches found. Example: total&#x3D;50 with limit&#x3D;20 means 3 pages of results. | 
**limit** | **int** | Results per page (from request). REQUIRED. Echo of the limit parameter from the request. Range: 1-100. | 
**offset** | **int** | Current pagination offset (from request). REQUIRED. Echo of the offset parameter from the request. Number of results skipped. Example: offset&#x3D;20 means results start from the 21st match. | 

## Example

```python
from mixpeek.models.search_response import SearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResponse from a JSON string
search_response_instance = SearchResponse.from_json(json)
# print the JSON string representation of the object
print(SearchResponse.to_json())

# convert the object into a dict
search_response_dict = search_response_instance.to_dict()
# create an instance of SearchResponse from a dict
search_response_from_dict = SearchResponse.from_dict(search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


