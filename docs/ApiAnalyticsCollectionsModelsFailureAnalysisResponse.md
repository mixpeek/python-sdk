# ApiAnalyticsCollectionsModelsFailureAnalysisResponse

Failure analysis response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_id** | **str** |  | 
**time_range** | [**ApiAnalyticsCollectionsModelsTimeRange**](ApiAnalyticsCollectionsModelsTimeRange.md) |  | 
**error_distribution** | [**List[ErrorMetrics]**](ErrorMetrics.md) |  | 
**total_errors** | **int** |  | 

## Example

```python
from mixpeek.models.api_analytics_collections_models_failure_analysis_response import ApiAnalyticsCollectionsModelsFailureAnalysisResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiAnalyticsCollectionsModelsFailureAnalysisResponse from a JSON string
api_analytics_collections_models_failure_analysis_response_instance = ApiAnalyticsCollectionsModelsFailureAnalysisResponse.from_json(json)
# print the JSON string representation of the object
print(ApiAnalyticsCollectionsModelsFailureAnalysisResponse.to_json())

# convert the object into a dict
api_analytics_collections_models_failure_analysis_response_dict = api_analytics_collections_models_failure_analysis_response_instance.to_dict()
# create an instance of ApiAnalyticsCollectionsModelsFailureAnalysisResponse from a dict
api_analytics_collections_models_failure_analysis_response_from_dict = ApiAnalyticsCollectionsModelsFailureAnalysisResponse.from_dict(api_analytics_collections_models_failure_analysis_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


