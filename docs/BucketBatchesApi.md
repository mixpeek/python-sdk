# mixpeek.BucketBatchesApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_objects_to_batch_buckets_batches**](BucketBatchesApi.md#add_objects_to_batch_buckets_batches) | **POST** /v1/buckets/{bucket_identifier}/batches/{batch_id}/objects | Add Objects to Batch
[**cancel_batch_buckets_batches**](BucketBatchesApi.md#cancel_batch_buckets_batches) | **POST** /v1/buckets/{bucket_identifier}/batches/{batch_id}/cancel | Cancel Batch
[**create_batch_buckets_batches**](BucketBatchesApi.md#create_batch_buckets_batches) | **POST** /v1/buckets/{bucket_identifier}/batches | Create Batch
[**delete_batch_buckets_batches**](BucketBatchesApi.md#delete_batch_buckets_batches) | **DELETE** /v1/buckets/{bucket_identifier}/batches/{batch_id} | Delete Batch
[**list_batches_buckets**](BucketBatchesApi.md#list_batches_buckets) | **POST** /v1/buckets/{bucket_identifier}/batches/list | List Batches
[**submit_batch_buckets_batches**](BucketBatchesApi.md#submit_batch_buckets_batches) | **POST** /v1/buckets/{bucket_identifier}/batches/{batch_id}/submit | Submit Batch for Processing


# **add_objects_to_batch_buckets_batches**
> BatchModel add_objects_to_batch_buckets_batches(bucket_identifier, batch_id, add_objects_to_batch_request, authorization=authorization, x_namespace=x_namespace)

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
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)
    x_namespace = 'x_namespace_example' # str | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. (optional)

    try:
        # Add Objects to Batch
        api_response = api_instance.add_objects_to_batch_buckets_batches(bucket_identifier, batch_id, add_objects_to_batch_request, authorization=authorization, x_namespace=x_namespace)
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
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 
 **x_namespace** | **str**| Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: &#39;netflix_prod&#39; or &#39;ns_1234567890&#39;. To create a namespace, use the /namespaces endpoint. | [optional] 

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
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)
    x_namespace = 'x_namespace_example' # str | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. (optional)

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
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 
 **x_namespace** | **str**| Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: &#39;netflix_prod&#39; or &#39;ns_1234567890&#39;. To create a namespace, use the /namespaces endpoint. | [optional] 

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
> BatchModel create_batch_buckets_batches(bucket_identifier, create_batch_request, authorization=authorization, x_namespace=x_namespace)

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
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)
    x_namespace = 'x_namespace_example' # str | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. (optional)

    try:
        # Create Batch
        api_response = api_instance.create_batch_buckets_batches(bucket_identifier, create_batch_request, authorization=authorization, x_namespace=x_namespace)
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
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 
 **x_namespace** | **str**| Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: &#39;netflix_prod&#39; or &#39;ns_1234567890&#39;. To create a namespace, use the /namespaces endpoint. | [optional] 

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
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)
    x_namespace = 'x_namespace_example' # str | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. (optional)

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
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)
    x_namespace = 'x_namespace_example' # str | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. (optional)
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
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 
 **x_namespace** | **str**| Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: &#39;netflix_prod&#39; or &#39;ns_1234567890&#39;. To create a namespace, use the /namespaces endpoint. | [optional] 
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

# **submit_batch_buckets_batches**
> TaskResponse submit_batch_buckets_batches(bucket_identifier, batch_id, authorization=authorization, x_namespace=x_namespace)

Submit Batch for Processing

Submit a batch for asynchronous processing. The batch must be in 'pending' status and contain objects.

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
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)
    x_namespace = 'x_namespace_example' # str | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. (optional)

    try:
        # Submit Batch for Processing
        api_response = api_instance.submit_batch_buckets_batches(bucket_identifier, batch_id, authorization=authorization, x_namespace=x_namespace)
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
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 
 **x_namespace** | **str**| Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: &#39;netflix_prod&#39; or &#39;ns_1234567890&#39;. To create a namespace, use the /namespaces endpoint. | [optional] 

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

