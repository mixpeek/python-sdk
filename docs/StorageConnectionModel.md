# StorageConnectionModel

Canonical representation of an external storage provider connection.  Storage connections enable Mixpeek to access external cloud storage providers (Google Drive, S3, etc.) for automated file ingestion and synchronization. Each connection represents a configured integration with credentials, health monitoring, and usage tracking.  Lifecycle States:     - ACTIVE: Connection is healthy and ready for sync operations     - SUSPENDED: Temporarily disabled by user (credentials preserved)     - FAILED: Health checks failing (may need credential refresh)     - ARCHIVED: Permanently retired (cannot be reactivated)  Security:     - Sensitive credential fields are encrypted at rest using MongoDB       client-side field level encryption (CSFLE)     - Credentials never appear in API responses or logs     - Failed authentication attempts are logged in last_error     - Consecutive failures trigger automatic suspension  Use Cases:     - Connect to team Google Drive for document ingestion     - Sync files from customer S3 buckets     - Monitor and process uploaded media files     - Schedule periodic sync operations  Health Monitoring:     - Automatic health checks validate connectivity and credentials     - consecutive_failures tracks authentication/network issues     - Auto-disable after 5 consecutive failures to prevent lockout     - last_error stores diagnostic information for debugging

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_id** | **str** | Unique identifier for the storage connection. Auto-generated with &#39;conn_&#39; prefix followed by secure random token. Format: conn_{15-character alphanumeric}. Used for API operations and audit trails. | [optional] 
**internal_id** | **str** | REQUIRED. Organization internal identifier for multi-tenancy scoping. All connection operations are scoped to this organization. Format: int_{24-character secure token}. | 
**provider_type** | [**StorageProvider**](StorageProvider.md) | REQUIRED. Storage provider implementation to use. Determines which client adapter is loaded for sync operations. Supported: google_drive, s3, snowflake, sharepoint, tigris. | 
**provider_config** | [**ProviderConfig**](ProviderConfig.md) |  | 
**name** | **str** | REQUIRED. Human-readable connection name for identification. Displayed in dashboards, sync logs, and API responses. Must be unique within the organization for clarity. Format: 1-100 characters, descriptive of the connection&#39;s purpose. | 
**description** | **str** | NOT REQUIRED. Optional description explaining the connection&#39;s purpose and scope. Helpful for team collaboration and documentation. Format: Up to 500 characters. | [optional] 
**status** | [**TaskStatusEnum**](TaskStatusEnum.md) | Operational status of the connection. ACTIVE: Connection is healthy and ready for use in sync operations. SUSPENDED: Temporarily disabled by user, credentials preserved but sync paused. FAILED: Health checks failing, credentials may be invalid or expired. ARCHIVED: Permanently retired, cannot be reactivated. Status transitions automatically based on health checks and user actions. | [optional] 
**is_active** | **bool** | Quick boolean flag for filtering active connections in queries. True when status is ACTIVE, False for SUSPENDED/FAILED/ARCHIVED. Maintained automatically when status changes. Use for efficient filtering: db.connections.find({&#39;is_active&#39;: True}) | [optional] [default to True]
**last_used_at** | **datetime** | NOT REQUIRED. UTC timestamp of the most recent successful sync operation. Updated automatically after each successful file sync/list operation. None if connection has never been used. Useful for identifying stale connections and usage analytics. | [optional] 
**last_error** | **str** | NOT REQUIRED. Most recent error message from failed health check or sync. Populated when authentication fails, network errors occur, or permissions denied. None when connection is healthy. Format: Error message truncated to 1000 characters. Used for diagnostics and troubleshooting. | [optional] 
**consecutive_failures** | **int** | Counter tracking consecutive failed health checks or sync attempts. Incremented on each failure, reset to 0 on success. Used to implement automatic connection suspension. Auto-suspend after 5 consecutive failures to prevent account lockout. Range: 0 to infinity (typically 0-10). | [optional] [default to 0]
**created_at** | **datetime** | UTC timestamp when the connection was created. Auto-generated using shared.utilities.helpers.current_time(). Immutable after creation. Format: ISO 8601 datetime. | [optional] 
**updated_at** | **datetime** | UTC timestamp of the most recent update to the connection. Updated automatically on any field modification. Tracks configuration changes, status updates, and credential refreshes. Format: ISO 8601 datetime. | [optional] 
**created_by_user_id** | **str** | REQUIRED. User identifier of the user who created this connection. Used for audit trails and permission checks. Format: usr_{15-character alphanumeric}. Immutable after creation. | 
**metadata** | **Dict[str, object]** | Arbitrary key-value metadata provided by the user. Useful for tagging, categorization, and custom annotations. NOT REQUIRED - defaults to empty dictionary. Common uses: team tags, cost center codes, project identifiers. | [optional] 

## Example

```python
from mixpeek.models.storage_connection_model import StorageConnectionModel

# TODO update the JSON string below
json = "{}"
# create an instance of StorageConnectionModel from a JSON string
storage_connection_model_instance = StorageConnectionModel.from_json(json)
# print the JSON string representation of the object
print(StorageConnectionModel.to_json())

# convert the object into a dict
storage_connection_model_dict = storage_connection_model_instance.to_dict()
# create an instance of StorageConnectionModel from a dict
storage_connection_model_from_dict = StorageConnectionModel.from_dict(storage_connection_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


