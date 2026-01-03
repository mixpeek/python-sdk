# StagePerformanceMetrics

Stage-level performance metrics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stage_name** | **str** | Name of the stage | 
**stage_type** | **str** | Type of the stage | 
**execution_count** | **int** | Number of executions | 
**avg_latency_ms** | **float** | Average latency | 
**p95_latency_ms** | **float** | P95 latency | 
**avg_documents_in** | **float** | Average documents input | 
**avg_documents_out** | **float** | Average documents output | 

## Example

```python
from mixpeek.models.stage_performance_metrics import StagePerformanceMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of StagePerformanceMetrics from a JSON string
stage_performance_metrics_instance = StagePerformanceMetrics.from_json(json)
# print the JSON string representation of the object
print(StagePerformanceMetrics.to_json())

# convert the object into a dict
stage_performance_metrics_dict = stage_performance_metrics_instance.to_dict()
# create an instance of StagePerformanceMetrics from a dict
stage_performance_metrics_from_dict = StagePerformanceMetrics.from_dict(stage_performance_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


