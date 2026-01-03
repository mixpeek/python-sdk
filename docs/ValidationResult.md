# ValidationResult

Result of pre-flight validation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid** | **bool** | Whether migration can proceed | 
**errors** | [**List[ValidationError]**](ValidationError.md) | Validation errors | [optional] 
**warnings** | [**List[ValidationError]**](ValidationError.md) | Validation warnings | [optional] 
**estimated_resources** | **Dict[str, int]** | Estimated resource counts | [optional] 
**estimated_duration_seconds** | **int** | Estimated migration duration | [optional] 

## Example

```python
from mixpeek.models.validation_result import ValidationResult

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationResult from a JSON string
validation_result_instance = ValidationResult.from_json(json)
# print the JSON string representation of the object
print(ValidationResult.to_json())

# convert the object into a dict
validation_result_dict = validation_result_instance.to_dict()
# create an instance of ValidationResult from a dict
validation_result_from_dict = ValidationResult.from_dict(validation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


