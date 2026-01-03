# ApiAnalyticsBucketsModelsTimeRange

Time range for analytics queries.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **datetime** | Start of time range | 
**end** | **datetime** | End of time range | 

## Example

```python
from mixpeek.models.api_analytics_buckets_models_time_range import ApiAnalyticsBucketsModelsTimeRange

# TODO update the JSON string below
json = "{}"
# create an instance of ApiAnalyticsBucketsModelsTimeRange from a JSON string
api_analytics_buckets_models_time_range_instance = ApiAnalyticsBucketsModelsTimeRange.from_json(json)
# print the JSON string representation of the object
print(ApiAnalyticsBucketsModelsTimeRange.to_json())

# convert the object into a dict
api_analytics_buckets_models_time_range_dict = api_analytics_buckets_models_time_range_instance.to_dict()
# create an instance of ApiAnalyticsBucketsModelsTimeRange from a dict
api_analytics_buckets_models_time_range_from_dict = ApiAnalyticsBucketsModelsTimeRange.from_dict(api_analytics_buckets_models_time_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


