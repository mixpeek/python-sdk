# mixpeek.AnalyticsNamespacesApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_compound_index_patterns_analytics_namespaces_indexes**](AnalyticsNamespacesApi.md#get_compound_index_patterns_analytics_namespaces_indexes) | **GET** /v1/analytics/namespaces/indexes/compound-patterns | Get Compound Index Patterns
[**get_field_performance_analytics_namespaces**](AnalyticsNamespacesApi.md#get_field_performance_analytics_namespaces) | **GET** /v1/analytics/namespaces/fields/performance | Get Field Performance
[**get_index_recommendations_analytics_namespaces_indexes**](AnalyticsNamespacesApi.md#get_index_recommendations_analytics_namespaces_indexes) | **GET** /v1/analytics/namespaces/indexes/recommendations | Get Index Recommendations
[**get_most_queried_fields_analytics_namespaces**](AnalyticsNamespacesApi.md#get_most_queried_fields_analytics_namespaces) | **GET** /v1/analytics/namespaces/fields/most-queried | Get Most Queried Fields
[**get_namespace_summary_analytics**](AnalyticsNamespacesApi.md#get_namespace_summary_analytics) | **GET** /v1/analytics/namespaces/summary | Get Namespace Summary
[**get_slow_queries_analytics_namespaces**](AnalyticsNamespacesApi.md#get_slow_queries_analytics_namespaces) | **GET** /v1/analytics/namespaces/queries/slow | Get Slow Queries


# **get_compound_index_patterns_analytics_namespaces_indexes**
> CompoundIndexResponse get_compound_index_patterns_analytics_namespaces_indexes(days=days, limit=limit, authorization=authorization, x_namespace=x_namespace)

Get Compound Index Patterns

Identify compound index opportunities.

Finds metadata fields commonly used together in filters, suggesting
opportunities for compound (multi-field) indexes.

**Use Cases:**
- Optimize multi-field queries
- Create compound indexes
- Understand query complexity
- Improve complex filter performance

**Response Includes:**
- Field combinations used together
- Frequency of combination usage
- Average and P95 latency
- Sorted by combination frequency

**Compound Index Example:**
If `brand + status` appears frequently, create:
```javascript
db.documents.createIndex({"metadata.brand": 1, "metadata.status": 1})
```

**Example:**
```bash
curl -X GET "https://api.mixpeek.com/v1/analytics/namespaces/indexes/compound-patterns" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "X-Namespace: your-namespace"
```

### Example


```python
import mixpeek
from mixpeek.models.compound_index_response import CompoundIndexResponse
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
    api_instance = mixpeek.AnalyticsNamespacesApi(api_client)
    days = 30 # int | Days of history to analyze (optional) (default to 30)
    limit = 50 # int | Maximum patterns to return (optional) (default to 50)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Compound Index Patterns
        api_response = api_instance.get_compound_index_patterns_analytics_namespaces_indexes(days=days, limit=limit, authorization=authorization, x_namespace=x_namespace)
        print("The response of AnalyticsNamespacesApi->get_compound_index_patterns_analytics_namespaces_indexes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsNamespacesApi->get_compound_index_patterns_analytics_namespaces_indexes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**| Days of history to analyze | [optional] [default to 30]
 **limit** | **int**| Maximum patterns to return | [optional] [default to 50]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**CompoundIndexResponse**](CompoundIndexResponse.md)

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

# **get_field_performance_analytics_namespaces**
> FieldPerformanceResponse get_field_performance_analytics_namespaces(days=days, limit=limit, authorization=authorization, x_namespace=x_namespace)

Get Field Performance

Analyze field performance correlation.

Shows which metadata fields correlate with slow queries, helping identify
fields that would benefit most from indexing.

**Use Cases:**
- Identify fields causing performance issues
- Quantify indexing impact potential
- Prioritize index creation
- Monitor field usage patterns

**Response Includes:**
- Field usage count
- Latency statistics (avg, P50, P95, P99, max)
- Index priority score (usage × latency)
- Sorted by priority score

**Index Priority Score:**
Higher scores indicate fields where indexing would have greatest impact.
Score = (query count) × (average latency)

**Example:**
```bash
curl -X GET "https://api.mixpeek.com/v1/analytics/namespaces/fields/performance?days=30" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "X-Namespace: your-namespace"
```

### Example


```python
import mixpeek
from mixpeek.models.field_performance_response import FieldPerformanceResponse
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
    api_instance = mixpeek.AnalyticsNamespacesApi(api_client)
    days = 30 # int | Days of history to analyze (optional) (default to 30)
    limit = 50 # int | Maximum fields to return (optional) (default to 50)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Field Performance
        api_response = api_instance.get_field_performance_analytics_namespaces(days=days, limit=limit, authorization=authorization, x_namespace=x_namespace)
        print("The response of AnalyticsNamespacesApi->get_field_performance_analytics_namespaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsNamespacesApi->get_field_performance_analytics_namespaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**| Days of history to analyze | [optional] [default to 30]
 **limit** | **int**| Maximum fields to return | [optional] [default to 50]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**FieldPerformanceResponse**](FieldPerformanceResponse.md)

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

# **get_index_recommendations_analytics_namespaces_indexes**
> IndexRecommendationsResponse get_index_recommendations_analytics_namespaces_indexes(days=days, min_usage_count=min_usage_count, limit=limit, authorization=authorization, x_namespace=x_namespace)

Get Index Recommendations

Get comprehensive MongoDB index recommendations.

Analyzes query patterns and generates prioritized index recommendations
with ready-to-use MongoDB commands.

**Use Cases:**
- Get actionable index suggestions
- Prioritize database optimization
- Copy/paste index creation commands
- Track optimization opportunities

**Recommendation Levels:**
- **HIGH PRIORITY**: >100 queries, >300ms avg OR >10 very slow queries
- **MEDIUM PRIORITY**: >50 queries, >200ms avg OR >20 slow queries
- **LOW PRIORITY**: >10 queries but acceptable performance
- **NO ACTION**: Low usage, no optimization needed

**Response Includes:**
- Prioritized recommendations
- Usage and latency statistics
- MongoDB index creation commands
- Summary by priority level

**Example:**
```bash
curl -X GET "https://api.mixpeek.com/v1/analytics/namespaces/indexes/recommendations" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "X-Namespace: your-namespace"
```

### Example


```python
import mixpeek
from mixpeek.models.index_recommendations_response import IndexRecommendationsResponse
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
    api_instance = mixpeek.AnalyticsNamespacesApi(api_client)
    days = 30 # int | Days of history to analyze (optional) (default to 30)
    min_usage_count = 5 # int | Minimum queries to consider (optional) (default to 5)
    limit = 50 # int | Maximum recommendations to return (optional) (default to 50)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Index Recommendations
        api_response = api_instance.get_index_recommendations_analytics_namespaces_indexes(days=days, min_usage_count=min_usage_count, limit=limit, authorization=authorization, x_namespace=x_namespace)
        print("The response of AnalyticsNamespacesApi->get_index_recommendations_analytics_namespaces_indexes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsNamespacesApi->get_index_recommendations_analytics_namespaces_indexes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**| Days of history to analyze | [optional] [default to 30]
 **min_usage_count** | **int**| Minimum queries to consider | [optional] [default to 5]
 **limit** | **int**| Maximum recommendations to return | [optional] [default to 50]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**IndexRecommendationsResponse**](IndexRecommendationsResponse.md)

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

# **get_most_queried_fields_analytics_namespaces**
> MostQueriedFieldsResponse get_most_queried_fields_analytics_namespaces(days=days, limit=limit, authorization=authorization, x_namespace=x_namespace)

Get Most Queried Fields

Get most frequently queried metadata fields.

Identifies which metadata fields are accessed most often in retriever queries,
helping prioritize index creation and understand query patterns.

**Use Cases:**
- Identify fields that need indexing
- Understand common query patterns
- Prioritize optimization efforts
- Plan database schema improvements

**Response Includes:**
- Field name and usage frequency
- Average and P95 latency metrics
- Total unique fields analyzed

**Example:**
```bash
curl -X GET "https://api.mixpeek.com/v1/analytics/namespaces/fields/most-queried?days=30&limit=20" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "X-Namespace: your-namespace"
```

### Example


```python
import mixpeek
from mixpeek.models.most_queried_fields_response import MostQueriedFieldsResponse
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
    api_instance = mixpeek.AnalyticsNamespacesApi(api_client)
    days = 30 # int | Days of history to analyze (optional) (default to 30)
    limit = 50 # int | Maximum fields to return (optional) (default to 50)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Most Queried Fields
        api_response = api_instance.get_most_queried_fields_analytics_namespaces(days=days, limit=limit, authorization=authorization, x_namespace=x_namespace)
        print("The response of AnalyticsNamespacesApi->get_most_queried_fields_analytics_namespaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsNamespacesApi->get_most_queried_fields_analytics_namespaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**| Days of history to analyze | [optional] [default to 30]
 **limit** | **int**| Maximum fields to return | [optional] [default to 50]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**MostQueriedFieldsResponse**](MostQueriedFieldsResponse.md)

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

# **get_namespace_summary_analytics**
> NamespaceSummaryResponse get_namespace_summary_analytics(days=days, authorization=authorization, x_namespace=x_namespace)

Get Namespace Summary

Get comprehensive namespace optimization summary.

Provides a complete overview of namespace performance including:
- Top index recommendations
- Most queried fields
- Slowest fields
- Compound index opportunities
- Summary statistics

**Use Cases:**
- Get full optimization picture
- Regular performance reviews
- Database health checks
- Planning optimization work

**Response Includes:**
- Summary statistics (field counts, priority levels)
- Top 10 index recommendations
- Top 10 most queried fields
- Top 10 slowest fields
- Top 10 compound index opportunities

**Recommended Workflow:**
1. Call this endpoint for overview
2. Use specific endpoints for details
3. Implement high-priority recommendations
4. Monitor improvement over time

**Example:**
```bash
curl -X GET "https://api.mixpeek.com/v1/analytics/namespaces/summary?days=30" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "X-Namespace: your-namespace"
```

### Example


```python
import mixpeek
from mixpeek.models.namespace_summary_response import NamespaceSummaryResponse
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
    api_instance = mixpeek.AnalyticsNamespacesApi(api_client)
    days = 30 # int | Days of history to analyze (optional) (default to 30)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Namespace Summary
        api_response = api_instance.get_namespace_summary_analytics(days=days, authorization=authorization, x_namespace=x_namespace)
        print("The response of AnalyticsNamespacesApi->get_namespace_summary_analytics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsNamespacesApi->get_namespace_summary_analytics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**| Days of history to analyze | [optional] [default to 30]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**NamespaceSummaryResponse**](NamespaceSummaryResponse.md)

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

# **get_slow_queries_analytics_namespaces**
> SlowQueriesResponse get_slow_queries_analytics_namespaces(days=days, latency_threshold_ms=latency_threshold_ms, limit=limit, authorization=authorization, x_namespace=x_namespace)

Get Slow Queries

Get slow queries and their filter patterns.

Identifies queries exceeding a latency threshold and shows which metadata
fields they're filtering on, helping pinpoint optimization opportunities.

**Use Cases:**
- Troubleshoot slow queries
- Identify unindexed fields causing slowdowns
- Debug performance issues
- Optimize query patterns

**Response Includes:**
- Query details (retriever, inputs, latency)
- Results count
- Metadata fields being filtered
- Full query context

**Example:**
```bash
curl -X GET "https://api.mixpeek.com/v1/analytics/namespaces/queries/slow?latency_threshold_ms=1000" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "X-Namespace: your-namespace"
```

### Example


```python
import mixpeek
from mixpeek.models.slow_queries_response import SlowQueriesResponse
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
    api_instance = mixpeek.AnalyticsNamespacesApi(api_client)
    days = 30 # int | Days of history to analyze (optional) (default to 30)
    latency_threshold_ms = 500 # float | Latency threshold in ms (optional) (default to 500)
    limit = 100 # int | Maximum queries to return (optional) (default to 100)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Slow Queries
        api_response = api_instance.get_slow_queries_analytics_namespaces(days=days, latency_threshold_ms=latency_threshold_ms, limit=limit, authorization=authorization, x_namespace=x_namespace)
        print("The response of AnalyticsNamespacesApi->get_slow_queries_analytics_namespaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsNamespacesApi->get_slow_queries_analytics_namespaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**| Days of history to analyze | [optional] [default to 30]
 **latency_threshold_ms** | **float**| Latency threshold in ms | [optional] [default to 500]
 **limit** | **int**| Maximum queries to return | [optional] [default to 100]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**SlowQueriesResponse**](SlowQueriesResponse.md)

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

