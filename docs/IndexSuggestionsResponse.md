# IndexSuggestionsResponse

Response containing index suggestions for a namespace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespace_id** | **str** | Namespace being analyzed | 
**analysis_period** | **str** | Time period analyzed (e.g., &#39;24h&#39;, &#39;7d&#39;) | 
**suggestions** | [**List[IndexSuggestion]**](IndexSuggestion.md) | List of index suggestions | 
**auto_create_enabled** | **bool** | Whether auto-indexing is enabled for this namespace | 
**next_auto_create_run** | **datetime** | Next scheduled auto-creation run (if enabled) | [optional] 

## Example

```python
from mixpeek.models.index_suggestions_response import IndexSuggestionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IndexSuggestionsResponse from a JSON string
index_suggestions_response_instance = IndexSuggestionsResponse.from_json(json)
# print the JSON string representation of the object
print(IndexSuggestionsResponse.to_json())

# convert the object into a dict
index_suggestions_response_dict = index_suggestions_response_instance.to_dict()
# create an instance of IndexSuggestionsResponse from a dict
index_suggestions_response_from_dict = IndexSuggestionsResponse.from_dict(index_suggestions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


