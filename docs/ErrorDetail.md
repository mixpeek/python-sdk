# ErrorDetail

Error detail model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Human-readable error message | 
**type** | **str** | Stable error type identifier (machine-readable) | 
**details** | **object** | Optional structured details to help debugging (validation errors, IDs, etc.) | [optional] 

## Example

```python
from mixpeek.models.error_detail import ErrorDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorDetail from a JSON string
error_detail_instance = ErrorDetail.from_json(json)
# print the JSON string representation of the object
print(ErrorDetail.to_json())

# convert the object into a dict
error_detail_dict = error_detail_instance.to_dict()
# create an instance of ErrorDetail from a dict
error_detail_from_dict = ErrorDetail.from_dict(error_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


