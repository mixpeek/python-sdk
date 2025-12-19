# CacheStatistics

Statistics about cache performance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hit_count** | **int** | Number of cache hits | [optional] [default to 0]
**miss_count** | **int** | Number of cache misses | [optional] [default to 0]
**hit_rate** | **float** | Cache hit rate (0.0 - 1.0) | [optional] [default to 0.0]
**size_bytes** | **int** | Total size of cached data in bytes | [optional] [default to 0]
**entry_count** | **int** | Number of entries in cache | [optional] [default to 0]
**last_invalidated_at** | **datetime** | When the cache was last invalidated | [optional] 

## Example

```python
from mixpeek.models.cache_statistics import CacheStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of CacheStatistics from a JSON string
cache_statistics_instance = CacheStatistics.from_json(json)
# print the JSON string representation of the object
print(CacheStatistics.to_json())

# convert the object into a dict
cache_statistics_dict = cache_statistics_instance.to_dict()
# create an instance of CacheStatistics from a dict
cache_statistics_from_dict = CacheStatistics.from_dict(cache_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


