# TaskResponse

Task response model returned by the API.  Extends TaskModel with additional convenience fields for API responses. This is the model returned when you GET /v1/tasks/{task_id}.  Additional Fields:     error_message: Convenience field that surfaces errors from additional_data                   for easier error handling in client code.  Inheritance:     Inherits all fields and documentation from TaskModel, including:     - task_id: Unique identifier     - task_type: Operation type     - status: Current status     - inputs: Input parameters     - outputs: Output results     - additional_data: Metadata and context  Storage Architecture:     Same as TaskModel - stored in Redis (24hr TTL) with MongoDB fallback.  Usage:     This model is automatically returned by task API endpoints. You don't     need to construct it manually - just call GET /v1/tasks/{task_id}.  Error Handling:     Check the error_message field for a user-friendly error string, or     additional_data['error'] for the full error details.  Example Response:     {         \"task_id\": \"task_abc123\",         \"task_type\": \"api_buckets_batches_process\",         \"status\": \"FAILED\",         \"inputs\": [\"batch_xyz\"],         \"outputs\": null,         \"additional_data\": {             \"error\": \"Failed to process batch: Object not found\",             \"batch_id\": \"batch_xyz\"         },         \"error_message\": \"Failed to process batch: Object not found\"     }

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** | Unique identifier for the task. REQUIRED. Used to poll task status via GET /v1/tasks/{task_id}. This ID is also stored on parent resources (batches, clusters, etc.) for cross-referencing. Format: UUID v4 or custom string identifier. | 
**task_type** | [**TaskType**](TaskType.md) | Type of operation this task represents. REQUIRED. Identifies the specific async operation being performed. Used for filtering and categorizing tasks. Common types: api_buckets_batches_process, engine_cluster_build, api_taxonomies_execute. See TaskType enum for complete list of supported operations. | 
**status** | [**TaskStatusEnum**](TaskStatusEnum.md) | Current status of the task. REQUIRED. Indicates the current state of the async operation. Terminal statuses (COMPLETED, FAILED, CANCELED) indicate the task has finished and will not change. Active statuses (PENDING, IN_PROGRESS, PROCESSING) indicate the task is still running and should be polled. Use this field to determine when to stop polling. | 
**inputs** | [**List[TaskResponseInputsInner]**](TaskResponseInputsInner.md) | Input parameters or data used to start the task. OPTIONAL. May include IDs, configuration objects, or file references. Useful for debugging and understanding what data the task processed. Format: List of strings (IDs) or objects (configuration). Example: [&#39;batch_id_123&#39;] or [{&#39;bucket_id&#39;: &#39;bkt_abc&#39;, &#39;config&#39;: {...}}] | [optional] 
**outputs** | [**List[TaskResponseInputsInner]**](TaskResponseInputsInner.md) | Output results produced by the task. OPTIONAL. Populated when task completes successfully. May include processed file IDs, result metrics, or status summaries. Check this field after task reaches COMPLETED status to get results. Format: List of strings (output IDs) or objects (result data). | [optional] 
**additional_data** | **object** | Additional metadata and context for the task. OPTIONAL. Contains job IDs, error details, progress info, and other task-specific metadata.   Common fields (all task types): - &#39;error&#39;: Error message if task failed - &#39;job_id&#39;: Ray job ID for engine tasks - &#39;from_mongodb&#39;: True if retrieved from MongoDB fallback (not Redis)   Batch-specific fields (task_type&#x3D;api_buckets_batches_process): - &#39;batch_id&#39;: Batch identifier (REQUIRED) - &#39;bucket_id&#39;: Source bucket identifier (REQUIRED) - &#39;namespace_id&#39;: Namespace identifier (REQUIRED) - &#39;current_tier&#39;: Currently processing tier number, 0-indexed (OPTIONAL, None if not started) - &#39;total_tiers&#39;: Total number of tiers in the batch pipeline (REQUIRED) - &#39;collection_ids&#39;: Array of ALL collection IDs across all tiers (REQUIRED) - &#39;object_count&#39;: Number of objects being processed (REQUIRED) - &#39;sample_object_ids&#39;: First 5 object IDs for debugging/display (OPTIONAL)   Performance Note: Full object_ids array is NOT stored in task metadata to avoid bloating task documents (batches with 10k+ objects would add 200KB+ per task). For full object list, query the batch directly via GET /v1/buckets/{bucket_id}/batches/{batch_id}.   Note: For detailed per-tier status, use GET /v1/buckets/{bucket_id}/batches/{batch_id} to access the tier_tasks[] array which contains individual tier statuses, collection_ids, and timestamps for each tier. | [optional] 
**error** | **str** | Flattened error message for convenient error handling. OPTIONAL. Automatically populated from additional_data[&#39;error&#39;] when the task has FAILED status. This is a convenience field - the full error details are always available in additional_data[&#39;error&#39;]. Use this field for displaying errors to users or logging. Will be None if task has not failed or if no error details are available. Serialized as &#39;error&#39; in API responses for backward compatibility. | [optional] 

## Example

```python
from mixpeek.models.task_response import TaskResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TaskResponse from a JSON string
task_response_instance = TaskResponse.from_json(json)
# print the JSON string representation of the object
print(TaskResponse.to_json())

# convert the object into a dict
task_response_dict = task_response_instance.to_dict()
# create an instance of TaskResponse from a dict
task_response_from_dict = TaskResponse.from_dict(task_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


