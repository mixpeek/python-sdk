# ValidateResult

Result of validating a manifest.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid** | **bool** | Whether the manifest is valid | 
**resources** | **Dict[str, int]** | Count of each resource type | [optional] 
**missing_secrets** | **List[str]** | Secret names referenced but not configured | [optional] 
**errors** | **List[str]** | Validation errors | [optional] 
**warnings** | **List[str]** | Validation warnings | [optional] 

## Example

```python
from mixpeek.models.validate_result import ValidateResult

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateResult from a JSON string
validate_result_instance = ValidateResult.from_json(json)
# print the JSON string representation of the object
print(ValidateResult.to_json())

# convert the object into a dict
validate_result_dict = validate_result_instance.to_dict()
# create an instance of ValidateResult from a dict
validate_result_from_dict = ValidateResult.from_dict(validate_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


