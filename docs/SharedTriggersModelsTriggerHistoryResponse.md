# SharedTriggersModelsTriggerHistoryResponse

Response for trigger execution history.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trigger_id** | **str** | Trigger ID | 
**executions** | [**List[TriggerExecutionHistory]**](TriggerExecutionHistory.md) | Execution history | 
**total** | **int** | Total executions | 
**offset** | **int** | Current offset | 
**limit** | **int** | Current limit | 

## Example

```python
from mixpeek.models.shared_triggers_models_trigger_history_response import SharedTriggersModelsTriggerHistoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SharedTriggersModelsTriggerHistoryResponse from a JSON string
shared_triggers_models_trigger_history_response_instance = SharedTriggersModelsTriggerHistoryResponse.from_json(json)
# print the JSON string representation of the object
print(SharedTriggersModelsTriggerHistoryResponse.to_json())

# convert the object into a dict
shared_triggers_models_trigger_history_response_dict = shared_triggers_models_trigger_history_response_instance.to_dict()
# create an instance of SharedTriggersModelsTriggerHistoryResponse from a dict
shared_triggers_models_trigger_history_response_from_dict = SharedTriggersModelsTriggerHistoryResponse.from_dict(shared_triggers_models_trigger_history_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


