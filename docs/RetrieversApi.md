# mixpeek.RetrieversApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clone_retriever**](RetrieversApi.md#clone_retriever) | **POST** /v1/retrievers/{retriever_id}/clone | Clone Retriever
[**create_retriever**](RetrieversApi.md#create_retriever) | **POST** /v1/retrievers | Create Retriever
[**delete_retriever**](RetrieversApi.md#delete_retriever) | **DELETE** /v1/retrievers/{retriever_id} | Delete Retriever
[**execute_retriever**](RetrieversApi.md#execute_retriever) | **POST** /v1/retrievers/{retriever_id}/execute | Execute Retriever (Auto-Optimized)
[**explain_retriever_execution_id_execute**](RetrieversApi.md#explain_retriever_execution_id_execute) | **POST** /v1/retrievers/{retriever_id}/execute/explain | Explain Retriever Execution Plan
[**get_execution_retrievers**](RetrieversApi.md#get_execution_retrievers) | **GET** /v1/retrievers/{retriever_id}/executions/{execution_id} | Get Execution
[**get_retriever**](RetrieversApi.md#get_retriever) | **GET** /v1/retrievers/{retriever_id} | Get Retriever
[**list_executions_retrievers**](RetrieversApi.md#list_executions_retrievers) | **POST** /v1/retrievers/{retriever_id}/executions/list | List Executions
[**list_retrievers**](RetrieversApi.md#list_retrievers) | **POST** /v1/retrievers/list | List Retrievers
[**patch_retriever**](RetrieversApi.md#patch_retriever) | **PATCH** /v1/retrievers/{retriever_id} | Patch Retriever


# **clone_retriever**
> CloneRetrieverResponse clone_retriever(retriever_id, clone_retriever_request, authorization=authorization, x_namespace=x_namespace)

Clone Retriever

Clone a retriever with optional modifications.

**Purpose:**
Creates a NEW retriever (with new ID) based on an existing one. This is the
recommended way to iterate on retriever designs when you need to modify core
logic that PATCH doesn't allow (stages, input_schema, collections).

**Clone vs PATCH vs Template:**
- **PATCH**: Update metadata only (name, description, tags, display_config)
- **Clone**: Copy and modify core logic (stages, input_schema, collections)
- **Template**: Start from a pre-configured pattern (for new projects)

**Common Use Cases:**
- Fix a typo in a stage name
- Add or remove stages
- Change target collections
- Create variants (e.g., "strict" vs "relaxed" versions)
- Test modifications before replacing production retriever

**How it works:**
1. Source retriever is copied
2. You provide a new name (REQUIRED)
3. Optionally override any other fields
4. A new retriever is created with a new ID
5. Original retriever remains unchanged

**All fields except retriever_name are OPTIONAL:**
- Omit a field to copy from source
- Provide a field to override the source value

### Example


```python
import mixpeek
from mixpeek.models.clone_retriever_request import CloneRetrieverRequest
from mixpeek.models.clone_retriever_response import CloneRetrieverResponse
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
    api_instance = mixpeek.RetrieversApi(api_client)
    retriever_id = 'retriever_id_example' # str | Source retriever ID or name to clone.
    clone_retriever_request = mixpeek.CloneRetrieverRequest() # CloneRetrieverRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Clone Retriever
        api_response = api_instance.clone_retriever(retriever_id, clone_retriever_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of RetrieversApi->clone_retriever:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrieversApi->clone_retriever: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retriever_id** | **str**| Source retriever ID or name to clone. | 
 **clone_retriever_request** | [**CloneRetrieverRequest**](CloneRetrieverRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**CloneRetrieverResponse**](CloneRetrieverResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_retriever**
> CreateRetrieverResponse create_retriever(create_retriever_request, authorization=authorization, x_namespace=x_namespace)

Create Retriever

Create a new retriever.

A retriever executes a series of stages to find and process documents
from one or more collections.

### Example


```python
import mixpeek
from mixpeek.models.create_retriever_request import CreateRetrieverRequest
from mixpeek.models.create_retriever_response import CreateRetrieverResponse
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
    api_instance = mixpeek.RetrieversApi(api_client)
    create_retriever_request = mixpeek.CreateRetrieverRequest() # CreateRetrieverRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Create Retriever
        api_response = api_instance.create_retriever(create_retriever_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of RetrieversApi->create_retriever:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrieversApi->create_retriever: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_retriever_request** | [**CreateRetrieverRequest**](CreateRetrieverRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**CreateRetrieverResponse**](CreateRetrieverResponse.md)

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

# **delete_retriever**
> object delete_retriever(retriever_id, authorization=authorization, x_namespace=x_namespace)

Delete Retriever

Delete a retriever and all its resources comprehensively.

Deletes:
- Published retrievers
- Execution history
- Interactions (user feedback)
- Evaluations
- Cache entries
- Retriever metadata

The deletion is performed synchronously and returns when complete.

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
    api_instance = mixpeek.RetrieversApi(api_client)
    retriever_id = 'retriever_id_example' # str | Retriever ID or name.
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Delete Retriever
        api_response = api_instance.delete_retriever(retriever_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of RetrieversApi->delete_retriever:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrieversApi->delete_retriever: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retriever_id** | **str**| Retriever ID or name. | 
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

# **execute_retriever**
> object execute_retriever(retriever_id, execute_retriever_request, return_presigned_urls=return_presigned_urls, return_vectors=return_vectors, authorization=authorization, x_namespace=x_namespace)

Execute Retriever (Auto-Optimized)

Execute a retriever and return matching documents. The pipeline is automatically optimized before execution for best performance.

**Automatic Optimization:**
Your pipeline stages are automatically transformed for optimal performance:
- Filters pushed down to reduce expensive operations
- Redundant stages merged or eliminated
- Grouping operations pushed to database layer (10-100x faster)
- Operations reordered for efficiency

**Streaming Support:**
Set stream=true in the request body to receive real-time stage updates via SSE:
- Response uses text/event-stream content type
- Each stage emits stage_start and stage_complete events
- Final event contains complete results and pagination
- Useful for progress tracking and debugging

**Response Includes (when stream=false):**
- documents: Final matching documents
- pagination: Pagination metadata
- stage_statistics: Per-stage execution metrics
- budget: Credit/time consumption
- optimization_applied: Whether optimizations were applied
- optimization_summary: Details about transformations (when applied)

**Optimization Summary Example:**
```json
{
  "optimization_applied": true,
  "optimization_summary": {
    "original_stage_count": 5,
    "optimized_stage_count": 3,
    "optimization_time_ms": 8.2,
    "rules_applied": ["push_down_filters", "group_by_push_down"],
    "stage_reduction_pct": 40.0
  }
}
```

Use the /explain endpoint to see the optimized execution plan before running.

### Example


```python
import mixpeek
from mixpeek.models.execute_retriever_request import ExecuteRetrieverRequest
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
    api_instance = mixpeek.RetrieversApi(api_client)
    retriever_id = 'retriever_id_example' # str | Retriever ID or name. Pipeline will be automatically optimized before execution.
    execute_retriever_request = mixpeek.ExecuteRetrieverRequest() # ExecuteRetrieverRequest | 
    return_presigned_urls = False # bool |  (optional) (default to False)
    return_vectors = False # bool |  (optional) (default to False)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Execute Retriever (Auto-Optimized)
        api_response = api_instance.execute_retriever(retriever_id, execute_retriever_request, return_presigned_urls=return_presigned_urls, return_vectors=return_vectors, authorization=authorization, x_namespace=x_namespace)
        print("The response of RetrieversApi->execute_retriever:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrieversApi->execute_retriever: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retriever_id** | **str**| Retriever ID or name. Pipeline will be automatically optimized before execution. | 
 **execute_retriever_request** | [**ExecuteRetrieverRequest**](ExecuteRetrieverRequest.md)|  | 
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
**200** | Execution results with documents, pagination, statistics, and optimization details. When stream&#x3D;true, returns Server-Sent Events. When stream&#x3D;false, returns JSON response. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **explain_retriever_execution_id_execute**
> ExplainRetrieverResponse explain_retriever_execution_id_execute(retriever_id, explain_retriever_request, authorization=authorization, x_namespace=x_namespace)

Explain Retriever Execution Plan

Get a detailed execution plan for a retriever without actually executing it. Similar to MongoDB's explain plan or SQL's EXPLAIN command, this endpoint helps you understand performance characteristics, identify bottlenecks, estimate costs, and troubleshoot retrieval issues before running expensive queries.

**What This Returns:**
- Stage-by-stage execution plan (AFTER automatic optimizations)
- Estimated costs (credits + time per stage)
- Document flow projections (input/output counts per stage)
- Efficiency metrics (selectivity ratios, cache likelihood)
- Bottleneck identification (slowest/most expensive stages)
- Optimization details (transformations applied by the optimizer)
- Performance warnings and improvement suggestions


**Key Features:**
- **Cost Estimation**: See how many credits and milliseconds each stage will consume
- **Bottleneck Detection**: Identify which stages dominate execution time
- **Optimization Transparency**: Understand how your pipeline was optimized
- **Cache Analysis**: See which stages are likely to hit cache
- **Accuracy Troubleshooting**: Analyze stage efficiency and document flow
- **Latency Analysis**: Break down estimated duration by stage


**Important:** The execution_plan shows OPTIMIZED stages (after automatic transformations like filter push-down, stage fusion, and grouping optimization). Check optimization_details to understand what changed from your original configuration.


**Use Cases:**
- Debug slow retrievers by identifying bottleneck stages
- Estimate costs before running expensive queries
- Understand how the optimizer transformed your pipeline
- Troubleshoot accuracy issues by analyzing stage selectivity
- Compare different retriever configurations
- Plan budget allocation for production workloads


**Example Response:**
```json
{
  "retriever_id": "ret_abc123",
  "retriever_name": "product_search",
  "execution_plan": [
    {
      "stage_index": 0,
      "stage_name": "attribute_filter",
      "stage_type": "filter",
      "estimated_input": 10000,
      "estimated_output": 5000,
      "estimated_efficiency": 0.5,
      "estimated_cost_credits": 0.01,
      "estimated_duration_ms": 20,
      "cache_likely": true,
      "optimization_notes": ["Pushed down from stage 2"],
      "warnings": []
    },
    {
      "stage_index": 1,
      "stage_name": "semantic_search",
      "stage_type": "filter",
      "estimated_input": 5000,
      "estimated_output": 100,
      "estimated_efficiency": 0.02,
      "estimated_cost_credits": 0.5,
      "estimated_duration_ms": 200,
      "cache_likely": false,
      "optimization_notes": [],
      "warnings": ["High cost stage - consider reducing limit"]
    }
  ],
  "estimated_cost": {
    "total_credits": 0.51,
    "total_duration_ms": 220
  },
  "bottleneck_stages": ["semantic_search"],
  "optimization_applied": true,
  "optimization_details": {
    "original_stage_count": 3,
    "optimized_stage_count": 2,
    "optimization_time_ms": 8.2,
    "stage_reduction_pct": 33.3,
    "decisions": [
      {
        "rule_type": "push_down_filters",
        "applied": true,
        "reason": "Moved attribute_filter before semantic_search to reduce search scope"
      }
    ]
  },
  "optimization_suggestions": [
    {
      "type": "reduce_limit",
      "stage": "semantic_search",
      "message": "Consider reducing limit to improve latency"
    }
  ]
}
```

### Example


```python
import mixpeek
from mixpeek.models.explain_retriever_request import ExplainRetrieverRequest
from mixpeek.models.explain_retriever_response import ExplainRetrieverResponse
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
    api_instance = mixpeek.RetrieversApi(api_client)
    retriever_id = 'retriever_id_example' # str | Retriever ID or name to explain. The execution plan will show the OPTIMIZED version after automatic transformations.
    explain_retriever_request = mixpeek.ExplainRetrieverRequest() # ExplainRetrieverRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Explain Retriever Execution Plan
        api_response = api_instance.explain_retriever_execution_id_execute(retriever_id, explain_retriever_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of RetrieversApi->explain_retriever_execution_id_execute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrieversApi->explain_retriever_execution_id_execute: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retriever_id** | **str**| Retriever ID or name to explain. The execution plan will show the OPTIMIZED version after automatic transformations. | 
 **explain_retriever_request** | [**ExplainRetrieverRequest**](ExplainRetrieverRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**ExplainRetrieverResponse**](ExplainRetrieverResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Detailed execution plan with stage-by-stage cost estimates, optimization details, bottleneck identification, and performance insights. Use this to troubleshoot slow queries, estimate costs, and understand optimizer transformations. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_execution_retrievers**
> ExecutionDetail get_execution_retrievers(retriever_id, execution_id, authorization=authorization, x_namespace=x_namespace)

Get Execution

Get execution details and statistics.

### Example


```python
import mixpeek
from mixpeek.models.execution_detail import ExecutionDetail
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
    api_instance = mixpeek.RetrieversApi(api_client)
    retriever_id = 'retriever_id_example' # str | Retriever ID or name.
    execution_id = 'execution_id_example' # str | Execution identifier.
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Execution
        api_response = api_instance.get_execution_retrievers(retriever_id, execution_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of RetrieversApi->get_execution_retrievers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrieversApi->get_execution_retrievers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retriever_id** | **str**| Retriever ID or name. | 
 **execution_id** | **str**| Execution identifier. | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**ExecutionDetail**](ExecutionDetail.md)

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

# **get_retriever**
> RetrieverModelOutput get_retriever(retriever_id, authorization=authorization, x_namespace=x_namespace)

Get Retriever

Get a retriever by ID or name.

### Example


```python
import mixpeek
from mixpeek.models.retriever_model_output import RetrieverModelOutput
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
    api_instance = mixpeek.RetrieversApi(api_client)
    retriever_id = 'retriever_id_example' # str | Retriever ID or name.
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Retriever
        api_response = api_instance.get_retriever(retriever_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of RetrieversApi->get_retriever:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrieversApi->get_retriever: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retriever_id** | **str**| Retriever ID or name. | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**RetrieverModelOutput**](RetrieverModelOutput.md)

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

# **list_executions_retrievers**
> ListExecutionsResponse list_executions_retrievers(retriever_id, limit=limit, offset=offset, cursor=cursor, include_total=include_total, authorization=authorization, x_namespace=x_namespace, list_executions_request=list_executions_request)

List Executions

List execution history for a retriever.

### Example


```python
import mixpeek
from mixpeek.models.list_executions_request import ListExecutionsRequest
from mixpeek.models.list_executions_response import ListExecutionsResponse
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
    api_instance = mixpeek.RetrieversApi(api_client)
    retriever_id = 'retriever_id_example' # str | Retriever ID or name.
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    cursor = 'cursor_example' # str |  (optional)
    include_total = False # bool |  (optional) (default to False)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)
    list_executions_request = mixpeek.ListExecutionsRequest() # ListExecutionsRequest |  (optional)

    try:
        # List Executions
        api_response = api_instance.list_executions_retrievers(retriever_id, limit=limit, offset=offset, cursor=cursor, include_total=include_total, authorization=authorization, x_namespace=x_namespace, list_executions_request=list_executions_request)
        print("The response of RetrieversApi->list_executions_retrievers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrieversApi->list_executions_retrievers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retriever_id** | **str**| Retriever ID or name. | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **cursor** | **str**|  | [optional] 
 **include_total** | **bool**|  | [optional] [default to False]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 
 **list_executions_request** | [**ListExecutionsRequest**](ListExecutionsRequest.md)|  | [optional] 

### Return type

[**ListExecutionsResponse**](ListExecutionsResponse.md)

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

# **list_retrievers**
> ListRetrieversResponse list_retrievers(limit=limit, offset=offset, cursor=cursor, include_total=include_total, authorization=authorization, x_namespace=x_namespace, list_retrievers_request=list_retrievers_request)

List Retrievers

List all retrievers in the namespace.

### Example


```python
import mixpeek
from mixpeek.models.list_retrievers_request import ListRetrieversRequest
from mixpeek.models.list_retrievers_response import ListRetrieversResponse
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
    api_instance = mixpeek.RetrieversApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    cursor = 'cursor_example' # str |  (optional)
    include_total = False # bool |  (optional) (default to False)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)
    list_retrievers_request = mixpeek.ListRetrieversRequest() # ListRetrieversRequest |  (optional)

    try:
        # List Retrievers
        api_response = api_instance.list_retrievers(limit=limit, offset=offset, cursor=cursor, include_total=include_total, authorization=authorization, x_namespace=x_namespace, list_retrievers_request=list_retrievers_request)
        print("The response of RetrieversApi->list_retrievers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrieversApi->list_retrievers: %s\n" % e)
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
 **list_retrievers_request** | [**ListRetrieversRequest**](ListRetrieversRequest.md)|  | [optional] 

### Return type

[**ListRetrieversResponse**](ListRetrieversResponse.md)

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

# **patch_retriever**
> PatchRetrieverResponse patch_retriever(retriever_id, patch_retriever_request, authorization=authorization, x_namespace=x_namespace)

Patch Retriever

Update a retriever's metadata.

Only metadata fields can be updated:
- name: Rename the retriever
- description: Update the description
- tags: Update tags for organization
- display_config: Update display configuration

Core logic (input_schema, stages, collection_ids) is immutable.
To modify core logic, use POST /{retriever_id}/clone instead.

### Example


```python
import mixpeek
from mixpeek.models.patch_retriever_request import PatchRetrieverRequest
from mixpeek.models.patch_retriever_response import PatchRetrieverResponse
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
    api_instance = mixpeek.RetrieversApi(api_client)
    retriever_id = 'retriever_id_example' # str | Retriever ID or name.
    patch_retriever_request = mixpeek.PatchRetrieverRequest() # PatchRetrieverRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Patch Retriever
        api_response = api_instance.patch_retriever(retriever_id, patch_retriever_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of RetrieversApi->patch_retriever:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrieversApi->patch_retriever: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retriever_id** | **str**| Retriever ID or name. | 
 **patch_retriever_request** | [**PatchRetrieverRequest**](PatchRetrieverRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**PatchRetrieverResponse**](PatchRetrieverResponse.md)

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

