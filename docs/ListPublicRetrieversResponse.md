# ListPublicRetrieversResponse

Response for listing public retrievers.  Follows the same pattern as ListCollectionsResponse for consistent developer experience.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[PublicRetrieverListItem]**](PublicRetrieverListItem.md) | List of public retrievers | 
**total_count** | **int** | Total number of public retrievers matching the query | 
**page** | **int** | Current page number | 
**page_size** | **int** | Results per page | 
**total_pages** | **int** | Total number of pages | 
**stats** | [**PublicRetrieverListStats**](PublicRetrieverListStats.md) | Aggregate statistics across all public retrievers | [optional] 

## Example

```python
from mixpeek.models.list_public_retrievers_response import ListPublicRetrieversResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListPublicRetrieversResponse from a JSON string
list_public_retrievers_response_instance = ListPublicRetrieversResponse.from_json(json)
# print the JSON string representation of the object
print(ListPublicRetrieversResponse.to_json())

# convert the object into a dict
list_public_retrievers_response_dict = list_public_retrievers_response_instance.to_dict()
# create an instance of ListPublicRetrieversResponse from a dict
list_public_retrievers_response_from_dict = ListPublicRetrieversResponse.from_dict(list_public_retrievers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


