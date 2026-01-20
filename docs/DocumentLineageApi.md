# mixpeek.DocumentLineageApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_decomposition_tree_objects**](DocumentLineageApi.md#get_decomposition_tree_objects) | **GET** /v1/objects/{object_id}/decomposition-tree | Get decomposition tree visualization
[**get_document_lineage**](DocumentLineageApi.md#get_document_lineage) | **GET** /v1/collections/{collection_id}/documents/{document_id}/lineage | Get document lineage
[**get_documents_by_object**](DocumentLineageApi.md#get_documents_by_object) | **GET** /v1/objects/{object_id}/documents | Get all documents derived from an object


# **get_decomposition_tree_objects**
> object get_decomposition_tree_objects(object_id, include_document_ids=include_document_ids, authorization=authorization, x_namespace=x_namespace)

Get decomposition tree visualization

Get a hierarchical tree structure showing all collections and documents derived from a root object. Shows the complete multi-stage processing pipeline.

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
    api_instance = mixpeek.DocumentLineageApi(api_client)
    object_id = 'object_id_example' # str | Root object ID to build decomposition tree for
    include_document_ids = False # bool | Include full list of document IDs (can be large) (optional) (default to False)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get decomposition tree visualization
        api_response = api_instance.get_decomposition_tree_objects(object_id, include_document_ids=include_document_ids, authorization=authorization, x_namespace=x_namespace)
        print("The response of DocumentLineageApi->get_decomposition_tree_objects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentLineageApi->get_decomposition_tree_objects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Root object ID to build decomposition tree for | 
 **include_document_ids** | **bool**| Include full list of document IDs (can be large) | [optional] [default to False]
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

# **get_document_lineage**
> object get_document_lineage(collection_id, document_id, authorization=authorization, x_namespace=x_namespace)

Get document lineage

Get the complete processing lineage for a document. Shows the full chain of transformations from the root bucket object through all collection processing stages.

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
    api_instance = mixpeek.DocumentLineageApi(api_client)
    collection_id = 'collection_id_example' # str | ID of the collection containing the document
    document_id = 'document_id_example' # str | ID of the document to trace
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get document lineage
        api_response = api_instance.get_document_lineage(collection_id, document_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of DocumentLineageApi->get_document_lineage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentLineageApi->get_document_lineage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| ID of the collection containing the document | 
 **document_id** | **str**| ID of the document to trace | 
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
**200** | Document lineage information |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_documents_by_object**
> object get_documents_by_object(object_id, collection_ids=collection_ids, authorization=authorization, x_namespace=x_namespace)

Get all documents derived from an object

Get all documents created from a specific root object. Useful for finding all processing outputs across multiple collections.

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
    api_instance = mixpeek.DocumentLineageApi(api_client)
    object_id = 'object_id_example' # str | Root object ID to find all derived documents
    collection_ids = ['collection_ids_example'] # List[str] | Optional: Filter to specific collections (optional)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get all documents derived from an object
        api_response = api_instance.get_documents_by_object(object_id, collection_ids=collection_ids, authorization=authorization, x_namespace=x_namespace)
        print("The response of DocumentLineageApi->get_documents_by_object:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentLineageApi->get_documents_by_object: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| Root object ID to find all derived documents | 
 **collection_ids** | [**List[str]**](str.md)| Optional: Filter to specific collections | [optional] 
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

