# MigrationProgress

Overall progress tracking for a migration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**overall_status** | [**MigrationStatus**](MigrationStatus.md) | Overall migration status | 
**overall_progress_percent** | **float** | Overall progress % | [optional] [default to 0.0]
**current_stage** | [**MigrationStage**](MigrationStage.md) | Currently executing stage | [optional] 
**stages** | [**List[StageProgress]**](StageProgress.md) | Progress for each stage | [optional] 
**resources** | [**List[ResourceProgress]**](ResourceProgress.md) | Progress for each resource | [optional] 
**started_at** | **datetime** | Migration start time | [optional] 
**estimated_completion** | **datetime** | Estimated completion time | [optional] 

## Example

```python
from mixpeek.models.migration_progress import MigrationProgress

# TODO update the JSON string below
json = "{}"
# create an instance of MigrationProgress from a JSON string
migration_progress_instance = MigrationProgress.from_json(json)
# print the JSON string representation of the object
print(MigrationProgress.to_json())

# convert the object into a dict
migration_progress_dict = migration_progress_instance.to_dict()
# create an instance of MigrationProgress from a dict
migration_progress_from_dict = MigrationProgress.from_dict(migration_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


