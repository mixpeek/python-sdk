# mixpeek.BucketsApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bucket**](BucketsApi.md#create_bucket) | **POST** /v1/buckets | Create Bucket
[**delete_bucket**](BucketsApi.md#delete_bucket) | **DELETE** /v1/buckets/{bucket_identifier} | Delete Bucket
[**get_bucket**](BucketsApi.md#get_bucket) | **GET** /v1/buckets/{bucket_identifier} | Get Bucket
[**list_buckets**](BucketsApi.md#list_buckets) | **POST** /v1/buckets/list | List Buckets
[**update_bucket**](BucketsApi.md#update_bucket) | **PUT** /v1/buckets/{bucket_identifier} | Update Bucket


# **create_bucket**
> BucketResponse create_bucket(bucket_create_request, authorization=authorization, x_namespace=x_namespace)

Create Bucket

This endpoint allows you to create a new bucket with a defined schema.
    A bucket is a collection of objects that conform to the schema.
    The schema defines the structure and validation rules for objects in the bucket.

### Example


```python
import mixpeek
from mixpeek.models.bucket_create_request import BucketCreateRequest
from mixpeek.models.bucket_response import BucketResponse
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
    api_instance = mixpeek.BucketsApi(api_client)
    bucket_create_request = mixpeek.BucketCreateRequest() # BucketCreateRequest | 
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)
    x_namespace = 'x_namespace_example' # str | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. (optional)

    try:
        # Create Bucket
        api_response = api_instance.create_bucket(bucket_create_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of BucketsApi->create_bucket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketsApi->create_bucket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_create_request** | [**BucketCreateRequest**](BucketCreateRequest.md)|  | 
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 
 **x_namespace** | **str**| Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: &#39;netflix_prod&#39; or &#39;ns_1234567890&#39;. To create a namespace, use the /namespaces endpoint. | [optional] 

### Return type

[**BucketResponse**](BucketResponse.md)

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

# **delete_bucket**
> TaskResponse delete_bucket(bucket_identifier, authorization=authorization, x_namespace=x_namespace)

Delete Bucket

This endpoint deletes a bucket and all its objects.

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
    api_instance = mixpeek.BucketsApi(api_client)
    bucket_identifier = 'bucket_identifier_example' # str | 
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)
    x_namespace = 'x_namespace_example' # str | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. (optional)

    try:
        # Delete Bucket
        api_response = api_instance.delete_bucket(bucket_identifier, authorization=authorization, x_namespace=x_namespace)
        print("The response of BucketsApi->delete_bucket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketsApi->delete_bucket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_identifier** | **str**|  | 
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

# **get_bucket**
> BucketResponse get_bucket(bucket_identifier, authorization=authorization, x_namespace=x_namespace)

Get Bucket

This endpoint retrieves a bucket by its ID.

### Example


```python
import mixpeek
from mixpeek.models.bucket_response import BucketResponse
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
    api_instance = mixpeek.BucketsApi(api_client)
    bucket_identifier = 'bucket_identifier_example' # str | 
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)
    x_namespace = 'x_namespace_example' # str | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. (optional)

    try:
        # Get Bucket
        api_response = api_instance.get_bucket(bucket_identifier, authorization=authorization, x_namespace=x_namespace)
        print("The response of BucketsApi->get_bucket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketsApi->get_bucket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_identifier** | **str**|  | 
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 
 **x_namespace** | **str**| Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: &#39;netflix_prod&#39; or &#39;ns_1234567890&#39;. To create a namespace, use the /namespaces endpoint. | [optional] 

### Return type

[**BucketResponse**](BucketResponse.md)

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

# **list_buckets**
> ListBucketsResponse list_buckets(authorization=authorization, x_namespace=x_namespace, list_buckets_request=list_buckets_request)

List Buckets

This endpoint lists buckets with pagination, sorting, and filtering options.

### Example


```python
import mixpeek
from mixpeek.models.list_buckets_request import ListBucketsRequest
from mixpeek.models.list_buckets_response import ListBucketsResponse
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
    api_instance = mixpeek.BucketsApi(api_client)
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)
    x_namespace = 'x_namespace_example' # str | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. (optional)
    list_buckets_request = mixpeek.ListBucketsRequest() # ListBucketsRequest |  (optional)

    try:
        # List Buckets
        api_response = api_instance.list_buckets(authorization=authorization, x_namespace=x_namespace, list_buckets_request=list_buckets_request)
        print("The response of BucketsApi->list_buckets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketsApi->list_buckets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 
 **x_namespace** | **str**| Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: &#39;netflix_prod&#39; or &#39;ns_1234567890&#39;. To create a namespace, use the /namespaces endpoint. | [optional] 
 **list_buckets_request** | [**ListBucketsRequest**](ListBucketsRequest.md)|  | [optional] 

### Return type

[**ListBucketsResponse**](ListBucketsResponse.md)

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

# **update_bucket**
> BucketResponse update_bucket(bucket_identifier, bucket_update_request, authorization=authorization, x_namespace=x_namespace)

Update Bucket

This endpoint allows you to update an existing bucket.
    You can update the bucket's name, description, and metadata.

### Example


```python
import mixpeek
from mixpeek.models.bucket_response import BucketResponse
from mixpeek.models.bucket_update_request import BucketUpdateRequest
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
    api_instance = mixpeek.BucketsApi(api_client)
    bucket_identifier = 'bucket_identifier_example' # str | 
    bucket_update_request = mixpeek.BucketUpdateRequest() # BucketUpdateRequest | 
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)
    x_namespace = 'x_namespace_example' # str | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. (optional)

    try:
        # Update Bucket
        api_response = api_instance.update_bucket(bucket_identifier, bucket_update_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of BucketsApi->update_bucket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketsApi->update_bucket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_identifier** | **str**|  | 
 **bucket_update_request** | [**BucketUpdateRequest**](BucketUpdateRequest.md)|  | 
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 
 **x_namespace** | **str**| Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: &#39;netflix_prod&#39; or &#39;ns_1234567890&#39;. To create a namespace, use the /namespaces endpoint. | [optional] 

### Return type

[**BucketResponse**](BucketResponse.md)

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

