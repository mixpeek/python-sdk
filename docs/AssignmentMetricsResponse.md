# AssignmentMetricsResponse

Taxonomy assignment metrics response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taxonomy_id** | **str** |  | 
**time_range** | [**ApiAnalyticsTaxonomiesModelsTimeRange**](ApiAnalyticsTaxonomiesModelsTimeRange.md) |  | 
**metrics** | [**List[AssignmentMetric]**](AssignmentMetric.md) |  | 
**summary** | **object** |  | [optional] 

## Example

```python
from mixpeek.models.assignment_metrics_response import AssignmentMetricsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssignmentMetricsResponse from a JSON string
assignment_metrics_response_instance = AssignmentMetricsResponse.from_json(json)
# print the JSON string representation of the object
print(AssignmentMetricsResponse.to_json())

# convert the object into a dict
assignment_metrics_response_dict = assignment_metrics_response_instance.to_dict()
# create an instance of AssignmentMetricsResponse from a dict
assignment_metrics_response_from_dict = AssignmentMetricsResponse.from_dict(assignment_metrics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


