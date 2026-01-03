# FailureMetric

Cluster failure metrics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** |  | 
**execution_id** | **str** |  | 
**error_message** | **str** |  | 
**error_type** | **str** |  | 

## Example

```python
from mixpeek.models.failure_metric import FailureMetric

# TODO update the JSON string below
json = "{}"
# create an instance of FailureMetric from a JSON string
failure_metric_instance = FailureMetric.from_json(json)
# print the JSON string representation of the object
print(FailureMetric.to_json())

# convert the object into a dict
failure_metric_dict = failure_metric_instance.to_dict()
# create an instance of FailureMetric from a dict
failure_metric_from_dict = FailureMetric.from_dict(failure_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


