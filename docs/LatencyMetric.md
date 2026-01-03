# LatencyMetric

Latency distribution metric.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_bucket** | **datetime** |  | 
**document_count** | **int** |  | 
**avg_latency_ms** | **float** |  | 
**p95_latency_ms** | **float** |  | 
**p99_latency_ms** | **float** |  | 

## Example

```python
from mixpeek.models.latency_metric import LatencyMetric

# TODO update the JSON string below
json = "{}"
# create an instance of LatencyMetric from a JSON string
latency_metric_instance = LatencyMetric.from_json(json)
# print the JSON string representation of the object
print(LatencyMetric.to_json())

# convert the object into a dict
latency_metric_dict = latency_metric_instance.to_dict()
# create an instance of LatencyMetric from a dict
latency_metric_from_dict = LatencyMetric.from_dict(latency_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


