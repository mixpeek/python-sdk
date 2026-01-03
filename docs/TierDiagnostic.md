# TierDiagnostic

Diagnostic information for a single tier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tier_num** | **int** | Tier number | 
**task_id** | **str** | Task ID for this tier | [optional] 
**status** | **str** | Tier status (PENDING, PROCESSING, COMPLETED, FAILED) | 
**started_at** | **datetime** | When tier started | [optional] 
**completed_at** | **datetime** | When tier completed | [optional] 
**duration_seconds** | **float** | Duration in seconds | [optional] 
**progress** | [**TaskProgress**](TaskProgress.md) | Progress information | [optional] 
**ray_job_id** | **str** | Ray job ID | [optional] 
**ray_dashboard_url** | **str** | Link to Ray dashboard | [optional] 
**error** | **str** | Error message if failed | [optional] 
**error_type** | **str** | Error type if failed | [optional] 

## Example

```python
from mixpeek.models.tier_diagnostic import TierDiagnostic

# TODO update the JSON string below
json = "{}"
# create an instance of TierDiagnostic from a JSON string
tier_diagnostic_instance = TierDiagnostic.from_json(json)
# print the JSON string representation of the object
print(TierDiagnostic.to_json())

# convert the object into a dict
tier_diagnostic_dict = tier_diagnostic_instance.to_dict()
# create an instance of TierDiagnostic from a dict
tier_diagnostic_from_dict = TierDiagnostic.from_dict(tier_diagnostic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


