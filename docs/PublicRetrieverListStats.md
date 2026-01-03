# PublicRetrieverListStats

Aggregate statistics for public retrievers list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_active** | **int** | Number of active public retrievers | [optional] [default to 0]
**total_password_protected** | **int** | Number of password-protected retrievers | [optional] [default to 0]
**total_open** | **int** | Number of fully open (no password) retrievers | [optional] [default to 0]

## Example

```python
from mixpeek.models.public_retriever_list_stats import PublicRetrieverListStats

# TODO update the JSON string below
json = "{}"
# create an instance of PublicRetrieverListStats from a JSON string
public_retriever_list_stats_instance = PublicRetrieverListStats.from_json(json)
# print the JSON string representation of the object
print(PublicRetrieverListStats.to_json())

# convert the object into a dict
public_retriever_list_stats_dict = public_retriever_list_stats_instance.to_dict()
# create an instance of PublicRetrieverListStats from a dict
public_retriever_list_stats_from_dict = PublicRetrieverListStats.from_dict(public_retriever_list_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


