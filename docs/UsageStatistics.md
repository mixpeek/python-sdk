# UsageStatistics

Usage statistics for a retriever.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_queries** | **int** | Total number of queries executed | [optional] [default to 0]
**queries_last_24h** | **int** | Number of queries in the last 24 hours | [optional] [default to 0]
**avg_latency_ms** | **float** | Average latency in milliseconds | [optional] [default to 0.0]
**error_rate** | **float** | Error rate as a fraction (0.0 - 1.0) | [optional] [default to 0.0]
**last_error** | **str** | Most recent error message for debugging | [optional] 
**cache_hit_rate** | **float** | Cache hit rate if caching is enabled (0.0 - 1.0) | [optional] 

## Example

```python
from mixpeek.models.usage_statistics import UsageStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of UsageStatistics from a JSON string
usage_statistics_instance = UsageStatistics.from_json(json)
# print the JSON string representation of the object
print(UsageStatistics.to_json())

# convert the object into a dict
usage_statistics_dict = usage_statistics_instance.to_dict()
# create an instance of UsageStatistics from a dict
usage_statistics_from_dict = UsageStatistics.from_dict(usage_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


