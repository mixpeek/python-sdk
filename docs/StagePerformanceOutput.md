# StagePerformanceOutput

Performance breakdown by stage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stage_name** | **str** | Name of the profiled stage | 
**component** | **str** | Component (e.g., extractor, cluster) | 
**execution_count** | **int** | Number of executions | 
**avg_latency_ms** | **float** | Average latency | 
**p95_latency_ms** | **float** | 95th percentile latency | 
**max_latency_ms** | **float** | Maximum latency | 
**total_time_ms** | **float** | Total time spent in this stage | 
**pct_of_total** | **float** | Percentage of total time spent in this stage | 

## Example

```python
from mixpeek.models.stage_performance_output import StagePerformanceOutput

# TODO update the JSON string below
json = "{}"
# create an instance of StagePerformanceOutput from a JSON string
stage_performance_output_instance = StagePerformanceOutput.from_json(json)
# print the JSON string representation of the object
print(StagePerformanceOutput.to_json())

# convert the object into a dict
stage_performance_output_dict = stage_performance_output_instance.to_dict()
# create an instance of StagePerformanceOutput from a dict
stage_performance_output_from_dict = StagePerformanceOutput.from_dict(stage_performance_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


