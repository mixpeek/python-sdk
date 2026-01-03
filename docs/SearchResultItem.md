# SearchResultItem

Individual search result representing a matched resource.  Contains essential metadata about the matched resource including type, ID, name, description, and timestamps. Results are sorted by relevance (exact matches first) and creation time.  Use Cases:     - Display search results in UI     - Navigate to specific resources by ID     - Show resource metadata in search results     - Filter or sort results client-side  Fields:     - resource_type: Type of resource (bucket, collection, etc.)     - resource_id: Unique identifier for the resource     - resource_name: Human-readable name     - description: Optional description text     - created_at: When the resource was created     - updated_at: When the resource was last updated (if applicable)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | **str** | Type of resource this result represents. REQUIRED. One of: &#39;bucket&#39;, &#39;collection&#39;, &#39;retriever&#39;, &#39;taxonomy&#39;, &#39;cluster&#39;, &#39;published_retriever&#39;, &#39;namespace&#39;. Used to identify which resource type was matched and how to navigate to it. Example: &#39;bucket&#39; indicates this is a bucket resource. | 
**resource_id** | **str** | Unique identifier for the resource. REQUIRED. Format depends on resource_type: - bucket: &#39;bkt_XXXXXXXX&#39; - collection: &#39;col_XXXXXXXXXX&#39; - retriever: &#39;ret_XXXXXXXXXXXXXX&#39; - taxonomy: &#39;tax_XXXXXXXXXXXX&#39; - cluster: &#39;clust_XXXXXXXXXX&#39; - published_retriever: &#39;pk_XXXXXXXXXX&#39; - namespace: &#39;ns_XXXXXXXXXX&#39;. Use this ID to fetch the full resource or perform operations on it. | 
**resource_name** | **str** | Human-readable name of the resource. REQUIRED. This is the field that was matched in the search. Corresponds to: bucket_name, collection_name, retriever_name, taxonomy_name, cluster_name, or public_name. Example: &#39;Production Videos&#39;, &#39;Product Embeddings&#39;, &#39;Recommendation Engine&#39;, &#39;my-public-search&#39;. | 
**description** | **str** | Description of the resource if provided. OPTIONAL - May be null if no description was set. Provides additional context about the resource&#39;s purpose or contents. | [optional] 
**created_at** | **datetime** | Timestamp when the resource was created. REQUIRED. ISO 8601 format with UTC timezone. Used for sorting results by creation time. | 
**updated_at** | **datetime** | Timestamp when the resource was last updated. OPTIONAL - May be null if resource has never been updated. ISO 8601 format with UTC timezone. | [optional] 

## Example

```python
from mixpeek.models.search_result_item import SearchResultItem

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResultItem from a JSON string
search_result_item_instance = SearchResultItem.from_json(json)
# print the JSON string representation of the object
print(SearchResultItem.to_json())

# convert the object into a dict
search_result_item_dict = search_result_item_instance.to_dict()
# create an instance of SearchResultItem from a dict
search_result_item_from_dict = SearchResultItem.from_dict(search_result_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


