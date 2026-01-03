# mixpeek.BucketUploadsApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**confirm_upload_buckets**](BucketUploadsApi.md#confirm_upload_buckets) | **POST** /v1/buckets/{bucket_identifier}/uploads/{upload_id}/confirm | Confirm Upload
[**confirm_uploads_batch_buckets**](BucketUploadsApi.md#confirm_uploads_batch_buckets) | **POST** /v1/buckets/{bucket_identifier}/uploads/confirm/batch | Batch Confirm Uploads
[**create_upload_buckets**](BucketUploadsApi.md#create_upload_buckets) | **POST** /v1/buckets/{bucket_identifier}/uploads | Create Upload
[**create_uploads_batch_buckets**](BucketUploadsApi.md#create_uploads_batch_buckets) | **POST** /v1/buckets/{bucket_identifier}/uploads/batch | Batch Create Uploads
[**delete_upload_buckets**](BucketUploadsApi.md#delete_upload_buckets) | **DELETE** /v1/buckets/{bucket_identifier}/uploads/{upload_id} | Delete Upload
[**get_upload_buckets**](BucketUploadsApi.md#get_upload_buckets) | **GET** /v1/buckets/{bucket_identifier}/uploads/{upload_id} | Get Upload
[**list_uploads_buckets**](BucketUploadsApi.md#list_uploads_buckets) | **POST** /v1/buckets/{bucket_identifier}/uploads/list | List Uploads


# **confirm_upload_buckets**
> ConfirmUploadResponse confirm_upload_buckets(bucket_identifier, upload_id, confirm_upload_request, var_async=var_async, authorization=authorization, x_namespace=x_namespace)

Confirm Upload

Verify S3 upload completion and create bucket object.

    After uploading to S3 using the presigned URL, call this endpoint to:
    1. Verify the file exists in S3
    2. Validate ETag and file size (if provided)
    3. Create bucket object (default, unless create_object_on_confirm=false)
    4. Update upload status to COMPLETED

    **Sync vs Async**:
    - Files < 100MB: Processed synchronously (~100ms)
    - Files >= 100MB or async=true: Processed asynchronously (returns task_id)

    **Duplicate Detection**:
    - If file hash matches existing upload, marks as duplicate
    - References original object_id if available

### Example


```python
import mixpeek
from mixpeek.models.confirm_upload_request import ConfirmUploadRequest
from mixpeek.models.confirm_upload_response import ConfirmUploadResponse
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
    api_instance = mixpeek.BucketUploadsApi(api_client)
    bucket_identifier = 'bucket_identifier_example' # str | The unique identifier of the bucket
    upload_id = 'upload_id_example' # str | The unique identifier of the upload
    confirm_upload_request = mixpeek.ConfirmUploadRequest() # ConfirmUploadRequest | 
    var_async = False # bool | Process confirmation asynchronously (recommended for files >= 100MB) (optional) (default to False)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Confirm Upload
        api_response = api_instance.confirm_upload_buckets(bucket_identifier, upload_id, confirm_upload_request, var_async=var_async, authorization=authorization, x_namespace=x_namespace)
        print("The response of BucketUploadsApi->confirm_upload_buckets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketUploadsApi->confirm_upload_buckets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_identifier** | **str**| The unique identifier of the bucket | 
 **upload_id** | **str**| The unique identifier of the upload | 
 **confirm_upload_request** | [**ConfirmUploadRequest**](ConfirmUploadRequest.md)|  | 
 **var_async** | **bool**| Process confirmation asynchronously (recommended for files &gt;&#x3D; 100MB) | [optional] [default to False]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**ConfirmUploadResponse**](ConfirmUploadResponse.md)

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

# **confirm_uploads_batch_buckets**
> BatchConfirmResponse confirm_uploads_batch_buckets(bucket_identifier, batch_confirm_request, authorization=authorization, x_namespace=x_namespace)

Batch Confirm Uploads

Confirm multiple uploads in a single request (processed asynchronously).

    Maximum 100 confirmations per batch.
    All uploads must belong to the same bucket.

    Returns a task_id to track progress via GET /v1/tasks/{task_id}.

### Example


```python
import mixpeek
from mixpeek.models.batch_confirm_request import BatchConfirmRequest
from mixpeek.models.batch_confirm_response import BatchConfirmResponse
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
    api_instance = mixpeek.BucketUploadsApi(api_client)
    bucket_identifier = 'bucket_identifier_example' # str | The unique identifier of the bucket
    batch_confirm_request = mixpeek.BatchConfirmRequest() # BatchConfirmRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Batch Confirm Uploads
        api_response = api_instance.confirm_uploads_batch_buckets(bucket_identifier, batch_confirm_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of BucketUploadsApi->confirm_uploads_batch_buckets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketUploadsApi->confirm_uploads_batch_buckets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_identifier** | **str**| The unique identifier of the bucket | 
 **batch_confirm_request** | [**BatchConfirmRequest**](BatchConfirmRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**BatchConfirmResponse**](BatchConfirmResponse.md)

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

# **create_upload_buckets**
> UploadResponse create_upload_buckets(bucket_identifier, create_upload_request, authorization=authorization, x_namespace=x_namespace)

Create Upload

Generate a presigned URL for direct S3 upload.

    This endpoint validates all requirements BEFORE generating the presigned URL,
    ensuring immediate feedback if something is wrong (bucket inactive, quota exceeded, etc.).

    **Duplicate Detection (Enabled by Default)**:
    - If `file_hash` provided and `skip_duplicates=true`: Checks for existing upload
    - If duplicate found: Returns existing upload (200 OK) with `is_duplicate=true`
    - If new file: Returns presigned URL (201 Created) with `is_duplicate=false`

    **Two-Step Flow**:
    1. Call this endpoint → Get presigned URL
    2. PUT file to presigned URL → Upload directly to S3
    3. Call confirm endpoint → Verify upload and create object

### Example


```python
import mixpeek
from mixpeek.models.create_upload_request import CreateUploadRequest
from mixpeek.models.upload_response import UploadResponse
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
    api_instance = mixpeek.BucketUploadsApi(api_client)
    bucket_identifier = 'bucket_identifier_example' # str | The unique identifier of the bucket
    create_upload_request = mixpeek.CreateUploadRequest() # CreateUploadRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Create Upload
        api_response = api_instance.create_upload_buckets(bucket_identifier, create_upload_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of BucketUploadsApi->create_upload_buckets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketUploadsApi->create_upload_buckets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_identifier** | **str**| The unique identifier of the bucket | 
 **create_upload_request** | [**CreateUploadRequest**](CreateUploadRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**UploadResponse**](UploadResponse.md)

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

# **create_uploads_batch_buckets**
> BatchUploadResponse create_uploads_batch_buckets(bucket_identifier, batch_upload_request, authorization=authorization, x_namespace=x_namespace)

Batch Create Uploads

Generate multiple presigned URLs in a single request.

    All uploads belong to the same bucket (from path parameter).
    Maximum 100 uploads per batch.

    Shared metadata is merged with individual upload metadata (individual takes precedence).

### Example


```python
import mixpeek
from mixpeek.models.batch_upload_request import BatchUploadRequest
from mixpeek.models.batch_upload_response import BatchUploadResponse
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
    api_instance = mixpeek.BucketUploadsApi(api_client)
    bucket_identifier = 'bucket_identifier_example' # str | The unique identifier of the bucket
    batch_upload_request = mixpeek.BatchUploadRequest() # BatchUploadRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Batch Create Uploads
        api_response = api_instance.create_uploads_batch_buckets(bucket_identifier, batch_upload_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of BucketUploadsApi->create_uploads_batch_buckets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketUploadsApi->create_uploads_batch_buckets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_identifier** | **str**| The unique identifier of the bucket | 
 **batch_upload_request** | [**BatchUploadRequest**](BatchUploadRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**BatchUploadResponse**](BatchUploadResponse.md)

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

# **delete_upload_buckets**
> delete_upload_buckets(bucket_identifier, upload_id, delete_s3_object=delete_s3_object, authorization=authorization, x_namespace=x_namespace)

Delete Upload

Cancel an upload and optionally delete the S3 object.

    Cannot cancel uploads with status COMPLETED.
    Can cancel uploads with status: PENDING, IN_PROGRESS, FAILED.

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
    api_instance = mixpeek.BucketUploadsApi(api_client)
    bucket_identifier = 'bucket_identifier_example' # str | The unique identifier of the bucket
    upload_id = 'upload_id_example' # str | The unique identifier of the upload
    delete_s3_object = True # bool | Whether to delete the S3 object (optional) (default to True)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Delete Upload
        api_instance.delete_upload_buckets(bucket_identifier, upload_id, delete_s3_object=delete_s3_object, authorization=authorization, x_namespace=x_namespace)
    except Exception as e:
        print("Exception when calling BucketUploadsApi->delete_upload_buckets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_identifier** | **str**| The unique identifier of the bucket | 
 **upload_id** | **str**| The unique identifier of the upload | 
 **delete_s3_object** | **bool**| Whether to delete the S3 object | [optional] [default to True]
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

# **get_upload_buckets**
> object get_upload_buckets(bucket_identifier, upload_id, return_presigned_urls=return_presigned_urls, authorization=authorization, x_namespace=x_namespace)

Get Upload

Retrieve an upload by its ID.

    Use this to check upload status, get S3 key, or retrieve created object_id after confirmation.

    **Presigned URLs**: Set `return_presigned_urls=true` query parameter to generate fresh presigned download URLs (default: false).
    The presigned URLs expire after 1 hour and allow direct download from S3.

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
    api_instance = mixpeek.BucketUploadsApi(api_client)
    bucket_identifier = 'bucket_identifier_example' # str | The unique identifier of the bucket
    upload_id = 'upload_id_example' # str | The unique identifier of the upload
    return_presigned_urls = False # bool | Generate fresh presigned download URLs for all blobs with S3 storage (optional) (default to False)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Upload
        api_response = api_instance.get_upload_buckets(bucket_identifier, upload_id, return_presigned_urls=return_presigned_urls, authorization=authorization, x_namespace=x_namespace)
        print("The response of BucketUploadsApi->get_upload_buckets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketUploadsApi->get_upload_buckets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_identifier** | **str**| The unique identifier of the bucket | 
 **upload_id** | **str**| The unique identifier of the upload | 
 **return_presigned_urls** | **bool**| Generate fresh presigned download URLs for all blobs with S3 storage | [optional] [default to False]
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

# **list_uploads_buckets**
> ListUploadsResponse list_uploads_buckets(bucket_identifier, limit=limit, offset=offset, cursor=cursor, include_total=include_total, authorization=authorization, x_namespace=x_namespace, list_uploads_request=list_uploads_request)

List Uploads

List uploads in a bucket with filtering, sorting, search, and pagination.

    **Filtering**: Use LogicalOperator with shorthand syntax
    - Simple: `{"status": "PENDING", "metadata.campaign": "summer_2024"}`
    - Complex: `{"AND": [{"field": "file_size_bytes", "operator": "gte", "value": 1000000}]}`

    **Sorting**: Specify field and direction
    - Example: `{"field": "created_at", "direction": "desc"}`

    **Search**: Full-text search across filename and metadata
    - Example: `"search": "video"`

    **Pagination**: Use limit and offset
    - Example: `"limit": 50, "offset": 100`

### Example


```python
import mixpeek
from mixpeek.models.list_uploads_request import ListUploadsRequest
from mixpeek.models.list_uploads_response import ListUploadsResponse
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
    api_instance = mixpeek.BucketUploadsApi(api_client)
    bucket_identifier = 'bucket_identifier_example' # str | The unique identifier of the bucket
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    cursor = 'cursor_example' # str |  (optional)
    include_total = False # bool |  (optional) (default to False)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)
    list_uploads_request = mixpeek.ListUploadsRequest() # ListUploadsRequest |  (optional)

    try:
        # List Uploads
        api_response = api_instance.list_uploads_buckets(bucket_identifier, limit=limit, offset=offset, cursor=cursor, include_total=include_total, authorization=authorization, x_namespace=x_namespace, list_uploads_request=list_uploads_request)
        print("The response of BucketUploadsApi->list_uploads_buckets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketUploadsApi->list_uploads_buckets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_identifier** | **str**| The unique identifier of the bucket | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **cursor** | **str**|  | [optional] 
 **include_total** | **bool**|  | [optional] [default to False]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 
 **list_uploads_request** | [**ListUploadsRequest**](ListUploadsRequest.md)|  | [optional] 

### Return type

[**ListUploadsResponse**](ListUploadsResponse.md)

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

