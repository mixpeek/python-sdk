# CancelMigrationRequest

Request to cancel a migration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | Cancellation reason | [optional] 

## Example

```python
from mixpeek.models.cancel_migration_request import CancelMigrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CancelMigrationRequest from a JSON string
cancel_migration_request_instance = CancelMigrationRequest.from_json(json)
# print the JSON string representation of the object
print(CancelMigrationRequest.to_json())

# convert the object into a dict
cancel_migration_request_dict = cancel_migration_request_instance.to_dict()
# create an instance of CancelMigrationRequest from a dict
cancel_migration_request_from_dict = CancelMigrationRequest.from_dict(cancel_migration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


