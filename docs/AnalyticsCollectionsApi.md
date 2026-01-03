# mixpeek.AnalyticsCollectionsApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_collection_overview_analytics**](AnalyticsCollectionsApi.md#get_collection_overview_analytics) | **GET** /v1/analytics/collections/{collection_id}/overview | Get Collection Overview
[**get_document_growth_analytics**](AnalyticsCollectionsApi.md#get_document_growth_analytics) | **GET** /v1/analytics/collections/{collection_id}/growth | Get Document Growth
[**get_extractor_performance_analytics**](AnalyticsCollectionsApi.md#get_extractor_performance_analytics) | **GET** /v1/analytics/collections/{collection_id}/extractors | Get Extractor Performance
[**get_failure_analysis_analytics**](AnalyticsCollectionsApi.md#get_failure_analysis_analytics) | **GET** /v1/analytics/collections/{collection_id}/failures | Get Failure Analysis
[**get_latency_metrics_analytics**](AnalyticsCollectionsApi.md#get_latency_metrics_analytics) | **GET** /v1/analytics/collections/{collection_id}/latency | Get Latency Metrics


# **get_collection_overview_analytics**
> CollectionOverviewResponse get_collection_overview_analytics(collection_id, authorization=authorization, x_namespace=x_namespace)

Get Collection Overview

Get high-level collection health and status metrics.

Provides collection health including:
- Total document count and recent growth
- Processing performance and success rates
- Active enrichments (taxonomies, clusters)

**Use Cases:**
- Monitor collection health
- Quick status check
- Identify collections needing attention

### Example


```python
import mixpeek
from mixpeek.models.collection_overview_response import CollectionOverviewResponse
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
    api_instance = mixpeek.AnalyticsCollectionsApi(api_client)
    collection_id = 'collection_id_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Collection Overview
        api_response = api_instance.get_collection_overview_analytics(collection_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of AnalyticsCollectionsApi->get_collection_overview_analytics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsCollectionsApi->get_collection_overview_analytics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**CollectionOverviewResponse**](CollectionOverviewResponse.md)

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

# **get_document_growth_analytics**
> GrowthMetricsResponse get_document_growth_analytics(collection_id, start_date=start_date, end_date=end_date, group_by=group_by, authorization=authorization, x_namespace=x_namespace)

Get Document Growth

Get document growth trends over time.

Tracks document additions over time, useful for understanding
batch processing patterns and indexing velocity.

### Example


```python
import mixpeek
from mixpeek.models.growth_metrics_response import GrowthMetricsResponse
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
    api_instance = mixpeek.AnalyticsCollectionsApi(api_client)
    collection_id = 'collection_id_example' # str | 
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    group_by = 'day' # str | hour, day, week, month (optional) (default to 'day')
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Document Growth
        api_response = api_instance.get_document_growth_analytics(collection_id, start_date=start_date, end_date=end_date, group_by=group_by, authorization=authorization, x_namespace=x_namespace)
        print("The response of AnalyticsCollectionsApi->get_document_growth_analytics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsCollectionsApi->get_document_growth_analytics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**|  | 
 **start_date** | **datetime**|  | [optional] 
 **end_date** | **datetime**|  | [optional] 
 **group_by** | **str**| hour, day, week, month | [optional] [default to &#39;day&#39;]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**GrowthMetricsResponse**](GrowthMetricsResponse.md)

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

# **get_extractor_performance_analytics**
> ExtractorPerformanceResponse get_extractor_performance_analytics(collection_id, hours=hours, authorization=authorization, x_namespace=x_namespace)

Get Extractor Performance

Get feature extractor performance breakdown.

Analyzes extractor execution metrics including:
- Execution counts and success/failure rates
- Latency percentiles (P95, P99)
- Total processing time

**Use Cases:**
- Identify slow extractors for optimization
- Monitor extraction success rates
- Understanding processing bottlenecks

### Example


```python
import mixpeek
from mixpeek.models.extractor_performance_response import ExtractorPerformanceResponse
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
    api_instance = mixpeek.AnalyticsCollectionsApi(api_client)
    collection_id = 'collection_id_example' # str | 
    hours = 24 # int |  (optional) (default to 24)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Extractor Performance
        api_response = api_instance.get_extractor_performance_analytics(collection_id, hours=hours, authorization=authorization, x_namespace=x_namespace)
        print("The response of AnalyticsCollectionsApi->get_extractor_performance_analytics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsCollectionsApi->get_extractor_performance_analytics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**|  | 
 **hours** | **int**|  | [optional] [default to 24]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**ExtractorPerformanceResponse**](ExtractorPerformanceResponse.md)

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

# **get_failure_analysis_analytics**
> ApiAnalyticsCollectionsModelsFailureAnalysisResponse get_failure_analysis_analytics(collection_id, hours=hours, authorization=authorization, x_namespace=x_namespace)

Get Failure Analysis

Get failure analysis metrics.

Debug processing failures including:
- Error distribution by type
- Recent error messages
- Failure patterns

**Use Cases:**
- Debug processing failures
- Identify common error patterns
- Track error trends

### Example


```python
import mixpeek
from mixpeek.models.api_analytics_collections_models_failure_analysis_response import ApiAnalyticsCollectionsModelsFailureAnalysisResponse
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
    api_instance = mixpeek.AnalyticsCollectionsApi(api_client)
    collection_id = 'collection_id_example' # str | 
    hours = 72 # int |  (optional) (default to 72)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Failure Analysis
        api_response = api_instance.get_failure_analysis_analytics(collection_id, hours=hours, authorization=authorization, x_namespace=x_namespace)
        print("The response of AnalyticsCollectionsApi->get_failure_analysis_analytics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsCollectionsApi->get_failure_analysis_analytics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**|  | 
 **hours** | **int**|  | [optional] [default to 72]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**ApiAnalyticsCollectionsModelsFailureAnalysisResponse**](ApiAnalyticsCollectionsModelsFailureAnalysisResponse.md)

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

# **get_latency_metrics_analytics**
> LatencyResponse get_latency_metrics_analytics(collection_id, hours=hours, group_by=group_by, authorization=authorization, x_namespace=x_namespace)

Get Latency Metrics

Get processing latency distribution.

Analyzes document processing latency including:
- Latency percentiles over time
- Slowest document operations
- Performance trends

### Example


```python
import mixpeek
from mixpeek.models.latency_response import LatencyResponse
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
    api_instance = mixpeek.AnalyticsCollectionsApi(api_client)
    collection_id = 'collection_id_example' # str | 
    hours = 24 # int |  (optional) (default to 24)
    group_by = 'hour' # str |  (optional) (default to 'hour')
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Latency Metrics
        api_response = api_instance.get_latency_metrics_analytics(collection_id, hours=hours, group_by=group_by, authorization=authorization, x_namespace=x_namespace)
        print("The response of AnalyticsCollectionsApi->get_latency_metrics_analytics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsCollectionsApi->get_latency_metrics_analytics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**|  | 
 **hours** | **int**|  | [optional] [default to 24]
 **group_by** | **str**|  | [optional] [default to &#39;hour&#39;]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**LatencyResponse**](LatencyResponse.md)

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

