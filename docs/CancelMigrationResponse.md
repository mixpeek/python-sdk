# CancelMigrationResponse

Response after cancelling a migration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**migration_id** | **str** | Migration ID | 
**status** | [**MigrationStatus**](MigrationStatus.md) | Current status | 
**cancelled_at** | **datetime** | Cancellation timestamp | 
**message** | **str** | Human-readable message | 

## Example

```python
from mixpeek.models.cancel_migration_response import CancelMigrationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CancelMigrationResponse from a JSON string
cancel_migration_response_instance = CancelMigrationResponse.from_json(json)
# print the JSON string representation of the object
print(CancelMigrationResponse.to_json())

# convert the object into a dict
cancel_migration_response_dict = cancel_migration_response_instance.to_dict()
# create an instance of CancelMigrationResponse from a dict
cancel_migration_response_from_dict = CancelMigrationResponse.from_dict(cancel_migration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


