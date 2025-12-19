# UpdateTriggerRequest

Request to update an existing trigger.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule_config** | **Dict[str, object]** | Updated schedule configuration | [optional] 
**description** | **str** | Updated description | [optional] 
**status** | [**TriggerStatus**](TriggerStatus.md) | Updated status | [optional] 

## Example

```python
from mixpeek.models.update_trigger_request import UpdateTriggerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTriggerRequest from a JSON string
update_trigger_request_instance = UpdateTriggerRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateTriggerRequest.to_json())

# convert the object into a dict
update_trigger_request_dict = update_trigger_request_instance.to_dict()
# create an instance of UpdateTriggerRequest from a dict
update_trigger_request_from_dict = UpdateTriggerRequest.from_dict(update_trigger_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


