# StagePerformance

Performance statistics for a retriever stage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg_execution_ms** | **float** | Average execution time in milliseconds | [optional] [default to 0.0]
**execution_count** | **int** | Number of times executed | [optional] [default to 0]
**error_count** | **int** | Number of errors encountered | [optional] [default to 0]
**last_executed_at** | **datetime** | Last time this stage was executed | [optional] 

## Example

```python
from mixpeek.models.stage_performance import StagePerformance

# TODO update the JSON string below
json = "{}"
# create an instance of StagePerformance from a JSON string
stage_performance_instance = StagePerformance.from_json(json)
# print the JSON string representation of the object
print(StagePerformance.to_json())

# convert the object into a dict
stage_performance_dict = stage_performance_instance.to_dict()
# create an instance of StagePerformance from a dict
stage_performance_from_dict = StagePerformance.from_dict(stage_performance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


