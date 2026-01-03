# mixpeek.AnalyticsIndexesApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_field_usage_analytics_indexes**](AnalyticsIndexesApi.md#get_field_usage_analytics_indexes) | **GET** /v1/analytics/indexes/usage | Get Field Usage
[**get_index_suggestions_analytics_indexes**](AnalyticsIndexesApi.md#get_index_suggestions_analytics_indexes) | **GET** /v1/analytics/indexes/suggestions | Get Index Suggestions


# **get_field_usage_analytics_indexes**
> FieldUsageResponse get_field_usage_analytics_indexes(period=period, min_count=min_count, authorization=authorization, x_namespace=x_namespace)

Get Field Usage

Get usage statistics for all filtered fields.

### Example


```python
import mixpeek
from mixpeek.models.field_usage_response import FieldUsageResponse
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
    api_instance = mixpeek.AnalyticsIndexesApi(api_client)
    period = '24h' # str | Time period: Xh (hours) or Xd (days), e.g., 24h, 7d, 30d (optional) (default to '24h')
    min_count = 1 # int | Minimum query count to include a field (optional) (default to 1)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Field Usage
        api_response = api_instance.get_field_usage_analytics_indexes(period=period, min_count=min_count, authorization=authorization, x_namespace=x_namespace)
        print("The response of AnalyticsIndexesApi->get_field_usage_analytics_indexes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsIndexesApi->get_field_usage_analytics_indexes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **period** | **str**| Time period: Xh (hours) or Xd (days), e.g., 24h, 7d, 30d | [optional] [default to &#39;24h&#39;]
 **min_count** | **int**| Minimum query count to include a field | [optional] [default to 1]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**FieldUsageResponse**](FieldUsageResponse.md)

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

# **get_index_suggestions_analytics_indexes**
> IndexSuggestionsResponse get_index_suggestions_analytics_indexes(hours=hours, min_count=min_count, authorization=authorization, x_namespace=x_namespace)

Get Index Suggestions

Get index suggestions based on filter usage patterns.

### Example


```python
import mixpeek
from mixpeek.models.index_suggestions_response import IndexSuggestionsResponse
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
    api_instance = mixpeek.AnalyticsIndexesApi(api_client)
    hours = 24 # int | Time window in hours to analyze (max 30 days) (optional) (default to 24)
    min_count = 100 # int | Minimum query count threshold for suggestions (optional) (default to 100)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Index Suggestions
        api_response = api_instance.get_index_suggestions_analytics_indexes(hours=hours, min_count=min_count, authorization=authorization, x_namespace=x_namespace)
        print("The response of AnalyticsIndexesApi->get_index_suggestions_analytics_indexes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsIndexesApi->get_index_suggestions_analytics_indexes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hours** | **int**| Time window in hours to analyze (max 30 days) | [optional] [default to 24]
 **min_count** | **int**| Minimum query count threshold for suggestions | [optional] [default to 100]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**IndexSuggestionsResponse**](IndexSuggestionsResponse.md)

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

