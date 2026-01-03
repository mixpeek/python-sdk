# mixpeek.EvaluationDatasetsApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dataset_retrievers_evaluations**](EvaluationDatasetsApi.md#create_dataset_retrievers_evaluations) | **POST** /v1/retrievers/evaluations/datasets | Create evaluation dataset
[**get_dataset_retrievers_evaluations**](EvaluationDatasetsApi.md#get_dataset_retrievers_evaluations) | **GET** /v1/retrievers/evaluations/datasets/{dataset_identifier} | Get evaluation dataset
[**list_datasets_retrievers_evaluations**](EvaluationDatasetsApi.md#list_datasets_retrievers_evaluations) | **GET** /v1/retrievers/evaluations/datasets | List evaluation datasets


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
    api_instance = mixpeek.EvaluationDatasetsApi(api_client)
    create_dataset_request = mixpeek.CreateDatasetRequest() # CreateDatasetRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Create evaluation dataset
        api_response = api_instance.create_dataset_retrievers_evaluations(create_dataset_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of EvaluationDatasetsApi->create_dataset_retrievers_evaluations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EvaluationDatasetsApi->create_dataset_retrievers_evaluations: %s\n" % e)
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
    api_instance = mixpeek.EvaluationDatasetsApi(api_client)
    dataset_identifier = 'dataset_identifier_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get evaluation dataset
        api_response = api_instance.get_dataset_retrievers_evaluations(dataset_identifier, authorization=authorization, x_namespace=x_namespace)
        print("The response of EvaluationDatasetsApi->get_dataset_retrievers_evaluations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EvaluationDatasetsApi->get_dataset_retrievers_evaluations: %s\n" % e)
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
    api_instance = mixpeek.EvaluationDatasetsApi(api_client)
    page = 1 # int | Page number (1-indexed) (optional) (default to 1)
    page_size = 20 # int | Items per page (optional) (default to 20)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # List evaluation datasets
        api_response = api_instance.list_datasets_retrievers_evaluations(page=page, page_size=page_size, authorization=authorization, x_namespace=x_namespace)
        print("The response of EvaluationDatasetsApi->list_datasets_retrievers_evaluations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EvaluationDatasetsApi->list_datasets_retrievers_evaluations: %s\n" % e)
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

