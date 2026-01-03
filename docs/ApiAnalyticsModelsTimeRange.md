# ApiAnalyticsModelsTimeRange

Time range for analytics queries.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **datetime** | Start time (UTC) | 
**end** | **datetime** | End time (UTC) | 

## Example

```python
from mixpeek.models.api_analytics_models_time_range import ApiAnalyticsModelsTimeRange

# TODO update the JSON string below
json = "{}"
# create an instance of ApiAnalyticsModelsTimeRange from a JSON string
api_analytics_models_time_range_instance = ApiAnalyticsModelsTimeRange.from_json(json)
# print the JSON string representation of the object
print(ApiAnalyticsModelsTimeRange.to_json())

# convert the object into a dict
api_analytics_models_time_range_dict = api_analytics_models_time_range_instance.to_dict()
# create an instance of ApiAnalyticsModelsTimeRange from a dict
api_analytics_models_time_range_from_dict = ApiAnalyticsModelsTimeRange.from_dict(api_analytics_models_time_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


