# ExtractorMetrics

Extractor performance metrics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extractor_name** | **str** |  | 
**version** | **str** |  | 
**execution_count** | **int** |  | 
**success_count** | **int** |  | 
**failure_count** | **int** |  | 
**success_rate** | **float** |  | 
**avg_latency_ms** | **float** |  | 
**p95_latency_ms** | **float** |  | 
**p99_latency_ms** | **float** |  | 

## Example

```python
from mixpeek.models.extractor_metrics import ExtractorMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of ExtractorMetrics from a JSON string
extractor_metrics_instance = ExtractorMetrics.from_json(json)
# print the JSON string representation of the object
print(ExtractorMetrics.to_json())

# convert the object into a dict
extractor_metrics_dict = extractor_metrics_instance.to_dict()
# create an instance of ExtractorMetrics from a dict
extractor_metrics_from_dict = ExtractorMetrics.from_dict(extractor_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


