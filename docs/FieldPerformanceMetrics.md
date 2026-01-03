# FieldPerformanceMetrics

Performance correlation metrics for a field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** | Metadata field name | 
**usage_count** | **int** | Number of times field was queried | 
**avg_latency_ms** | **float** | Average latency when field is used | 
**p50_latency_ms** | **float** | 50th percentile latency | 
**p95_latency_ms** | **float** | 95th percentile latency | 
**p99_latency_ms** | **float** | 99th percentile latency | 
**max_latency_ms** | **float** | Maximum latency observed | 
**index_priority_score** | **float** | Priority score for indexing (usage_count * avg_latency) | 

## Example

```python
from mixpeek.models.field_performance_metrics import FieldPerformanceMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of FieldPerformanceMetrics from a JSON string
field_performance_metrics_instance = FieldPerformanceMetrics.from_json(json)
# print the JSON string representation of the object
print(FieldPerformanceMetrics.to_json())

# convert the object into a dict
field_performance_metrics_dict = field_performance_metrics_instance.to_dict()
# create an instance of FieldPerformanceMetrics from a dict
field_performance_metrics_from_dict = FieldPerformanceMetrics.from_dict(field_performance_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


