# TriggerHistoryResponse

Response for trigger execution history.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trigger_id** | **str** | Trigger ID | 
**executions** | [**List[TriggerExecutionHistoryItem]**](TriggerExecutionHistoryItem.md) | Execution history | 
**total** | **int** | Total executions | 
**offset** | **int** | Current offset | 
**limit** | **int** | Current limit | 

## Example

```python
from mixpeek.models.trigger_history_response import TriggerHistoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerHistoryResponse from a JSON string
trigger_history_response_instance = TriggerHistoryResponse.from_json(json)
# print the JSON string representation of the object
print(TriggerHistoryResponse.to_json())

# convert the object into a dict
trigger_history_response_dict = trigger_history_response_instance.to_dict()
# create an instance of TriggerHistoryResponse from a dict
trigger_history_response_from_dict = TriggerHistoryResponse.from_dict(trigger_history_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


