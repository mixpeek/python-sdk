# mixpeek.AnalyticsRetrieversApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyze_for_tuning_analytics_retrievers**](AnalyticsRetrieversApi.md#analyze_for_tuning_analytics_retrievers) | **POST** /v1/analytics/retrievers/{retriever_id}/analyze-tuning | Analyze For Tuning
[**get_cache_performance_analytics_retrievers**](AnalyticsRetrieversApi.md#get_cache_performance_analytics_retrievers) | **GET** /v1/analytics/retrievers/{retriever_id}/cache-performance | Get Cache Performance
[**get_retriever_performance_analytics**](AnalyticsRetrieversApi.md#get_retriever_performance_analytics) | **GET** /v1/analytics/retrievers/{retriever_id}/performance | Get Retriever Performance
[**get_retriever_signals_analytics**](AnalyticsRetrieversApi.md#get_retriever_signals_analytics) | **GET** /v1/analytics/retrievers/{retriever_id}/signals | Get Retriever Signals
[**get_slowest_queries_analytics_retrievers_id_slow**](AnalyticsRetrieversApi.md#get_slowest_queries_analytics_retrievers_id_slow) | **GET** /v1/analytics/retrievers/{retriever_id}/slow-queries | Get Slowest Queries
[**get_stage_breakdown_analytics_retrievers**](AnalyticsRetrieversApi.md#get_stage_breakdown_analytics_retrievers) | **GET** /v1/analytics/retrievers/{retriever_id}/stages | Get Stage Breakdown


# **analyze_for_tuning_analytics_retrievers**
> InteractionTuningResponse analyze_for_tuning_analytics_retrievers(retriever_id, days=days, authorization=authorization, x_namespace=x_namespace)

Analyze For Tuning

Analyze retriever and generate tuning recommendations.

Performs comprehensive analysis and generates actionable recommendations:
- Parameter tuning suggestions
- Cache optimization opportunities
- Performance improvement estimates

**Recommendations Include:**
- Increase/decrease k value
- Adjust reranking thresholds
- Enable/optimize caching
- Stage reordering suggestions

**Use Cases:**
- Initial retriever configuration
- Periodic performance optimization
- A/B testing parameter changes
- Cost optimization

**Example:**
```bash
curl -X POST "https://api.mixpeek.com/v1/analytics/retrievers/ret_abc123/analyze-tuning?days=7" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "X-Namespace: your-namespace"
```

### Example


```python
import mixpeek
from mixpeek.models.interaction_tuning_response import InteractionTuningResponse
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
    api_instance = mixpeek.AnalyticsRetrieversApi(api_client)
    retriever_id = 'retriever_id_example' # str | 
    days = 7 # int | Days of history to analyze (optional) (default to 7)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Analyze For Tuning
        api_response = api_instance.analyze_for_tuning_analytics_retrievers(retriever_id, days=days, authorization=authorization, x_namespace=x_namespace)
        print("The response of AnalyticsRetrieversApi->analyze_for_tuning_analytics_retrievers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsRetrieversApi->analyze_for_tuning_analytics_retrievers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retriever_id** | **str**|  | 
 **days** | **int**| Days of history to analyze | [optional] [default to 7]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**InteractionTuningResponse**](InteractionTuningResponse.md)

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

# **get_cache_performance_analytics_retrievers**
> CachePerformanceResponse get_cache_performance_analytics_retrievers(retriever_id, hours=hours, authorization=authorization, x_namespace=x_namespace)

Get Cache Performance

Get cache performance metrics.

Analyzes cache effectiveness including:
- Hit/miss rates
- Latency comparison (cache vs full search)
- Hourly cache performance trends

**Use Cases:**
- Evaluate cache effectiveness
- Optimize cache TTL settings
- Monitor cache performance
- Identify cache warming opportunities

**Example:**
```bash
curl -X GET "https://api.mixpeek.com/v1/analytics/retrievers/ret_abc123/cache-performance?hours=168" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "X-Namespace: your-namespace"
```

### Example


```python
import mixpeek
from mixpeek.models.cache_performance_response import CachePerformanceResponse
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
    api_instance = mixpeek.AnalyticsRetrieversApi(api_client)
    retriever_id = 'retriever_id_example' # str | 
    hours = 24 # int | Hours of history (optional) (default to 24)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Cache Performance
        api_response = api_instance.get_cache_performance_analytics_retrievers(retriever_id, hours=hours, authorization=authorization, x_namespace=x_namespace)
        print("The response of AnalyticsRetrieversApi->get_cache_performance_analytics_retrievers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsRetrieversApi->get_cache_performance_analytics_retrievers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retriever_id** | **str**|  | 
 **hours** | **int**| Hours of history | [optional] [default to 24]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**CachePerformanceResponse**](CachePerformanceResponse.md)

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

# **get_retriever_performance_analytics**
> RetrieverPerformanceResponse get_retriever_performance_analytics(retriever_id, start_date=start_date, end_date=end_date, group_by=group_by, authorization=authorization, x_namespace=x_namespace)

Get Retriever Performance

Get retriever performance metrics for tuning.

Retrieves time-series performance data including:
- Query latency (P50, P95, P99)
- Query counts
- Result counts
- Latency trends

**Use Cases:**
- Monitor retriever performance over time
- Identify performance degradations
- Compare performance across time periods
- Establish performance baselines

**Example:**
```bash
curl -X GET "https://api.mixpeek.com/v1/analytics/retrievers/ret_abc123/performance?hours=24&group_by=hour" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "X-Namespace: your-namespace"
```

### Example


```python
import mixpeek
from mixpeek.models.retriever_performance_response import RetrieverPerformanceResponse
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
    api_instance = mixpeek.AnalyticsRetrieversApi(api_client)
    retriever_id = 'retriever_id_example' # str | 
    start_date = '2013-10-20T19:20:30+01:00' # datetime | Start date (UTC) (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime | End date (UTC) (optional)
    group_by = 'hour' # str | Time grouping: hour, day, week (optional) (default to 'hour')
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Retriever Performance
        api_response = api_instance.get_retriever_performance_analytics(retriever_id, start_date=start_date, end_date=end_date, group_by=group_by, authorization=authorization, x_namespace=x_namespace)
        print("The response of AnalyticsRetrieversApi->get_retriever_performance_analytics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsRetrieversApi->get_retriever_performance_analytics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retriever_id** | **str**|  | 
 **start_date** | **datetime**| Start date (UTC) | [optional] 
 **end_date** | **datetime**| End date (UTC) | [optional] 
 **group_by** | **str**| Time grouping: hour, day, week | [optional] [default to &#39;hour&#39;]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**RetrieverPerformanceResponse**](RetrieverPerformanceResponse.md)

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

# **get_retriever_signals_analytics**
> List[RetrieverSignal] get_retriever_signals_analytics(retriever_id, signal_type=signal_type, limit=limit, hours=hours, authorization=authorization, x_namespace=x_namespace)

Get Retriever Signals

Get retriever signals for interaction tuning.

Retrieves fine-grained signals about retriever behavior:
- Cache hits/misses
- Reranking scores
- Filter effectiveness
- Query expansion results

**Signal Types:**
- `cache_hit`: Successful cache lookups
- `cache_miss`: Cache misses requiring full search
- `rerank_scores`: Reranking effectiveness metrics
- `filter_reduction`: Pre-filter document reduction
- `expansion_results`: Query expansion impact

**Use Cases:**
- Fine-tune retrieval parameters
- Analyze query patterns
- Optimize cache strategies
- Validate optimization improvements

**Example:**
```bash
curl -X GET "https://api.mixpeek.com/v1/analytics/retrievers/ret_abc123/signals?signal_type=rerank_scores&limit=50" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "X-Namespace: your-namespace"
```

### Example


```python
import mixpeek
from mixpeek.models.retriever_signal import RetrieverSignal
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
    api_instance = mixpeek.AnalyticsRetrieversApi(api_client)
    retriever_id = 'retriever_id_example' # str | 
    signal_type = 'signal_type_example' # str | Filter by signal type (cache_hit, rerank_scores, etc.) (optional)
    limit = 100 # int | Maximum results (optional) (default to 100)
    hours = 24 # int | Hours of history (optional) (default to 24)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Retriever Signals
        api_response = api_instance.get_retriever_signals_analytics(retriever_id, signal_type=signal_type, limit=limit, hours=hours, authorization=authorization, x_namespace=x_namespace)
        print("The response of AnalyticsRetrieversApi->get_retriever_signals_analytics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsRetrieversApi->get_retriever_signals_analytics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retriever_id** | **str**|  | 
 **signal_type** | **str**| Filter by signal type (cache_hit, rerank_scores, etc.) | [optional] 
 **limit** | **int**| Maximum results | [optional] [default to 100]
 **hours** | **int**| Hours of history | [optional] [default to 24]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**List[RetrieverSignal]**](RetrieverSignal.md)

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

# **get_slowest_queries_analytics_retrievers_id_slow**
> List[object] get_slowest_queries_analytics_retrievers_id_slow(retriever_id, limit=limit, hours=hours, authorization=authorization, x_namespace=x_namespace)

Get Slowest Queries

Get slowest queries for troubleshooting.

Identifies slowest-performing queries for optimization:
- Query text
- Execution time
- Result counts
- Stage breakdown

**Use Cases:**
- Identify problematic queries
- Debug performance issues
- Optimize query patterns
- User experience improvements

**Example:**
```bash
curl -X GET "https://api.mixpeek.com/v1/analytics/retrievers/ret_abc123/slow-queries?limit=10&hours=24" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "X-Namespace: your-namespace"
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
    api_instance = mixpeek.AnalyticsRetrieversApi(api_client)
    retriever_id = 'retriever_id_example' # str | 
    limit = 10 # int | Number of queries to return (optional) (default to 10)
    hours = 24 # int | Hours of history (optional) (default to 24)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Slowest Queries
        api_response = api_instance.get_slowest_queries_analytics_retrievers_id_slow(retriever_id, limit=limit, hours=hours, authorization=authorization, x_namespace=x_namespace)
        print("The response of AnalyticsRetrieversApi->get_slowest_queries_analytics_retrievers_id_slow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsRetrieversApi->get_slowest_queries_analytics_retrievers_id_slow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retriever_id** | **str**|  | 
 **limit** | **int**| Number of queries to return | [optional] [default to 10]
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

# **get_stage_breakdown_analytics_retrievers**
> StageBreakdownResponse get_stage_breakdown_analytics_retrievers(retriever_id, hours=hours, authorization=authorization, x_namespace=x_namespace)

Get Stage Breakdown

Get stage-level performance breakdown.

Analyzes individual stage performance to identify bottlenecks:
- Stage execution times
- Document flow (in/out)
- Stage-level latency distribution

**Use Cases:**
- Identify slow stages in retrieval pipeline
- Optimize stage ordering
- Debug pipeline bottlenecks
- Understand document reduction rates

**Example:**
```bash
curl -X GET "https://api.mixpeek.com/v1/analytics/retrievers/ret_abc123/stages?hours=24" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "X-Namespace: your-namespace"
```

### Example


```python
import mixpeek
from mixpeek.models.stage_breakdown_response import StageBreakdownResponse
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
    api_instance = mixpeek.AnalyticsRetrieversApi(api_client)
    retriever_id = 'retriever_id_example' # str | 
    hours = 24 # int | Hours of history (optional) (default to 24)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Stage Breakdown
        api_response = api_instance.get_stage_breakdown_analytics_retrievers(retriever_id, hours=hours, authorization=authorization, x_namespace=x_namespace)
        print("The response of AnalyticsRetrieversApi->get_stage_breakdown_analytics_retrievers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsRetrieversApi->get_stage_breakdown_analytics_retrievers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retriever_id** | **str**|  | 
 **hours** | **int**| Hours of history | [optional] [default to 24]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**StageBreakdownResponse**](StageBreakdownResponse.md)

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

