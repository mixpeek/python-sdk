# SyncComparisonResponse

Sync configuration comparison response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_id** | **str** | Bucket identifier | 
**time_range** | [**ApiAnalyticsBucketsModelsTimeRange**](ApiAnalyticsBucketsModelsTimeRange.md) | Query time range | 
**configs** | [**List[SyncConfigMetric]**](SyncConfigMetric.md) | Metrics per sync config | 

## Example

```python
from mixpeek.models.sync_comparison_response import SyncComparisonResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SyncComparisonResponse from a JSON string
sync_comparison_response_instance = SyncComparisonResponse.from_json(json)
# print the JSON string representation of the object
print(SyncComparisonResponse.to_json())

# convert the object into a dict
sync_comparison_response_dict = sync_comparison_response_instance.to_dict()
# create an instance of SyncComparisonResponse from a dict
sync_comparison_response_from_dict = SyncComparisonResponse.from_dict(sync_comparison_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


