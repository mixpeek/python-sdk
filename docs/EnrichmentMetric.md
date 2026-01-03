# EnrichmentMetric

Taxonomy enrichment metrics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_bucket** | **datetime** |  | 
**enrichment_count** | **int** |  | 
**success_count** | **int** |  | 
**failure_count** | **int** |  | 
**avg_latency_ms** | **float** |  | 
**success_rate** | **float** |  | 

## Example

```python
from mixpeek.models.enrichment_metric import EnrichmentMetric

# TODO update the JSON string below
json = "{}"
# create an instance of EnrichmentMetric from a JSON string
enrichment_metric_instance = EnrichmentMetric.from_json(json)
# print the JSON string representation of the object
print(EnrichmentMetric.to_json())

# convert the object into a dict
enrichment_metric_dict = enrichment_metric_instance.to_dict()
# create an instance of EnrichmentMetric from a dict
enrichment_metric_from_dict = EnrichmentMetric.from_dict(enrichment_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


