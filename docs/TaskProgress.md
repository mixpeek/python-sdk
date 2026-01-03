# TaskProgress

Progress information for a task.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**processed_documents** | **int** | Number of documents processed | [optional] [default to 0]
**total_documents** | **int** | Total documents to process | [optional] [default to 0]
**percentage** | **float** | Progress percentage (0-100) | [optional] [default to 0.0]

## Example

```python
from mixpeek.models.task_progress import TaskProgress

# TODO update the JSON string below
json = "{}"
# create an instance of TaskProgress from a JSON string
task_progress_instance = TaskProgress.from_json(json)
# print the JSON string representation of the object
print(TaskProgress.to_json())

# convert the object into a dict
task_progress_dict = task_progress_instance.to_dict()
# create an instance of TaskProgress from a dict
task_progress_from_dict = TaskProgress.from_dict(task_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


