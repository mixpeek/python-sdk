# SharedClustersTriggersModelsUpdateTriggerRequest

Request to update an existing trigger.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule_config** | **object** | Updated schedule configuration | [optional] 
**description** | **str** | Updated description | [optional] 
**status** | [**SharedClustersTriggersModelsTriggerStatus**](SharedClustersTriggersModelsTriggerStatus.md) | Updated status | [optional] 

## Example

```python
from mixpeek.models.shared_clusters_triggers_models_update_trigger_request import SharedClustersTriggersModelsUpdateTriggerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SharedClustersTriggersModelsUpdateTriggerRequest from a JSON string
shared_clusters_triggers_models_update_trigger_request_instance = SharedClustersTriggersModelsUpdateTriggerRequest.from_json(json)
# print the JSON string representation of the object
print(SharedClustersTriggersModelsUpdateTriggerRequest.to_json())

# convert the object into a dict
shared_clusters_triggers_models_update_trigger_request_dict = shared_clusters_triggers_models_update_trigger_request_instance.to_dict()
# create an instance of SharedClustersTriggersModelsUpdateTriggerRequest from a dict
shared_clusters_triggers_models_update_trigger_request_from_dict = SharedClustersTriggersModelsUpdateTriggerRequest.from_dict(shared_clusters_triggers_models_update_trigger_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


