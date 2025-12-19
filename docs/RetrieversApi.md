# mixpeek.RetrieversApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_retriever**](RetrieversApi.md#create_retriever) | **POST** /v1/retrievers | Create Retriever
[**debug_inference_retrievers**](RetrieversApi.md#debug_inference_retrievers) | **POST** /v1/retrievers/debug-inference | Debug Inference
[**delete_retriever**](RetrieversApi.md#delete_retriever) | **DELETE** /v1/retrievers/{retriever_identifier} | Delete Retriever
[**execute_retriever**](RetrieversApi.md#execute_retriever) | **POST** /v1/retrievers/{retriever_identifier}/execute | Execute Retriever
[**get_retriever**](RetrieversApi.md#get_retriever) | **GET** /v1/retrievers/{retriever_identifier} | Get Retriever
[**list_retrievers**](RetrieversApi.md#list_retrievers) | **POST** /v1/retrievers/list | List Retrievers


# **create_retriever**
> RetrieverModelOutput create_retriever(create_retriever_request, authorization=authorization, x_namespace=x_namespace)

Create Retriever

Create retriever.

### Example


```python
import mixpeek
from mixpeek.models.create_retriever_request import CreateRetrieverRequest
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
    create_retriever_request = mixpeek.CreateRetrieverRequest() # CreateRetrieverRequest | 
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)
    x_namespace = 'x_namespace_example' # str | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. (optional)

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
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 
 **x_namespace** | **str**| Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: &#39;netflix_prod&#39; or &#39;ns_1234567890&#39;. To create a namespace, use the /namespaces endpoint. | [optional] 

### Return type

[**RetrieverModelOutput**](RetrieverModelOutput.md)

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

# **debug_inference_retrievers**
> DebugInferenceResponse debug_inference_retrievers(inference_request, authorization=authorization, x_namespace=x_namespace)

Debug Inference

Debug inference by directly calling the inference API.

### Example


```python
import mixpeek
from mixpeek.models.debug_inference_response import DebugInferenceResponse
from mixpeek.models.inference_request import InferenceRequest
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
    inference_request = mixpeek.InferenceRequest() # InferenceRequest | 
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)
    x_namespace = 'x_namespace_example' # str | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. (optional)

    try:
        # Debug Inference
        api_response = api_instance.debug_inference_retrievers(inference_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of RetrieversApi->debug_inference_retrievers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrieversApi->debug_inference_retrievers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inference_request** | [**InferenceRequest**](InferenceRequest.md)|  | 
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 
 **x_namespace** | **str**| Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: &#39;netflix_prod&#39; or &#39;ns_1234567890&#39;. To create a namespace, use the /namespaces endpoint. | [optional] 

### Return type

[**DebugInferenceResponse**](DebugInferenceResponse.md)

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
> GenericDeleteResponse delete_retriever(retriever_identifier, authorization=authorization, x_namespace=x_namespace)

Delete Retriever

This endpoint allows you to delete a retriever by ID or name.

### Example


```python
import mixpeek
from mixpeek.models.generic_delete_response import GenericDeleteResponse
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
    retriever_identifier = 'retriever_identifier_example' # str | The ID or name of the retriever.
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)
    x_namespace = 'x_namespace_example' # str | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. (optional)

    try:
        # Delete Retriever
        api_response = api_instance.delete_retriever(retriever_identifier, authorization=authorization, x_namespace=x_namespace)
        print("The response of RetrieversApi->delete_retriever:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrieversApi->delete_retriever: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retriever_identifier** | **str**| The ID or name of the retriever. | 
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 
 **x_namespace** | **str**| Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: &#39;netflix_prod&#39; or &#39;ns_1234567890&#39;. To create a namespace, use the /namespaces endpoint. | [optional] 

### Return type

[**GenericDeleteResponse**](GenericDeleteResponse.md)

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
> RetrieverResponse execute_retriever(retriever_identifier, retriever_query_request, if_none_match=if_none_match, authorization=authorization, x_namespace=x_namespace)

Execute Retriever

Execute retriever with caching support.

### Example


```python
import mixpeek
from mixpeek.models.retriever_query_request import RetrieverQueryRequest
from mixpeek.models.retriever_response import RetrieverResponse
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
    retriever_identifier = 'retriever_identifier_example' # str | The ID or name of the retriever.
    retriever_query_request = mixpeek.RetrieverQueryRequest() # RetrieverQueryRequest | 
    if_none_match = 'if_none_match_example' # str | ETag for cache validation (optional)
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)
    x_namespace = 'x_namespace_example' # str | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. (optional)

    try:
        # Execute Retriever
        api_response = api_instance.execute_retriever(retriever_identifier, retriever_query_request, if_none_match=if_none_match, authorization=authorization, x_namespace=x_namespace)
        print("The response of RetrieversApi->execute_retriever:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrieversApi->execute_retriever: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retriever_identifier** | **str**| The ID or name of the retriever. | 
 **retriever_query_request** | [**RetrieverQueryRequest**](RetrieverQueryRequest.md)|  | 
 **if_none_match** | **str**| ETag for cache validation | [optional] 
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 
 **x_namespace** | **str**| Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: &#39;netflix_prod&#39; or &#39;ns_1234567890&#39;. To create a namespace, use the /namespaces endpoint. | [optional] 

### Return type

[**RetrieverResponse**](RetrieverResponse.md)

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

# **get_retriever**
> RetrieverModelOutput get_retriever(retriever_identifier, expand_collections=expand_collections, authorization=authorization, x_namespace=x_namespace)

Get Retriever

Get retriever with optional expanded collection details.

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
    retriever_identifier = 'retriever_identifier_example' # str | The ID or name of the retriever.
    expand_collections = False # bool |  (optional) (default to False)
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)
    x_namespace = 'x_namespace_example' # str | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. (optional)

    try:
        # Get Retriever
        api_response = api_instance.get_retriever(retriever_identifier, expand_collections=expand_collections, authorization=authorization, x_namespace=x_namespace)
        print("The response of RetrieversApi->get_retriever:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrieversApi->get_retriever: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retriever_identifier** | **str**| The ID or name of the retriever. | 
 **expand_collections** | **bool**|  | [optional] [default to False]
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 
 **x_namespace** | **str**| Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: &#39;netflix_prod&#39; or &#39;ns_1234567890&#39;. To create a namespace, use the /namespaces endpoint. | [optional] 

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

# **list_retrievers**
> ListRetrieversResponse list_retrievers(authorization=authorization, x_namespace=x_namespace, list_retrievers_request=list_retrievers_request)

List Retrievers

This endpoint allows you to list retrievers.

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
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)
    x_namespace = 'x_namespace_example' # str | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. (optional)
    list_retrievers_request = mixpeek.ListRetrieversRequest() # ListRetrieversRequest |  (optional)

    try:
        # List Retrievers
        api_response = api_instance.list_retrievers(authorization=authorization, x_namespace=x_namespace, list_retrievers_request=list_retrievers_request)
        print("The response of RetrieversApi->list_retrievers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrieversApi->list_retrievers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 
 **x_namespace** | **str**| Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: &#39;netflix_prod&#39; or &#39;ns_1234567890&#39;. To create a namespace, use the /namespaces endpoint. | [optional] 
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

