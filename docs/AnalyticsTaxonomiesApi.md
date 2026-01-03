# mixpeek.AnalyticsTaxonomiesApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_assignment_metrics_analytics_taxonomies_taxonomy**](AnalyticsTaxonomiesApi.md#get_assignment_metrics_analytics_taxonomies_taxonomy) | **GET** /v1/analytics/taxonomies/{taxonomy_id}/assignments | Get Assignment Metrics
[**get_confidence_distribution_analytics_taxonomies_taxonomy**](AnalyticsTaxonomiesApi.md#get_confidence_distribution_analytics_taxonomies_taxonomy) | **GET** /v1/analytics/taxonomies/{taxonomy_id}/confidence | Get Confidence Distribution
[**get_enrichment_history_analytics_taxonomies_taxonomy**](AnalyticsTaxonomiesApi.md#get_enrichment_history_analytics_taxonomies_taxonomy) | **GET** /v1/analytics/taxonomies/{taxonomy_id}/enrichments | Get Enrichment History
[**get_label_distribution_analytics_taxonomies_taxonomy**](AnalyticsTaxonomiesApi.md#get_label_distribution_analytics_taxonomies_taxonomy) | **GET** /v1/analytics/taxonomies/{taxonomy_id}/labels | Get Label Distribution


# **get_assignment_metrics_analytics_taxonomies_taxonomy**
> AssignmentMetricsResponse get_assignment_metrics_analytics_taxonomies_taxonomy(taxonomy_id, start_date=start_date, end_date=end_date, group_by=group_by, authorization=authorization, x_namespace=x_namespace)

Get Assignment Metrics

Get taxonomy assignment metrics over time.

Tracks assignment counts including:
- Assignment volume over time
- Average confidence scores
- Unique labels assigned

**Use Cases:**
- Monitor taxonomy usage
- Track assignment trends
- Identify popular labels

### Example


```python
import mixpeek
from mixpeek.models.assignment_metrics_response import AssignmentMetricsResponse
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
    api_instance = mixpeek.AnalyticsTaxonomiesApi(api_client)
    taxonomy_id = 'taxonomy_id_example' # str | 
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    group_by = 'day' # str |  (optional) (default to 'day')
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Assignment Metrics
        api_response = api_instance.get_assignment_metrics_analytics_taxonomies_taxonomy(taxonomy_id, start_date=start_date, end_date=end_date, group_by=group_by, authorization=authorization, x_namespace=x_namespace)
        print("The response of AnalyticsTaxonomiesApi->get_assignment_metrics_analytics_taxonomies_taxonomy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsTaxonomiesApi->get_assignment_metrics_analytics_taxonomies_taxonomy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxonomy_id** | **str**|  | 
 **start_date** | **datetime**|  | [optional] 
 **end_date** | **datetime**|  | [optional] 
 **group_by** | **str**|  | [optional] [default to &#39;day&#39;]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**AssignmentMetricsResponse**](AssignmentMetricsResponse.md)

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

# **get_confidence_distribution_analytics_taxonomies_taxonomy**
> ConfidenceResponse get_confidence_distribution_analytics_taxonomies_taxonomy(taxonomy_id, hours=hours, authorization=authorization, x_namespace=x_namespace)

Get Confidence Distribution

Get confidence score distribution.

Analyzes assignment confidence including:
- Distribution across confidence ranges
- Low-confidence assignment alerts
- Average confidence trends

**Use Cases:**
- Monitor taxonomy quality
- Identify low-confidence assignments
- Track confidence improvements

### Example


```python
import mixpeek
from mixpeek.models.confidence_response import ConfidenceResponse
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
    api_instance = mixpeek.AnalyticsTaxonomiesApi(api_client)
    taxonomy_id = 'taxonomy_id_example' # str | 
    hours = 168 # int |  (optional) (default to 168)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Confidence Distribution
        api_response = api_instance.get_confidence_distribution_analytics_taxonomies_taxonomy(taxonomy_id, hours=hours, authorization=authorization, x_namespace=x_namespace)
        print("The response of AnalyticsTaxonomiesApi->get_confidence_distribution_analytics_taxonomies_taxonomy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsTaxonomiesApi->get_confidence_distribution_analytics_taxonomies_taxonomy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxonomy_id** | **str**|  | 
 **hours** | **int**|  | [optional] [default to 168]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**ConfidenceResponse**](ConfidenceResponse.md)

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

# **get_enrichment_history_analytics_taxonomies_taxonomy**
> EnrichmentHistoryResponse get_enrichment_history_analytics_taxonomies_taxonomy(taxonomy_id, start_date=start_date, end_date=end_date, group_by=group_by, authorization=authorization, x_namespace=x_namespace)

Get Enrichment History

Get enrichment execution history.

Tracks enrichment operations including:
- Enrichment success rates
- Average latency
- Volume trends

**Use Cases:**
- Monitor enrichment performance
- Track success rates
- Identify performance issues

### Example


```python
import mixpeek
from mixpeek.models.enrichment_history_response import EnrichmentHistoryResponse
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
    api_instance = mixpeek.AnalyticsTaxonomiesApi(api_client)
    taxonomy_id = 'taxonomy_id_example' # str | 
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    group_by = 'day' # str |  (optional) (default to 'day')
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Enrichment History
        api_response = api_instance.get_enrichment_history_analytics_taxonomies_taxonomy(taxonomy_id, start_date=start_date, end_date=end_date, group_by=group_by, authorization=authorization, x_namespace=x_namespace)
        print("The response of AnalyticsTaxonomiesApi->get_enrichment_history_analytics_taxonomies_taxonomy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsTaxonomiesApi->get_enrichment_history_analytics_taxonomies_taxonomy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxonomy_id** | **str**|  | 
 **start_date** | **datetime**|  | [optional] 
 **end_date** | **datetime**|  | [optional] 
 **group_by** | **str**|  | [optional] [default to &#39;day&#39;]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**EnrichmentHistoryResponse**](EnrichmentHistoryResponse.md)

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

# **get_label_distribution_analytics_taxonomies_taxonomy**
> LabelDistributionResponse get_label_distribution_analytics_taxonomies_taxonomy(taxonomy_id, hours=hours, limit=limit, authorization=authorization, x_namespace=x_namespace)

Get Label Distribution

Get label distribution.

Analyzes label usage including:
- Top labels by assignment count
- Label popularity percentages
- Confidence by label

**Use Cases:**
- Understand label usage
- Identify most common categories
- Balance taxonomy coverage

### Example


```python
import mixpeek
from mixpeek.models.label_distribution_response import LabelDistributionResponse
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
    api_instance = mixpeek.AnalyticsTaxonomiesApi(api_client)
    taxonomy_id = 'taxonomy_id_example' # str | 
    hours = 168 # int |  (optional) (default to 168)
    limit = 50 # int |  (optional) (default to 50)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Label Distribution
        api_response = api_instance.get_label_distribution_analytics_taxonomies_taxonomy(taxonomy_id, hours=hours, limit=limit, authorization=authorization, x_namespace=x_namespace)
        print("The response of AnalyticsTaxonomiesApi->get_label_distribution_analytics_taxonomies_taxonomy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsTaxonomiesApi->get_label_distribution_analytics_taxonomies_taxonomy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxonomy_id** | **str**|  | 
 **hours** | **int**|  | [optional] [default to 168]
 **limit** | **int**|  | [optional] [default to 50]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**LabelDistributionResponse**](LabelDistributionResponse.md)

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

