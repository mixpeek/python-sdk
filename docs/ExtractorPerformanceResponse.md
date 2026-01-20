# ExtractorPerformanceResponse

Extractor performance breakdown.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_id** | **str** |  | 
**time_range** | [**ApiAnalyticsCollectionsModelsTimeRange**](ApiAnalyticsCollectionsModelsTimeRange.md) |  | 
**extractors** | [**List[ExtractorMetrics]**](ExtractorMetrics.md) |  | 
**summary** | **object** |  | [optional] 

## Example

```python
from mixpeek.models.extractor_performance_response import ExtractorPerformanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExtractorPerformanceResponse from a JSON string
extractor_performance_response_instance = ExtractorPerformanceResponse.from_json(json)
# print the JSON string representation of the object
print(ExtractorPerformanceResponse.to_json())

# convert the object into a dict
extractor_performance_response_dict = extractor_performance_response_instance.to_dict()
# create an instance of ExtractorPerformanceResponse from a dict
extractor_performance_response_from_dict = ExtractorPerformanceResponse.from_dict(extractor_performance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


