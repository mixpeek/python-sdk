# mixpeek.BucketObjectsApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_object_buckets**](BucketObjectsApi.md#create_object_buckets) | **POST** /v1/buckets/{bucket_identifier}/objects | Create Object
[**create_objects_batch_buckets**](BucketObjectsApi.md#create_objects_batch_buckets) | **POST** /v1/buckets/{bucket_identifier}/objects/batch | Create Objects in Batch
[**delete_object_buckets**](BucketObjectsApi.md#delete_object_buckets) | **DELETE** /v1/buckets/{bucket_identifier}/objects/{object_identifier} | Delete Object
[**get_object_buckets**](BucketObjectsApi.md#get_object_buckets) | **GET** /v1/buckets/{bucket_identifier}/objects/{object_identifier} | Get Object
[**list_objects_buckets**](BucketObjectsApi.md#list_objects_buckets) | **POST** /v1/buckets/{bucket_identifier}/objects/list | List Objects
[**update_object_buckets**](BucketObjectsApi.md#update_object_buckets) | **PUT** /v1/buckets/{bucket_identifier}/objects/{object_identifier} | Update Object


# **create_object_buckets**
> ObjectResponse create_object_buckets(bucket_identifier, create_object_request, authorization=authorization, x_namespace=x_namespace)

Create Object

This endpoint creates a new object in the specified bucket.
    The object must conform to the bucket's schema. It does not trigger processing.

### Example


```python
import mixpeek
from mixpeek.models.create_object_request import CreateObjectRequest
from mixpeek.models.object_response import ObjectResponse
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
    api_instance = mixpeek.BucketObjectsApi(api_client)
    bucket_identifier = 'bucket_identifier_example' # str | The unique identifier of the bucket.
    create_object_request = mixpeek.CreateObjectRequest() # CreateObjectRequest | 
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)
    x_namespace = 'x_namespace_example' # str | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. (optional)

    try:
        # Create Object
        api_response = api_instance.create_object_buckets(bucket_identifier, create_object_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of BucketObjectsApi->create_object_buckets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketObjectsApi->create_object_buckets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_identifier** | **str**| The unique identifier of the bucket. | 
 **create_object_request** | [**CreateObjectRequest**](CreateObjectRequest.md)|  | 
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 
 **x_namespace** | **str**| Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: &#39;netflix_prod&#39; or &#39;ns_1234567890&#39;. To create a namespace, use the /namespaces endpoint. | [optional] 

### Return type

[**ObjectResponse**](ObjectResponse.md)

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

# **create_objects_batch_buckets**
> List[ObjectResponse] create_objects_batch_buckets(bucket_identifier, create_objects_batch_request, authorization=authorization, x_namespace=x_namespace)

Create Objects in Batch

This endpoint creates multiple new objects in the specified bucket as a batch.
    Each object must conform to the bucket's schema. It does not trigger processing.

### Example


```python
import mixpeek
from mixpeek.models.create_objects_batch_request import CreateObjectsBatchRequest
from mixpeek.models.object_response import ObjectResponse
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
    api_instance = mixpeek.BucketObjectsApi(api_client)
    bucket_identifier = 'bucket_identifier_example' # str | The unique identifier of the bucket.
    create_objects_batch_request = mixpeek.CreateObjectsBatchRequest() # CreateObjectsBatchRequest | 
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)
    x_namespace = 'x_namespace_example' # str | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. (optional)

    try:
        # Create Objects in Batch
        api_response = api_instance.create_objects_batch_buckets(bucket_identifier, create_objects_batch_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of BucketObjectsApi->create_objects_batch_buckets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketObjectsApi->create_objects_batch_buckets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_identifier** | **str**| The unique identifier of the bucket. | 
 **create_objects_batch_request** | [**CreateObjectsBatchRequest**](CreateObjectsBatchRequest.md)|  | 
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 
 **x_namespace** | **str**| Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: &#39;netflix_prod&#39; or &#39;ns_1234567890&#39;. To create a namespace, use the /namespaces endpoint. | [optional] 

### Return type

[**List[ObjectResponse]**](ObjectResponse.md)

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

# **delete_object_buckets**
> delete_object_buckets(bucket_identifier, object_identifier, authorization=authorization, x_namespace=x_namespace)

Delete Object

This endpoint deletes an object from the specified bucket.

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
    api_instance = mixpeek.BucketObjectsApi(api_client)
    bucket_identifier = 'bucket_identifier_example' # str | The unique identifier of the bucket.
    object_identifier = 'object_identifier_example' # str | The unique identifier of the object.
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)
    x_namespace = 'x_namespace_example' # str | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. (optional)

    try:
        # Delete Object
        api_instance.delete_object_buckets(bucket_identifier, object_identifier, authorization=authorization, x_namespace=x_namespace)
    except Exception as e:
        print("Exception when calling BucketObjectsApi->delete_object_buckets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_identifier** | **str**| The unique identifier of the bucket. | 
 **object_identifier** | **str**| The unique identifier of the object. | 
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 
 **x_namespace** | **str**| Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: &#39;netflix_prod&#39; or &#39;ns_1234567890&#39;. To create a namespace, use the /namespaces endpoint. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_buckets**
> ObjectResponse get_object_buckets(bucket_identifier, object_identifier, authorization=authorization, x_namespace=x_namespace)

Get Object

This endpoint retrieves an object by its ID from the specified bucket.

### Example


```python
import mixpeek
from mixpeek.models.object_response import ObjectResponse
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
    api_instance = mixpeek.BucketObjectsApi(api_client)
    bucket_identifier = 'bucket_identifier_example' # str | The unique identifier of the bucket.
    object_identifier = 'object_identifier_example' # str | The unique identifier of the object.
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)
    x_namespace = 'x_namespace_example' # str | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. (optional)

    try:
        # Get Object
        api_response = api_instance.get_object_buckets(bucket_identifier, object_identifier, authorization=authorization, x_namespace=x_namespace)
        print("The response of BucketObjectsApi->get_object_buckets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketObjectsApi->get_object_buckets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_identifier** | **str**| The unique identifier of the bucket. | 
 **object_identifier** | **str**| The unique identifier of the object. | 
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 
 **x_namespace** | **str**| Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: &#39;netflix_prod&#39; or &#39;ns_1234567890&#39;. To create a namespace, use the /namespaces endpoint. | [optional] 

### Return type

[**ObjectResponse**](ObjectResponse.md)

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

# **list_objects_buckets**
> ListObjectsResponse list_objects_buckets(bucket_identifier, limit=limit, offset=offset, authorization=authorization, x_namespace=x_namespace)

List Objects

This endpoint lists objects in a bucket with pagination.
    Note: Filtering, sorting, and search capabilities will be added in a future update.

### Example


```python
import mixpeek
from mixpeek.models.list_objects_response import ListObjectsResponse
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
    api_instance = mixpeek.BucketObjectsApi(api_client)
    bucket_identifier = 'bucket_identifier_example' # str | The unique identifier of the bucket.
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)
    x_namespace = 'x_namespace_example' # str | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. (optional)

    try:
        # List Objects
        api_response = api_instance.list_objects_buckets(bucket_identifier, limit=limit, offset=offset, authorization=authorization, x_namespace=x_namespace)
        print("The response of BucketObjectsApi->list_objects_buckets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketObjectsApi->list_objects_buckets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_identifier** | **str**| The unique identifier of the bucket. | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 
 **x_namespace** | **str**| Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: &#39;netflix_prod&#39; or &#39;ns_1234567890&#39;. To create a namespace, use the /namespaces endpoint. | [optional] 

### Return type

[**ListObjectsResponse**](ListObjectsResponse.md)

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

# **update_object_buckets**
> ObjectResponse update_object_buckets(bucket_identifier, object_identifier, update_object_request, authorization=authorization, x_namespace=x_namespace)

Update Object

This endpoint updates an existing object in the specified bucket.
    The updated object must conform to the bucket's schema. It does not trigger processing.

### Example


```python
import mixpeek
from mixpeek.models.object_response import ObjectResponse
from mixpeek.models.update_object_request import UpdateObjectRequest
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
    api_instance = mixpeek.BucketObjectsApi(api_client)
    bucket_identifier = 'bucket_identifier_example' # str | The unique identifier of the bucket.
    object_identifier = 'object_identifier_example' # str | The unique identifier of the object.
    update_object_request = mixpeek.UpdateObjectRequest() # UpdateObjectRequest | 
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)
    x_namespace = 'x_namespace_example' # str | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. (optional)

    try:
        # Update Object
        api_response = api_instance.update_object_buckets(bucket_identifier, object_identifier, update_object_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of BucketObjectsApi->update_object_buckets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketObjectsApi->update_object_buckets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_identifier** | **str**| The unique identifier of the bucket. | 
 **object_identifier** | **str**| The unique identifier of the object. | 
 **update_object_request** | [**UpdateObjectRequest**](UpdateObjectRequest.md)|  | 
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 
 **x_namespace** | **str**| Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: &#39;netflix_prod&#39; or &#39;ns_1234567890&#39;. To create a namespace, use the /namespaces endpoint. | [optional] 

### Return type

[**ObjectResponse**](ObjectResponse.md)

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

