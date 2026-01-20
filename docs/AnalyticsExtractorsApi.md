# mixpeek.AnalyticsExtractorsApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_extractor_performance_analytics**](AnalyticsExtractorsApi.md#get_extractor_performance_analytics) | **GET** /v1/analytics/extractors/performance | Get Extractor Performance


# **get_extractor_performance_analytics**
> List[object] get_extractor_performance_analytics(extractor_name=extractor_name, hours=hours, authorization=authorization, x_namespace=x_namespace)

Get Extractor Performance

Get feature extraction performance metrics.

Returns performance metrics for feature extractors including:
- Total executions per extractor
- Average duration
- P95/P99 latencies
- Success/failure rates

**Example:**
```bash
GET /v1/analytics/extractors/performance?hours=24
GET /v1/analytics/extractors/performance?extractor_name=text_extractor&hours=168
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
    api_instance = mixpeek.AnalyticsExtractorsApi(api_client)
    extractor_name = 'extractor_name_example' # str | Filter by extractor (optional)
    hours = 24 # int | Hours of history (optional) (default to 24)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Extractor Performance
        api_response = api_instance.get_extractor_performance_analytics(extractor_name=extractor_name, hours=hours, authorization=authorization, x_namespace=x_namespace)
        print("The response of AnalyticsExtractorsApi->get_extractor_performance_analytics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsExtractorsApi->get_extractor_performance_analytics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extractor_name** | **str**| Filter by extractor | [optional] 
 **hours** | **int**| Hours of history | [optional] [default to 24]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

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

