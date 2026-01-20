# mixpeek.BucketBatchesApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_objects_to_batch_buckets_batches**](BucketBatchesApi.md#add_objects_to_batch_buckets_batches) | **POST** /v1/buckets/{bucket_identifier}/batches/{batch_id}/objects | Add Objects to Batch
[**cancel_batch_buckets_batches**](BucketBatchesApi.md#cancel_batch_buckets_batches) | **POST** /v1/buckets/{bucket_identifier}/batches/{batch_id}/cancel | Cancel Batch
[**create_batch_buckets_batches**](BucketBatchesApi.md#create_batch_buckets_batches) | **POST** /v1/buckets/{bucket_identifier}/batches | Create Batch
[**delete_batch_buckets_batches**](BucketBatchesApi.md#delete_batch_buckets_batches) | **DELETE** /v1/buckets/{bucket_identifier}/batches/{batch_id} | Delete Batch
[**get_batch_buckets_batches**](BucketBatchesApi.md#get_batch_buckets_batches) | **GET** /v1/buckets/{bucket_identifier}/batches/{batch_id} | Get Batch Configuration
[**get_batch_logs_buckets_batches**](BucketBatchesApi.md#get_batch_logs_buckets_batches) | **GET** /v1/buckets/{bucket_identifier}/batches/{batch_id}/logs | Get Ray Job Logs for Batch
[**get_failed_documents_buckets_batches_batch**](BucketBatchesApi.md#get_failed_documents_buckets_batches_batch) | **GET** /v1/buckets/{bucket_identifier}/batches/{batch_id}/failed-documents | Get Failed Documents for Batch
[**list_batches_buckets**](BucketBatchesApi.md#list_batches_buckets) | **POST** /v1/buckets/{bucket_identifier}/batches/list | List Batches
[**patch_batch_buckets_batches**](BucketBatchesApi.md#patch_batch_buckets_batches) | **PATCH** /v1/buckets/{bucket_identifier}/batches/{batch_id} | Partially Update Batch
[**retry_batch_buckets_batches**](BucketBatchesApi.md#retry_batch_buckets_batches) | **POST** /v1/buckets/{bucket_identifier}/batches/{batch_id}/retry | Retry Failed Documents
[**retry_qdrant_write_buckets_batches_batch_id_tiers_num**](BucketBatchesApi.md#retry_qdrant_write_buckets_batches_batch_id_tiers_num) | **POST** /v1/buckets/{bucket_identifier}/batches/{batch_id}/tiers/{tier_num}/retry-qdrant-write | Retry Qdrant Write from S3
[**submit_batch_buckets_batches**](BucketBatchesApi.md#submit_batch_buckets_batches) | **POST** /v1/buckets/{bucket_identifier}/batches/{batch_id}/submit | Submit Batch for Processing


# **add_objects_to_batch_buckets_batches**
> BatchModel add_objects_to_batch_buckets_batches(bucket_identifier, batch_id, add_objects_to_batch_request, skip_validation=skip_validation, authorization=authorization, x_namespace=x_namespace)

Add Objects to Batch

Add objects to an existing batch. The batch must be in 'draft' status.

### Example


```python
import mixpeek
from mixpeek.models.add_objects_to_batch_request import AddObjectsToBatchRequest
from mixpeek.models.batch_model import BatchModel
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
    api_instance = mixpeek.BucketBatchesApi(api_client)
    bucket_identifier = 'bucket_identifier_example' # str | The unique identifier of the bucket.
    batch_id = 'batch_id_example' # str | The unique identifier of the batch.
    add_objects_to_batch_request = mixpeek.AddObjectsToBatchRequest() # AddObjectsToBatchRequest | 
    skip_validation = False # bool | Skip object existence validation. Use this for large batches (>10k objects) or when you're certain all object IDs are valid. Improves performance significantly. (optional) (default to False)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Add Objects to Batch
        api_response = api_instance.add_objects_to_batch_buckets_batches(bucket_identifier, batch_id, add_objects_to_batch_request, skip_validation=skip_validation, authorization=authorization, x_namespace=x_namespace)
        print("The response of BucketBatchesApi->add_objects_to_batch_buckets_batches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketBatchesApi->add_objects_to_batch_buckets_batches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_identifier** | **str**| The unique identifier of the bucket. | 
 **batch_id** | **str**| The unique identifier of the batch. | 
 **add_objects_to_batch_request** | [**AddObjectsToBatchRequest**](AddObjectsToBatchRequest.md)|  | 
 **skip_validation** | **bool**| Skip object existence validation. Use this for large batches (&gt;10k objects) or when you&#39;re certain all object IDs are valid. Improves performance significantly. | [optional] [default to False]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**BatchModel**](BatchModel.md)

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

# **cancel_batch_buckets_batches**
> TaskResponse cancel_batch_buckets_batches(bucket_identifier, batch_id, authorization=authorization, x_namespace=x_namespace)

Cancel Batch

Cancel a submitted/processing batch: cancels Ray job via engine and marks task/batch as CANCELLED.

### Example


```python
import mixpeek
from mixpeek.models.task_response import TaskResponse
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
    api_instance = mixpeek.BucketBatchesApi(api_client)
    bucket_identifier = 'bucket_identifier_example' # str | The unique identifier of the bucket.
    batch_id = 'batch_id_example' # str | The unique identifier of the batch.
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Cancel Batch
        api_response = api_instance.cancel_batch_buckets_batches(bucket_identifier, batch_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of BucketBatchesApi->cancel_batch_buckets_batches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketBatchesApi->cancel_batch_buckets_batches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_identifier** | **str**| The unique identifier of the bucket. | 
 **batch_id** | **str**| The unique identifier of the batch. | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**TaskResponse**](TaskResponse.md)

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

# **create_batch_buckets_batches**
> BatchModel create_batch_buckets_batches(bucket_identifier, create_batch_request, skip_validation=skip_validation, authorization=authorization, x_namespace=x_namespace)

Create Batch

Create a new batch for grouping bucket objects.

### Example


```python
import mixpeek
from mixpeek.models.batch_model import BatchModel
from mixpeek.models.create_batch_request import CreateBatchRequest
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
    api_instance = mixpeek.BucketBatchesApi(api_client)
    bucket_identifier = 'bucket_identifier_example' # str | The unique identifier of the bucket.
    create_batch_request = mixpeek.CreateBatchRequest() # CreateBatchRequest | 
    skip_validation = False # bool | Skip object existence validation. Use this for large batches (>10k objects) or when you're certain all object IDs are valid. Improves performance significantly. (optional) (default to False)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Create Batch
        api_response = api_instance.create_batch_buckets_batches(bucket_identifier, create_batch_request, skip_validation=skip_validation, authorization=authorization, x_namespace=x_namespace)
        print("The response of BucketBatchesApi->create_batch_buckets_batches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketBatchesApi->create_batch_buckets_batches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_identifier** | **str**| The unique identifier of the bucket. | 
 **create_batch_request** | [**CreateBatchRequest**](CreateBatchRequest.md)|  | 
 **skip_validation** | **bool**| Skip object existence validation. Use this for large batches (&gt;10k objects) or when you&#39;re certain all object IDs are valid. Improves performance significantly. | [optional] [default to False]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**BatchModel**](BatchModel.md)

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

# **delete_batch_buckets_batches**
> GenericDeleteResponse delete_batch_buckets_batches(bucket_identifier, batch_id, authorization=authorization, x_namespace=x_namespace)

Delete Batch

Delete a batch by its ID.

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
    api_instance = mixpeek.BucketBatchesApi(api_client)
    bucket_identifier = 'bucket_identifier_example' # str | The unique identifier of the bucket.
    batch_id = 'batch_id_example' # str | The unique identifier of the batch.
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Delete Batch
        api_response = api_instance.delete_batch_buckets_batches(bucket_identifier, batch_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of BucketBatchesApi->delete_batch_buckets_batches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketBatchesApi->delete_batch_buckets_batches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_identifier** | **str**| The unique identifier of the bucket. | 
 **batch_id** | **str**| The unique identifier of the batch. | 
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

# **get_batch_buckets_batches**
> BatchModel get_batch_buckets_batches(bucket_identifier, batch_id, authorization=authorization, x_namespace=x_namespace)

Get Batch Configuration

Retrieve batch configuration and historical data from MongoDB. Status is automatically synchronized from Task API. For real-time monitoring, use GET /v1/tasks/{task_id} (Redis, faster).

### Example


```python
import mixpeek
from mixpeek.models.batch_model import BatchModel
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
    api_instance = mixpeek.BucketBatchesApi(api_client)
    bucket_identifier = 'bucket_identifier_example' # str | The unique identifier of the bucket.
    batch_id = 'batch_id_example' # str | The unique identifier of the batch.
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Batch Configuration
        api_response = api_instance.get_batch_buckets_batches(bucket_identifier, batch_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of BucketBatchesApi->get_batch_buckets_batches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketBatchesApi->get_batch_buckets_batches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_identifier** | **str**| The unique identifier of the bucket. | 
 **batch_id** | **str**| The unique identifier of the batch. | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**BatchModel**](BatchModel.md)

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

# **get_batch_logs_buckets_batches**
> object get_batch_logs_buckets_batches(bucket_identifier, batch_id, tier_num=tier_num, authorization=authorization, x_namespace=x_namespace)

Get Ray Job Logs for Batch

Retrieve Ray job submission logs for a batch's processing tiers. You can get logs for a specific tier or all tiers. User must have access to the batch to retrieve logs.

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
    api_instance = mixpeek.BucketBatchesApi(api_client)
    bucket_identifier = 'bucket_identifier_example' # str | The unique identifier of the bucket.
    batch_id = 'batch_id_example' # str | The unique identifier of the batch.
    tier_num = 56 # int | Optional tier number (0-based). If not provided, returns logs for all tiers. (optional)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Ray Job Logs for Batch
        api_response = api_instance.get_batch_logs_buckets_batches(bucket_identifier, batch_id, tier_num=tier_num, authorization=authorization, x_namespace=x_namespace)
        print("The response of BucketBatchesApi->get_batch_logs_buckets_batches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketBatchesApi->get_batch_logs_buckets_batches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_identifier** | **str**| The unique identifier of the bucket. | 
 **batch_id** | **str**| The unique identifier of the batch. | 
 **tier_num** | **int**| Optional tier number (0-based). If not provided, returns logs for all tiers. | [optional] 
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

# **get_failed_documents_buckets_batches_batch**
> object get_failed_documents_buckets_batches_batch(bucket_identifier, batch_id, tier_num=tier_num, collection_id=collection_id, limit=limit, offset=offset, authorization=authorization, x_namespace=x_namespace)

Get Failed Documents for Batch

Retrieve failed documents for a batch, optionally filtered by tier or collection.

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
    api_instance = mixpeek.BucketBatchesApi(api_client)
    bucket_identifier = 'bucket_identifier_example' # str | The unique identifier of the bucket.
    batch_id = 'batch_id_example' # str | The unique identifier of the batch.
    tier_num = 56 # int |  (optional)
    collection_id = 'collection_id_example' # str |  (optional)
    limit = 100 # int |  (optional) (default to 100)
    offset = 0 # int |  (optional) (default to 0)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Failed Documents for Batch
        api_response = api_instance.get_failed_documents_buckets_batches_batch(bucket_identifier, batch_id, tier_num=tier_num, collection_id=collection_id, limit=limit, offset=offset, authorization=authorization, x_namespace=x_namespace)
        print("The response of BucketBatchesApi->get_failed_documents_buckets_batches_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketBatchesApi->get_failed_documents_buckets_batches_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_identifier** | **str**| The unique identifier of the bucket. | 
 **batch_id** | **str**| The unique identifier of the batch. | 
 **tier_num** | **int**|  | [optional] 
 **collection_id** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] [default to 0]
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

# **list_batches_buckets**
> ListBatchesResponse list_batches_buckets(bucket_identifier, authorization=authorization, x_namespace=x_namespace, list_batches_request=list_batches_request)

List Batches

List batches with pagination and filtering options.

### Example


```python
import mixpeek
from mixpeek.models.list_batches_request import ListBatchesRequest
from mixpeek.models.list_batches_response import ListBatchesResponse
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
    api_instance = mixpeek.BucketBatchesApi(api_client)
    bucket_identifier = 'bucket_identifier_example' # str | The unique identifier of the bucket.
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)
    list_batches_request = mixpeek.ListBatchesRequest() # ListBatchesRequest |  (optional)

    try:
        # List Batches
        api_response = api_instance.list_batches_buckets(bucket_identifier, authorization=authorization, x_namespace=x_namespace, list_batches_request=list_batches_request)
        print("The response of BucketBatchesApi->list_batches_buckets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketBatchesApi->list_batches_buckets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_identifier** | **str**| The unique identifier of the bucket. | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 
 **list_batches_request** | [**ListBatchesRequest**](ListBatchesRequest.md)|  | [optional] 

### Return type

[**ListBatchesResponse**](ListBatchesResponse.md)

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

# **patch_batch_buckets_batches**
> BatchModel patch_batch_buckets_batches(bucket_identifier, batch_id, patch_batch_request, authorization=authorization, x_namespace=x_namespace)

Partially Update Batch

This endpoint partially updates a batch (PATCH operation).
    Only provided fields will be updated. At minimum, metadata can always be updated.
    Immutable fields like batch_id and timestamps cannot be modified.

### Example


```python
import mixpeek
from mixpeek.models.batch_model import BatchModel
from mixpeek.models.patch_batch_request import PatchBatchRequest
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
    api_instance = mixpeek.BucketBatchesApi(api_client)
    bucket_identifier = 'bucket_identifier_example' # str | The unique identifier of the bucket.
    batch_id = 'batch_id_example' # str | The unique identifier of the batch.
    patch_batch_request = mixpeek.PatchBatchRequest() # PatchBatchRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Partially Update Batch
        api_response = api_instance.patch_batch_buckets_batches(bucket_identifier, batch_id, patch_batch_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of BucketBatchesApi->patch_batch_buckets_batches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketBatchesApi->patch_batch_buckets_batches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_identifier** | **str**| The unique identifier of the bucket. | 
 **batch_id** | **str**| The unique identifier of the batch. | 
 **patch_batch_request** | [**PatchBatchRequest**](PatchBatchRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**BatchModel**](BatchModel.md)

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

# **retry_batch_buckets_batches**
> object retry_batch_buckets_batches(bucket_identifier, batch_id, retry_batch_request, authorization=authorization, x_namespace=x_namespace)

Retry Failed Documents

Retry failed documents in a batch with intelligent filtering by error type and tier.

### Example


```python
import mixpeek
from mixpeek.models.retry_batch_request import RetryBatchRequest
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
    api_instance = mixpeek.BucketBatchesApi(api_client)
    bucket_identifier = 'bucket_identifier_example' # str | The unique identifier of the bucket.
    batch_id = 'batch_id_example' # str | The unique identifier of the batch.
    retry_batch_request = mixpeek.RetryBatchRequest() # RetryBatchRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Retry Failed Documents
        api_response = api_instance.retry_batch_buckets_batches(bucket_identifier, batch_id, retry_batch_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of BucketBatchesApi->retry_batch_buckets_batches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketBatchesApi->retry_batch_buckets_batches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_identifier** | **str**| The unique identifier of the bucket. | 
 **batch_id** | **str**| The unique identifier of the batch. | 
 **retry_batch_request** | [**RetryBatchRequest**](RetryBatchRequest.md)|  | 
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

# **retry_qdrant_write_buckets_batches_batch_id_tiers_num**
> object retry_qdrant_write_buckets_batches_batch_id_tiers_num(bucket_identifier, batch_id, tier_num, authorization=authorization, x_namespace=x_namespace)

Retry Qdrant Write from S3

Retry Qdrant write by reading processed output from S3. Use when validation detects 'qdrant_write_failed'.

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
    api_instance = mixpeek.BucketBatchesApi(api_client)
    bucket_identifier = 'bucket_identifier_example' # str | The unique identifier of the bucket.
    batch_id = 'batch_id_example' # str | The unique identifier of the batch.
    tier_num = 56 # int | The tier number to retry (0-based).
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Retry Qdrant Write from S3
        api_response = api_instance.retry_qdrant_write_buckets_batches_batch_id_tiers_num(bucket_identifier, batch_id, tier_num, authorization=authorization, x_namespace=x_namespace)
        print("The response of BucketBatchesApi->retry_qdrant_write_buckets_batches_batch_id_tiers_num:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketBatchesApi->retry_qdrant_write_buckets_batches_batch_id_tiers_num: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_identifier** | **str**| The unique identifier of the bucket. | 
 **batch_id** | **str**| The unique identifier of the batch. | 
 **tier_num** | **int**| The tier number to retry (0-based). | 
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

# **submit_batch_buckets_batches**
> TaskResponse submit_batch_buckets_batches(bucket_identifier, batch_id, authorization=authorization, x_namespace=x_namespace, submit_batch_request=submit_batch_request)

Submit Batch for Processing

Submit a batch for asynchronous processing. The batch must be in 'pending' status and contain objects.

### Example


```python
import mixpeek
from mixpeek.models.submit_batch_request import SubmitBatchRequest
from mixpeek.models.task_response import TaskResponse
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
    api_instance = mixpeek.BucketBatchesApi(api_client)
    bucket_identifier = 'bucket_identifier_example' # str | The unique identifier of the bucket.
    batch_id = 'batch_id_example' # str | The unique identifier of the batch.
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)
    submit_batch_request = mixpeek.SubmitBatchRequest() # SubmitBatchRequest |  (optional)

    try:
        # Submit Batch for Processing
        api_response = api_instance.submit_batch_buckets_batches(bucket_identifier, batch_id, authorization=authorization, x_namespace=x_namespace, submit_batch_request=submit_batch_request)
        print("The response of BucketBatchesApi->submit_batch_buckets_batches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketBatchesApi->submit_batch_buckets_batches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_identifier** | **str**| The unique identifier of the bucket. | 
 **batch_id** | **str**| The unique identifier of the batch. | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 
 **submit_batch_request** | [**SubmitBatchRequest**](SubmitBatchRequest.md)|  | [optional] 

### Return type

[**TaskResponse**](TaskResponse.md)

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

