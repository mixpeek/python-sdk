# ValidateMigrationRequest

Request to validate a migration configuration without creating it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**MigrationConfig**](MigrationConfig.md) | Migration configuration | 

## Example

```python
from mixpeek.models.validate_migration_request import ValidateMigrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateMigrationRequest from a JSON string
validate_migration_request_instance = ValidateMigrationRequest.from_json(json)
# print the JSON string representation of the object
print(ValidateMigrationRequest.to_json())

# convert the object into a dict
validate_migration_request_dict = validate_migration_request_instance.to_dict()
# create an instance of ValidateMigrationRequest from a dict
validate_migration_request_from_dict = ValidateMigrationRequest.from_dict(validate_migration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


