# SharedTriggersModelsListTriggersRequest

Request to list triggers with filters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_type** | [**TriggerActionType**](TriggerActionType.md) | Filter by action type | [optional] 
**trigger_type** | [**SharedTriggersModelsTriggerType**](SharedTriggersModelsTriggerType.md) | Filter by trigger type | [optional] 
**status** | [**SharedTriggersModelsTriggerStatus**](SharedTriggersModelsTriggerStatus.md) | Filter by status | [optional] 
**resource_id** | **str** | Filter by resource ID (cluster_id or taxonomy_id) | [optional] 
**offset** | **int** | Pagination offset | [optional] [default to 0]
**limit** | **int** | Results per page | [optional] [default to 50]
**sort_by** | **str** | Field to sort by | [optional] [default to 'created_at']
**direction** | **str** | Sort direction (asc/desc) | [optional] [default to 'desc']

## Example

```python
from mixpeek.models.shared_triggers_models_list_triggers_request import SharedTriggersModelsListTriggersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SharedTriggersModelsListTriggersRequest from a JSON string
shared_triggers_models_list_triggers_request_instance = SharedTriggersModelsListTriggersRequest.from_json(json)
# print the JSON string representation of the object
print(SharedTriggersModelsListTriggersRequest.to_json())

# convert the object into a dict
shared_triggers_models_list_triggers_request_dict = shared_triggers_models_list_triggers_request_instance.to_dict()
# create an instance of SharedTriggersModelsListTriggersRequest from a dict
shared_triggers_models_list_triggers_request_from_dict = SharedTriggersModelsListTriggersRequest.from_dict(shared_triggers_models_list_triggers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


