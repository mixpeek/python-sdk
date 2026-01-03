# LabelMetric

Label distribution metrics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | 
**count** | **int** |  | 
**percentage** | **float** |  | 
**avg_confidence** | **float** |  | 

## Example

```python
from mixpeek.models.label_metric import LabelMetric

# TODO update the JSON string below
json = "{}"
# create an instance of LabelMetric from a JSON string
label_metric_instance = LabelMetric.from_json(json)
# print the JSON string representation of the object
print(LabelMetric.to_json())

# convert the object into a dict
label_metric_dict = label_metric_instance.to_dict()
# create an instance of LabelMetric from a dict
label_metric_from_dict = LabelMetric.from_dict(label_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


