# mixpeek.OrganizationAuditApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_audit_log_organizations**](OrganizationAuditApi.md#get_audit_log_organizations) | **GET** /v1/organizations/audit/logs/{audit_id} | Get Audit Log
[**get_audit_settings_organizations**](OrganizationAuditApi.md#get_audit_settings_organizations) | **GET** /v1/organizations/audit/settings | Get Audit Settings
[**list_audit_logs_organizations**](OrganizationAuditApi.md#list_audit_logs_organizations) | **GET** /v1/organizations/audit/logs | List Audit Logs
[**update_audit_settings_organizations**](OrganizationAuditApi.md#update_audit_settings_organizations) | **PATCH** /v1/organizations/audit/settings | Update Audit Settings


# **get_audit_log_organizations**
> AuditEventResponse get_audit_log_organizations(audit_id, authorization=authorization)

Get Audit Log

Get a specific audit log entry by ID.

Requires ADMIN permission.

### Example


```python
import mixpeek
from mixpeek.models.audit_event_response import AuditEventResponse
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
    api_instance = mixpeek.OrganizationAuditApi(api_client)
    audit_id = 'audit_id_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Get Audit Log
        api_response = api_instance.get_audit_log_organizations(audit_id, authorization=authorization)
        print("The response of OrganizationAuditApi->get_audit_log_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationAuditApi->get_audit_log_organizations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audit_id** | **str**|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**AuditEventResponse**](AuditEventResponse.md)

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

# **get_audit_settings_organizations**
> AuditSettings get_audit_settings_organizations(authorization=authorization)

Get Audit Settings

Get current audit configuration for the organization.

Returns the audit settings including whether read auditing is enabled.
Requires ADMIN permission.

### Example


```python
import mixpeek
from mixpeek.models.audit_settings import AuditSettings
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
    api_instance = mixpeek.OrganizationAuditApi(api_client)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Get Audit Settings
        api_response = api_instance.get_audit_settings_organizations(authorization=authorization)
        print("The response of OrganizationAuditApi->get_audit_settings_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationAuditApi->get_audit_settings_organizations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**AuditSettings**](AuditSettings.md)

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

# **list_audit_logs_organizations**
> AuditEventListResponse list_audit_logs_organizations(resource_type=resource_type, resource_id=resource_id, actor_id=actor_id, action=action, start=start, end=end, skip=skip, limit=limit, authorization=authorization)

List Audit Logs

List organization audit logs with filtering and pagination.

Returns audit events for the organization, sorted by timestamp descending.
Requires ADMIN permission.

### Example


```python
import mixpeek
from mixpeek.models.audit_action import AuditAction
from mixpeek.models.audit_event_list_response import AuditEventListResponse
from mixpeek.models.resource_type_input import ResourceTypeInput
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
    api_instance = mixpeek.OrganizationAuditApi(api_client)
    resource_type = mixpeek.ResourceTypeInput() # ResourceTypeInput | Filter by resource type (optional)
    resource_id = 'resource_id_example' # str | Filter by resource ID (optional)
    actor_id = 'actor_id_example' # str | Filter by actor ID (optional)
    action = mixpeek.AuditAction() # AuditAction | Filter by action (optional)
    start = 'start_example' # str | ISO8601 start timestamp (optional)
    end = 'end_example' # str | ISO8601 end timestamp (optional)
    skip = 0 # int | Number of results to skip (optional) (default to 0)
    limit = 50 # int | Number of results to return (optional) (default to 50)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # List Audit Logs
        api_response = api_instance.list_audit_logs_organizations(resource_type=resource_type, resource_id=resource_id, actor_id=actor_id, action=action, start=start, end=end, skip=skip, limit=limit, authorization=authorization)
        print("The response of OrganizationAuditApi->list_audit_logs_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationAuditApi->list_audit_logs_organizations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_type** | [**ResourceTypeInput**](.md)| Filter by resource type | [optional] 
 **resource_id** | **str**| Filter by resource ID | [optional] 
 **actor_id** | **str**| Filter by actor ID | [optional] 
 **action** | [**AuditAction**](.md)| Filter by action | [optional] 
 **start** | **str**| ISO8601 start timestamp | [optional] 
 **end** | **str**| ISO8601 end timestamp | [optional] 
 **skip** | **int**| Number of results to skip | [optional] [default to 0]
 **limit** | **int**| Number of results to return | [optional] [default to 50]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**AuditEventListResponse**](AuditEventListResponse.md)

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

# **update_audit_settings_organizations**
> AuditSettings update_audit_settings_organizations(audit_settings_update_request, authorization=authorization)

Update Audit Settings

Update audit configuration for the organization.

Use this to enable or disable read auditing.
Requires ADMIN permission.

### Example


```python
import mixpeek
from mixpeek.models.audit_settings import AuditSettings
from mixpeek.models.audit_settings_update_request import AuditSettingsUpdateRequest
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
    api_instance = mixpeek.OrganizationAuditApi(api_client)
    audit_settings_update_request = mixpeek.AuditSettingsUpdateRequest() # AuditSettingsUpdateRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Update Audit Settings
        api_response = api_instance.update_audit_settings_organizations(audit_settings_update_request, authorization=authorization)
        print("The response of OrganizationAuditApi->update_audit_settings_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationAuditApi->update_audit_settings_organizations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audit_settings_update_request** | [**AuditSettingsUpdateRequest**](AuditSettingsUpdateRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**AuditSettings**](AuditSettings.md)

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

