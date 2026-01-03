# mixpeek.BucketSyncsApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sync_configuration_buckets**](BucketSyncsApi.md#create_sync_configuration_buckets) | **POST** /v1/buckets/{bucket_id}/syncs | Create Sync Configuration
[**delete_sync_configuration_buckets_id_config**](BucketSyncsApi.md#delete_sync_configuration_buckets_id_config) | **DELETE** /v1/buckets/{bucket_id}/syncs/{sync_config_id} | Delete Sync Configuration
[**get_sync_configuration_buckets_id_config**](BucketSyncsApi.md#get_sync_configuration_buckets_id_config) | **GET** /v1/buckets/{bucket_id}/syncs/{sync_config_id} | Get Sync Configuration
[**list_sync_configurations_buckets**](BucketSyncsApi.md#list_sync_configurations_buckets) | **POST** /v1/buckets/{bucket_id}/syncs/list | List Sync Configurations
[**pause_sync_configuration_buckets_id_config**](BucketSyncsApi.md#pause_sync_configuration_buckets_id_config) | **POST** /v1/buckets/{bucket_id}/syncs/{sync_config_id}/pause | Pause Sync Configuration
[**resume_sync_configuration_buckets_id_config**](BucketSyncsApi.md#resume_sync_configuration_buckets_id_config) | **POST** /v1/buckets/{bucket_id}/syncs/{sync_config_id}/resume | Resume Sync Configuration
[**trigger_sync_configuration_buckets_id_config**](BucketSyncsApi.md#trigger_sync_configuration_buckets_id_config) | **POST** /v1/buckets/{bucket_id}/syncs/{sync_config_id}/trigger | Trigger Sync Configuration
[**update_sync_configuration_buckets_id_config**](BucketSyncsApi.md#update_sync_configuration_buckets_id_config) | **PATCH** /v1/buckets/{bucket_id}/syncs/{sync_config_id} | Update Sync Configuration


# **create_sync_configuration_buckets**
> SyncConfigurationModel create_sync_configuration_buckets(bucket_id, sync_create_request, authorization=authorization, x_namespace=x_namespace)

Create Sync Configuration

Create a sync configuration for automated storage ingestion.

Establishes automated synchronization between an external storage provider
and a Mixpeek bucket. The sync monitors the source path and ingests files
according to the specified mode and filters.

**Supported Providers:** google_drive, s3, snowflake, sharepoint, tigris

**Built-in Robustness:**
- Dead Letter Queue (DLQ): Failed objects tracked with 3 retries
- Idempotent ingestion: Deduplication prevents duplicate objects
- Distributed locking: Prevents concurrent sync execution
- Rate limit handling: Automatic backoff on 429 responses
- Metrics: Duration, files synced/failed, batches created

**Sync Modes:**
- `continuous`: Real-time monitoring with configurable polling interval
- `one_time`: Single bulk import, then sync stops
- `scheduled`: Polling-based batch imports at fixed intervals

### Example


```python
import mixpeek
from mixpeek.models.sync_configuration_model import SyncConfigurationModel
from mixpeek.models.sync_create_request import SyncCreateRequest
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
    api_instance = mixpeek.BucketSyncsApi(api_client)
    bucket_id = 'bucket_id_example' # str | 
    sync_create_request = mixpeek.SyncCreateRequest() # SyncCreateRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Create Sync Configuration
        api_response = api_instance.create_sync_configuration_buckets(bucket_id, sync_create_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of BucketSyncsApi->create_sync_configuration_buckets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketSyncsApi->create_sync_configuration_buckets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **str**|  | 
 **sync_create_request** | [**SyncCreateRequest**](SyncCreateRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**SyncConfigurationModel**](SyncConfigurationModel.md)

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

# **delete_sync_configuration_buckets_id_config**
> object delete_sync_configuration_buckets_id_config(bucket_id, sync_config_id, authorization=authorization, x_namespace=x_namespace)

Delete Sync Configuration

Delete a sync configuration.

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
    api_instance = mixpeek.BucketSyncsApi(api_client)
    bucket_id = 'bucket_id_example' # str | 
    sync_config_id = 'sync_config_id_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Delete Sync Configuration
        api_response = api_instance.delete_sync_configuration_buckets_id_config(bucket_id, sync_config_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of BucketSyncsApi->delete_sync_configuration_buckets_id_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketSyncsApi->delete_sync_configuration_buckets_id_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **str**|  | 
 **sync_config_id** | **str**|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

**object**

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

# **get_sync_configuration_buckets_id_config**
> SyncConfigurationModel get_sync_configuration_buckets_id_config(bucket_id, sync_config_id, authorization=authorization, x_namespace=x_namespace)

Get Sync Configuration

Fetch a sync configuration.

### Example


```python
import mixpeek
from mixpeek.models.sync_configuration_model import SyncConfigurationModel
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
    api_instance = mixpeek.BucketSyncsApi(api_client)
    bucket_id = 'bucket_id_example' # str | 
    sync_config_id = 'sync_config_id_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Sync Configuration
        api_response = api_instance.get_sync_configuration_buckets_id_config(bucket_id, sync_config_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of BucketSyncsApi->get_sync_configuration_buckets_id_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketSyncsApi->get_sync_configuration_buckets_id_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **str**|  | 
 **sync_config_id** | **str**|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**SyncConfigurationModel**](SyncConfigurationModel.md)

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

# **list_sync_configurations_buckets**
> SyncListResponse list_sync_configurations_buckets(bucket_id, limit=limit, offset=offset, cursor=cursor, include_total=include_total, authorization=authorization, x_namespace=x_namespace, list_sync_configurations_request=list_sync_configurations_request)

List Sync Configurations

List all sync configurations for a bucket with optional filtering.

Returns paginated list of sync configurations with status, metrics, and settings.
Use filters to find syncs by connection, status, or active state.

### Example


```python
import mixpeek
from mixpeek.models.list_sync_configurations_request import ListSyncConfigurationsRequest
from mixpeek.models.sync_list_response import SyncListResponse
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
    api_instance = mixpeek.BucketSyncsApi(api_client)
    bucket_id = 'bucket_id_example' # str | 
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    cursor = 'cursor_example' # str |  (optional)
    include_total = False # bool |  (optional) (default to False)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)
    list_sync_configurations_request = mixpeek.ListSyncConfigurationsRequest() # ListSyncConfigurationsRequest |  (optional)

    try:
        # List Sync Configurations
        api_response = api_instance.list_sync_configurations_buckets(bucket_id, limit=limit, offset=offset, cursor=cursor, include_total=include_total, authorization=authorization, x_namespace=x_namespace, list_sync_configurations_request=list_sync_configurations_request)
        print("The response of BucketSyncsApi->list_sync_configurations_buckets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketSyncsApi->list_sync_configurations_buckets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **str**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **cursor** | **str**|  | [optional] 
 **include_total** | **bool**|  | [optional] [default to False]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 
 **list_sync_configurations_request** | [**ListSyncConfigurationsRequest**](ListSyncConfigurationsRequest.md)|  | [optional] 

### Return type

[**SyncListResponse**](SyncListResponse.md)

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

# **pause_sync_configuration_buckets_id_config**
> SyncConfigurationModel pause_sync_configuration_buckets_id_config(bucket_id, sync_config_id, authorization=authorization, x_namespace=x_namespace)

Pause Sync Configuration

Pause a sync configuration.

Pauses the sync, preventing new sync jobs from executing.
Running jobs will complete but no new jobs will be scheduled.
The sync configuration and all settings are preserved.

**Note:** Use POST /resume to reactivate the sync.

### Example


```python
import mixpeek
from mixpeek.models.sync_configuration_model import SyncConfigurationModel
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
    api_instance = mixpeek.BucketSyncsApi(api_client)
    bucket_id = 'bucket_id_example' # str | 
    sync_config_id = 'sync_config_id_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Pause Sync Configuration
        api_response = api_instance.pause_sync_configuration_buckets_id_config(bucket_id, sync_config_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of BucketSyncsApi->pause_sync_configuration_buckets_id_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketSyncsApi->pause_sync_configuration_buckets_id_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **str**|  | 
 **sync_config_id** | **str**|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**SyncConfigurationModel**](SyncConfigurationModel.md)

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

# **resume_sync_configuration_buckets_id_config**
> SyncConfigurationModel resume_sync_configuration_buckets_id_config(bucket_id, sync_config_id, authorization=authorization, x_namespace=x_namespace)

Resume Sync Configuration

Resume a paused sync configuration.

Reactivates a paused sync, allowing new sync jobs to be scheduled.
For continuous syncs, polling will resume at the configured interval.
The next sync will be incremental (only files modified since last sync).

### Example


```python
import mixpeek
from mixpeek.models.sync_configuration_model import SyncConfigurationModel
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
    api_instance = mixpeek.BucketSyncsApi(api_client)
    bucket_id = 'bucket_id_example' # str | 
    sync_config_id = 'sync_config_id_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Resume Sync Configuration
        api_response = api_instance.resume_sync_configuration_buckets_id_config(bucket_id, sync_config_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of BucketSyncsApi->resume_sync_configuration_buckets_id_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketSyncsApi->resume_sync_configuration_buckets_id_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **str**|  | 
 **sync_config_id** | **str**|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**SyncConfigurationModel**](SyncConfigurationModel.md)

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

# **trigger_sync_configuration_buckets_id_config**
> object trigger_sync_configuration_buckets_id_config(bucket_id, sync_config_id, authorization=authorization, x_namespace=x_namespace)

Trigger Sync Configuration

Manually trigger a sync execution.

Creates a sync job and immediately dispatches it for async execution via Celery.
The sync job processes files from the storage provider and creates objects in the bucket.

**Execution Flow:**
1. Acquires distributed lock (prevents concurrent runs)
2. Iterates files from storage provider with configured filters
3. Creates objects idempotently (skips duplicates)
4. Failed objects go to Dead Letter Queue (3 retries)
5. Creates batches for collection processing (100 objects/batch)
6. Emits metrics and releases lock

**Use Cases:**
- Test sync configuration after creation
- Force sync outside of scheduled intervals
- Re-sync after updating connection credentials
- Trigger incremental sync (only modified files)

**Returns:** `sync_job_id` to track progress via GET /syncs/{id}

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
    api_instance = mixpeek.BucketSyncsApi(api_client)
    bucket_id = 'bucket_id_example' # str | 
    sync_config_id = 'sync_config_id_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Trigger Sync Configuration
        api_response = api_instance.trigger_sync_configuration_buckets_id_config(bucket_id, sync_config_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of BucketSyncsApi->trigger_sync_configuration_buckets_id_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketSyncsApi->trigger_sync_configuration_buckets_id_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **str**|  | 
 **sync_config_id** | **str**|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

**object**

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

# **update_sync_configuration_buckets_id_config**
> SyncConfigurationModel update_sync_configuration_buckets_id_config(bucket_id, sync_config_id, sync_update_request, authorization=authorization, x_namespace=x_namespace)

Update Sync Configuration

Update a sync configuration.

### Example


```python
import mixpeek
from mixpeek.models.sync_configuration_model import SyncConfigurationModel
from mixpeek.models.sync_update_request import SyncUpdateRequest
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
    api_instance = mixpeek.BucketSyncsApi(api_client)
    bucket_id = 'bucket_id_example' # str | 
    sync_config_id = 'sync_config_id_example' # str | 
    sync_update_request = mixpeek.SyncUpdateRequest() # SyncUpdateRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Update Sync Configuration
        api_response = api_instance.update_sync_configuration_buckets_id_config(bucket_id, sync_config_id, sync_update_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of BucketSyncsApi->update_sync_configuration_buckets_id_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketSyncsApi->update_sync_configuration_buckets_id_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **str**|  | 
 **sync_config_id** | **str**|  | 
 **sync_update_request** | [**SyncUpdateRequest**](SyncUpdateRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**SyncConfigurationModel**](SyncConfigurationModel.md)

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

