# TaskStatusUpdateRequest

Request to update task status (Engine callback).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal_id** | **str** |  | 
**namespace_id** | **str** |  | 
**status** | **str** |  | 
**outputs** | **List[object]** |  | [optional] 
**additional_data** | **object** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from mixpeek.models.task_status_update_request import TaskStatusUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TaskStatusUpdateRequest from a JSON string
task_status_update_request_instance = TaskStatusUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(TaskStatusUpdateRequest.to_json())

# convert the object into a dict
task_status_update_request_dict = task_status_update_request_instance.to_dict()
# create an instance of TaskStatusUpdateRequest from a dict
task_status_update_request_from_dict = TaskStatusUpdateRequest.from_dict(task_status_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


