# ValidateMigrationResponse

Response for migration validation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**validation_result** | [**ValidationResult**](ValidationResult.md) | Validation result | 
**dependency_graph** | [**DependencyGraph**](DependencyGraph.md) | Dependency graph if validation passed | [optional] 
**message** | **str** | Human-readable message | 

## Example

```python
from mixpeek.models.validate_migration_response import ValidateMigrationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateMigrationResponse from a JSON string
validate_migration_response_instance = ValidateMigrationResponse.from_json(json)
# print the JSON string representation of the object
print(ValidateMigrationResponse.to_json())

# convert the object into a dict
validate_migration_response_dict = validate_migration_response_instance.to_dict()
# create an instance of ValidateMigrationResponse from a dict
validate_migration_response_from_dict = ValidateMigrationResponse.from_dict(validate_migration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


