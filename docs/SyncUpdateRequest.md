# SyncUpdateRequest

Request to update an existing sync configuration.  Allows partial updates to sync settings without recreating the configuration. All fields are optional - only provided fields will be updated.  Use Cases:     - Pause/resume syncs by toggling is_active     - Adjust polling intervals based on activity patterns     - Update batch sizes for performance tuning     - Add metadata tags for organization  Requirements:     - All fields are OPTIONAL     - At least one field should be provided for the update     - Changes take effect on the next sync cycle

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Optional human-readable description of the sync configuration. NOT REQUIRED. Used for documentation and UI display. Maximum 500 characters. | [optional] 
**metadata** | **object** | Optional custom metadata to replace existing metadata. NOT REQUIRED. Completely replaces existing metadata (not merged). Use for tagging, categorization, or custom attributes. Maximum 50 keys, values must be JSON-serializable. | [optional] 
**status** | [**TaskStatusEnum**](TaskStatusEnum.md) | Optional status to set for the sync configuration. NOT REQUIRED. Valid values: &#39;pending&#39;, &#39;processing&#39;, &#39;completed&#39;, &#39;failed&#39;, &#39;paused&#39;. Typically managed automatically but can be manually overridden. Use pause/resume endpoints instead for active control. | [optional] 
**is_active** | **bool** | Optional flag to enable or disable the sync configuration. NOT REQUIRED. When False, sync will not process new files. Prefer using the /pause and /resume endpoints for clarity. Changes take effect immediately. | [optional] 
**polling_interval_seconds** | **int** | Optional new polling interval in seconds. NOT REQUIRED. Must be between 30 and 900 seconds if provided. Only applies to &#39;continuous&#39; and &#39;scheduled&#39; sync modes. Lower values increase responsiveness but API usage. | [optional] 
**batch_size** | **int** | Optional new batch size for file processing. NOT REQUIRED. Must be between 1 and 100 if provided. Larger batches improve throughput but use more memory. Changes apply to subsequent batches only. | [optional] 
**schema_mapping** | [**SchemaMappingInput**](SchemaMappingInput.md) | Optional schema mapping to replace existing mapping. NOT REQUIRED. Completely replaces existing schema_mapping (not merged). Defines how source data maps to bucket schema fields and blobs. See SyncCreateRequest.schema_mapping for detailed documentation. | [optional] 
**skip_batch_submission** | **bool** | If True, sync objects to the bucket without creating or submitting batches for collection processing. Objects are created in the bucket but no tier processing is triggered. NOT REQUIRED. When omitted, existing value is preserved. | [optional] 

## Example

```python
from mixpeek.models.sync_update_request import SyncUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SyncUpdateRequest from a JSON string
sync_update_request_instance = SyncUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(SyncUpdateRequest.to_json())

# convert the object into a dict
sync_update_request_dict = sync_update_request_instance.to_dict()
# create an instance of SyncUpdateRequest from a dict
sync_update_request_from_dict = SyncUpdateRequest.from_dict(sync_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


