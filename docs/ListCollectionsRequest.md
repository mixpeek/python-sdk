# ListCollectionsRequest

Request model for listing collections.  To filter by taxonomy, use dot notation in filters: filters.AND = [{\"field\": \"taxonomy_applications.taxonomy_id\", \"operator\": \"eq\", \"value\": \"tax_123\"}]

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | **object** | Filters to apply when listing collections. Supports nested field filtering like &#39;taxonomy_applications.taxonomy_id&#39;. Format: {\&quot;AND\&quot;: [{\&quot;field\&quot;: \&quot;field_name\&quot;, \&quot;operator\&quot;: \&quot;eq\&quot;, \&quot;value\&quot;: \&quot;value\&quot;}]} | [optional] 
**sort** | [**SortOption**](SortOption.md) | Sort options for the results | [optional] 
**search** | **str** | Search term for wildcard search across collection_id, collection_name, description, and other text fields | [optional] 
**case_sensitive** | **bool** | If True, filters and search will be case-sensitive | [optional] [default to False]

## Example

```python
from mixpeek.models.list_collections_request import ListCollectionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListCollectionsRequest from a JSON string
list_collections_request_instance = ListCollectionsRequest.from_json(json)
# print the JSON string representation of the object
print(ListCollectionsRequest.to_json())

# convert the object into a dict
list_collections_request_dict = list_collections_request_instance.to_dict()
# create an instance of ListCollectionsRequest from a dict
list_collections_request_from_dict = ListCollectionsRequest.from_dict(list_collections_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


