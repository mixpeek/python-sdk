# mixpeek.AnalyticsPerformanceApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyze_bottlenecks_analytics_performance_engine**](AnalyticsPerformanceApi.md#analyze_bottlenecks_analytics_performance_engine) | **GET** /v1/analytics/performance/engine/bottlenecks | Analyze Bottlenecks
[**get_batch_diagnostics_analytics_performance_batches**](AnalyticsPerformanceApi.md#get_batch_diagnostics_analytics_performance_batches) | **GET** /v1/analytics/performance/batches/{batch_id}/diagnostics | Get Batch Diagnostics
[**get_engine_performance_analytics**](AnalyticsPerformanceApi.md#get_engine_performance_analytics) | **GET** /v1/analytics/performance/engine | Get Engine Performance
[**get_engine_stage_breakdown_analytics_performance**](AnalyticsPerformanceApi.md#get_engine_stage_breakdown_analytics_performance) | **GET** /v1/analytics/performance/engine/stages | Get Engine Stage Breakdown
[**get_extractor_breakdown_analytics_performance_engine**](AnalyticsPerformanceApi.md#get_extractor_breakdown_analytics_performance_engine) | **GET** /v1/analytics/performance/engine/extractors | Get Extractor Breakdown
[**get_slowest_operations_analytics_performance_engine_slow**](AnalyticsPerformanceApi.md#get_slowest_operations_analytics_performance_engine_slow) | **GET** /v1/analytics/performance/engine/slow-operations | Get Slowest Operations


# **analyze_bottlenecks_analytics_performance_engine**
> BottleneckResponse analyze_bottlenecks_analytics_performance_engine(hours=hours, limit=limit, authorization=authorization, x_namespace=x_namespace)

Analyze Bottlenecks

Identify performance bottlenecks.

Analyzes profiling data to identify the biggest bottlenecks,
ranked by total time spent.

**Use Cases:**
- Find what's slowing down your pipelines
- Prioritize optimization efforts
- Monitor bottleneck trends

**Ranking:**
- Sorted by total time spent (sum across all executions)
- Shows percentage of total execution time
- Includes execution count and average time

**Example:**
```bash
GET /v1/analytics/performance/engine/bottlenecks?hours=24&limit=10
```

### Example


```python
import mixpeek
from mixpeek.models.bottleneck_response import BottleneckResponse
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
    api_instance = mixpeek.AnalyticsPerformanceApi(api_client)
    hours = 24 # int | Hours of history (optional) (default to 24)
    limit = 10 # int | Number of bottlenecks to return (optional) (default to 10)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Analyze Bottlenecks
        api_response = api_instance.analyze_bottlenecks_analytics_performance_engine(hours=hours, limit=limit, authorization=authorization, x_namespace=x_namespace)
        print("The response of AnalyticsPerformanceApi->analyze_bottlenecks_analytics_performance_engine:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsPerformanceApi->analyze_bottlenecks_analytics_performance_engine: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hours** | **int**| Hours of history | [optional] [default to 24]
 **limit** | **int**| Number of bottlenecks to return | [optional] [default to 10]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**BottleneckResponse**](BottleneckResponse.md)

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

# **get_batch_diagnostics_analytics_performance_batches**
> BatchDiagnostics get_batch_diagnostics_analytics_performance_batches(batch_id, authorization=authorization, x_namespace=x_namespace)

Get Batch Diagnostics

Get comprehensive diagnostics for a batch.

Combines batch status, task progress, collection info, performance metrics,
and actionable insights into a single response for easy frontend rendering.

**Use Cases:**
- Monitor batch processing in real-time
- Debug failed batches
- View performance breakdown after completion
- Get actionable next steps

**Response includes:**
- Overall batch status and progress
- Per-tier task details with Ray job links
- Collection document counts
- Performance insights and bottlenecks (if completed)
- Error details (if failed)
- Recommended next actions

**Example:**
```bash
GET /v1/analytics/performance/batches/{batch_id}/diagnostics
```

**Perfect for:**
- Real-time progress tracking UI
- Batch monitoring dashboards
- Debugging failed extractions
- Performance optimization

### Example


```python
import mixpeek
from mixpeek.models.batch_diagnostics import BatchDiagnostics
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
    api_instance = mixpeek.AnalyticsPerformanceApi(api_client)
    batch_id = 'batch_id_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Batch Diagnostics
        api_response = api_instance.get_batch_diagnostics_analytics_performance_batches(batch_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of AnalyticsPerformanceApi->get_batch_diagnostics_analytics_performance_batches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsPerformanceApi->get_batch_diagnostics_analytics_performance_batches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_id** | **str**|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**BatchDiagnostics**](BatchDiagnostics.md)

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

# **get_engine_performance_analytics**
> EnginePerformanceResponse get_engine_performance_analytics(hours=hours, start_date=start_date, end_date=end_date, group_by=group_by, authorization=authorization, x_namespace=x_namespace)

Get Engine Performance

Get engine performance metrics over time.

Query profiling data logged by the engine's profiling infrastructure.
All queries are automatically filtered to your namespace.

**Time Range:**
- Specify `hours` for recent history (e.g., `hours=24` for last 24 hours)
- OR specify `start_date` and `end_date` for custom range
- Defaults to last 24 hours if neither provided

**Grouping:**
- `minute`: High-resolution (for short time ranges)
- `hour`: Standard resolution (default)
- `day`: For longer time ranges
- `week`, `month`: For historical trends

**Response:**
- Time-series metrics (avg, p50, p95, p99 latencies)
- Summary statistics across the entire time range
- All latencies in milliseconds

**Example:**
```bash
GET /v1/analytics/performance/engine?hours=24&group_by=hour
```

### Example


```python
import mixpeek
from mixpeek.models.engine_performance_response import EnginePerformanceResponse
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
    api_instance = mixpeek.AnalyticsPerformanceApi(api_client)
    hours = 56 # int | Hours of history (alternative to date range) (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | Start date for time range (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime | End date for time range (optional)
    group_by = 'hour' # str | Time grouping (minute, hour, day, week) (optional) (default to 'hour')
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Engine Performance
        api_response = api_instance.get_engine_performance_analytics(hours=hours, start_date=start_date, end_date=end_date, group_by=group_by, authorization=authorization, x_namespace=x_namespace)
        print("The response of AnalyticsPerformanceApi->get_engine_performance_analytics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsPerformanceApi->get_engine_performance_analytics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hours** | **int**| Hours of history (alternative to date range) | [optional] 
 **start_date** | **datetime**| Start date for time range | [optional] 
 **end_date** | **datetime**| End date for time range | [optional] 
 **group_by** | **str**| Time grouping (minute, hour, day, week) | [optional] [default to &#39;hour&#39;]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**EnginePerformanceResponse**](EnginePerformanceResponse.md)

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

# **get_engine_stage_breakdown_analytics_performance**
> EngineStageBreakdownResponse get_engine_stage_breakdown_analytics_performance(hours=hours, start_date=start_date, end_date=end_date, authorization=authorization, x_namespace=x_namespace)

Get Engine Stage Breakdown

Get stage-level performance breakdown.

Breaks down engine performance by individual profiled stages
(e.g., pipeline_run, generate_input_dataset, gcs_batch_upload).

**Use Cases:**
- Identify which stages are slowest
- See percentage of total time per stage
- Optimize specific bottlenecks

**Response:**
- Per-stage metrics (count, avg, p95, max latencies)
- Total time spent in each stage
- Percentage of total execution time
- Sorted by total time (worst bottlenecks first)

**Example:**
```bash
GET /v1/analytics/performance/engine/stages?hours=24
```

### Example


```python
import mixpeek
from mixpeek.models.engine_stage_breakdown_response import EngineStageBreakdownResponse
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
    api_instance = mixpeek.AnalyticsPerformanceApi(api_client)
    hours = 56 # int | Hours of history (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | Start date (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime | End date (optional)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Engine Stage Breakdown
        api_response = api_instance.get_engine_stage_breakdown_analytics_performance(hours=hours, start_date=start_date, end_date=end_date, authorization=authorization, x_namespace=x_namespace)
        print("The response of AnalyticsPerformanceApi->get_engine_stage_breakdown_analytics_performance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsPerformanceApi->get_engine_stage_breakdown_analytics_performance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hours** | **int**| Hours of history | [optional] 
 **start_date** | **datetime**| Start date | [optional] 
 **end_date** | **datetime**| End date | [optional] 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**EngineStageBreakdownResponse**](EngineStageBreakdownResponse.md)

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

# **get_extractor_breakdown_analytics_performance_engine**
> ExtractorBreakdownResponse get_extractor_breakdown_analytics_performance_engine(hours=hours, start_date=start_date, end_date=end_date, authorization=authorization, x_namespace=x_namespace)

Get Extractor Breakdown

Get extractor performance breakdown.

Shows performance metrics for each extractor and its stages.

**Use Cases:**
- Compare performance across extractors
- Identify slow extractor stages
- Monitor specific extractor performance

**Response:**
- Per-extractor, per-stage metrics
- Execution counts
- Latency statistics (avg, p95, max)

**Example:**
```bash
GET /v1/analytics/performance/engine/extractors?hours=24
```

### Example


```python
import mixpeek
from mixpeek.models.extractor_breakdown_response import ExtractorBreakdownResponse
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
    api_instance = mixpeek.AnalyticsPerformanceApi(api_client)
    hours = 56 # int | Hours of history (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | Start date (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime | End date (optional)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Extractor Breakdown
        api_response = api_instance.get_extractor_breakdown_analytics_performance_engine(hours=hours, start_date=start_date, end_date=end_date, authorization=authorization, x_namespace=x_namespace)
        print("The response of AnalyticsPerformanceApi->get_extractor_breakdown_analytics_performance_engine:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsPerformanceApi->get_extractor_breakdown_analytics_performance_engine: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hours** | **int**| Hours of history | [optional] 
 **start_date** | **datetime**| Start date | [optional] 
 **end_date** | **datetime**| End date | [optional] 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**ExtractorBreakdownResponse**](ExtractorBreakdownResponse.md)

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

# **get_slowest_operations_analytics_performance_engine_slow**
> SlowOperationsResponse get_slowest_operations_analytics_performance_engine_slow(hours=hours, limit=limit, threshold_ms=threshold_ms, authorization=authorization, x_namespace=x_namespace)

Get Slowest Operations

Get slowest individual operations.

Returns the slowest profiled operations, useful for debugging
specific slow executions.

**Use Cases:**
- Troubleshoot specific slow operations
- Identify outliers
- Deep dive into problematic executions

**Filtering:**
- `threshold_ms`: Only show operations slower than this
- Default: 1000ms (1 second)

**Response:**
- Timestamp of slow operation
- Stage name and component
- Latency in milliseconds
- Full metadata context

**Example:**
```bash
GET /v1/analytics/performance/engine/slow-operations?hours=24&threshold_ms=5000
```

### Example


```python
import mixpeek
from mixpeek.models.slow_operations_response import SlowOperationsResponse
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
    api_instance = mixpeek.AnalyticsPerformanceApi(api_client)
    hours = 24 # int | Hours of history (optional) (default to 24)
    limit = 10 # int | Number of operations to return (optional) (default to 10)
    threshold_ms = 1000.0 # float | Only show operations slower than this (ms) (optional) (default to 1000.0)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Slowest Operations
        api_response = api_instance.get_slowest_operations_analytics_performance_engine_slow(hours=hours, limit=limit, threshold_ms=threshold_ms, authorization=authorization, x_namespace=x_namespace)
        print("The response of AnalyticsPerformanceApi->get_slowest_operations_analytics_performance_engine_slow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsPerformanceApi->get_slowest_operations_analytics_performance_engine_slow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hours** | **int**| Hours of history | [optional] [default to 24]
 **limit** | **int**| Number of operations to return | [optional] [default to 10]
 **threshold_ms** | **float**| Only show operations slower than this (ms) | [optional] [default to 1000.0]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**SlowOperationsResponse**](SlowOperationsResponse.md)

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

