# mixpeek.OrganizationConnectionsApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_storage_connection_organizations**](OrganizationConnectionsApi.md#create_storage_connection_organizations) | **POST** /v1/organizations/connections | Create Storage Connection
[**delete_storage_connection_organizations**](OrganizationConnectionsApi.md#delete_storage_connection_organizations) | **DELETE** /v1/organizations/connections/{connection_identifier} | Delete Storage Connection
[**get_storage_connection_organizations**](OrganizationConnectionsApi.md#get_storage_connection_organizations) | **GET** /v1/organizations/connections/{connection_identifier} | Get Storage Connection
[**list_google_drive_files_organizations_connections**](OrganizationConnectionsApi.md#list_google_drive_files_organizations_connections) | **GET** /v1/organizations/connections/{connection_identifier}/files | List Google Drive Files
[**list_google_drive_folders_organizations_connections**](OrganizationConnectionsApi.md#list_google_drive_folders_organizations_connections) | **GET** /v1/organizations/connections/{connection_identifier}/folders | List Google Drive Folders
[**list_storage_connections_organizations**](OrganizationConnectionsApi.md#list_storage_connections_organizations) | **POST** /v1/organizations/connections/list | List Storage Connections
[**test_storage_connection_organizations**](OrganizationConnectionsApi.md#test_storage_connection_organizations) | **POST** /v1/organizations/connections/{connection_identifier}/test | Test Storage Connection
[**update_storage_connection_organizations**](OrganizationConnectionsApi.md#update_storage_connection_organizations) | **PATCH** /v1/organizations/connections/{connection_identifier} | Update Storage Connection


# **create_storage_connection_organizations**
> StorageConnectionModel create_storage_connection_organizations(storage_connection_create_request, authorization=authorization)

Create Storage Connection

Create a new storage provider connection.

Establishes a connection to an external storage provider (Google Drive, S3, etc.)
for use in sync operations. Credentials are validated before saving unless
test_before_save is False.

**Use Cases:**
- Connect to team Google Drive for automated file ingestion
- Link customer S3 buckets for batch processing
- Set up storage connections for sync operations

**Security:**
- Requires ADMIN permission
- Credentials are encrypted at rest
- Connection is tested before saving (unless test_before_save=False)
- Audit log entry created for compliance

**Example:**
```bash
curl -X POST "http://localhost:8000/v1/organizations/connections" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Marketing Drive",
    "provider_type": "google_drive",
    "provider_config": {
      "credentials": {...},
      "shared_drive_id": "0AH-Xabc123"
    }
  }'
```

### Example


```python
import mixpeek
from mixpeek.models.storage_connection_create_request import StorageConnectionCreateRequest
from mixpeek.models.storage_connection_model import StorageConnectionModel
from mixpeek.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mixpeek.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mixpeek.Configuration(
    host = "https://api.mixpeek.com"
)


# Enter a context with an instance of the API client
with mixpeek.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mixpeek.OrganizationConnectionsApi(api_client)
    storage_connection_create_request = mixpeek.StorageConnectionCreateRequest() # StorageConnectionCreateRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Create Storage Connection
        api_response = api_instance.create_storage_connection_organizations(storage_connection_create_request, authorization=authorization)
        print("The response of OrganizationConnectionsApi->create_storage_connection_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationConnectionsApi->create_storage_connection_organizations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_connection_create_request** | [**StorageConnectionCreateRequest**](StorageConnectionCreateRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**StorageConnectionModel**](StorageConnectionModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_storage_connection_organizations**
> Dict[str, str] delete_storage_connection_organizations(connection_identifier, authorization=authorization)

Delete Storage Connection

Soft-delete a connection (mark archived).

Permanently retires a connection by marking it as ARCHIVED. The connection
cannot be reactivated after deletion. Credentials are preserved for audit
purposes but the connection is no longer usable.

**Example:**
```bash
curl -X DELETE "http://localhost:8000/v1/organizations/connections/conn_abc123" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Example


```python
import mixpeek
from mixpeek.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mixpeek.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mixpeek.Configuration(
    host = "https://api.mixpeek.com"
)


# Enter a context with an instance of the API client
with mixpeek.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mixpeek.OrganizationConnectionsApi(api_client)
    connection_identifier = 'connection_identifier_example' # str | Connection identifier - either connection ID (conn_...) or name. The system will automatically resolve names to IDs.
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Delete Storage Connection
        api_response = api_instance.delete_storage_connection_organizations(connection_identifier, authorization=authorization)
        print("The response of OrganizationConnectionsApi->delete_storage_connection_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationConnectionsApi->delete_storage_connection_organizations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_identifier** | **str**| Connection identifier - either connection ID (conn_...) or name. The system will automatically resolve names to IDs. | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

**Dict[str, str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storage_connection_organizations**
> StorageConnectionModel get_storage_connection_organizations(connection_identifier, authorization=authorization)

Get Storage Connection

Retrieve a storage connection by ID or name.

Returns connection metadata including name, provider type, status, and
health information. Credentials are automatically redacted from responses.

**Identifier Resolution:**
- If identifier starts with 'conn_', treated as connection ID
- Otherwise, treated as connection name

**Example:**
```bash
# By ID
curl -X GET "http://localhost:8000/v1/organizations/connections/conn_abc123" \
  -H "Authorization: Bearer YOUR_API_KEY"

# By name
curl -X GET "http://localhost:8000/v1/organizations/connections/Marketing%20Drive" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Example


```python
import mixpeek
from mixpeek.models.storage_connection_model import StorageConnectionModel
from mixpeek.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mixpeek.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mixpeek.Configuration(
    host = "https://api.mixpeek.com"
)


# Enter a context with an instance of the API client
with mixpeek.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mixpeek.OrganizationConnectionsApi(api_client)
    connection_identifier = 'connection_identifier_example' # str | Connection identifier - either connection ID (conn_...) or name. The system will automatically resolve names to IDs.
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Get Storage Connection
        api_response = api_instance.get_storage_connection_organizations(connection_identifier, authorization=authorization)
        print("The response of OrganizationConnectionsApi->get_storage_connection_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationConnectionsApi->get_storage_connection_organizations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_identifier** | **str**| Connection identifier - either connection ID (conn_...) or name. The system will automatically resolve names to IDs. | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**StorageConnectionModel**](StorageConnectionModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_google_drive_files_organizations_connections**
> Dict[str, object] list_google_drive_files_organizations_connections(connection_identifier, path=path, max_results=max_results, authorization=authorization)

List Google Drive Files

List files in Google Drive folder for preview.

Shows a preview of files in the selected folder when configuring sync operations.
Only available for Google Drive connections.

**Use Cases:**
- Preview files in a folder before selecting it for sync
- Verify folder contains expected files
- Check file types and counts

**Example:**
```bash
curl -X GET "http://localhost:8000/v1/organizations/connections/conn_abc123/files?path=/Marketing&max_results=20" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Example


```python
import mixpeek
from mixpeek.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mixpeek.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mixpeek.Configuration(
    host = "https://api.mixpeek.com"
)


# Enter a context with an instance of the API client
with mixpeek.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mixpeek.OrganizationConnectionsApi(api_client)
    connection_identifier = 'connection_identifier_example' # str | Connection identifier - either connection ID (conn_...) or name. The system will automatically resolve names to IDs.
    path = '/' # str | Folder path to list files from (optional) (default to '/')
    max_results = 50 # int | Maximum number of files to return (optional) (default to 50)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # List Google Drive Files
        api_response = api_instance.list_google_drive_files_organizations_connections(connection_identifier, path=path, max_results=max_results, authorization=authorization)
        print("The response of OrganizationConnectionsApi->list_google_drive_files_organizations_connections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationConnectionsApi->list_google_drive_files_organizations_connections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_identifier** | **str**| Connection identifier - either connection ID (conn_...) or name. The system will automatically resolve names to IDs. | 
 **path** | **str**| Folder path to list files from | [optional] [default to &#39;/&#39;]
 **max_results** | **int**| Maximum number of files to return | [optional] [default to 50]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_google_drive_folders_organizations_connections**
> ListFoldersResponse list_google_drive_folders_organizations_connections(connection_identifier, path=path, authorization=authorization)

List Google Drive Folders

List folders in Google Drive for folder selection in sync configuration.

Enables users to browse and select folders when configuring sync operations.
Only available for Google Drive connections.

**Use Cases:**
- Browse available folders for sync configuration
- Select source folder for bucket sync
- Navigate nested folder structures

**Example:**
```bash
curl -X GET "http://localhost:8000/v1/organizations/connections/conn_abc123/folders?path=/Marketing" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Example


```python
import mixpeek
from mixpeek.models.list_folders_response import ListFoldersResponse
from mixpeek.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mixpeek.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mixpeek.Configuration(
    host = "https://api.mixpeek.com"
)


# Enter a context with an instance of the API client
with mixpeek.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mixpeek.OrganizationConnectionsApi(api_client)
    connection_identifier = 'connection_identifier_example' # str | Connection identifier - either connection ID (conn_...) or name. The system will automatically resolve names to IDs.
    path = '/' # str | Parent folder path to list from (optional) (default to '/')
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # List Google Drive Folders
        api_response = api_instance.list_google_drive_folders_organizations_connections(connection_identifier, path=path, authorization=authorization)
        print("The response of OrganizationConnectionsApi->list_google_drive_folders_organizations_connections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationConnectionsApi->list_google_drive_folders_organizations_connections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_identifier** | **str**| Connection identifier - either connection ID (conn_...) or name. The system will automatically resolve names to IDs. | 
 **path** | **str**| Parent folder path to list from | [optional] [default to &#39;/&#39;]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**ListFoldersResponse**](ListFoldersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_storage_connections_organizations**
> StorageConnectionListResponse list_storage_connections_organizations(limit=limit, offset=offset, cursor=cursor, include_total=include_total, authorization=authorization, list_storage_connections_request=list_storage_connections_request)

List Storage Connections

List storage connections for the authenticated organization.

Returns paginated results with optional filters for provider type, status,
and active flag. Results are sorted by creation date (newest first).

**Use Cases:**
- List all active Google Drive connections
- Find failed connections that need attention
- Filter by provider type for sync configuration

**Example:**
```bash
curl -X POST "http://localhost:8000/v1/organizations/connections/list" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "provider_type": "google_drive",
    "is_active": true
  }'
```

### Example


```python
import mixpeek
from mixpeek.models.list_storage_connections_request import ListStorageConnectionsRequest
from mixpeek.models.storage_connection_list_response import StorageConnectionListResponse
from mixpeek.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mixpeek.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mixpeek.Configuration(
    host = "https://api.mixpeek.com"
)


# Enter a context with an instance of the API client
with mixpeek.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mixpeek.OrganizationConnectionsApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    cursor = 'cursor_example' # str |  (optional)
    include_total = False # bool |  (optional) (default to False)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    list_storage_connections_request = mixpeek.ListStorageConnectionsRequest() # ListStorageConnectionsRequest |  (optional)

    try:
        # List Storage Connections
        api_response = api_instance.list_storage_connections_organizations(limit=limit, offset=offset, cursor=cursor, include_total=include_total, authorization=authorization, list_storage_connections_request=list_storage_connections_request)
        print("The response of OrganizationConnectionsApi->list_storage_connections_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationConnectionsApi->list_storage_connections_organizations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **cursor** | **str**|  | [optional] 
 **include_total** | **bool**|  | [optional] [default to False]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **list_storage_connections_request** | [**ListStorageConnectionsRequest**](ListStorageConnectionsRequest.md)|  | [optional] 

### Return type

[**StorageConnectionListResponse**](StorageConnectionListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_storage_connection_organizations**
> StorageConnectionTestResponse test_storage_connection_organizations(connection_identifier, authorization=authorization)

Test Storage Connection

Perform a credential test against the external provider.

Validates that connection credentials are still valid and the provider
is accessible. Result is logged in audit trail.

**Use Cases:**
- Validate credentials before using in sync operations
- Diagnose connection issues
- Refresh credentials after expiration

**Example:**
```bash
curl -X POST "http://localhost:8000/v1/organizations/connections/conn_abc123/test" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Example


```python
import mixpeek
from mixpeek.models.storage_connection_test_response import StorageConnectionTestResponse
from mixpeek.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mixpeek.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mixpeek.Configuration(
    host = "https://api.mixpeek.com"
)


# Enter a context with an instance of the API client
with mixpeek.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mixpeek.OrganizationConnectionsApi(api_client)
    connection_identifier = 'connection_identifier_example' # str | Connection identifier - either connection ID (conn_...) or name. The system will automatically resolve names to IDs.
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Test Storage Connection
        api_response = api_instance.test_storage_connection_organizations(connection_identifier, authorization=authorization)
        print("The response of OrganizationConnectionsApi->test_storage_connection_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationConnectionsApi->test_storage_connection_organizations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_identifier** | **str**| Connection identifier - either connection ID (conn_...) or name. The system will automatically resolve names to IDs. | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**StorageConnectionTestResponse**](StorageConnectionTestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_storage_connection_organizations**
> StorageConnectionModel update_storage_connection_organizations(connection_identifier, storage_connection_update_request, authorization=authorization)

Update Storage Connection

Update connection metadata or credentials.

Allows partial updates to connection metadata without changing credentials.
Credentials can be updated via provider_config. All changes are logged
in audit trail.

**What You Can Update:**
- Connection name and description
- Metadata tags
- Status (active/suspended)
- Provider credentials (via provider_config)

**Example:**
```bash
curl -X PATCH "http://localhost:8000/v1/organizations/connections/conn_abc123" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Updated Drive Name",
    "status": "suspended"
  }'
```

### Example


```python
import mixpeek
from mixpeek.models.storage_connection_model import StorageConnectionModel
from mixpeek.models.storage_connection_update_request import StorageConnectionUpdateRequest
from mixpeek.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mixpeek.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mixpeek.Configuration(
    host = "https://api.mixpeek.com"
)


# Enter a context with an instance of the API client
with mixpeek.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mixpeek.OrganizationConnectionsApi(api_client)
    connection_identifier = 'connection_identifier_example' # str | Connection identifier - either connection ID (conn_...) or name. The system will automatically resolve names to IDs.
    storage_connection_update_request = mixpeek.StorageConnectionUpdateRequest() # StorageConnectionUpdateRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Update Storage Connection
        api_response = api_instance.update_storage_connection_organizations(connection_identifier, storage_connection_update_request, authorization=authorization)
        print("The response of OrganizationConnectionsApi->update_storage_connection_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationConnectionsApi->update_storage_connection_organizations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_identifier** | **str**| Connection identifier - either connection ID (conn_...) or name. The system will automatically resolve names to IDs. | 
 **storage_connection_update_request** | [**StorageConnectionUpdateRequest**](StorageConnectionUpdateRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**StorageConnectionModel**](StorageConnectionModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

