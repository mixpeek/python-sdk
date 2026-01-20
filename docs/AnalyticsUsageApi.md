# mixpeek.AnalyticsUsageApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_usage_summary_analytics**](AnalyticsUsageApi.md#get_usage_summary_analytics) | **GET** /v1/analytics/usage/summary | Get Usage Summary


# **get_usage_summary_analytics**
> object get_usage_summary_analytics(start_date=start_date, end_date=end_date, authorization=authorization, x_namespace=x_namespace)

Get Usage Summary

Get usage summary for billing.

Returns usage statistics for the namespace including:
- Total API requests
- Compute usage (seconds)
- Storage usage (bytes)
- Total cost

**Time Range:**
- If both `start_date` and `end_date` are provided, uses that range
- If neither provided, defaults to last 30 days
- If only one provided, defaults to now as the other bound

**Example:**
```bash
GET /v1/analytics/usage/summary
GET /v1/analytics/usage/summary?start_date=2025-01-01T00:00:00Z&end_date=2025-01-31T23:59:59Z
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
    api_instance = mixpeek.AnalyticsUsageApi(api_client)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | Start date (UTC) (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime | End date (UTC) (optional)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Usage Summary
        api_response = api_instance.get_usage_summary_analytics(start_date=start_date, end_date=end_date, authorization=authorization, x_namespace=x_namespace)
        print("The response of AnalyticsUsageApi->get_usage_summary_analytics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsUsageApi->get_usage_summary_analytics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**| Start date (UTC) | [optional] 
 **end_date** | **datetime**| End date (UTC) | [optional] 
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

