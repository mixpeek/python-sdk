# CachePerformanceResponse

Cache performance metrics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retriever_id** | **str** | Retriever identifier | 
**time_range** | [**ApiAnalyticsModelsTimeRange**](ApiAnalyticsModelsTimeRange.md) | Time range | 
**cache_hit_rate** | **float** | Overall cache hit rate | 
**total_cache_hits** | **int** | Total cache hits | 
**total_cache_misses** | **int** | Total cache misses | 
**avg_cache_hit_latency_ms** | **float** | Average latency on cache hit | 
**avg_cache_miss_latency_ms** | **float** | Average latency on cache miss | 
**hourly_breakdown** | **List[object]** | Hourly cache performance | 

## Example

```python
from mixpeek.models.cache_performance_response import CachePerformanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CachePerformanceResponse from a JSON string
cache_performance_response_instance = CachePerformanceResponse.from_json(json)
# print the JSON string representation of the object
print(CachePerformanceResponse.to_json())

# convert the object into a dict
cache_performance_response_dict = cache_performance_response_instance.to_dict()
# create an instance of CachePerformanceResponse from a dict
cache_performance_response_from_dict = CachePerformanceResponse.from_dict(cache_performance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


