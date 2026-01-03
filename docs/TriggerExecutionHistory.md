# TriggerExecutionHistory

Single execution history item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** | Task ID | 
**triggered_at** | **datetime** | When trigger fired | 
**status** | **str** | Execution status | 
**execution_time_ms** | **int** | Execution time in milliseconds | [optional] 
**error** | **str** | Error message if failed | [optional] 

## Example

```python
from mixpeek.models.trigger_execution_history import TriggerExecutionHistory

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerExecutionHistory from a JSON string
trigger_execution_history_instance = TriggerExecutionHistory.from_json(json)
# print the JSON string representation of the object
print(TriggerExecutionHistory.to_json())

# convert the object into a dict
trigger_execution_history_dict = trigger_execution_history_instance.to_dict()
# create an instance of TriggerExecutionHistory from a dict
trigger_execution_history_from_dict = TriggerExecutionHistory.from_dict(trigger_execution_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


