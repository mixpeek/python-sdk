# ErrorBreakdown

Error breakdown by type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_type** | **str** | Error type | 
**count** | **int** | Error count | 
**percentage** | **float** | Percentage of total errors | 
**first_seen** | **datetime** | First occurrence | 
**last_seen** | **datetime** | Last occurrence | 

## Example

```python
from mixpeek.models.error_breakdown import ErrorBreakdown

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorBreakdown from a JSON string
error_breakdown_instance = ErrorBreakdown.from_json(json)
# print the JSON string representation of the object
print(ErrorBreakdown.to_json())

# convert the object into a dict
error_breakdown_dict = error_breakdown_instance.to_dict()
# create an instance of ErrorBreakdown from a dict
error_breakdown_from_dict = ErrorBreakdown.from_dict(error_breakdown_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


