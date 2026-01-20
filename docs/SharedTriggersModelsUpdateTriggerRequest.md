# SharedTriggersModelsUpdateTriggerRequest

Request to update an existing trigger.  Only provided fields will be updated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule_config** | **object** | Updated schedule configuration | [optional] 
**description** | **str** | Updated description | [optional] 
**status** | [**SharedTriggersModelsTriggerStatus**](SharedTriggersModelsTriggerStatus.md) | Updated status | [optional] 

## Example

```python
from mixpeek.models.shared_triggers_models_update_trigger_request import SharedTriggersModelsUpdateTriggerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SharedTriggersModelsUpdateTriggerRequest from a JSON string
shared_triggers_models_update_trigger_request_instance = SharedTriggersModelsUpdateTriggerRequest.from_json(json)
# print the JSON string representation of the object
print(SharedTriggersModelsUpdateTriggerRequest.to_json())

# convert the object into a dict
shared_triggers_models_update_trigger_request_dict = shared_triggers_models_update_trigger_request_instance.to_dict()
# create an instance of SharedTriggersModelsUpdateTriggerRequest from a dict
shared_triggers_models_update_trigger_request_from_dict = SharedTriggersModelsUpdateTriggerRequest.from_dict(shared_triggers_models_update_trigger_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


