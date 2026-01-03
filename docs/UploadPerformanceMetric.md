# UploadPerformanceMetric

Upload performance metrics for a time bucket.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_bucket** | **datetime** | Time bucket timestamp | 
**upload_count** | **int** | Number of uploads | 
**avg_latency_ms** | **float** | Average upload latency | 
**p95_latency_ms** | **float** | 95th percentile latency | 
**p99_latency_ms** | **float** | 99th percentile latency | 
**avg_throughput_mbps** | **float** | Average throughput in MB/s | 
**error_rate** | **float** | Error rate (0-1) | 

## Example

```python
from mixpeek.models.upload_performance_metric import UploadPerformanceMetric

# TODO update the JSON string below
json = "{}"
# create an instance of UploadPerformanceMetric from a JSON string
upload_performance_metric_instance = UploadPerformanceMetric.from_json(json)
# print the JSON string representation of the object
print(UploadPerformanceMetric.to_json())

# convert the object into a dict
upload_performance_metric_dict = upload_performance_metric_instance.to_dict()
# create an instance of UploadPerformanceMetric from a dict
upload_performance_metric_from_dict = UploadPerformanceMetric.from_dict(upload_performance_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


