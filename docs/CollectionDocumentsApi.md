# mixpeek.CollectionDocumentsApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_document**](CollectionDocumentsApi.md#create_document) | **POST** /v1/collections/{collection_identifier}/documents | Create a document.
[**delete_document**](CollectionDocumentsApi.md#delete_document) | **DELETE** /v1/collections/{collection_identifier}/documents/{document_id} | Delete a document by ID.
[**get_document**](CollectionDocumentsApi.md#get_document) | **GET** /v1/collections/{collection_identifier}/documents/{document_id} | Get a document by ID.
[**list_documents**](CollectionDocumentsApi.md#list_documents) | **POST** /v1/collections/{collection_identifier}/documents/list | List documents.
[**update_document**](CollectionDocumentsApi.md#update_document) | **PUT** /v1/collections/{collection_identifier}/documents/{document_id} | Update Document


# **create_document**
> DocumentResponse create_document(collection_identifier, document_create_request, authorization=authorization, x_namespace=x_namespace)

Create a document.

Create a document by ID.

### Example


```python
import mixpeek
from mixpeek.models.document_create_request import DocumentCreateRequest
from mixpeek.models.document_response import DocumentResponse
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
    api_instance = mixpeek.CollectionDocumentsApi(api_client)
    collection_identifier = 'collection_identifier_example' # str | The ID of the collection.
    document_create_request = mixpeek.DocumentCreateRequest() # DocumentCreateRequest | 
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)
    x_namespace = 'x_namespace_example' # str | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. (optional)

    try:
        # Create a document.
        api_response = api_instance.create_document(collection_identifier, document_create_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of CollectionDocumentsApi->create_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionDocumentsApi->create_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_identifier** | **str**| The ID of the collection. | 
 **document_create_request** | [**DocumentCreateRequest**](DocumentCreateRequest.md)|  | 
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 
 **x_namespace** | **str**| Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: &#39;netflix_prod&#39; or &#39;ns_1234567890&#39;. To create a namespace, use the /namespaces endpoint. | [optional] 

### Return type

[**DocumentResponse**](DocumentResponse.md)

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

# **delete_document**
> GenericDeleteResponse delete_document(collection_identifier, document_id, authorization=authorization, x_namespace=x_namespace)

Delete a document by ID.

Delete a document by ID.

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
    api_instance = mixpeek.CollectionDocumentsApi(api_client)
    collection_identifier = 'collection_identifier_example' # str | The ID of the collection.
    document_id = 'document_id_example' # str | The ID of the document to delete.
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)
    x_namespace = 'x_namespace_example' # str | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. (optional)

    try:
        # Delete a document by ID.
        api_response = api_instance.delete_document(collection_identifier, document_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of CollectionDocumentsApi->delete_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionDocumentsApi->delete_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_identifier** | **str**| The ID of the collection. | 
 **document_id** | **str**| The ID of the document to delete. | 
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

# **get_document**
> DocumentResponse get_document(collection_identifier, document_id, return_url=return_url, return_vectors=return_vectors, authorization=authorization, x_namespace=x_namespace)

Get a document by ID.

Get a document by ID.

### Example


```python
import mixpeek
from mixpeek.models.document_response import DocumentResponse
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
    api_instance = mixpeek.CollectionDocumentsApi(api_client)
    collection_identifier = 'collection_identifier_example' # str | The ID of the collection.
    document_id = 'document_id_example' # str | The ID of the document to retrieve.
    return_url = False # bool |  (optional) (default to False)
    return_vectors = False # bool |  (optional) (default to False)
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)
    x_namespace = 'x_namespace_example' # str | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. (optional)

    try:
        # Get a document by ID.
        api_response = api_instance.get_document(collection_identifier, document_id, return_url=return_url, return_vectors=return_vectors, authorization=authorization, x_namespace=x_namespace)
        print("The response of CollectionDocumentsApi->get_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionDocumentsApi->get_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_identifier** | **str**| The ID of the collection. | 
 **document_id** | **str**| The ID of the document to retrieve. | 
 **return_url** | **bool**|  | [optional] [default to False]
 **return_vectors** | **bool**|  | [optional] [default to False]
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 
 **x_namespace** | **str**| Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: &#39;netflix_prod&#39; or &#39;ns_1234567890&#39;. To create a namespace, use the /namespaces endpoint. | [optional] 

### Return type

[**DocumentResponse**](DocumentResponse.md)

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

# **list_documents**
> ListDocumentsResponse list_documents(collection_identifier, limit=limit, offset=offset, authorization=authorization, x_namespace=x_namespace, list_documents_request=list_documents_request)

List documents.

List documents.

### Example


```python
import mixpeek
from mixpeek.models.list_documents_request import ListDocumentsRequest
from mixpeek.models.list_documents_response import ListDocumentsResponse
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
    api_instance = mixpeek.CollectionDocumentsApi(api_client)
    collection_identifier = 'collection_identifier_example' # str | The ID of the collection to list documents from.
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)
    x_namespace = 'x_namespace_example' # str | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. (optional)
    list_documents_request = mixpeek.ListDocumentsRequest() # ListDocumentsRequest |  (optional)

    try:
        # List documents.
        api_response = api_instance.list_documents(collection_identifier, limit=limit, offset=offset, authorization=authorization, x_namespace=x_namespace, list_documents_request=list_documents_request)
        print("The response of CollectionDocumentsApi->list_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionDocumentsApi->list_documents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_identifier** | **str**| The ID of the collection to list documents from. | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 
 **x_namespace** | **str**| Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: &#39;netflix_prod&#39; or &#39;ns_1234567890&#39;. To create a namespace, use the /namespaces endpoint. | [optional] 
 **list_documents_request** | [**ListDocumentsRequest**](ListDocumentsRequest.md)|  | [optional] 

### Return type

[**ListDocumentsResponse**](ListDocumentsResponse.md)

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

# **update_document**
> DocumentResponse update_document(collection_identifier, document_id, document_update_request, authorization=authorization, x_namespace=x_namespace)

Update Document

Update a document by ID.

### Example


```python
import mixpeek
from mixpeek.models.document_response import DocumentResponse
from mixpeek.models.document_update_request import DocumentUpdateRequest
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
    api_instance = mixpeek.CollectionDocumentsApi(api_client)
    collection_identifier = 'collection_identifier_example' # str | The ID of the collection.
    document_id = 'document_id_example' # str | The ID of the document to update.
    document_update_request = mixpeek.DocumentUpdateRequest() # DocumentUpdateRequest | 
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)
    x_namespace = 'x_namespace_example' # str | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. (optional)

    try:
        # Update Document
        api_response = api_instance.update_document(collection_identifier, document_id, document_update_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of CollectionDocumentsApi->update_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionDocumentsApi->update_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_identifier** | **str**| The ID of the collection. | 
 **document_id** | **str**| The ID of the document to update. | 
 **document_update_request** | [**DocumentUpdateRequest**](DocumentUpdateRequest.md)|  | 
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 
 **x_namespace** | **str**| Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: &#39;netflix_prod&#39; or &#39;ns_1234567890&#39;. To create a namespace, use the /namespaces endpoint. | [optional] 

### Return type

[**DocumentResponse**](DocumentResponse.md)

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

