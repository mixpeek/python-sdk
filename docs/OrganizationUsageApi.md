# mixpeek.OrganizationUsageApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_key_breakdown_organizations_id_usage_endpoints**](OrganizationUsageApi.md#get_key_breakdown_organizations_id_usage_endpoints) | **GET** /v1/organizations/api-keys/{key_id}/usage/endpoints | Get Api Key Endpoint Breakdown
[**get_key_usage_organizations**](OrganizationUsageApi.md#get_key_usage_organizations) | **GET** /v1/organizations/api-keys/{key_id}/usage | Get Api Key Usage
[**get_org_usage_organizations**](OrganizationUsageApi.md#get_org_usage_organizations) | **GET** /v1/organizations/usage | Get Org Usage


# **get_key_breakdown_organizations_id_usage_endpoints**
> List[object] get_key_breakdown_organizations_id_usage_endpoints(key_id, start=start, end=end, authorization=authorization)

Get Api Key Endpoint Breakdown

Return endpoint-level usage metrics for a specific API key.

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
    api_instance = mixpeek.OrganizationUsageApi(api_client)
    key_id = 'key_id_example' # str | 
    start = 'start_example' # str | ISO8601 start timestamp (optional)
    end = 'end_example' # str | ISO8601 end timestamp (optional)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Get Api Key Endpoint Breakdown
        api_response = api_instance.get_key_breakdown_organizations_id_usage_endpoints(key_id, start=start, end=end, authorization=authorization)
        print("The response of OrganizationUsageApi->get_key_breakdown_organizations_id_usage_endpoints:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationUsageApi->get_key_breakdown_organizations_id_usage_endpoints: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**|  | 
 **start** | **str**| ISO8601 start timestamp | [optional] 
 **end** | **str**| ISO8601 end timestamp | [optional] 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

**List[object]**

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

# **get_key_usage_organizations**
> object get_key_usage_organizations(key_id, start=start, end=end, authorization=authorization)

Get Api Key Usage

Return usage metrics for a specific API key.

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
    api_instance = mixpeek.OrganizationUsageApi(api_client)
    key_id = 'key_id_example' # str | 
    start = 'start_example' # str | ISO8601 start timestamp (optional)
    end = 'end_example' # str | ISO8601 end timestamp (optional)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Get Api Key Usage
        api_response = api_instance.get_key_usage_organizations(key_id, start=start, end=end, authorization=authorization)
        print("The response of OrganizationUsageApi->get_key_usage_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationUsageApi->get_key_usage_organizations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**|  | 
 **start** | **str**| ISO8601 start timestamp | [optional] 
 **end** | **str**| ISO8601 end timestamp | [optional] 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

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

# **get_org_usage_organizations**
> object get_org_usage_organizations(start=start, end=end, authorization=authorization)

Get Org Usage

Return aggregated usage for the organization.

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
    api_instance = mixpeek.OrganizationUsageApi(api_client)
    start = 'start_example' # str | ISO8601 start timestamp (optional)
    end = 'end_example' # str | ISO8601 end timestamp (optional)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Get Org Usage
        api_response = api_instance.get_org_usage_organizations(start=start, end=end, authorization=authorization)
        print("The response of OrganizationUsageApi->get_org_usage_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationUsageApi->get_org_usage_organizations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **str**| ISO8601 start timestamp | [optional] 
 **end** | **str**| ISO8601 end timestamp | [optional] 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

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

