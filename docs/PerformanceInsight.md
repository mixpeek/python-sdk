# PerformanceInsight

Performance insight or recommendation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Insight type (bottleneck, optimization, warning) | 
**severity** | **str** | Severity (info, warning, critical) | 
**message** | **str** | Human-readable message | 
**stage** | **str** | Related stage name | [optional] 
**metric_value** | **float** | Related metric value | [optional] 
**recommendation** | **str** | Recommended action | [optional] 

## Example

```python
from mixpeek.models.performance_insight import PerformanceInsight

# TODO update the JSON string below
json = "{}"
# create an instance of PerformanceInsight from a JSON string
performance_insight_instance = PerformanceInsight.from_json(json)
# print the JSON string representation of the object
print(PerformanceInsight.to_json())

# convert the object into a dict
performance_insight_dict = performance_insight_instance.to_dict()
# create an instance of PerformanceInsight from a dict
performance_insight_from_dict = PerformanceInsight.from_dict(performance_insight_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


