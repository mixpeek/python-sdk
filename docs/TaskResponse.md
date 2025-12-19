# TaskResponse

Task response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** | Unique identifier for the task | 
**task_type** | [**TaskType**](TaskType.md) | Type of the task | 
**status** | [**TaskStatusEnum**](TaskStatusEnum.md) | Current status of the task | 
**inputs** | [**List[TaskResponseInputsInner]**](TaskResponseInputsInner.md) | List of input parameters or data for the task | [optional] 
**outputs** | [**List[TaskResponseInputsInner]**](TaskResponseInputsInner.md) | List of output results from the task | [optional] 
**additional_data** | **Dict[str, object]** | Additional metadata or context for the task | [optional] 
**error_message** | **str** | Flattened error message derived from additional_data[&#39;error&#39;] if present. | [optional] 

## Example

```python
from mixpeek.models.task_response import TaskResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TaskResponse from a JSON string
task_response_instance = TaskResponse.from_json(json)
# print the JSON string representation of the object
print(TaskResponse.to_json())

# convert the object into a dict
task_response_dict = task_response_instance.to_dict()
# create an instance of TaskResponse from a dict
task_response_from_dict = TaskResponse.from_dict(task_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


