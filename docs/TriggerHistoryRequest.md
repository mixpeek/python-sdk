# TriggerHistoryRequest

Request for trigger execution history.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** | Pagination offset | [optional] [default to 0]
**limit** | **int** | Results per page | [optional] [default to 50]
**status_filter** | **str** | Filter by execution status | [optional] 

## Example

```python
from mixpeek.models.trigger_history_request import TriggerHistoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerHistoryRequest from a JSON string
trigger_history_request_instance = TriggerHistoryRequest.from_json(json)
# print the JSON string representation of the object
print(TriggerHistoryRequest.to_json())

# convert the object into a dict
trigger_history_request_dict = trigger_history_request_instance.to_dict()
# create an instance of TriggerHistoryRequest from a dict
trigger_history_request_from_dict = TriggerHistoryRequest.from_dict(trigger_history_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


