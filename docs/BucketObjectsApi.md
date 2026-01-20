# mixpeek.BucketObjectsApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aggregate_objects_buckets**](BucketObjectsApi.md#aggregate_objects_buckets) | **POST** /v1/buckets/{bucket_identifier}/objects/aggregate | Aggregate Objects
[**create_object_buckets**](BucketObjectsApi.md#create_object_buckets) | **POST** /v1/buckets/{bucket_identifier}/objects | Create Object
[**create_objects_batch_buckets**](BucketObjectsApi.md#create_objects_batch_buckets) | **POST** /v1/buckets/{bucket_identifier}/objects/batch | Create Objects in Batch
[**delete_object_buckets**](BucketObjectsApi.md#delete_object_buckets) | **DELETE** /v1/buckets/{bucket_identifier}/objects/{object_identifier} | Delete Object
[**get_object_buckets**](BucketObjectsApi.md#get_object_buckets) | **GET** /v1/buckets/{bucket_identifier}/objects/{object_identifier} | Get Object
[**list_objects_buckets**](BucketObjectsApi.md#list_objects_buckets) | **POST** /v1/buckets/{bucket_identifier}/objects/list | List Objects
[**patch_object_buckets**](BucketObjectsApi.md#patch_object_buckets) | **PATCH** /v1/buckets/{bucket_identifier}/objects/{object_identifier} | Partially Update Object
[**update_object_buckets**](BucketObjectsApi.md#update_object_buckets) | **PUT** /v1/buckets/{bucket_identifier}/objects/{object_identifier} | Update Object


# **aggregate_objects_buckets**
> ObjectAggregationResponse aggregate_objects_buckets(bucket_identifier, object_aggregation_request, authorization=authorization, x_namespace=x_namespace)

Aggregate Objects

This endpoint performs aggregation operations on objects in a bucket.

    **Aggregation Framework**: Provides MongoDB-style aggregation operations:
    - GROUP BY: Group objects by one or more fields
    - Aggregations: COUNT, SUM, AVG, MIN, MAX, COUNT_DISTINCT, etc.
    - Date Operations: Truncate or extract date parts for time-series analysis
    - Filtering: Pre-aggregation filters (WHERE) and post-aggregation filters (HAVING)
    - Sorting & Limiting: Control result ordering and size

    **Use Cases**:
    - Count objects by status or category
    - Calculate daily/monthly upload statistics
    - Analyze content distribution and trends
    - Generate reports with multiple metrics

    **Note**: This endpoint works with both MongoDB objects and Qdrant documents
    using the same interface. The system automatically selects the appropriate
    aggregation provider.

### Example


```python
import mixpeek
from mixpeek.models.object_aggregation_request import ObjectAggregationRequest
from mixpeek.models.object_aggregation_response import ObjectAggregationResponse
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
    object_aggregation_request = mixpeek.ObjectAggregationRequest() # ObjectAggregationRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Aggregate Objects
        api_response = api_instance.aggregate_objects_buckets(bucket_identifier, object_aggregation_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of BucketObjectsApi->aggregate_objects_buckets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketObjectsApi->aggregate_objects_buckets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_identifier** | **str**| The unique identifier of the bucket. | 
 **object_aggregation_request** | [**ObjectAggregationRequest**](ObjectAggregationRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**ObjectAggregationResponse**](ObjectAggregationResponse.md)

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

# **create_object_buckets**
> ObjectResponse create_object_buckets(bucket_identifier, create_object_request, policy=policy, auto_process=auto_process, authorization=authorization, x_namespace=x_namespace)

Create Object

This endpoint creates a new object in the specified bucket.
    The object must conform to the bucket's schema.

    **Processing**: By default, objects are created in DRAFT status and require
    batch submission for processing. Set `auto_process=true` to automatically
    create a batch and submit it for processing (zero-touch workflow).

    If the bucket has a unique_key configured, the insertion policy determines behavior:
    - insert: Create only. Fail with 409 Conflict if unique key exists.
    - update: Update only. Fail with 404 Not Found if unique key doesn't exist.
    - upsert: Create if new, update if exists (idempotent).

    Policy resolution:
    1. Use ?policy= query parameter if provided
    2. Fall back to bucket's default_policy if configured
    3. Error 400 if neither is specified

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
    policy = 'policy_example' # str | Insertion policy for unique key enforcement. Valid values: 'insert', 'update', 'upsert'. Only applies if bucket has unique_key configured. Overrides bucket's default_policy if provided. (optional)
    auto_process = False # bool | Automatically create a batch and submit it for processing. When true, the object will be immediately queued for processing without requiring separate batch creation and submission calls. Ideal for onboarding and single-object workflows. (optional) (default to False)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Create Object
        api_response = api_instance.create_object_buckets(bucket_identifier, create_object_request, policy=policy, auto_process=auto_process, authorization=authorization, x_namespace=x_namespace)
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
 **policy** | **str**| Insertion policy for unique key enforcement. Valid values: &#39;insert&#39;, &#39;update&#39;, &#39;upsert&#39;. Only applies if bucket has unique_key configured. Overrides bucket&#39;s default_policy if provided. | [optional] 
 **auto_process** | **bool**| Automatically create a batch and submit it for processing. When true, the object will be immediately queued for processing without requiring separate batch creation and submission calls. Ideal for onboarding and single-object workflows. | [optional] [default to False]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

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
> CreateObjectsBatchResponse create_objects_batch_buckets(bucket_identifier, create_objects_batch_request, auto_process=auto_process, authorization=authorization, x_namespace=x_namespace)

Create Objects in Batch

This endpoint creates multiple new objects in the specified bucket as a batch.
    Each object must conform to the bucket's schema.

    **Processing**: By default, objects are created in DRAFT status and require
    batch submission for processing. Set `auto_process=true` to automatically
    create a processing batch and submit it (zero-touch workflow).

    **Partial Success**: This endpoint uses partial success - valid objects are created
    even if some fail validation. Failed objects are returned separately with error details,
    allowing you to fix and retry only the failed ones.

    **Response**: Returns both succeeded and failed objects. The batch succeeds (200 OK) as long
    as at least one object is created. Check the `failed` array for objects that need attention.

### Example


```python
import mixpeek
from mixpeek.models.create_objects_batch_request import CreateObjectsBatchRequest
from mixpeek.models.create_objects_batch_response import CreateObjectsBatchResponse
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
    auto_process = False # bool | Automatically create a batch and submit it for processing. When true, all successfully created objects will be immediately queued for processing without requiring separate batch calls. Ideal for onboarding and bulk upload workflows. (optional) (default to False)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Create Objects in Batch
        api_response = api_instance.create_objects_batch_buckets(bucket_identifier, create_objects_batch_request, auto_process=auto_process, authorization=authorization, x_namespace=x_namespace)
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
 **auto_process** | **bool**| Automatically create a batch and submit it for processing. When true, all successfully created objects will be immediately queued for processing without requiring separate batch calls. Ideal for onboarding and bulk upload workflows. | [optional] [default to False]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**CreateObjectsBatchResponse**](CreateObjectsBatchResponse.md)

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
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

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
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

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
> ObjectResponse get_object_buckets(bucket_identifier, object_identifier, return_presigned_urls=return_presigned_urls, authorization=authorization, x_namespace=x_namespace)

Get Object

This endpoint retrieves an object by its ID from the specified bucket.

    **Presigned URLs**: Set `return_presigned_urls=true` query parameter to generate fresh presigned download URLs
    for all blobs with S3 storage (default: false). URLs are added to each blob's properties as
    `presigned_url` and expire after 1 hour.

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
    return_presigned_urls = False # bool | Generate fresh presigned download URLs for all blobs with S3 storage (optional) (default to False)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Object
        api_response = api_instance.get_object_buckets(bucket_identifier, object_identifier, return_presigned_urls=return_presigned_urls, authorization=authorization, x_namespace=x_namespace)
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
 **return_presigned_urls** | **bool**| Generate fresh presigned download URLs for all blobs with S3 storage | [optional] [default to False]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

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
> ListObjectsResponse list_objects_buckets(bucket_identifier, limit=limit, offset=offset, cursor=cursor, include_total=include_total, authorization=authorization, x_namespace=x_namespace, list_objects_request=list_objects_request)

List Objects

This endpoint lists objects in a bucket with cursor-based pagination, filtering, and sorting.

    **Filtering**: Use dot notation for metadata fields
    - Example: ?metadata.type=video&metadata.status=ready

    **Sorting**: Specify field and direction
    - Example: ?sort_field=metadata.created_at&sort_direction=desc
    - Direction: asc (ascending) or desc (descending), defaults to asc

    **Pagination**: Cursor-based for efficient deep pagination
    - First page: ?limit=100 (omit cursor)
    - Next pages: ?limit=100&cursor={next_cursor}
    - Use next_cursor from response to navigate
    - No limit on pagination depth

    **Total Count**: Optional (expensive operation)
    - Use ?include_total=true to get total count
    - Adds 50-200ms to response time
    - Returns total, page, page_size, total_pages fields in pagination response

### Example


```python
import mixpeek
from mixpeek.models.list_objects_request import ListObjectsRequest
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
    cursor = 'cursor_example' # str |  (optional)
    include_total = False # bool |  (optional) (default to False)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)
    list_objects_request = mixpeek.ListObjectsRequest() # ListObjectsRequest |  (optional)

    try:
        # List Objects
        api_response = api_instance.list_objects_buckets(bucket_identifier, limit=limit, offset=offset, cursor=cursor, include_total=include_total, authorization=authorization, x_namespace=x_namespace, list_objects_request=list_objects_request)
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
 **cursor** | **str**|  | [optional] 
 **include_total** | **bool**|  | [optional] [default to False]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 
 **list_objects_request** | [**ListObjectsRequest**](ListObjectsRequest.md)|  | [optional] 

### Return type

[**ListObjectsResponse**](ListObjectsResponse.md)

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

# **patch_object_buckets**
> ObjectResponse patch_object_buckets(bucket_identifier, object_identifier, patch_object_request, authorization=authorization, x_namespace=x_namespace)

Partially Update Object

This endpoint partially updates an existing object in the specified bucket (PATCH operation).
    Only provided fields will be updated. At minimum, metadata can always be updated.
    Immutable fields like object_id and timestamps cannot be modified.
    It does not trigger processing.

### Example


```python
import mixpeek
from mixpeek.models.object_response import ObjectResponse
from mixpeek.models.patch_object_request import PatchObjectRequest
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
    patch_object_request = mixpeek.PatchObjectRequest() # PatchObjectRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Partially Update Object
        api_response = api_instance.patch_object_buckets(bucket_identifier, object_identifier, patch_object_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of BucketObjectsApi->patch_object_buckets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketObjectsApi->patch_object_buckets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_identifier** | **str**| The unique identifier of the bucket. | 
 **object_identifier** | **str**| The unique identifier of the object. | 
 **patch_object_request** | [**PatchObjectRequest**](PatchObjectRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

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
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

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
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

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

