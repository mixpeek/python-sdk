# PerformanceMetric

Single performance metric data point.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_bucket** | **datetime** | Time bucket for this metric (hour, day, etc.) | 
**execution_count** | **int** | Number of executions in this period | 
**avg_latency_ms** | **float** | Average latency in milliseconds | 
**p50_latency_ms** | **float** | 50th percentile (median) latency | 
**p95_latency_ms** | **float** | 95th percentile latency | 
**p99_latency_ms** | **float** | 99th percentile latency | 
**max_latency_ms** | **float** | Maximum latency observed | 

## Example

```python
from mixpeek.models.performance_metric import PerformanceMetric

# TODO update the JSON string below
json = "{}"
# create an instance of PerformanceMetric from a JSON string
performance_metric_instance = PerformanceMetric.from_json(json)
# print the JSON string representation of the object
print(PerformanceMetric.to_json())

# convert the object into a dict
performance_metric_dict = performance_metric_instance.to_dict()
# create an instance of PerformanceMetric from a dict
performance_metric_from_dict = PerformanceMetric.from_dict(performance_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


