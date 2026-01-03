# PerformanceSummary

Summary statistics for performance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_executions** | **int** | Total number of executions | [optional] [default to 0]
**avg_latency_ms** | **float** | Average latency | [optional] [default to 0.0]
**p50_latency_ms** | **float** | Median latency | [optional] [default to 0.0]
**p95_latency_ms** | **float** | 95th percentile latency | [optional] [default to 0.0]
**p99_latency_ms** | **float** | 99th percentile latency | [optional] [default to 0.0]
**max_latency_ms** | **float** | Maximum latency | [optional] [default to 0.0]
**total_time_seconds** | **float** | Total time spent across all executions | [optional] [default to 0.0]

## Example

```python
from mixpeek.models.performance_summary import PerformanceSummary

# TODO update the JSON string below
json = "{}"
# create an instance of PerformanceSummary from a JSON string
performance_summary_instance = PerformanceSummary.from_json(json)
# print the JSON string representation of the object
print(PerformanceSummary.to_json())

# convert the object into a dict
performance_summary_dict = performance_summary_instance.to_dict()
# create an instance of PerformanceSummary from a dict
performance_summary_from_dict = PerformanceSummary.from_dict(performance_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


