# mixpeek.CollectionDocumentsApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aggregate_documents**](CollectionDocumentsApi.md#aggregate_documents) | **POST** /v1/collections/{collection_identifier}/documents/aggregate | Aggregate Documents
[**batch_delete**](CollectionDocumentsApi.md#batch_delete) | **DELETE** /v1/collections/{collection_identifier}/documents/batch | Batch Delete Documents
[**batch_update**](CollectionDocumentsApi.md#batch_update) | **POST** /v1/collections/{collection_identifier}/documents/batch | Batch Update Documents
[**bulk_update**](CollectionDocumentsApi.md#bulk_update) | **PATCH** /v1/collections/{collection_identifier}/documents/bulk | Bulk Update Documents
[**create_document**](CollectionDocumentsApi.md#create_document) | **POST** /v1/collections/{collection_identifier}/documents | Create a document.
[**delete_document**](CollectionDocumentsApi.md#delete_document) | **DELETE** /v1/collections/{collection_identifier}/documents/{document_id} | Delete a document by ID.
[**get_document**](CollectionDocumentsApi.md#get_document) | **GET** /v1/collections/{collection_identifier}/documents/{document_id} | Get a document by ID.
[**list_documents**](CollectionDocumentsApi.md#list_documents) | **POST** /v1/collections/{collection_identifier}/documents/list | List documents.
[**patch_document**](CollectionDocumentsApi.md#patch_document) | **PATCH** /v1/collections/{collection_identifier}/documents/{document_id} | Patch Document
[**update_document**](CollectionDocumentsApi.md#update_document) | **PUT** /v1/collections/{collection_identifier}/documents/{document_id} | Update Document


# **aggregate_documents**
> DocumentAggregationResponse aggregate_documents(collection_identifier, document_aggregation_request, authorization=authorization, x_namespace=x_namespace)

Aggregate Documents

This endpoint performs aggregation operations on documents in a collection.

    **Aggregation Framework**: Provides MongoDB-style aggregation operations:
    - GROUP BY: Group documents by one or more fields
    - Aggregations: COUNT, SUM, AVG, MIN, MAX, COUNT_DISTINCT, etc.
    - Date Operations: Truncate or extract date parts for time-series analysis
    - Filtering: Pre-aggregation filters (WHERE) and post-aggregation filters (HAVING)
    - Sorting & Limiting: Control result ordering and size

    **Use Cases**:
    - Count documents by feature type or collection
    - Calculate daily/monthly processing statistics
    - Analyze feature distributions and confidence scores
    - Generate reports with multiple metrics

    **Note**: This endpoint works with both MongoDB and Qdrant using the same interface.
    The system automatically selects the appropriate aggregation provider based on
    the underlying metadata store.

### Example


```python
import mixpeek
from mixpeek.models.document_aggregation_request import DocumentAggregationRequest
from mixpeek.models.document_aggregation_response import DocumentAggregationResponse
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
    collection_identifier = 'collection_identifier_example' # str | The unique identifier of the collection.
    document_aggregation_request = mixpeek.DocumentAggregationRequest() # DocumentAggregationRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Aggregate Documents
        api_response = api_instance.aggregate_documents(collection_identifier, document_aggregation_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of CollectionDocumentsApi->aggregate_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionDocumentsApi->aggregate_documents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_identifier** | **str**| The unique identifier of the collection. | 
 **document_aggregation_request** | [**DocumentAggregationRequest**](DocumentAggregationRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**DocumentAggregationResponse**](DocumentAggregationResponse.md)

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

# **batch_delete**
> BatchDeleteDocumentsResponse batch_delete(collection_identifier, batch_delete_documents_request, authorization=authorization, x_namespace=x_namespace)

Batch Delete Documents

Batch delete multiple documents by explicit IDs or filters.

Supports TWO modes:
1. Explicit IDs mode: Provide 'document_ids' array
   - Deletes specific documents by ID
   - Returns detailed per-document results
   - Maximum 1000 documents per batch

2. Filter mode: Provide 'filters' to delete all matching documents
   - Deletes ALL documents matching the filters
   - Returns total count only
   - Use with caution - can delete many documents

Key Features:
- Per-document success/failure reporting in explicit mode
- Validates documents exist in the specified collection
- Automatic document count update for the collection
- Efficient bulk deletion

Examples:
    Explicit IDs mode:
    ```json
    {
        "document_ids": ["doc_123", "doc_456", "doc_789"]
    }
    ```

    Filter mode:
    ```json
    {
        "filters": {"must": [{"key": "metadata.status", "value": "archived"}]}
    }
    ```

### Example


```python
import mixpeek
from mixpeek.models.batch_delete_documents_request import BatchDeleteDocumentsRequest
from mixpeek.models.batch_delete_documents_response import BatchDeleteDocumentsResponse
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
    collection_identifier = 'collection_identifier_example' # str | The ID of the collection to delete documents from.
    batch_delete_documents_request = mixpeek.BatchDeleteDocumentsRequest() # BatchDeleteDocumentsRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Batch Delete Documents
        api_response = api_instance.batch_delete(collection_identifier, batch_delete_documents_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of CollectionDocumentsApi->batch_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionDocumentsApi->batch_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_identifier** | **str**| The ID of the collection to delete documents from. | 
 **batch_delete_documents_request** | [**BatchDeleteDocumentsRequest**](BatchDeleteDocumentsRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**BatchDeleteDocumentsResponse**](BatchDeleteDocumentsResponse.md)

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

# **batch_update**
> BatchUpdateDocumentsResponse batch_update(collection_identifier, batch_update_documents_request, authorization=authorization, x_namespace=x_namespace)

Batch Update Documents

Batch update multiple documents by explicit IDs or filters.

Supports TWO modes:
1. Explicit IDs mode: Provide 'updates' array with document_id + update_data for each document
   - Each document can have DIFFERENT update_data
   - Returns detailed per-document results

2. Filter mode: Provide 'filters' + 'update_data' to update all matching documents
   - All documents receive the SAME update_data
   - Returns total count only

Key Features:
- Update any document field except vectors (metadata, internal_metadata, source_blobs, etc.)
- Maximum 1000 documents per batch in explicit mode
- Per-document success/failure reporting in explicit mode
- Validates documents exist in the specified collection

Examples:
    Explicit IDs mode:
    ```json
    {
        "updates": [
            {"document_id": "doc_123", "update_data": {"metadata": {"status": "processed"}}},
            {"document_id": "doc_456", "update_data": {"metadata": {"status": "archived"}}}
        ]
    }
    ```

    Filter mode:
    ```json
    {
        "filters": {"must": [{"key": "metadata.status", "value": "pending"}]},
        "update_data": {"metadata": {"status": "processed"}}
    }
    ```

### Example


```python
import mixpeek
from mixpeek.models.batch_update_documents_request import BatchUpdateDocumentsRequest
from mixpeek.models.batch_update_documents_response import BatchUpdateDocumentsResponse
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
    collection_identifier = 'collection_identifier_example' # str | The ID of the collection to update documents in.
    batch_update_documents_request = mixpeek.BatchUpdateDocumentsRequest() # BatchUpdateDocumentsRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Batch Update Documents
        api_response = api_instance.batch_update(collection_identifier, batch_update_documents_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of CollectionDocumentsApi->batch_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionDocumentsApi->batch_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_identifier** | **str**| The ID of the collection to update documents in. | 
 **batch_update_documents_request** | [**BatchUpdateDocumentsRequest**](BatchUpdateDocumentsRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**BatchUpdateDocumentsResponse**](BatchUpdateDocumentsResponse.md)

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

# **bulk_update**
> BulkUpdateDocumentsResponse bulk_update(collection_identifier, bulk_update_documents_request, authorization=authorization, x_namespace=x_namespace)

Bulk Update Documents

Bulk update documents matching filter conditions.

Partially updates all documents in the collection that match the provided filters.
If no filters are provided, updates all documents in the collection.

This endpoint applies the SAME update_data to ALL documents matching the filters.
For per-document updates with different values, use POST /batch endpoint instead.

### Example


```python
import mixpeek
from mixpeek.models.bulk_update_documents_request import BulkUpdateDocumentsRequest
from mixpeek.models.bulk_update_documents_response import BulkUpdateDocumentsResponse
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
    collection_identifier = 'collection_identifier_example' # str | The ID of the collection to update documents in.
    bulk_update_documents_request = mixpeek.BulkUpdateDocumentsRequest() # BulkUpdateDocumentsRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Bulk Update Documents
        api_response = api_instance.bulk_update(collection_identifier, bulk_update_documents_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of CollectionDocumentsApi->bulk_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionDocumentsApi->bulk_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_identifier** | **str**| The ID of the collection to update documents in. | 
 **bulk_update_documents_request** | [**BulkUpdateDocumentsRequest**](BulkUpdateDocumentsRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**BulkUpdateDocumentsResponse**](BulkUpdateDocumentsResponse.md)

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
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

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
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
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
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

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
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

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
> DocumentResponse get_document(collection_identifier, document_id, return_presigned_urls=return_presigned_urls, return_vectors=return_vectors, authorization=authorization, x_namespace=x_namespace)

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
    return_presigned_urls = False # bool | Generate fresh presigned download URLs for all blobs with S3 storage (optional) (default to False)
    return_vectors = False # bool |  (optional) (default to False)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get a document by ID.
        api_response = api_instance.get_document(collection_identifier, document_id, return_presigned_urls=return_presigned_urls, return_vectors=return_vectors, authorization=authorization, x_namespace=x_namespace)
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
 **return_presigned_urls** | **bool**| Generate fresh presigned download URLs for all blobs with S3 storage | [optional] [default to False]
 **return_vectors** | **bool**|  | [optional] [default to False]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
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
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_documents**
> ListDocumentsResponse list_documents(collection_identifier, limit=limit, offset=offset, cursor=cursor, include_total=include_total, authorization=authorization, x_namespace=x_namespace, list_documents_request=list_documents_request)

List documents.

List documents with optional grouping support.

Supports two modes:
1. Regular listing: Returns flat list of documents with pagination
2. Grouped listing: When group_by is specified, returns documents grouped by field value

When using group_by:
- Requires a payload index on the specified field in Qdrant
- Pagination applies to groups, not individual documents
- Each group contains all documents sharing the same field value

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
    cursor = 'cursor_example' # str |  (optional)
    include_total = False # bool |  (optional) (default to False)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)
    list_documents_request = mixpeek.ListDocumentsRequest() # ListDocumentsRequest |  (optional)

    try:
        # List documents.
        api_response = api_instance.list_documents(collection_identifier, limit=limit, offset=offset, cursor=cursor, include_total=include_total, authorization=authorization, x_namespace=x_namespace, list_documents_request=list_documents_request)
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
 **cursor** | **str**|  | [optional] 
 **include_total** | **bool**|  | [optional] [default to False]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 
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

# **patch_document**
> DocumentResponse patch_document(collection_identifier, document_id, request_body, authorization=authorization, x_namespace=x_namespace)

Patch Document

Partially update a document by ID (PATCH operation).

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
    document_id = 'document_id_example' # str | The ID of the document to patch.
    request_body = None # Dict[str, object] | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Patch Document
        api_response = api_instance.patch_document(collection_identifier, document_id, request_body, authorization=authorization, x_namespace=x_namespace)
        print("The response of CollectionDocumentsApi->patch_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionDocumentsApi->patch_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_identifier** | **str**| The ID of the collection. | 
 **document_id** | **str**| The ID of the document to patch. | 
 **request_body** | [**Dict[str, object]**](object.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
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
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_document**
> DocumentResponse update_document(collection_identifier, document_id, request_body, authorization=authorization, x_namespace=x_namespace)

Update Document

Update a document by ID.

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
    document_id = 'document_id_example' # str | The ID of the document to update.
    request_body = None # Dict[str, object] | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Update Document
        api_response = api_instance.update_document(collection_identifier, document_id, request_body, authorization=authorization, x_namespace=x_namespace)
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
 **request_body** | [**Dict[str, object]**](object.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
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
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

