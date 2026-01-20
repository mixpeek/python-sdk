# GetMigrationResponse

Response for getting migration details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**migration_id** | **str** | Migration ID | 
**internal_id** | **str** | Organization internal ID | 
**namespace_id** | **str** | Source namespace ID | 
**config** | [**MigrationConfig**](MigrationConfig.md) | Migration configuration | 
**status** | [**MigrationStatus**](MigrationStatus.md) | Current status | 
**progress** | [**MigrationProgress**](MigrationProgress.md) | Progress tracking | 
**validation_result** | [**ValidationResult**](ValidationResult.md) | Validation result | [optional] 
**dependency_graph** | [**DependencyGraph**](DependencyGraph.md) | Dependency graph | [optional] 
**task_id** | **str** | Celery task ID | [optional] 
**created_at** | **datetime** | Creation timestamp | 
**started_at** | **datetime** | Start timestamp | [optional] 
**completed_at** | **datetime** | Completion timestamp | [optional] 
**error_message** | **str** | Error if failed | [optional] 
**additional_data** | **object** | Additional metadata | [optional] 

## Example

```python
from mixpeek.models.get_migration_response import GetMigrationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMigrationResponse from a JSON string
get_migration_response_instance = GetMigrationResponse.from_json(json)
# print the JSON string representation of the object
print(GetMigrationResponse.to_json())

# convert the object into a dict
get_migration_response_dict = get_migration_response_instance.to_dict()
# create an instance of GetMigrationResponse from a dict
get_migration_response_from_dict = GetMigrationResponse.from_dict(get_migration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


