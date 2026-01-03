# SearchRequest

Request model for searching across resource names and IDs.  Search is performed across all resource types within the authenticated namespace. The search is case-insensitive and supports partial matching on both names and IDs.  Use Cases:     - Find resources by partial name match     - Locate resources by ID prefix     - Filter search to specific resource types     - Paginate through large result sets  Requirements:     - query: REQUIRED - Search term (minimum 1 character)     - resource_types: OPTIONAL - Filter by specific types     - limit: OPTIONAL - Results per page (1-100, default 20)     - offset: OPTIONAL - Pagination offset (default 0)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | Search term to match against resource names and IDs. REQUIRED. Minimum 1 character. Case-insensitive partial matching is performed. Matches against: bucket_name, bucket_id, collection_name, collection_id, retriever_name, retriever_id, taxonomy_name, taxonomy_id, cluster_name, cluster_id, namespace_name, namespace_id. Example: &#39;prod&#39; matches &#39;production-videos&#39;, &#39;bkt_prod123&#39;, &#39;Products Collection&#39;. | 
**resource_types** | **List[str]** | Filter search to specific resource types. OPTIONAL - If not provided, searches all resource types. Valid values: &#39;bucket&#39;, &#39;collection&#39;, &#39;retriever&#39;, &#39;taxonomy&#39;, &#39;cluster&#39;, &#39;published_retriever&#39;, &#39;namespace&#39;. Example: [&#39;bucket&#39;, &#39;collection&#39;] searches only buckets and collections. | [optional] 
**limit** | **int** | Maximum number of results to return. OPTIONAL - Defaults to 20. Minimum: 1, Maximum: 100. Use with offset for pagination. | [optional] [default to 20]
**offset** | **int** | Number of results to skip for pagination. OPTIONAL - Defaults to 0. Minimum: 0. Use with limit for pagination. Example: offset&#x3D;20 with limit&#x3D;20 returns results 21-40. | [optional] [default to 0]

## Example

```python
from mixpeek.models.search_request import SearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SearchRequest from a JSON string
search_request_instance = SearchRequest.from_json(json)
# print the JSON string representation of the object
print(SearchRequest.to_json())

# convert the object into a dict
search_request_dict = search_request_instance.to_dict()
# create an instance of SearchRequest from a dict
search_request_from_dict = SearchRequest.from_dict(search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


