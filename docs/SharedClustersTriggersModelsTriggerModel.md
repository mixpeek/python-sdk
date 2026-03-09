# SharedClustersTriggersModelsTriggerModel

Model for cluster trigger.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trigger_id** | **str** | Unique trigger ID | [optional] 
**cluster_id** | **str** | Optional link to cluster definition | [optional] 
**namespace_id** | **str** | Namespace ID | 
**internal_id** | **str** | Organization internal ID | 
**execution_config** | [**TriggerExecutionConfig**](TriggerExecutionConfig.md) | Configuration for cluster execution | 
**trigger_type** | [**SharedClustersTriggersModelsTriggerType**](SharedClustersTriggersModelsTriggerType.md) | Type of trigger | 
**schedule_config** | **Dict[str, object]** | Type-specific schedule configuration | 
**status** | [**SharedClustersTriggersModelsTriggerStatus**](SharedClustersTriggersModelsTriggerStatus.md) | Current status | [optional] 
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
from mixpeek.models.shared_clusters_triggers_models_trigger_model import SharedClustersTriggersModelsTriggerModel

# TODO update the JSON string below
json = "{}"
# create an instance of SharedClustersTriggersModelsTriggerModel from a JSON string
shared_clusters_triggers_models_trigger_model_instance = SharedClustersTriggersModelsTriggerModel.from_json(json)
# print the JSON string representation of the object
print(SharedClustersTriggersModelsTriggerModel.to_json())

# convert the object into a dict
shared_clusters_triggers_models_trigger_model_dict = shared_clusters_triggers_models_trigger_model_instance.to_dict()
# create an instance of SharedClustersTriggersModelsTriggerModel from a dict
shared_clusters_triggers_models_trigger_model_from_dict = SharedClustersTriggersModelsTriggerModel.from_dict(shared_clusters_triggers_models_trigger_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


