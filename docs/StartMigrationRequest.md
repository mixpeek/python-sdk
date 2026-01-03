# StartMigrationRequest

Request to start a migration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**force** | **bool** | Force start even if validation warnings exist | [optional] [default to False]

## Example

```python
from mixpeek.models.start_migration_request import StartMigrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StartMigrationRequest from a JSON string
start_migration_request_instance = StartMigrationRequest.from_json(json)
# print the JSON string representation of the object
print(StartMigrationRequest.to_json())

# convert the object into a dict
start_migration_request_dict = start_migration_request_instance.to_dict()
# create an instance of StartMigrationRequest from a dict
start_migration_request_from_dict = StartMigrationRequest.from_dict(start_migration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


