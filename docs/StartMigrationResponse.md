# StartMigrationResponse

Response after starting a migration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**migration_id** | **str** | Migration ID | 
**status** | [**MigrationStatus**](MigrationStatus.md) | Current status | 
**task_id** | **str** | Celery task ID | 
**started_at** | **datetime** | Start timestamp | 
**message** | **str** | Human-readable message | 

## Example

```python
from mixpeek.models.start_migration_response import StartMigrationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StartMigrationResponse from a JSON string
start_migration_response_instance = StartMigrationResponse.from_json(json)
# print the JSON string representation of the object
print(StartMigrationResponse.to_json())

# convert the object into a dict
start_migration_response_dict = start_migration_response_instance.to_dict()
# create an instance of StartMigrationResponse from a dict
start_migration_response_from_dict = StartMigrationResponse.from_dict(start_migration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


