# FieldPerformanceResponse

Response for field performance correlation endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespace_id** | **str** | Namespace ID analyzed | 
**time_range_days** | **int** | Number of days analyzed | 
**fields** | [**List[FieldPerformanceMetrics]**](FieldPerformanceMetrics.md) | Field performance metrics | 
**total_fields** | **int** | Total fields analyzed | 

## Example

```python
from mixpeek.models.field_performance_response import FieldPerformanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FieldPerformanceResponse from a JSON string
field_performance_response_instance = FieldPerformanceResponse.from_json(json)
# print the JSON string representation of the object
print(FieldPerformanceResponse.to_json())

# convert the object into a dict
field_performance_response_dict = field_performance_response_instance.to_dict()
# create an instance of FieldPerformanceResponse from a dict
field_performance_response_from_dict = FieldPerformanceResponse.from_dict(field_performance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


