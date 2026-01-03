# CreateMigrationResponse

Response after creating a migration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**migration_id** | **str** | Created migration ID | 
**status** | [**MigrationStatus**](MigrationStatus.md) | Current status | 
**validation_result** | [**ValidationResult**](ValidationResult.md) | Validation result if available | [optional] 
**created_at** | **datetime** | Creation timestamp | 
**message** | **str** | Human-readable message | 

## Example

```python
from mixpeek.models.create_migration_response import CreateMigrationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMigrationResponse from a JSON string
create_migration_response_instance = CreateMigrationResponse.from_json(json)
# print the JSON string representation of the object
print(CreateMigrationResponse.to_json())

# convert the object into a dict
create_migration_response_dict = create_migration_response_instance.to_dict()
# create an instance of CreateMigrationResponse from a dict
create_migration_response_from_dict = CreateMigrationResponse.from_dict(create_migration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


