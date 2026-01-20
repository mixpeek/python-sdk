# LatencyMetrics

Performance timing statistics for a pipeline.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**p50_ms** | **float** | 50th percentile latency in milliseconds. | 
**p90_ms** | **float** | 90th percentile latency in milliseconds. | 
**p99_ms** | **float** | 99th percentile latency in milliseconds. | 
**mean_ms** | **float** | Mean latency in milliseconds. | 
**stage_latencies** | **Dict[str, float]** | Per-stage latency breakdown (stage_name -&gt; avg_ms). | [optional] 

## Example

```python
from mixpeek.models.latency_metrics import LatencyMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of LatencyMetrics from a JSON string
latency_metrics_instance = LatencyMetrics.from_json(json)
# print the JSON string representation of the object
print(LatencyMetrics.to_json())

# convert the object into a dict
latency_metrics_dict = latency_metrics_instance.to_dict()
# create an instance of LatencyMetrics from a dict
latency_metrics_from_dict = LatencyMetrics.from_dict(latency_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


