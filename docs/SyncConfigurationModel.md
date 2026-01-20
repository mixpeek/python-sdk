# SyncConfigurationModel

Bucket-scoped configuration for automated storage synchronization.  Defines how files are synced from external storage providers to a Mixpeek bucket. Includes configuration, status, metrics, and robustness control fields.  **Supported Providers:** google_drive, s3, snowflake, sharepoint, tigris  **Built-in Robustness:** - Distributed locking (locked_by_worker_id, lock_expires_at) - Pause/resume control (paused, pause_reason, paused_at) - Safety limits (max_objects_per_run, batch_chunk_size) - Resume checkpointing (resume_cursor, resume_objects_processed) - Batch tracking (batch_ids, task_ids, batches_created)  **Metrics Fields:** - total_files_discovered: Files found in source - total_files_synced: Successfully synced files - total_files_failed: Files that failed (check DLQ) - total_bytes_synced: Total data transferred - consecutive_failures: Failure count for auto-suspend

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sync_config_id** | **str** | Unique identifier for the sync configuration. | [optional] 
**bucket_id** | **str** | Target bucket identifier (e.g. &#39;bkt_marketing_assets&#39;). | 
**connection_id** | **str** | Storage connection identifier (e.g. &#39;conn_abc123&#39;). | 
**internal_id** | **str** | Organization internal identifier (multi-tenancy scope). | 
**namespace_id** | **str** | Namespace identifier owning the bucket. | 
**source_path** | **str** | Source path in the external storage provider. Format varies by provider: s3/tigris&#x3D;&#39;bucket/prefix&#39;, google_drive&#x3D;&#39;folder_id&#39;, sharepoint&#x3D;&#39;/sites/Name/Documents&#39;, snowflake&#x3D;&#39;DB.SCHEMA.TABLE&#39;. | 
**file_filters** | [**FileFilters**](FileFilters.md) | Optional filter rules limiting which files are synced. | [optional] 
**schema_mapping** | [**SchemaMappingOutput**](SchemaMappingOutput.md) | Schema mapping defining how source data maps to bucket schema fields. Maps external storage attributes (tags, metadata, columns, filenames) to bucket schema fields and blob properties. When provided, enables structured extraction of metadata from the sync source. See SchemaMapping for detailed configuration options. | [optional] 
**sync_mode** | [**SyncMode**](SyncMode.md) | Sync mode controlling lifecycle (initial_only or continuous). | [optional] 
**polling_interval_seconds** | **int** | Polling interval in seconds (continuous mode). | [optional] [default to 300]
**batch_size** | **int** | Number of files processed per sync batch. | [optional] [default to 50]
**create_object_on_confirm** | **bool** | Whether objects should be created immediately after confirmation. | [optional] [default to True]
**skip_duplicates** | **bool** | Skip files whose hashes already exist in the bucket. | [optional] [default to True]
**skip_batch_submission** | **bool** | If True, sync objects to the bucket without creating/submitting batches for processing. | [optional] [default to False]
**status** | [**TaskStatusEnum**](TaskStatusEnum.md) | Current lifecycle status for the sync configuration. PENDING: Not yet started. ACTIVE: Currently running/polling. SUSPENDED: Temporarily paused. COMPLETED: Initial sync completed (for initial_only mode). FAILED: Sync encountered errors. | [optional] 
**is_active** | **bool** | Convenience flag used for filtering active syncs. | [optional] [default to True]
**total_files_discovered** | **int** | Cumulative count of files found in source across all runs. | [optional] [default to 0]
**total_files_synced** | **int** | Cumulative count of successfully synced files. | [optional] [default to 0]
**total_files_failed** | **int** | Cumulative count of failed files (sent to DLQ after 3 retries). | [optional] [default to 0]
**total_bytes_synced** | **int** | Cumulative bytes transferred across all runs. | [optional] [default to 0]
**created_at** | **datetime** | When sync configuration was created. | [optional] 
**updated_at** | **datetime** | Last modification timestamp. | [optional] 
**last_sync_at** | **datetime** | When last successful sync completed. Used for incremental syncs. | [optional] 
**next_sync_at** | **datetime** | Scheduled time for next sync (continuous/scheduled modes). | [optional] 
**created_by_user_id** | **str** | User identifier that created the sync configuration. | 
**last_error** | **str** | Most recent error message if sync attempts failed. | [optional] 
**consecutive_failures** | **int** |  | [optional] [default to 0]
**metadata** | **object** | Arbitrary metadata supplied by the user. | [optional] 
**locked_by_worker_id** | **str** | Worker ID that currently holds the lock for this sync | [optional] 
**locked_at** | **datetime** | Timestamp when lock was acquired | [optional] 
**lock_expires_at** | **datetime** | Timestamp when lock expires (for stale lock recovery) | [optional] 
**paused** | **bool** | Whether sync is currently paused (user-controlled) | [optional] [default to False]
**pause_reason** | **str** | Reason for pause | [optional] 
**paused_at** | **datetime** | Timestamp when paused | [optional] 
**paused_by_user_id** | **str** | User who paused the sync | [optional] 
**max_objects_per_run** | **int** | Hard cap on objects per sync run (prevents runaway syncs) | [optional] [default to 100000]
**max_batch_chunk_size** | **int** | Maximum objects per batch chunk | [optional] [default to 1000]
**batch_chunk_size** | **int** | Number of objects per batch chunk (for concurrent processing) | [optional] [default to 100]
**current_sync_run_id** | **str** | UUID for current/last sync run | [optional] 
**sync_run_counter** | **int** | Increments on each sync execution | [optional] [default to 0]
**batch_ids** | **List[str]** | List of batch IDs created by this sync | [optional] 
**task_ids** | **List[str]** | List of task IDs for batches | [optional] 
**batches_created** | **int** | Total number of batches created | [optional] [default to 0]
**resume_enabled** | **bool** | Whether resuming partial runs is enabled | [optional] [default to True]
**resume_cursor** | **str** | Last page/cursor processed (for paginated APIs like Google Drive) | [optional] 
**resume_last_primary_key** | **str** | Last primary key processed (for database syncs with stable ordering) | [optional] 
**resume_objects_processed** | **int** | Count of objects processed in current/last run | [optional] [default to 0]
**resume_checkpoint_frequency** | **int** | How often to checkpoint (in objects). Default: every 1000 objects | [optional] [default to 1000]

## Example

```python
from mixpeek.models.sync_configuration_model import SyncConfigurationModel

# TODO update the JSON string below
json = "{}"
# create an instance of SyncConfigurationModel from a JSON string
sync_configuration_model_instance = SyncConfigurationModel.from_json(json)
# print the JSON string representation of the object
print(SyncConfigurationModel.to_json())

# convert the object into a dict
sync_configuration_model_dict = sync_configuration_model_instance.to_dict()
# create an instance of SyncConfigurationModel from a dict
sync_configuration_model_from_dict = SyncConfigurationModel.from_dict(sync_configuration_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


