# mixpeek.EvaluationsApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_evaluation_retrievers**](EvaluationsApi.md#get_evaluation_retrievers) | **GET** /v1/retrievers/{retriever_id}/evaluations/{evaluation_id} | Get evaluation results
[**list_evaluations_retrievers**](EvaluationsApi.md#list_evaluations_retrievers) | **GET** /v1/retrievers/{retriever_id}/evaluations | List evaluations
[**start_evaluation_retrievers**](EvaluationsApi.md#start_evaluation_retrievers) | **POST** /v1/retrievers/{retriever_id}/evaluations | Run evaluation


# **get_evaluation_retrievers**
> EvaluationRecord get_evaluation_retrievers(retriever_id, evaluation_id, authorization=authorization, x_namespace=x_namespace)

Get evaluation results

Retrieve evaluation results with all calculated metrics

### Example


```python
import mixpeek
from mixpeek.models.evaluation_record import EvaluationRecord
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
    api_instance = mixpeek.EvaluationsApi(api_client)
    retriever_id = 'retriever_id_example' # str | 
    evaluation_id = 'evaluation_id_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get evaluation results
        api_response = api_instance.get_evaluation_retrievers(retriever_id, evaluation_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of EvaluationsApi->get_evaluation_retrievers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EvaluationsApi->get_evaluation_retrievers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retriever_id** | **str**|  | 
 **evaluation_id** | **str**|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**EvaluationRecord**](EvaluationRecord.md)

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

# **list_evaluations_retrievers**
> EvaluationListResponse list_evaluations_retrievers(retriever_id, status=status, dataset_name=dataset_name, page=page, page_size=page_size, authorization=authorization, x_namespace=x_namespace)

List evaluations

List all evaluations for a retriever with optional filters

### Example


```python
import mixpeek
from mixpeek.models.evaluation_list_response import EvaluationListResponse
from mixpeek.models.evaluation_status import EvaluationStatus
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
    api_instance = mixpeek.EvaluationsApi(api_client)
    retriever_id = 'retriever_id_example' # str | 
    status = mixpeek.EvaluationStatus() # EvaluationStatus | Filter by status (pending, in_progress, completed, failed) (optional)
    dataset_name = 'dataset_name_example' # str | Filter by dataset name (optional)
    page = 1 # int | Page number (1-indexed) (optional) (default to 1)
    page_size = 20 # int | Items per page (optional) (default to 20)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # List evaluations
        api_response = api_instance.list_evaluations_retrievers(retriever_id, status=status, dataset_name=dataset_name, page=page, page_size=page_size, authorization=authorization, x_namespace=x_namespace)
        print("The response of EvaluationsApi->list_evaluations_retrievers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EvaluationsApi->list_evaluations_retrievers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retriever_id** | **str**|  | 
 **status** | [**EvaluationStatus**](.md)| Filter by status (pending, in_progress, completed, failed) | [optional] 
 **dataset_name** | **str**| Filter by dataset name | [optional] 
 **page** | **int**| Page number (1-indexed) | [optional] [default to 1]
 **page_size** | **int**| Items per page | [optional] [default to 20]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**EvaluationListResponse**](EvaluationListResponse.md)

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

# **start_evaluation_retrievers**
> StartEvaluationResponse start_evaluation_retrievers(retriever_id, start_evaluation_request, authorization=authorization, x_namespace=x_namespace)

Run evaluation

Evaluate a retriever's quality using a ground truth dataset. Returns immediately with a task ID - evaluation runs asynchronously.

### Example


```python
import mixpeek
from mixpeek.models.start_evaluation_request import StartEvaluationRequest
from mixpeek.models.start_evaluation_response import StartEvaluationResponse
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
    api_instance = mixpeek.EvaluationsApi(api_client)
    retriever_id = 'retriever_id_example' # str | 
    start_evaluation_request = mixpeek.StartEvaluationRequest() # StartEvaluationRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Run evaluation
        api_response = api_instance.start_evaluation_retrievers(retriever_id, start_evaluation_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of EvaluationsApi->start_evaluation_retrievers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EvaluationsApi->start_evaluation_retrievers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retriever_id** | **str**|  | 
 **start_evaluation_request** | [**StartEvaluationRequest**](StartEvaluationRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**StartEvaluationResponse**](StartEvaluationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

