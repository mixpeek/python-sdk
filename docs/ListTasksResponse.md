# ListTasksResponse

Response model for listing tasks.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[TaskResponse]**](TaskResponse.md) |  | 
**pagination** | [**PaginationResponse**](PaginationResponse.md) |  | 

## Example

```python
from mixpeek.models.list_tasks_response import ListTasksResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListTasksResponse from a JSON string
list_tasks_response_instance = ListTasksResponse.from_json(json)
# print the JSON string representation of the object
print(ListTasksResponse.to_json())

# convert the object into a dict
list_tasks_response_dict = list_tasks_response_instance.to_dict()
# create an instance of ListTasksResponse from a dict
list_tasks_response_from_dict = ListTasksResponse.from_dict(list_tasks_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


