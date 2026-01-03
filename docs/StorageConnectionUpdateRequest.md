# StorageConnectionUpdateRequest

Request payload for updating storage connection metadata.  Allows partial updates to connection metadata without changing credentials. Credentials can be updated via provider_config.  **What You Can Update:** - Connection name and description - Metadata tags - Status (active/suspended) - Provider credentials (via provider_config)  **Examples:** ```python # Update name and description {     \"name\": \"Updated Drive Name\",     \"description\": \"New description\" }  # Suspend connection {     \"status\": \"suspended\",     \"is_active\": False }  # Refresh credentials {     \"provider_config\": {         \"credentials\": {...}     } } ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | OPTIONAL. New name for the connection. Must be unique within the organization if provided. Format: 1-100 characters. | [optional] 
**description** | **str** | OPTIONAL. New description for the connection. Set to empty string to clear existing description. Format: Up to 500 characters. | [optional] 
**metadata** | **Dict[str, object]** | OPTIONAL. New metadata dictionary. Replaces existing metadata entirely (partial updates not supported). Set to empty dict {} to clear all metadata. | [optional] 
**status** | [**TaskStatusEnum**](TaskStatusEnum.md) | OPTIONAL. New operational status. ACTIVE: Connection is healthy and ready for use. SUSPENDED: Temporarily disabled, credentials preserved. FAILED: Health checks failing. ARCHIVED: Permanently retired (cannot be reactivated). | [optional] 
**is_active** | **bool** | OPTIONAL. Quick boolean flag for filtering. True when status is ACTIVE, False otherwise. Automatically maintained when status changes. | [optional] 
**provider_config** | **Dict[str, object]** | OPTIONAL. Updated provider configuration including credentials. Replaces entire provider_config (partial updates not supported). SECURITY: Sensitive fields are encrypted at rest. | [optional] 

## Example

```python
from mixpeek.models.storage_connection_update_request import StorageConnectionUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StorageConnectionUpdateRequest from a JSON string
storage_connection_update_request_instance = StorageConnectionUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(StorageConnectionUpdateRequest.to_json())

# convert the object into a dict
storage_connection_update_request_dict = storage_connection_update_request_instance.to_dict()
# create an instance of StorageConnectionUpdateRequest from a dict
storage_connection_update_request_from_dict = StorageConnectionUpdateRequest.from_dict(storage_connection_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


