# ExtractorBreakdownResponse

Response for extractor performance breakdown.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_range** | [**ApiAnalyticsModelsTimeRange**](ApiAnalyticsModelsTimeRange.md) | Time range of the analysis | 
**extractors** | [**List[ExtractorPerformance]**](ExtractorPerformance.md) | Performance by extractor and stage | 

## Example

```python
from mixpeek.models.extractor_breakdown_response import ExtractorBreakdownResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExtractorBreakdownResponse from a JSON string
extractor_breakdown_response_instance = ExtractorBreakdownResponse.from_json(json)
# print the JSON string representation of the object
print(ExtractorBreakdownResponse.to_json())

# convert the object into a dict
extractor_breakdown_response_dict = extractor_breakdown_response_instance.to_dict()
# create an instance of ExtractorBreakdownResponse from a dict
extractor_breakdown_response_from_dict = ExtractorBreakdownResponse.from_dict(extractor_breakdown_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


