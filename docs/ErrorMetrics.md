# ErrorMetrics

Error analysis metrics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_type** | **str** |  | 
**count** | **int** |  | 
**percentage** | **float** |  | 
**recent_message** | **str** |  | 

## Example

```python
from mixpeek.models.error_metrics import ErrorMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorMetrics from a JSON string
error_metrics_instance = ErrorMetrics.from_json(json)
# print the JSON string representation of the object
print(ErrorMetrics.to_json())

# convert the object into a dict
error_metrics_dict = error_metrics_instance.to_dict()
# create an instance of ErrorMetrics from a dict
error_metrics_from_dict = ErrorMetrics.from_dict(error_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


