# ListStorageConnectionsRequest

Request payload for listing storage connections with filters.  Use this to filter connections by provider type, status, or active flag. Results are paginated automatically.  **Use Cases:** - List all active Google Drive connections - Find failed connections that need attention - Filter by provider type for sync configuration  **Examples:** ```python # List all active Google Drive connections {     \"provider_type\": \"google_drive\",     \"is_active\": True }  # Find failed connections {     \"status\": \"failed\" } ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_type** | [**StorageProvider**](StorageProvider.md) | OPTIONAL. Filter connections by provider type. Supported: google_drive, s3, snowflake, sharepoint, tigris. If not provided, returns connections of all types. | [optional] 
**status** | [**TaskStatusEnum**](TaskStatusEnum.md) | OPTIONAL. Filter connections by operational status. ACTIVE: Healthy and ready for use. SUSPENDED: Temporarily disabled. FAILED: Health checks failing. ARCHIVED: Permanently retired. | [optional] 
**is_active** | **bool** | OPTIONAL. Filter by active flag. True: Returns only active connections (status&#x3D;ACTIVE). False: Returns only inactive connections (SUSPENDED/FAILED/ARCHIVED). If not provided, returns connections of all active states. | [optional] 

## Example

```python
from mixpeek.models.list_storage_connections_request import ListStorageConnectionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListStorageConnectionsRequest from a JSON string
list_storage_connections_request_instance = ListStorageConnectionsRequest.from_json(json)
# print the JSON string representation of the object
print(ListStorageConnectionsRequest.to_json())

# convert the object into a dict
list_storage_connections_request_dict = list_storage_connections_request_instance.to_dict()
# create an instance of ListStorageConnectionsRequest from a dict
list_storage_connections_request_from_dict = ListStorageConnectionsRequest.from_dict(list_storage_connections_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


