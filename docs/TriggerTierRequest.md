# TriggerTierRequest

Request to trigger next tier processing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal_id** | **str** |  | 
**namespace_id** | **str** |  | 
**ray_job_id** | **str** |  | 
**completed_tier** | **int** |  | 
**start_time_ms** | **int** |  | [optional] 
**end_time_ms** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from mixpeek.models.trigger_tier_request import TriggerTierRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerTierRequest from a JSON string
trigger_tier_request_instance = TriggerTierRequest.from_json(json)
# print the JSON string representation of the object
print(TriggerTierRequest.to_json())

# convert the object into a dict
trigger_tier_request_dict = trigger_tier_request_instance.to_dict()
# create an instance of TriggerTierRequest from a dict
trigger_tier_request_from_dict = TriggerTierRequest.from_dict(trigger_tier_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


