# SharedTriggersModelsTriggerModel

Unified trigger model for all action types.  A trigger defines: 1. **What** to execute (action_type + action_config) 2. **When** to execute (trigger_type + schedule_config) 3. **State** tracking (execution count, failures, next scheduled time)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trigger_id** | **str** | Unique trigger identifier | [optional] 
**namespace_id** | **str** | Namespace ID | 
**internal_id** | **str** | Organization internal ID | 
**action_type** | [**TriggerActionType**](TriggerActionType.md) | Type of action to execute | 
**action_config** | **Dict[str, object]** | Action-specific configuration | 
**trigger_type** | [**SharedTriggersModelsTriggerType**](SharedTriggersModelsTriggerType.md) | Type of schedule | 
**schedule_config** | **Dict[str, object]** | Schedule-specific configuration | 
**status** | [**SharedTriggersModelsTriggerStatus**](SharedTriggersModelsTriggerStatus.md) | Current trigger status | [optional] 
**last_triggered_at** | **datetime** | Last time trigger fired | [optional] 
**last_execution_task_id** | **str** | Task ID of last execution | [optional] 
**next_scheduled_at** | **datetime** | Next scheduled execution time | [optional] 
**execution_count** | **int** | Total successful executions | [optional] [default to 0]
**consecutive_failures** | **int** | Consecutive failures | [optional] [default to 0]
**last_execution_status** | **str** | Status of last execution | [optional] 
**last_execution_error** | **str** | Error from last execution (if failed) | [optional] 
**event_counter** | **int** | Current event count since last trigger | [optional] [default to 0]
**last_cooldown_at** | **datetime** | Last time cooldown was applied | [optional] 
**baseline_snapshot** | **Dict[str, object]** | Baseline snapshot for drift measurement (captured after successful execution) | [optional] 
**last_drift_measurement** | **Dict[str, object]** | Result of most recent drift measurement check | [optional] 
**last_condition_check_at** | **datetime** | When condition was last evaluated | [optional] 
**description** | **str** | Human-readable description | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 
**created_by** | **str** | User who created trigger | [optional] 

## Example

```python
from mixpeek.models.shared_triggers_models_trigger_model import SharedTriggersModelsTriggerModel

# TODO update the JSON string below
json = "{}"
# create an instance of SharedTriggersModelsTriggerModel from a JSON string
shared_triggers_models_trigger_model_instance = SharedTriggersModelsTriggerModel.from_json(json)
# print the JSON string representation of the object
print(SharedTriggersModelsTriggerModel.to_json())

# convert the object into a dict
shared_triggers_models_trigger_model_dict = shared_triggers_models_trigger_model_instance.to_dict()
# create an instance of SharedTriggersModelsTriggerModel from a dict
shared_triggers_models_trigger_model_from_dict = SharedTriggersModelsTriggerModel.from_dict(shared_triggers_models_trigger_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


