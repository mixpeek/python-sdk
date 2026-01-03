# GrowthMetric

Document growth metric.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_bucket** | **datetime** |  | 
**documents_added** | **int** |  | 
**success_rate** | **float** |  | 
**avg_latency_ms** | **float** |  | 

## Example

```python
from mixpeek.models.growth_metric import GrowthMetric

# TODO update the JSON string below
json = "{}"
# create an instance of GrowthMetric from a JSON string
growth_metric_instance = GrowthMetric.from_json(json)
# print the JSON string representation of the object
print(GrowthMetric.to_json())

# convert the object into a dict
growth_metric_dict = growth_metric_instance.to_dict()
# create an instance of GrowthMetric from a dict
growth_metric_from_dict = GrowthMetric.from_dict(growth_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


