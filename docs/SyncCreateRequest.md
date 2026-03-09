# SyncCreateRequest

Request to create a bucket sync configuration.  Establishes automated synchronization between a storage connection and a bucket. The sync monitors the source path for changes and ingests files according to the specified mode and filters.  Supported Storage Providers:     - google_drive: Google Drive and Workspace shared drives     - s3: Amazon S3 and S3-compatible (MinIO, DigitalOcean Spaces, Wasabi)     - snowflake: Snowflake data warehouse tables (rows become objects)     - sharepoint: Microsoft SharePoint and OneDrive for Business     - tigris: Tigris globally distributed object storage  Robustness Features (built-in):     - Dead Letter Queue (DLQ): Failed objects tracked with 3 retries before quarantine     - Idempotent ingestion: Deduplication via (bucket_id, source_provider, source_object_id)     - Distributed locking: Prevents concurrent execution of same sync config     - Rate limit handling: Automatic backoff on provider 429 responses     - Metrics: Duration, files synced/failed, batches created, rate limit hits  Sync Modes:     - continuous: Real-time monitoring with polling interval     - one_time: Single bulk import then stops     - scheduled: Polling-based batch imports  Requirements:     - connection_id: REQUIRED, must be an existing connection     - source_path: REQUIRED, path must exist in the storage provider     - sync_mode: OPTIONAL, defaults to 'continuous'     - All other fields are OPTIONAL with sensible defaults

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_id** | **str** | REQUIRED. Storage connection identifier to sync from. Must reference an existing connection created via POST /organizations/connections. The connection defines the storage provider and credentials. Supported providers: google_drive, s3, snowflake, sharepoint, tigris. | 
**source_path** | **str** | REQUIRED. Source path within the storage provider to monitor and sync. Path format varies by provider: - s3/tigris: &#39;bucket-name/prefix&#39; or &#39;bucket-name&#39;. - google_drive: folder ID or path like &#39;/Marketing/Assets&#39;. - sharepoint: &#39;/sites/SiteName/Shared Documents/folder&#39;. - snowflake: &#39;DATABASE.SCHEMA.TABLE&#39; or just &#39;TABLE&#39; if defaults set. | 
**sync_mode** | [**SyncMode**](SyncMode.md) | Synchronization mode determining how files are monitored and ingested. OPTIONAL. Defaults to &#39;continuous&#39;. &#39;continuous&#39;: Actively monitors for new files and syncs immediately. &#39;one_time&#39;: Performs a single sync of existing files then stops. &#39;scheduled&#39;: Syncs on polling intervals only. | [optional] 
**file_filters** | **Dict[str, object]** | OPTIONAL. Filters to control which files are synced. When omitted, all files in source_path are synced. Supported filters: - include_patterns: Glob patterns to include (e.g., [&#39;*.mp4&#39;, &#39;*.mov&#39;]). - exclude_patterns: Glob patterns to exclude (e.g., [&#39;*.tmp&#39;, &#39;.DS_Store&#39;]). - extensions: File extensions to include (e.g., [&#39;.mp4&#39;, &#39;.jpg&#39;]). - min_size_bytes: Minimum file size in bytes. - max_size_bytes: Maximum file size in bytes. - modified_after: ISO datetime, only sync files modified after this time. - mime_types: List of MIME types to include (e.g., [&#39;video/*&#39;, &#39;image/jpeg&#39;]). | [optional] 
**schema_mapping** | [**SchemaMappingInput**](SchemaMappingInput.md) | OPTIONAL. Defines how source data maps to bucket schema fields and blobs. When provided, enables structured extraction of metadata from the sync source. Keys are target bucket schema field names, values define the source extraction method.   **Blob Mappings** (target_type&#x3D;&#39;blob&#39;): Map files or URLs to blob fields. Use source.type&#x3D;&#39;file&#39; for the synced file itself, or source.type&#x3D;&#39;column&#39;/&#39;metadata&#39; for URLs.   **Field Mappings** (target_type&#x3D;&#39;field&#39;): Map metadata to schema fields. Source options by provider: - S3/Tigris: &#39;tag&#39; (object tags), &#39;metadata&#39; (x-amz-meta-*) - Snowflake: &#39;column&#39; (table columns) - Google Drive: &#39;drive_property&#39; (file properties) - All: &#39;filename_regex&#39;, &#39;folder_path&#39;, &#39;constant&#39;   If omitted, default behavior depends on provider - typically maps file to &#39;content&#39; blob. | [optional] 
**polling_interval_seconds** | **int** | Interval in seconds between polling checks for new files. OPTIONAL. Defaults to 300 seconds (5 minutes). Must be between 30 and 900 seconds (0.5 to 15 minutes). Only applies to &#39;continuous&#39; and &#39;scheduled&#39; sync modes. Lower values mean faster detection but higher API usage. | [optional] [default to 300]
**batch_size** | **int** | Number of files to process in each batch during sync. OPTIONAL. Defaults to 50 files per batch. Must be between 1 and 100. Larger batches improve throughput but require more memory. Smaller batches provide more granular progress tracking. | [optional] [default to 50]
**skip_batch_submission** | **bool** | If True, sync objects to the bucket without creating or submitting batches for collection processing. Objects are created in the bucket but no tier processing is triggered. Useful for bulk data migration or when you want to manually control when processing occurs. OPTIONAL. Defaults to False (batches are created and submitted). | [optional] [default to False]
**metadata** | **Dict[str, object]** | Optional custom metadata to attach to the sync configuration. NOT REQUIRED. Arbitrary key-value pairs for tagging and organization. Common uses: project tags, environment labels, cost centers. Maximum 50 keys, values must be JSON-serializable. | [optional] 

## Example

```python
from mixpeek.models.sync_create_request import SyncCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SyncCreateRequest from a JSON string
sync_create_request_instance = SyncCreateRequest.from_json(json)
# print the JSON string representation of the object
print(SyncCreateRequest.to_json())

# convert the object into a dict
sync_create_request_dict = sync_create_request_instance.to_dict()
# create an instance of SyncCreateRequest from a dict
sync_create_request_from_dict = SyncCreateRequest.from_dict(sync_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


