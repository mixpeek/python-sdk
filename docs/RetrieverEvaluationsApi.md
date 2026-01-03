# mixpeek.RetrieverEvaluationsApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dataset_retrievers_evaluations**](RetrieverEvaluationsApi.md#create_dataset_retrievers_evaluations) | **POST** /v1/retrievers/evaluations/datasets | Create evaluation dataset
[**get_dataset_retrievers_evaluations**](RetrieverEvaluationsApi.md#get_dataset_retrievers_evaluations) | **GET** /v1/retrievers/evaluations/datasets/{dataset_identifier} | Get evaluation dataset
[**get_evaluation_retrievers**](RetrieverEvaluationsApi.md#get_evaluation_retrievers) | **GET** /v1/retrievers/{retriever_id}/evaluations/{evaluation_id} | Get evaluation results
[**list_datasets_retrievers_evaluations**](RetrieverEvaluationsApi.md#list_datasets_retrievers_evaluations) | **GET** /v1/retrievers/evaluations/datasets | List evaluation datasets
[**list_evaluations_retrievers**](RetrieverEvaluationsApi.md#list_evaluations_retrievers) | **GET** /v1/retrievers/{retriever_id}/evaluations | List evaluations
[**start_evaluation_retrievers**](RetrieverEvaluationsApi.md#start_evaluation_retrievers) | **POST** /v1/retrievers/{retriever_id}/evaluations | Run evaluation


# **create_dataset_retrievers_evaluations**
> EvaluationDataset create_dataset_retrievers_evaluations(create_dataset_request, authorization=authorization, x_namespace=x_namespace)

Create evaluation dataset

Create a ground truth dataset for evaluating retrievers. Include queries with their relevant documents and optional graded relevance scores.

### Example


```python
import mixpeek
from mixpeek.models.create_dataset_request import CreateDatasetRequest
from mixpeek.models.evaluation_dataset import EvaluationDataset
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
    api_instance = mixpeek.RetrieverEvaluationsApi(api_client)
    create_dataset_request = mixpeek.CreateDatasetRequest() # CreateDatasetRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Create evaluation dataset
        api_response = api_instance.create_dataset_retrievers_evaluations(create_dataset_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of RetrieverEvaluationsApi->create_dataset_retrievers_evaluations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrieverEvaluationsApi->create_dataset_retrievers_evaluations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_dataset_request** | [**CreateDatasetRequest**](CreateDatasetRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**EvaluationDataset**](EvaluationDataset.md)

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

# **get_dataset_retrievers_evaluations**
> EvaluationDataset get_dataset_retrievers_evaluations(dataset_identifier, authorization=authorization, x_namespace=x_namespace)

Get evaluation dataset

Retrieve a specific dataset by ID or name

### Example


```python
import mixpeek
from mixpeek.models.evaluation_dataset import EvaluationDataset
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
    api_instance = mixpeek.RetrieverEvaluationsApi(api_client)
    dataset_identifier = 'dataset_identifier_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get evaluation dataset
        api_response = api_instance.get_dataset_retrievers_evaluations(dataset_identifier, authorization=authorization, x_namespace=x_namespace)
        print("The response of RetrieverEvaluationsApi->get_dataset_retrievers_evaluations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrieverEvaluationsApi->get_dataset_retrievers_evaluations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_identifier** | **str**|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**EvaluationDataset**](EvaluationDataset.md)

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
    api_instance = mixpeek.RetrieverEvaluationsApi(api_client)
    retriever_id = 'retriever_id_example' # str | 
    evaluation_id = 'evaluation_id_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get evaluation results
        api_response = api_instance.get_evaluation_retrievers(retriever_id, evaluation_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of RetrieverEvaluationsApi->get_evaluation_retrievers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrieverEvaluationsApi->get_evaluation_retrievers: %s\n" % e)
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

# **list_datasets_retrievers_evaluations**
> DatasetListResponse list_datasets_retrievers_evaluations(page=page, page_size=page_size, authorization=authorization, x_namespace=x_namespace)

List evaluation datasets

List all evaluation datasets with pagination

### Example


```python
import mixpeek
from mixpeek.models.dataset_list_response import DatasetListResponse
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
    api_instance = mixpeek.RetrieverEvaluationsApi(api_client)
    page = 1 # int | Page number (1-indexed) (optional) (default to 1)
    page_size = 20 # int | Items per page (optional) (default to 20)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # List evaluation datasets
        api_response = api_instance.list_datasets_retrievers_evaluations(page=page, page_size=page_size, authorization=authorization, x_namespace=x_namespace)
        print("The response of RetrieverEvaluationsApi->list_datasets_retrievers_evaluations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrieverEvaluationsApi->list_datasets_retrievers_evaluations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number (1-indexed) | [optional] [default to 1]
 **page_size** | **int**| Items per page | [optional] [default to 20]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**DatasetListResponse**](DatasetListResponse.md)

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
    api_instance = mixpeek.RetrieverEvaluationsApi(api_client)
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
        print("The response of RetrieverEvaluationsApi->list_evaluations_retrievers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrieverEvaluationsApi->list_evaluations_retrievers: %s\n" % e)
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
    api_instance = mixpeek.RetrieverEvaluationsApi(api_client)
    retriever_id = 'retriever_id_example' # str | 
    start_evaluation_request = mixpeek.StartEvaluationRequest() # StartEvaluationRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Run evaluation
        api_response = api_instance.start_evaluation_retrievers(retriever_id, start_evaluation_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of RetrieverEvaluationsApi->start_evaluation_retrievers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrieverEvaluationsApi->start_evaluation_retrievers: %s\n" % e)
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

