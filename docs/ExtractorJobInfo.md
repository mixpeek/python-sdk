# ExtractorJobInfo

Tracking information for a single feature extractor job within a tier.  Each tier can have multiple extractor jobs running in parallel, one per unique feature_extractor_type. This allows different extractors to have independent: - Resource requirements (GPUs, CPU, memory) - Status tracking and retry logic - Ray job IDs and Celery task IDs - Completion times and performance metrics  Example:     Tier 1 with collections using different extractors:     - col_A: image_extractor     - col_B: face_identity_extractor     - col_C: image_extractor      Creates 2 ExtractorJobInfo instances:     1. extractor_type=\"image_extractor\", collection_ids=[\"col_A\", \"col_C\"]     2. extractor_type=\"face_identity_extractor\", collection_ids=[\"col_B\"]  Lifecycle:     1. Created with status=PENDING when tier is scheduled     2. Updated to IN_PROGRESS when Ray job starts     3. Finalized to COMPLETED/FAILED when Ray job completes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extractor_type** | **str** | Feature extractor type (e.g., &#39;image_extractor&#39;, &#39;face_identity_extractor&#39;) | 
**collection_ids** | **List[str]** | Collections processed by this extractor job | [optional] 
**ray_job_id** | **str** | Ray job ID for this extractor job | [optional] 
**celery_task_id** | **str** | Celery task ID that submitted this Ray job | [optional] 
**status** | [**TaskStatusEnum**](TaskStatusEnum.md) | Current status of this extractor job | [optional] 
**started_at** | **datetime** | When this extractor job started processing | [optional] 
**completed_at** | **datetime** | When this extractor job finished processing | [optional] 
**duration_ms** | **float** | Processing duration in milliseconds | [optional] 
**documents_written** | **int** | Number of documents written by this extractor job | [optional] 
**errors** | [**List[BatchErrorDetail]**](BatchErrorDetail.md) | Detailed errors from this extractor job | [optional] 

## Example

```python
from mixpeek.models.extractor_job_info import ExtractorJobInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ExtractorJobInfo from a JSON string
extractor_job_info_instance = ExtractorJobInfo.from_json(json)
# print the JSON string representation of the object
print(ExtractorJobInfo.to_json())

# convert the object into a dict
extractor_job_info_dict = extractor_job_info_instance.to_dict()
# create an instance of ExtractorJobInfo from a dict
extractor_job_info_from_dict = ExtractorJobInfo.from_dict(extractor_job_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


