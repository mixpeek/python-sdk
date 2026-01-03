# BucketHealthResponse

Bucket health monitoring response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_id** | **str** | Bucket identifier | 
**time_range** | [**ApiAnalyticsBucketsModelsTimeRange**](ApiAnalyticsBucketsModelsTimeRange.md) | Query time range | 
**overall_health** | **str** | Overall health status | 
**total_errors** | **int** | Total error count | 
**error_breakdown** | [**List[ErrorBreakdown]**](ErrorBreakdown.md) | Errors by type | 
**sync_health** | [**List[SyncHealthMetric]**](SyncHealthMetric.md) | Sync health per config | 
**stuck_syncs** | **List[str]** | Sync configs with no recent activity | 

## Example

```python
from mixpeek.models.bucket_health_response import BucketHealthResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BucketHealthResponse from a JSON string
bucket_health_response_instance = BucketHealthResponse.from_json(json)
# print the JSON string representation of the object
print(BucketHealthResponse.to_json())

# convert the object into a dict
bucket_health_response_dict = bucket_health_response_instance.to_dict()
# create an instance of BucketHealthResponse from a dict
bucket_health_response_from_dict = BucketHealthResponse.from_dict(bucket_health_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


