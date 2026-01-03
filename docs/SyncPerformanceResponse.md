# SyncPerformanceResponse

Sync performance analytics response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_id** | **str** | Bucket identifier | 
**sync_config_id** | **str** | Optional sync config filter | [optional] 
**time_range** | [**ApiAnalyticsBucketsModelsTimeRange**](ApiAnalyticsBucketsModelsTimeRange.md) | Query time range | 
**runs** | [**List[SyncRunMetric]**](SyncRunMetric.md) | Sync run metrics | 
**summary** | **Dict[str, object]** | Summary statistics | [optional] 

## Example

```python
from mixpeek.models.sync_performance_response import SyncPerformanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SyncPerformanceResponse from a JSON string
sync_performance_response_instance = SyncPerformanceResponse.from_json(json)
# print the JSON string representation of the object
print(SyncPerformanceResponse.to_json())

# convert the object into a dict
sync_performance_response_dict = sync_performance_response_instance.to_dict()
# create an instance of SyncPerformanceResponse from a dict
sync_performance_response_from_dict = SyncPerformanceResponse.from_dict(sync_performance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


