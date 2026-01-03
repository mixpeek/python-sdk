# ListAdhocExecutionsResponse

Response from listing ad-hoc retriever executions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[AdhocExecutionSummary]**](AdhocExecutionSummary.md) | List of ad-hoc execution summaries. | [optional] 
**total** | **int** | Total number of ad-hoc executions matching filters. | [optional] [default to 0]
**pagination** | **object** |  | 

## Example

```python
from mixpeek.models.list_adhoc_executions_response import ListAdhocExecutionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListAdhocExecutionsResponse from a JSON string
list_adhoc_executions_response_instance = ListAdhocExecutionsResponse.from_json(json)
# print the JSON string representation of the object
print(ListAdhocExecutionsResponse.to_json())

# convert the object into a dict
list_adhoc_executions_response_dict = list_adhoc_executions_response_instance.to_dict()
# create an instance of ListAdhocExecutionsResponse from a dict
list_adhoc_executions_response_from_dict = ListAdhocExecutionsResponse.from_dict(list_adhoc_executions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


