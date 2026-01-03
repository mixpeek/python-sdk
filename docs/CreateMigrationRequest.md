# CreateMigrationRequest

Request to create a new migration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**MigrationConfig**](MigrationConfig.md) | Migration configuration | 
**start_immediately** | **bool** | Start execution immediately after validation | [optional] [default to False]

## Example

```python
from mixpeek.models.create_migration_request import CreateMigrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMigrationRequest from a JSON string
create_migration_request_instance = CreateMigrationRequest.from_json(json)
# print the JSON string representation of the object
print(CreateMigrationRequest.to_json())

# convert the object into a dict
create_migration_request_dict = create_migration_request_instance.to_dict()
# create an instance of CreateMigrationRequest from a dict
create_migration_request_from_dict = CreateMigrationRequest.from_dict(create_migration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


