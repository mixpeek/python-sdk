# mixpeek.DocumentsApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_document_ns**](DocumentsApi.md#get_document_ns) | **GET** /v1/documents/{document_id} | Get a document by ID (namespace-scoped).
[**patch_document_ns**](DocumentsApi.md#patch_document_ns) | **PATCH** /v1/documents/{document_id} | Partially update a document by ID (namespace-scoped).
[**update_document_ns**](DocumentsApi.md#update_document_ns) | **PUT** /v1/documents/{document_id} | Update a document by ID (namespace-scoped).


# **get_document_ns**
> DocumentResponse get_document_ns(document_id, return_presigned_urls=return_presigned_urls, return_vectors=return_vectors, return_vector_names=return_vector_names, authorization=authorization, authorization2=authorization2, x_namespace=x_namespace)

Get a document by ID (namespace-scoped).

Get a document by ID without specifying a collection.

Searches across all collections in the namespace. Use the
collection-scoped GET /v1/collections/{collection_id}/documents/{document_id}
when you know the collection for a faster lookup.

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
    api_instance = mixpeek.DocumentsApi(api_client)
    document_id = 'document_id_example' # str | The ID of the document to retrieve.
    return_presigned_urls = False # bool | Generate fresh presigned download URLs for all blobs with S3 storage (optional) (default to False)
    return_vectors = False # bool |  (optional) (default to False)
    return_vector_names = False # bool | Include a '_vectors' field listing available vector names (optional) (default to False)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    authorization2 = 'authorization_example' # str |  (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get a document by ID (namespace-scoped).
        api_response = api_instance.get_document_ns(document_id, return_presigned_urls=return_presigned_urls, return_vectors=return_vectors, return_vector_names=return_vector_names, authorization=authorization, authorization2=authorization2, x_namespace=x_namespace)
        print("The response of DocumentsApi->get_document_ns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->get_document_ns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| The ID of the document to retrieve. | 
 **return_presigned_urls** | **bool**| Generate fresh presigned download URLs for all blobs with S3 storage | [optional] [default to False]
 **return_vectors** | **bool**|  | [optional] [default to False]
 **return_vector_names** | **bool**| Include a &#39;_vectors&#39; field listing available vector names | [optional] [default to False]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **authorization2** | **str**|  | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

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
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_document_ns**
> DocumentResponse patch_document_ns(document_id, request_body, authorization=authorization, authorization2=authorization2, x_namespace=x_namespace)

Partially update a document by ID (namespace-scoped).

Partially update a document by ID without specifying a collection.

Only the fields provided are updated; all other fields are left unchanged.

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
    api_instance = mixpeek.DocumentsApi(api_client)
    document_id = 'document_id_example' # str | The ID of the document to patch.
    request_body = None # Dict[str, object] | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    authorization2 = 'authorization_example' # str |  (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Partially update a document by ID (namespace-scoped).
        api_response = api_instance.patch_document_ns(document_id, request_body, authorization=authorization, authorization2=authorization2, x_namespace=x_namespace)
        print("The response of DocumentsApi->patch_document_ns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->patch_document_ns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| The ID of the document to patch. | 
 **request_body** | [**Dict[str, object]**](object.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **authorization2** | **str**|  | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

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
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_document_ns**
> DocumentResponse update_document_ns(document_id, request_body, authorization=authorization, authorization2=authorization2, x_namespace=x_namespace)

Update a document by ID (namespace-scoped).

Replace a document's fields by ID without specifying a collection.

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
    api_instance = mixpeek.DocumentsApi(api_client)
    document_id = 'document_id_example' # str | The ID of the document to update.
    request_body = None # Dict[str, object] | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    authorization2 = 'authorization_example' # str |  (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Update a document by ID (namespace-scoped).
        api_response = api_instance.update_document_ns(document_id, request_body, authorization=authorization, authorization2=authorization2, x_namespace=x_namespace)
        print("The response of DocumentsApi->update_document_ns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->update_document_ns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| The ID of the document to update. | 
 **request_body** | [**Dict[str, object]**](object.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **authorization2** | **str**|  | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

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
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

