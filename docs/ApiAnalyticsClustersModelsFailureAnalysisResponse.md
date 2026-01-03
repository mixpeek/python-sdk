# ApiAnalyticsClustersModelsFailureAnalysisResponse

Cluster failure analysis response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** |  | 
**time_range** | [**ApiAnalyticsClustersModelsTimeRange**](ApiAnalyticsClustersModelsTimeRange.md) |  | 
**failures** | [**List[FailureMetric]**](FailureMetric.md) |  | 
**total_failures** | **int** |  | 

## Example

```python
from mixpeek.models.api_analytics_clusters_models_failure_analysis_response import ApiAnalyticsClustersModelsFailureAnalysisResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiAnalyticsClustersModelsFailureAnalysisResponse from a JSON string
api_analytics_clusters_models_failure_analysis_response_instance = ApiAnalyticsClustersModelsFailureAnalysisResponse.from_json(json)
# print the JSON string representation of the object
print(ApiAnalyticsClustersModelsFailureAnalysisResponse.to_json())

# convert the object into a dict
api_analytics_clusters_models_failure_analysis_response_dict = api_analytics_clusters_models_failure_analysis_response_instance.to_dict()
# create an instance of ApiAnalyticsClustersModelsFailureAnalysisResponse from a dict
api_analytics_clusters_models_failure_analysis_response_from_dict = ApiAnalyticsClustersModelsFailureAnalysisResponse.from_dict(api_analytics_clusters_models_failure_analysis_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


