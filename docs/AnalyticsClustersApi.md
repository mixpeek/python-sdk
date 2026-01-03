# mixpeek.AnalyticsClustersApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_execution_history_analytics_clusters**](AnalyticsClustersApi.md#get_execution_history_analytics_clusters) | **GET** /v1/analytics/clusters/{cluster_id}/execution-history | Get Execution History
[**get_failure_analysis_analytics_clusters**](AnalyticsClustersApi.md#get_failure_analysis_analytics_clusters) | **GET** /v1/analytics/clusters/{cluster_id}/failures | Get Failure Analysis


# **get_execution_history_analytics_clusters**
> ExecutionHistoryResponse get_execution_history_analytics_clusters(cluster_id, hours=hours, limit=limit, authorization=authorization, x_namespace=x_namespace)

Get Execution History

Get cluster execution history with metrics.

Provides execution timeline including:
- Execution duration and document counts
- Algorithm and cluster counts
- Success/failure status

**Use Cases:**
- Monitor clustering performance
- Track execution patterns
- Identify execution issues

### Example


```python
import mixpeek
from mixpeek.models.execution_history_response import ExecutionHistoryResponse
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
    api_instance = mixpeek.AnalyticsClustersApi(api_client)
    cluster_id = 'cluster_id_example' # str | 
    hours = 168 # int | Hours of history (optional) (default to 168)
    limit = 100 # int |  (optional) (default to 100)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Execution History
        api_response = api_instance.get_execution_history_analytics_clusters(cluster_id, hours=hours, limit=limit, authorization=authorization, x_namespace=x_namespace)
        print("The response of AnalyticsClustersApi->get_execution_history_analytics_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsClustersApi->get_execution_history_analytics_clusters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **hours** | **int**| Hours of history | [optional] [default to 168]
 **limit** | **int**|  | [optional] [default to 100]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**ExecutionHistoryResponse**](ExecutionHistoryResponse.md)

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

# **get_failure_analysis_analytics_clusters**
> ApiAnalyticsClustersModelsFailureAnalysisResponse get_failure_analysis_analytics_clusters(cluster_id, hours=hours, authorization=authorization, x_namespace=x_namespace)

Get Failure Analysis

Get cluster failure analysis.

Analyzes clustering failures including:
- Error messages and types
- Failure timestamps
- Failure patterns

**Use Cases:**
- Debug clustering failures
- Identify common error patterns
- Monitor cluster health

### Example


```python
import mixpeek
from mixpeek.models.api_analytics_clusters_models_failure_analysis_response import ApiAnalyticsClustersModelsFailureAnalysisResponse
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
    api_instance = mixpeek.AnalyticsClustersApi(api_client)
    cluster_id = 'cluster_id_example' # str | 
    hours = 168 # int |  (optional) (default to 168)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Failure Analysis
        api_response = api_instance.get_failure_analysis_analytics_clusters(cluster_id, hours=hours, authorization=authorization, x_namespace=x_namespace)
        print("The response of AnalyticsClustersApi->get_failure_analysis_analytics_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsClustersApi->get_failure_analysis_analytics_clusters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **hours** | **int**|  | [optional] [default to 168]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**ApiAnalyticsClustersModelsFailureAnalysisResponse**](ApiAnalyticsClustersModelsFailureAnalysisResponse.md)

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

