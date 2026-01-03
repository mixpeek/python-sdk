# mixpeek.NamespaceMigrationsApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_migration_namespaces**](NamespaceMigrationsApi.md#cancel_migration_namespaces) | **POST** /v1/namespaces/migrations/{migration_id}/cancel | Cancel Migration
[**create_migration_namespaces**](NamespaceMigrationsApi.md#create_migration_namespaces) | **POST** /v1/namespaces/migrations/ | Create Migration
[**delete_migration_namespaces**](NamespaceMigrationsApi.md#delete_migration_namespaces) | **DELETE** /v1/namespaces/migrations/{migration_id} | Delete Migration
[**get_migration_namespaces**](NamespaceMigrationsApi.md#get_migration_namespaces) | **GET** /v1/namespaces/migrations/{migration_id} | Get Migration
[**list_migrations_namespaces**](NamespaceMigrationsApi.md#list_migrations_namespaces) | **POST** /v1/namespaces/migrations/list | List Migrations
[**start_migration_namespaces**](NamespaceMigrationsApi.md#start_migration_namespaces) | **POST** /v1/namespaces/migrations/{migration_id}/start | Start Migration
[**validate_migration_namespaces**](NamespaceMigrationsApi.md#validate_migration_namespaces) | **POST** /v1/namespaces/migrations/validate | Validate Migration


# **cancel_migration_namespaces**
> CancelMigrationResponse cancel_migration_namespaces(migration_id, authorization=authorization, cancel_migration_request=cancel_migration_request)

Cancel Migration

Cancel a running migration.

Args:
    request: FastAPI request
    migration_id: Migration ID
    cancel_request: Cancellation options

Returns:
    CancelMigrationResponse with updated status

### Example


```python
import mixpeek
from mixpeek.models.cancel_migration_request import CancelMigrationRequest
from mixpeek.models.cancel_migration_response import CancelMigrationResponse
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
    api_instance = mixpeek.NamespaceMigrationsApi(api_client)
    migration_id = 'migration_id_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    cancel_migration_request = mixpeek.CancelMigrationRequest() # CancelMigrationRequest |  (optional)

    try:
        # Cancel Migration
        api_response = api_instance.cancel_migration_namespaces(migration_id, authorization=authorization, cancel_migration_request=cancel_migration_request)
        print("The response of NamespaceMigrationsApi->cancel_migration_namespaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NamespaceMigrationsApi->cancel_migration_namespaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **migration_id** | **str**|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **cancel_migration_request** | [**CancelMigrationRequest**](CancelMigrationRequest.md)|  | [optional] 

### Return type

[**CancelMigrationResponse**](CancelMigrationResponse.md)

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

# **create_migration_namespaces**
> CreateMigrationResponse create_migration_namespaces(create_migration_request, authorization=authorization)

Create Migration

Create a new namespace migration.

This endpoint creates a migration and optionally validates it.
Use start_immediately=True to begin execution immediately.

Args:
    request: FastAPI request
    create_request: Migration configuration

Returns:
    CreateMigrationResponse with migration ID and status

### Example


```python
import mixpeek
from mixpeek.models.create_migration_request import CreateMigrationRequest
from mixpeek.models.create_migration_response import CreateMigrationResponse
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
    api_instance = mixpeek.NamespaceMigrationsApi(api_client)
    create_migration_request = mixpeek.CreateMigrationRequest() # CreateMigrationRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Create Migration
        api_response = api_instance.create_migration_namespaces(create_migration_request, authorization=authorization)
        print("The response of NamespaceMigrationsApi->create_migration_namespaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NamespaceMigrationsApi->create_migration_namespaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_migration_request** | [**CreateMigrationRequest**](CreateMigrationRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**CreateMigrationResponse**](CreateMigrationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_migration_namespaces**
> delete_migration_namespaces(migration_id, authorization=authorization)

Delete Migration

Delete a migration record.

Only draft, completed, failed, or cancelled migrations can be deleted.

Args:
    request: FastAPI request
    migration_id: Migration ID

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
    api_instance = mixpeek.NamespaceMigrationsApi(api_client)
    migration_id = 'migration_id_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Delete Migration
        api_instance.delete_migration_namespaces(migration_id, authorization=authorization)
    except Exception as e:
        print("Exception when calling NamespaceMigrationsApi->delete_migration_namespaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **migration_id** | **str**|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_migration_namespaces**
> GetMigrationResponse get_migration_namespaces(migration_id, authorization=authorization)

Get Migration

Get migration details and status.

Args:
    request: FastAPI request
    migration_id: Migration ID

Returns:
    GetMigrationResponse with full migration details

### Example


```python
import mixpeek
from mixpeek.models.get_migration_response import GetMigrationResponse
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
    api_instance = mixpeek.NamespaceMigrationsApi(api_client)
    migration_id = 'migration_id_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Get Migration
        api_response = api_instance.get_migration_namespaces(migration_id, authorization=authorization)
        print("The response of NamespaceMigrationsApi->get_migration_namespaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NamespaceMigrationsApi->get_migration_namespaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **migration_id** | **str**|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**GetMigrationResponse**](GetMigrationResponse.md)

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

# **list_migrations_namespaces**
> ListMigrationsResponse list_migrations_namespaces(list_migrations_request, authorization=authorization)

List Migrations

List migrations with optional filters.

Args:
    request: FastAPI request
    list_request: Filter and pagination parameters

Returns:
    ListMigrationsResponse with migrations list

### Example


```python
import mixpeek
from mixpeek.models.list_migrations_request import ListMigrationsRequest
from mixpeek.models.list_migrations_response import ListMigrationsResponse
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
    api_instance = mixpeek.NamespaceMigrationsApi(api_client)
    list_migrations_request = mixpeek.ListMigrationsRequest() # ListMigrationsRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # List Migrations
        api_response = api_instance.list_migrations_namespaces(list_migrations_request, authorization=authorization)
        print("The response of NamespaceMigrationsApi->list_migrations_namespaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NamespaceMigrationsApi->list_migrations_namespaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_migrations_request** | [**ListMigrationsRequest**](ListMigrationsRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**ListMigrationsResponse**](ListMigrationsResponse.md)

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

# **start_migration_namespaces**
> StartMigrationResponse start_migration_namespaces(migration_id, authorization=authorization, start_migration_request=start_migration_request)

Start Migration

Start a migration execution.

Args:
    request: FastAPI request
    migration_id: Migration ID
    start_request: Start options

Returns:
    StartMigrationResponse with task ID

### Example


```python
import mixpeek
from mixpeek.models.start_migration_request import StartMigrationRequest
from mixpeek.models.start_migration_response import StartMigrationResponse
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
    api_instance = mixpeek.NamespaceMigrationsApi(api_client)
    migration_id = 'migration_id_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    start_migration_request = mixpeek.StartMigrationRequest() # StartMigrationRequest |  (optional)

    try:
        # Start Migration
        api_response = api_instance.start_migration_namespaces(migration_id, authorization=authorization, start_migration_request=start_migration_request)
        print("The response of NamespaceMigrationsApi->start_migration_namespaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NamespaceMigrationsApi->start_migration_namespaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **migration_id** | **str**|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **start_migration_request** | [**StartMigrationRequest**](StartMigrationRequest.md)|  | [optional] 

### Return type

[**StartMigrationResponse**](StartMigrationResponse.md)

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

# **validate_migration_namespaces**
> ValidateMigrationResponse validate_migration_namespaces(validate_migration_request, authorization=authorization)

Validate Migration

Validate a migration configuration without creating it.

Use this endpoint to check if a migration configuration is valid
before actually creating and running it.

Args:
    request: FastAPI request
    validate_request: Configuration to validate

Returns:
    ValidateMigrationResponse with validation results

### Example


```python
import mixpeek
from mixpeek.models.validate_migration_request import ValidateMigrationRequest
from mixpeek.models.validate_migration_response import ValidateMigrationResponse
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
    api_instance = mixpeek.NamespaceMigrationsApi(api_client)
    validate_migration_request = mixpeek.ValidateMigrationRequest() # ValidateMigrationRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Validate Migration
        api_response = api_instance.validate_migration_namespaces(validate_migration_request, authorization=authorization)
        print("The response of NamespaceMigrationsApi->validate_migration_namespaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NamespaceMigrationsApi->validate_migration_namespaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validate_migration_request** | [**ValidateMigrationRequest**](ValidateMigrationRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**ValidateMigrationResponse**](ValidateMigrationResponse.md)

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

