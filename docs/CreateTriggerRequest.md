# CreateTriggerRequest

Request to create a new trigger.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** | Optional existing cluster ID | [optional] 
**execution_config** | [**TriggerExecutionConfig**](TriggerExecutionConfig.md) | Required if cluster_id not provided | [optional] 
**trigger_type** | [**TriggerType**](TriggerType.md) | Type of trigger | 
**schedule_config** | **Dict[str, object]** | Schedule configuration | 
**description** | **str** | Trigger description | [optional] 
**status** | [**TriggerStatus**](TriggerStatus.md) | Initial status | [optional] 

## Example

```python
from mixpeek.models.create_trigger_request import CreateTriggerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTriggerRequest from a JSON string
create_trigger_request_instance = CreateTriggerRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTriggerRequest.to_json())

# convert the object into a dict
create_trigger_request_dict = create_trigger_request_instance.to_dict()
# create an instance of CreateTriggerRequest from a dict
create_trigger_request_from_dict = CreateTriggerRequest.from_dict(create_trigger_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


