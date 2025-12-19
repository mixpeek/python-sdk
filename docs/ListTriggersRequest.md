# ListTriggersRequest

Request to list triggers with filters and pagination.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** | Filter by cluster ID | [optional] 
**trigger_type** | [**TriggerType**](TriggerType.md) | Filter by trigger type | [optional] 
**status** | [**TriggerStatus**](TriggerStatus.md) | Filter by status | [optional] 
**offset** | **int** | Pagination offset | [optional] [default to 0]
**limit** | **int** | Results per page | [optional] [default to 50]
**sort_by** | **str** | Field to sort by | [optional] [default to 'created_at']
**direction** | **str** | Sort direction (asc/desc) | [optional] [default to 'desc']

## Example

```python
from mixpeek.models.list_triggers_request import ListTriggersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListTriggersRequest from a JSON string
list_triggers_request_instance = ListTriggersRequest.from_json(json)
# print the JSON string representation of the object
print(ListTriggersRequest.to_json())

# convert the object into a dict
list_triggers_request_dict = list_triggers_request_instance.to_dict()
# create an instance of ListTriggersRequest from a dict
list_triggers_request_from_dict = ListTriggersRequest.from_dict(list_triggers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


