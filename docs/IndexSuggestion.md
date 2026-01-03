# IndexSuggestion

Suggestion for creating a payload index.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** | Field name to index | 
**query_count_24h** | **int** | Number of queries using this field in last 24 hours | 
**query_count_7d** | **int** | Number of queries in last 7 days | [optional] 
**suggested_type** | **str** | Suggested index type (keyword, integer, float, etc.) | 
**is_indexed** | **bool** | Whether field is already indexed | 
**first_seen** | **datetime** | First time field was seen in filters | 
**last_seen** | **datetime** | Most recent usage | 
**estimated_performance_gain** | **str** | Estimated query performance improvement (e.g., &#39;60-80%&#39;) | [optional] 

## Example

```python
from mixpeek.models.index_suggestion import IndexSuggestion

# TODO update the JSON string below
json = "{}"
# create an instance of IndexSuggestion from a JSON string
index_suggestion_instance = IndexSuggestion.from_json(json)
# print the JSON string representation of the object
print(IndexSuggestion.to_json())

# convert the object into a dict
index_suggestion_dict = index_suggestion_instance.to_dict()
# create an instance of IndexSuggestion from a dict
index_suggestion_from_dict = IndexSuggestion.from_dict(index_suggestion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


