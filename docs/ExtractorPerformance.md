# ExtractorPerformance

Performance breakdown by extractor.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extractor_name** | **str** | Name of the extractor | 
**stage_name** | **str** | Name of the stage | 
**execution_count** | **int** | Number of executions | 
**avg_latency_ms** | **float** | Average latency | 
**p95_latency_ms** | **float** | 95th percentile latency | 
**max_latency_ms** | **float** | Maximum latency | 

## Example

```python
from mixpeek.models.extractor_performance import ExtractorPerformance

# TODO update the JSON string below
json = "{}"
# create an instance of ExtractorPerformance from a JSON string
extractor_performance_instance = ExtractorPerformance.from_json(json)
# print the JSON string representation of the object
print(ExtractorPerformance.to_json())

# convert the object into a dict
extractor_performance_dict = extractor_performance_instance.to_dict()
# create an instance of ExtractorPerformance from a dict
extractor_performance_from_dict = ExtractorPerformance.from_dict(extractor_performance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


