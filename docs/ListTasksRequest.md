# ListTasksRequest

Request model for listing tasks.  Filter tasks by status, type, or other criteria.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**TaskStatusEnum**](TaskStatusEnum.md) | Filter by specific task status (PENDING, IN_PROGRESS, PROCESSING, COMPLETED, FAILED, CANCELED, etc.). | [optional] 
**task_type** | [**TaskType**](TaskType.md) | Filter by task type (e.g., API_BUCKETS_OBJECTS_CREATE, BATCH_CONFIRM, etc.) | [optional] 
**filters** | [**LogicalOperatorInput**](LogicalOperatorInput.md) | Advanced filters to apply. | [optional] 
**sort** | [**SortOption**](SortOption.md) | Sort options. | [optional] 
**search** | **str** | Search term. | [optional] 

## Example

```python
from mixpeek.models.list_tasks_request import ListTasksRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListTasksRequest from a JSON string
list_tasks_request_instance = ListTasksRequest.from_json(json)
# print the JSON string representation of the object
print(ListTasksRequest.to_json())

# convert the object into a dict
list_tasks_request_dict = list_tasks_request_instance.to_dict()
# create an instance of ListTasksRequest from a dict
list_tasks_request_from_dict = ListTasksRequest.from_dict(list_tasks_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


