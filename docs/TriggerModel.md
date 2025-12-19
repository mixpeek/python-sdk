# TriggerModel

Model for cluster trigger.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trigger_id** | **str** | Unique trigger ID | [optional] 
**cluster_id** | **str** | Optional link to cluster definition | [optional] 
**namespace_id** | **str** | Namespace ID | 
**internal_id** | **str** | Organization internal ID | 
**execution_config** | [**TriggerExecutionConfig**](TriggerExecutionConfig.md) | Configuration for cluster execution | 
**trigger_type** | [**TriggerType**](TriggerType.md) | Type of trigger | 
**schedule_config** | **Dict[str, object]** | Type-specific schedule configuration | 
**status** | [**TriggerStatus**](TriggerStatus.md) | Current status | [optional] 
**last_triggered_at** | **datetime** | Last time trigger fired | [optional] 
**last_execution_job_id** | **str** | Job ID of last execution | [optional] 
**next_scheduled_at** | **datetime** | Next scheduled execution time | [optional] 
**execution_count** | **int** | Total executions | [optional] [default to 0]
**consecutive_failures** | **int** | Consecutive execution failures | [optional] [default to 0]
**last_execution_status** | **str** | Status of last execution | [optional] 
**last_execution_error** | **str** | Error from last execution | [optional] 
**event_counter** | **int** | Current event count since last trigger | [optional] [default to 0]
**last_cooldown_at** | **datetime** | Last time cooldown was applied | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 
**created_by** | **str** | User who created trigger | [optional] 
**description** | **str** | Trigger description | [optional] 

## Example

```python
from mixpeek.models.trigger_model import TriggerModel

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerModel from a JSON string
trigger_model_instance = TriggerModel.from_json(json)
# print the JSON string representation of the object
print(TriggerModel.to_json())

# convert the object into a dict
trigger_model_dict = trigger_model_instance.to_dict()
# create an instance of TriggerModel from a dict
trigger_model_from_dict = TriggerModel.from_dict(trigger_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


