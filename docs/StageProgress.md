# StageProgress

Progress tracking for a migration stage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stage** | [**MigrationStage**](MigrationStage.md) | Stage name | 
**status** | [**MigrationStatus**](MigrationStatus.md) | Stage status | 
**started_at** | **datetime** | Stage start time | [optional] 
**completed_at** | **datetime** | Stage completion time | [optional] 
**progress_percent** | **float** | Progress % | [optional] [default to 0.0]
**items_total** | **int** | Total items to process | [optional] [default to 0]
**items_completed** | **int** | Items completed | [optional] [default to 0]
**items_failed** | **int** | Items failed | [optional] [default to 0]
**error_message** | **str** | Error if failed | [optional] 

## Example

```python
from mixpeek.models.stage_progress import StageProgress

# TODO update the JSON string below
json = "{}"
# create an instance of StageProgress from a JSON string
stage_progress_instance = StageProgress.from_json(json)
# print the JSON string representation of the object
print(StageProgress.to_json())

# convert the object into a dict
stage_progress_dict = stage_progress_instance.to_dict()
# create an instance of StageProgress from a dict
stage_progress_from_dict = StageProgress.from_dict(stage_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


