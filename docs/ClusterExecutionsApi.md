# mixpeek.ClusterExecutionsApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_execution_clusters_id_run**](ClusterExecutionsApi.md#cancel_execution_clusters_id_run) | **POST** /v1/clusters/{cluster_id}/executions/{run_id}/cancel | Cancel Execution
[**get_cluster_execution**](ClusterExecutionsApi.md#get_cluster_execution) | **GET** /v1/clusters/{cluster_id}/executions | Get Latest Cluster Execution
[**get_cluster_execution_by_run**](ClusterExecutionsApi.md#get_cluster_execution_by_run) | **GET** /v1/clusters/{cluster_id}/executions/{run_id} | Get Specific Cluster Execution
[**list_cluster_executions**](ClusterExecutionsApi.md#list_cluster_executions) | **POST** /v1/clusters/{cluster_id}/executions/list | List Cluster Execution History


# **cancel_execution_clusters_id_run**
> object cancel_execution_clusters_id_run(cluster_id, run_id, authorization=authorization, x_namespace=x_namespace)

Cancel Execution

Cancel a pending or processing cluster execution.

    This cancels the Ray job (if running) and marks the execution as CANCELED.
    Useful for:
    - Cleaning up orphaned executions where the Ray job was never submitted
    - Stopping long-running clustering jobs
    - Handling executions stuck in pending/processing state

    Only works for executions in 'pending' or 'processing' status.
    Returns an error if the execution is already 'completed', 'failed', or 'canceled'.

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
    api_instance = mixpeek.ClusterExecutionsApi(api_client)
    cluster_id = 'cluster_id_example' # str | Cluster ID
    run_id = 'run_id_example' # str | Run ID to cancel
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Cancel Execution
        api_response = api_instance.cancel_execution_clusters_id_run(cluster_id, run_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of ClusterExecutionsApi->cancel_execution_clusters_id_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterExecutionsApi->cancel_execution_clusters_id_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Cluster ID | 
 **run_id** | **str**| Run ID to cancel | 
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

# **get_cluster_execution**
> ClusterExecutionResult get_cluster_execution(cluster_id, authorization=authorization, x_namespace=x_namespace)

Get Latest Cluster Execution

Get the most recent execution results for a cluster.

    Returns execution metadata including:
    - Execution status (pending, processing, completed, failed)
    - Clustering metrics (silhouette score, Davies-Bouldin index, etc.)
    - Number of clusters found and documents processed
    - Centroid information with labels and summaries
    - Execution timestamps

    Useful for:
    - Displaying cluster statistics in dashboards
    - Showing cluster quality metrics to users
    - Rendering cluster labels and summaries in the UI
    - Tracking execution status and errors

### Example


```python
import mixpeek
from mixpeek.models.cluster_execution_result import ClusterExecutionResult
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
    api_instance = mixpeek.ClusterExecutionsApi(api_client)
    cluster_id = 'cluster_id_example' # str | Cluster ID
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Latest Cluster Execution
        api_response = api_instance.get_cluster_execution(cluster_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of ClusterExecutionsApi->get_cluster_execution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterExecutionsApi->get_cluster_execution: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Cluster ID | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**ClusterExecutionResult**](ClusterExecutionResult.md)

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

# **get_cluster_execution_by_run**
> ClusterExecutionResult get_cluster_execution_by_run(cluster_id, run_id, authorization=authorization, x_namespace=x_namespace)

Get Specific Cluster Execution

Get a specific execution by run ID.

    Returns detailed execution information for a particular clustering run,
    allowing you to review historical executions and compare results over time.

### Example


```python
import mixpeek
from mixpeek.models.cluster_execution_result import ClusterExecutionResult
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
    api_instance = mixpeek.ClusterExecutionsApi(api_client)
    cluster_id = 'cluster_id_example' # str | Cluster ID
    run_id = 'run_id_example' # str | Run ID
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Specific Cluster Execution
        api_response = api_instance.get_cluster_execution_by_run(cluster_id, run_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of ClusterExecutionsApi->get_cluster_execution_by_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterExecutionsApi->get_cluster_execution_by_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Cluster ID | 
 **run_id** | **str**| Run ID | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**ClusterExecutionResult**](ClusterExecutionResult.md)

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

# **list_cluster_executions**
> ListClusterExecutionsResponse list_cluster_executions(cluster_id, limit=limit, offset=offset, cursor=cursor, include_total=include_total, authorization=authorization, x_namespace=x_namespace, list_cluster_executions_request=list_cluster_executions_request)

List Cluster Execution History

List execution history for a cluster with pagination, filtering, sorting, and search.

    Returns all historical executions for the specified cluster, including:
    - Execution status (pending, processing, completed, failed)
    - Clustering metrics (silhouette score, Davies-Bouldin index, etc.)
    - Number of clusters found and documents processed
    - Execution timestamps and duration
    - Centroid information

    Supports:
    - **Filtering**: Filter by status, date range, metrics, etc.
    - **Sorting**: Sort by created_at, execution time, metrics
    - **Search**: Full-text search across execution metadata
    - **Pagination**: Limit and offset for large result sets

    Use cases:
    - View all past executions for a cluster
    - Compare metrics across runs
    - Track execution history over time
    - Debug failed executions
    - Analyze clustering performance trends

### Example


```python
import mixpeek
from mixpeek.models.list_cluster_executions_request import ListClusterExecutionsRequest
from mixpeek.models.list_cluster_executions_response import ListClusterExecutionsResponse
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
    api_instance = mixpeek.ClusterExecutionsApi(api_client)
    cluster_id = 'cluster_id_example' # str | Cluster ID
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    cursor = 'cursor_example' # str |  (optional)
    include_total = False # bool |  (optional) (default to False)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)
    list_cluster_executions_request = mixpeek.ListClusterExecutionsRequest() # ListClusterExecutionsRequest |  (optional)

    try:
        # List Cluster Execution History
        api_response = api_instance.list_cluster_executions(cluster_id, limit=limit, offset=offset, cursor=cursor, include_total=include_total, authorization=authorization, x_namespace=x_namespace, list_cluster_executions_request=list_cluster_executions_request)
        print("The response of ClusterExecutionsApi->list_cluster_executions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterExecutionsApi->list_cluster_executions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Cluster ID | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **cursor** | **str**|  | [optional] 
 **include_total** | **bool**|  | [optional] [default to False]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 
 **list_cluster_executions_request** | [**ListClusterExecutionsRequest**](ListClusterExecutionsRequest.md)|  | [optional] 

### Return type

[**ListClusterExecutionsResponse**](ListClusterExecutionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
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

