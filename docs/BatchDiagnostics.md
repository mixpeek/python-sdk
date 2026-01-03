# BatchDiagnostics

Comprehensive batch diagnostics response.  Combines batch status, task progress, collection info, and performance insights into a single response for easy frontend rendering.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_id** | **str** | Batch ID | 
**batch_name** | **str** | Batch name | 
**status** | **str** | Overall batch status | 
**bucket_id** | **str** | Source bucket ID | 
**current_tier** | **int** | Current tier being processed | [optional] [default to 0]
**total_tiers** | **int** | Total number of tiers | [optional] [default to 1]
**overall_progress** | **float** | Overall progress percentage (0-100) | [optional] [default to 0.0]
**created_at** | **datetime** | When batch was created | [optional] 
**submitted_at** | **datetime** | When batch was submitted | [optional] 
**started_at** | **datetime** | When processing started | [optional] 
**completed_at** | **datetime** | When processing completed | [optional] 
**duration_seconds** | **float** | Total duration in seconds | [optional] 
**estimated_completion** | **datetime** | Estimated completion time | [optional] 
**tiers** | [**List[TierDiagnostic]**](TierDiagnostic.md) | Diagnostic info for each tier | [optional] 
**collections** | [**List[CollectionDiagnostic]**](CollectionDiagnostic.md) | Status of target collections | [optional] 
**performance_summary** | **Dict[str, object]** | Performance metrics summary (available after completion) | [optional] 
**insights** | [**List[PerformanceInsight]**](PerformanceInsight.md) | Performance insights and recommendations | [optional] 
**has_failures** | **bool** | Whether batch has any failures | [optional] [default to False]
**failed_tier_count** | **int** | Number of failed tiers | [optional] [default to 0]
**total_objects** | **int** | Total objects in batch | [optional] [default to 0]
**next_actions** | **List[str]** | Recommended next steps for user | [optional] 

## Example

```python
from mixpeek.models.batch_diagnostics import BatchDiagnostics

# TODO update the JSON string below
json = "{}"
# create an instance of BatchDiagnostics from a JSON string
batch_diagnostics_instance = BatchDiagnostics.from_json(json)
# print the JSON string representation of the object
print(BatchDiagnostics.to_json())

# convert the object into a dict
batch_diagnostics_dict = batch_diagnostics_instance.to_dict()
# create an instance of BatchDiagnostics from a dict
batch_diagnostics_from_dict = BatchDiagnostics.from_dict(batch_diagnostics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


