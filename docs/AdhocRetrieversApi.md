# mixpeek.AdhocRetrieversApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_adhoc_retriever**](AdhocRetrieversApi.md#execute_adhoc_retriever) | **POST** /v1/retrievers/execute | Execute Adhoc Retriever
[**get_adhoc_execution_retrievers**](AdhocRetrieversApi.md#get_adhoc_execution_retrievers) | **GET** /v1/retrievers/executions/{execution_id} | Get Adhoc Execution
[**list_adhoc_executions_retrievers**](AdhocRetrieversApi.md#list_adhoc_executions_retrievers) | **POST** /v1/retrievers/executions/list | List Adhoc Executions


# **execute_adhoc_retriever**
> object execute_adhoc_retriever(adhoc_execute_request, return_presigned_urls=return_presigned_urls, return_vectors=return_vectors, authorization=authorization, x_namespace=x_namespace)

Execute Adhoc Retriever

Execute a retriever ad-hoc without persisting the configuration.

This endpoint allows you to execute a retriever without saving it to the database.
Useful for one-time queries, testing configurations, or temporary searches.

Streaming Execution (stream=True):
    Response uses Server-Sent Events (SSE) format with Content-Type: text/event-stream.
    Each stage emits events as it executes, formatted as: data: {json}\n\n

    Event Types (StreamEventType):
    - stage_start: Emitted when a stage begins (includes stage_name, stage_index, total_stages)
    - stage_complete: Emitted when a stage finishes (includes documents, statistics, budget_used)
    - stage_error: Emitted if a stage fails (includes error message)
    - execution_complete: Final event with complete results and pagination
    - execution_error: Emitted if entire execution fails

    StreamStageEvent Fields:
    - event_type: Type of event
    - execution_id: Unique execution identifier
    - stage_name/stage_index/total_stages: Stage progress info
    - documents: Intermediate results (stage_complete only)
    - statistics: Stage metrics (duration_ms, input_count, output_count, efficiency)
    - budget_used: Cumulative consumption (credits_used, time_elapsed_ms, tokens_used)

    Response Headers:
    - Content-Type: text/event-stream
    - Cache-Control: no-cache
    - Connection: keep-alive
    - X-Execution-Mode: adhoc

Standard Execution (stream=False, default):
    - Returns ExecuteRetrieverResponse after all stages complete
    - Includes X-Execution-Mode: adhoc header
    - execution_metadata.retriever_persisted = False

Use Cases:
    - One-time queries without saving retriever configuration
    - Testing stage configurations before persisting
    - Dynamic retrieval with varying parameters
    - Real-time progress tracking with streaming

### Example


```python
import mixpeek
from mixpeek.models.adhoc_execute_request import AdhocExecuteRequest
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
    api_instance = mixpeek.AdhocRetrieversApi(api_client)
    adhoc_execute_request = mixpeek.AdhocExecuteRequest() # AdhocExecuteRequest | 
    return_presigned_urls = False # bool |  (optional) (default to False)
    return_vectors = False # bool |  (optional) (default to False)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Execute Adhoc Retriever
        api_response = api_instance.execute_adhoc_retriever(adhoc_execute_request, return_presigned_urls=return_presigned_urls, return_vectors=return_vectors, authorization=authorization, x_namespace=x_namespace)
        print("The response of AdhocRetrieversApi->execute_adhoc_retriever:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdhocRetrieversApi->execute_adhoc_retriever: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **adhoc_execute_request** | [**AdhocExecuteRequest**](AdhocExecuteRequest.md)|  | 
 **return_presigned_urls** | **bool**|  | [optional] [default to False]
 **return_vectors** | **bool**|  | [optional] [default to False]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

**object**

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

# **get_adhoc_execution_retrievers**
> AdhocExecutionDetail get_adhoc_execution_retrievers(execution_id, authorization=authorization, x_namespace=x_namespace)

Get Adhoc Execution

Get detailed execution information for a specific ad-hoc retriever execution.

Returns comprehensive execution details including:
    - Execution metadata (status, duration, credits used)
    - Performance metrics (documents processed/returned, cache hit rate)
    - Input data and query summary
    - Stage completion information
    - Collections queried

Use Cases:
    - Debug specific ad-hoc executions
    - Analyze performance of a particular query
    - Retrieve execution inputs for reproduction
    - Audit ad-hoc retriever usage

Raises:
    404 NotFoundError: If execution not found or not an ad-hoc execution

### Example


```python
import mixpeek
from mixpeek.models.adhoc_execution_detail import AdhocExecutionDetail
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
    api_instance = mixpeek.AdhocRetrieversApi(api_client)
    execution_id = 'execution_id_example' # str | Execution identifier.
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Adhoc Execution
        api_response = api_instance.get_adhoc_execution_retrievers(execution_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of AdhocRetrieversApi->get_adhoc_execution_retrievers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdhocRetrieversApi->get_adhoc_execution_retrievers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **str**| Execution identifier. | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**AdhocExecutionDetail**](AdhocExecutionDetail.md)

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

# **list_adhoc_executions_retrievers**
> ListAdhocExecutionsResponse list_adhoc_executions_retrievers(limit=limit, offset=offset, cursor=cursor, include_total=include_total, authorization=authorization, x_namespace=x_namespace, list_adhoc_executions_request=list_adhoc_executions_request)

List Adhoc Executions

List execution history for ad-hoc retrievers.

Returns execution history for all ad-hoc retriever executions in the namespace,
sorted by timestamp descending (most recent first).

Use Cases:
    - Track ad-hoc retriever usage across the namespace
    - Debug ad-hoc retriever executions
    - Analyze query patterns from ad-hoc searches
    - Monitor performance of ad-hoc executions

Filtering:
    - Filter by status (completed, failed, etc.)
    - Filter by time range (start_time, end_time)

Pagination:
    - Supports offset-based pagination via query parameters
    - Default limit: 20, max limit: 100
    - Use ?page_size=X&page_number=Y for pagination

### Example


```python
import mixpeek
from mixpeek.models.list_adhoc_executions_request import ListAdhocExecutionsRequest
from mixpeek.models.list_adhoc_executions_response import ListAdhocExecutionsResponse
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
    api_instance = mixpeek.AdhocRetrieversApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    cursor = 'cursor_example' # str |  (optional)
    include_total = False # bool |  (optional) (default to False)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)
    list_adhoc_executions_request = mixpeek.ListAdhocExecutionsRequest() # ListAdhocExecutionsRequest |  (optional)

    try:
        # List Adhoc Executions
        api_response = api_instance.list_adhoc_executions_retrievers(limit=limit, offset=offset, cursor=cursor, include_total=include_total, authorization=authorization, x_namespace=x_namespace, list_adhoc_executions_request=list_adhoc_executions_request)
        print("The response of AdhocRetrieversApi->list_adhoc_executions_retrievers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdhocRetrieversApi->list_adhoc_executions_retrievers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **cursor** | **str**|  | [optional] 
 **include_total** | **bool**|  | [optional] [default to False]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 
 **list_adhoc_executions_request** | [**ListAdhocExecutionsRequest**](ListAdhocExecutionsRequest.md)|  | [optional] 

### Return type

[**ListAdhocExecutionsResponse**](ListAdhocExecutionsResponse.md)

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

