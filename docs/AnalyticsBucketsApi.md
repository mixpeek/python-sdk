# mixpeek.AnalyticsBucketsApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_bucket_health_analytics**](AnalyticsBucketsApi.md#get_bucket_health_analytics) | **GET** /v1/analytics/buckets/{bucket_id}/health | Get Bucket Health
[**get_bucket_storage_analytics**](AnalyticsBucketsApi.md#get_bucket_storage_analytics) | **GET** /v1/analytics/buckets/{bucket_id}/storage | Get Bucket Storage
[**get_bucket_usage_analytics**](AnalyticsBucketsApi.md#get_bucket_usage_analytics) | **GET** /v1/analytics/buckets/{bucket_id}/usage | Get Bucket Usage
[**get_sync_comparison_analytics_buckets**](AnalyticsBucketsApi.md#get_sync_comparison_analytics_buckets) | **GET** /v1/analytics/buckets/{bucket_id}/sync-comparison | Get Sync Comparison
[**get_sync_performance_analytics_buckets**](AnalyticsBucketsApi.md#get_sync_performance_analytics_buckets) | **GET** /v1/analytics/buckets/{bucket_id}/sync-performance | Get Sync Performance
[**get_upload_performance_analytics_buckets**](AnalyticsBucketsApi.md#get_upload_performance_analytics_buckets) | **GET** /v1/analytics/buckets/{bucket_id}/upload-performance | Get Upload Performance


# **get_bucket_health_analytics**
> BucketHealthResponse get_bucket_health_analytics(bucket_id, hours=hours, authorization=authorization, x_namespace=x_namespace)

Get Bucket Health

Get bucket health monitoring metrics.

Analyzes bucket health including:
- Error breakdown by type
- Sync health per configuration
- Stuck/failing syncs
- Overall health status

**Use Cases:**
- Monitor bucket health
- Identify failing syncs
- Debug errors by type
- Alert on unhealthy buckets

**Example:**
```bash
curl -X GET "https://api.mixpeek.com/v1/analytics/buckets/bkt_abc123/health?hours=24" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "X-Namespace: your-namespace"
```

### Example


```python
import mixpeek
from mixpeek.models.bucket_health_response import BucketHealthResponse
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
    api_instance = mixpeek.AnalyticsBucketsApi(api_client)
    bucket_id = 'bucket_id_example' # str | 
    hours = 24 # int | Hours of history (optional) (default to 24)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Bucket Health
        api_response = api_instance.get_bucket_health_analytics(bucket_id, hours=hours, authorization=authorization, x_namespace=x_namespace)
        print("The response of AnalyticsBucketsApi->get_bucket_health_analytics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsBucketsApi->get_bucket_health_analytics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **str**|  | 
 **hours** | **int**| Hours of history | [optional] [default to 24]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**BucketHealthResponse**](BucketHealthResponse.md)

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

# **get_bucket_storage_analytics**
> BucketStorageResponse get_bucket_storage_analytics(bucket_id, start_date=start_date, end_date=end_date, group_by=group_by, authorization=authorization, x_namespace=x_namespace)

Get Bucket Storage

Get storage growth trends over time.

Analyzes bucket storage metrics including:
- Total storage size over time
- Object count trends
- Growth rates

**Use Cases:**
- Monitor storage capacity planning
- Identify storage growth patterns
- Track object accumulation
- Alert on unexpected growth

**Example:**
```bash
curl -X GET "https://api.mixpeek.com/v1/analytics/buckets/bkt_abc123/storage?group_by=day" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "X-Namespace: your-namespace"
```

### Example


```python
import mixpeek
from mixpeek.models.bucket_storage_response import BucketStorageResponse
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
    api_instance = mixpeek.AnalyticsBucketsApi(api_client)
    bucket_id = 'bucket_id_example' # str | 
    start_date = '2013-10-20T19:20:30+01:00' # datetime | Start date (UTC) (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime | End date (UTC) (optional)
    group_by = 'day' # str | Time grouping: hour, day, week, month (optional) (default to 'day')
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Bucket Storage
        api_response = api_instance.get_bucket_storage_analytics(bucket_id, start_date=start_date, end_date=end_date, group_by=group_by, authorization=authorization, x_namespace=x_namespace)
        print("The response of AnalyticsBucketsApi->get_bucket_storage_analytics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsBucketsApi->get_bucket_storage_analytics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **str**|  | 
 **start_date** | **datetime**| Start date (UTC) | [optional] 
 **end_date** | **datetime**| End date (UTC) | [optional] 
 **group_by** | **str**| Time grouping: hour, day, week, month | [optional] [default to &#39;day&#39;]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**BucketStorageResponse**](BucketStorageResponse.md)

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

# **get_bucket_usage_analytics**
> BucketUsageResponse get_bucket_usage_analytics(bucket_id, start_date=start_date, end_date=end_date, group_by=group_by, authorization=authorization, x_namespace=x_namespace)

Get Bucket Usage

Get usage and cost metrics.

Analyzes bucket usage and costs including:
- Storage costs (GB-hours)
- Upload operation costs
- Sync operation costs
- Cost breakdown by category

**Use Cases:**
- Track bucket costs
- Optimize spending
- Forecast future costs
- Cost attribution

**Example:**
```bash
curl -X GET "https://api.mixpeek.com/v1/analytics/buckets/bkt_abc123/usage?group_by=day" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "X-Namespace: your-namespace"
```

### Example


```python
import mixpeek
from mixpeek.models.bucket_usage_response import BucketUsageResponse
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
    api_instance = mixpeek.AnalyticsBucketsApi(api_client)
    bucket_id = 'bucket_id_example' # str | 
    start_date = '2013-10-20T19:20:30+01:00' # datetime | Start date (UTC) (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime | End date (UTC) (optional)
    group_by = 'day' # str | Time grouping: hour, day, week, month (optional) (default to 'day')
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Bucket Usage
        api_response = api_instance.get_bucket_usage_analytics(bucket_id, start_date=start_date, end_date=end_date, group_by=group_by, authorization=authorization, x_namespace=x_namespace)
        print("The response of AnalyticsBucketsApi->get_bucket_usage_analytics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsBucketsApi->get_bucket_usage_analytics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **str**|  | 
 **start_date** | **datetime**| Start date (UTC) | [optional] 
 **end_date** | **datetime**| End date (UTC) | [optional] 
 **group_by** | **str**| Time grouping: hour, day, week, month | [optional] [default to &#39;day&#39;]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**BucketUsageResponse**](BucketUsageResponse.md)

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

# **get_sync_comparison_analytics_buckets**
> SyncComparisonResponse get_sync_comparison_analytics_buckets(bucket_id, hours=hours, authorization=authorization, x_namespace=x_namespace)

Get Sync Comparison

Compare performance across sync configurations.

Compares sync configurations by:
- Average duration and throughput
- Success rates
- Total files and bytes synced
- Provider performance

**Use Cases:**
- Compare sync providers (S3 vs GCS)
- Optimize sync configurations
- Identify best-performing syncs
- Benchmark sync strategies

**Example:**
```bash
curl -X GET "https://api.mixpeek.com/v1/analytics/buckets/bkt_abc123/sync-comparison?hours=168" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "X-Namespace: your-namespace"
```

### Example


```python
import mixpeek
from mixpeek.models.sync_comparison_response import SyncComparisonResponse
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
    api_instance = mixpeek.AnalyticsBucketsApi(api_client)
    bucket_id = 'bucket_id_example' # str | 
    hours = 168 # int | Hours of history (default: 7 days) (optional) (default to 168)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Sync Comparison
        api_response = api_instance.get_sync_comparison_analytics_buckets(bucket_id, hours=hours, authorization=authorization, x_namespace=x_namespace)
        print("The response of AnalyticsBucketsApi->get_sync_comparison_analytics_buckets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsBucketsApi->get_sync_comparison_analytics_buckets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **str**|  | 
 **hours** | **int**| Hours of history (default: 7 days) | [optional] [default to 168]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**SyncComparisonResponse**](SyncComparisonResponse.md)

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

# **get_sync_performance_analytics_buckets**
> SyncPerformanceResponse get_sync_performance_analytics_buckets(bucket_id, sync_config_id=sync_config_id, hours=hours, limit=limit, authorization=authorization, x_namespace=x_namespace)

Get Sync Performance

Get sync performance metrics.

Analyzes sync job execution including:
- Files synced/failed
- Sync duration and throughput
- Success rates by provider

**Use Cases:**
- Monitor sync reliability
- Compare sync configurations
- Identify slow syncs
- Debug sync failures

**Example:**
```bash
curl -X GET "https://api.mixpeek.com/v1/analytics/buckets/bkt_abc123/sync-performance?hours=168" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "X-Namespace: your-namespace"
```

### Example


```python
import mixpeek
from mixpeek.models.sync_performance_response import SyncPerformanceResponse
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
    api_instance = mixpeek.AnalyticsBucketsApi(api_client)
    bucket_id = 'bucket_id_example' # str | 
    sync_config_id = 'sync_config_id_example' # str | Filter by sync config ID (optional)
    hours = 168 # int | Hours of history (default: 7 days) (optional) (default to 168)
    limit = 100 # int | Maximum sync runs to return (optional) (default to 100)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Sync Performance
        api_response = api_instance.get_sync_performance_analytics_buckets(bucket_id, sync_config_id=sync_config_id, hours=hours, limit=limit, authorization=authorization, x_namespace=x_namespace)
        print("The response of AnalyticsBucketsApi->get_sync_performance_analytics_buckets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsBucketsApi->get_sync_performance_analytics_buckets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **str**|  | 
 **sync_config_id** | **str**| Filter by sync config ID | [optional] 
 **hours** | **int**| Hours of history (default: 7 days) | [optional] [default to 168]
 **limit** | **int**| Maximum sync runs to return | [optional] [default to 100]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**SyncPerformanceResponse**](SyncPerformanceResponse.md)

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

# **get_upload_performance_analytics_buckets**
> UploadPerformanceResponse get_upload_performance_analytics_buckets(bucket_id, hours=hours, group_by=group_by, authorization=authorization, x_namespace=x_namespace)

Get Upload Performance

Get upload performance metrics.

Analyzes upload operations including:
- Upload latency (P50, P95, P99)
- Throughput (MB/s)
- Error rates

**Use Cases:**
- Monitor upload performance
- Identify performance degradations
- Optimize upload strategies
- Debug upload issues

**Example:**
```bash
curl -X GET "https://api.mixpeek.com/v1/analytics/buckets/bkt_abc123/upload-performance?hours=24" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "X-Namespace: your-namespace"
```

### Example


```python
import mixpeek
from mixpeek.models.upload_performance_response import UploadPerformanceResponse
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
    api_instance = mixpeek.AnalyticsBucketsApi(api_client)
    bucket_id = 'bucket_id_example' # str | 
    hours = 24 # int | Hours of history (optional) (default to 24)
    group_by = 'hour' # str | Time grouping: hour, day (optional) (default to 'hour')
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Upload Performance
        api_response = api_instance.get_upload_performance_analytics_buckets(bucket_id, hours=hours, group_by=group_by, authorization=authorization, x_namespace=x_namespace)
        print("The response of AnalyticsBucketsApi->get_upload_performance_analytics_buckets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsBucketsApi->get_upload_performance_analytics_buckets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **str**|  | 
 **hours** | **int**| Hours of history | [optional] [default to 24]
 **group_by** | **str**| Time grouping: hour, day | [optional] [default to &#39;hour&#39;]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**UploadPerformanceResponse**](UploadPerformanceResponse.md)

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

