# StorageConnectionCreateRequest

Request payload for creating a new storage connection.  Use this to connect Mixpeek to external storage providers like Google Drive or S3. The connection will be tested before being saved (unless test_before_save is False).  **Use Cases:** - Connect to team Google Drive for automated file ingestion - Link customer S3 buckets for batch processing - Set up storage connections for sync operations  **Security:** - Credentials are encrypted at rest using MongoDB field-level encryption - Credentials never appear in API responses or logs - Connection is tested before saving to validate credentials  **Examples:** ```python # Google Drive connection {     \"name\": \"Marketing Drive\",     \"provider_type\": \"google_drive\",     \"provider_config\": {         \"credentials\": {...},         \"shared_drive_id\": \"0AH-Xabc123\"     },     \"description\": \"Team drive for marketing assets\" } ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | REQUIRED. Human-readable name for the storage connection. Must be unique within the organization. Displayed in dashboards and sync logs. Format: 1-100 characters, descriptive of the connection&#39;s purpose. | 
**provider_type** | [**StorageProvider**](StorageProvider.md) | REQUIRED. Storage provider to connect to. Supported providers: google_drive, s3, snowflake, sharepoint, tigris. Determines which authentication and sync logic is used. | 
**provider_config** | **object** | REQUIRED. Provider-specific configuration including credentials. Structure varies by provider_type. SECURITY: Sensitive credential fields (private_key, secret_access_key, client_secret, refresh_token, session_token) are automatically encrypted at rest and never appear in responses or logs. | 
**description** | **str** | OPTIONAL. Description explaining the connection&#39;s purpose and scope. Helpful for team collaboration and documentation. Format: Up to 500 characters. | [optional] 
**metadata** | **object** | OPTIONAL. Arbitrary key-value metadata for tagging and categorization. Common uses: team tags, cost center codes, project identifiers. | [optional] 
**test_before_save** | **bool** | OPTIONAL. Whether to validate credentials before saving the connection. Defaults to True. If True, connection will be tested against the provider before creation. If False, connection is saved without validation (use with caution). | [optional] [default to True]

## Example

```python
from mixpeek.models.storage_connection_create_request import StorageConnectionCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StorageConnectionCreateRequest from a JSON string
storage_connection_create_request_instance = StorageConnectionCreateRequest.from_json(json)
# print the JSON string representation of the object
print(StorageConnectionCreateRequest.to_json())

# convert the object into a dict
storage_connection_create_request_dict = storage_connection_create_request_instance.to_dict()
# create an instance of StorageConnectionCreateRequest from a dict
storage_connection_create_request_from_dict = StorageConnectionCreateRequest.from_dict(storage_connection_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


