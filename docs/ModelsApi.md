# mixpeek.ModelsApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**confirm_upload_models**](ModelsApi.md#confirm_upload_models) | **POST** /v1/models/uploads/{upload_id}/confirm | Confirm model upload
[**delete_model**](ModelsApi.md#delete_model) | **DELETE** /v1/models/{model_id} | Delete model
[**generate_upload_url_models**](ModelsApi.md#generate_upload_url_models) | **POST** /v1/models/uploads | Generate presigned URL for model upload
[**get_model**](ModelsApi.md#get_model) | **GET** /v1/models/{model_id} | Get model details
[**list_models**](ModelsApi.md#list_models) | **GET** /v1/models | List organization models


# **confirm_upload_models**
> ConfirmModelUploadResponse confirm_upload_models(upload_id, authorization=authorization, confirm_model_upload_request=confirm_model_upload_request)

Confirm model upload

Confirm a model upload after the S3 upload completes.

This is step 3 of the presigned URL workflow. Call this after
uploading the model archive to the presigned URL.

The service will:
1. Verify the S3 object exists
2. Validate the archive structure
3. Create the model record

### Example


```python
import mixpeek
from mixpeek.models.confirm_model_upload_request import ConfirmModelUploadRequest
from mixpeek.models.confirm_model_upload_response import ConfirmModelUploadResponse
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
    api_instance = mixpeek.ModelsApi(api_client)
    upload_id = 'upload_id_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    confirm_model_upload_request = mixpeek.ConfirmModelUploadRequest() # ConfirmModelUploadRequest |  (optional)

    try:
        # Confirm model upload
        api_response = api_instance.confirm_upload_models(upload_id, authorization=authorization, confirm_model_upload_request=confirm_model_upload_request)
        print("The response of ModelsApi->confirm_upload_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->confirm_upload_models: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_id** | **str**|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **confirm_model_upload_request** | [**ConfirmModelUploadRequest**](ConfirmModelUploadRequest.md)|  | [optional] 

### Return type

[**ConfirmModelUploadResponse**](ConfirmModelUploadResponse.md)

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

# **delete_model**
> OrgModelDeleteResponse delete_model(model_id, authorization=authorization)

Delete model

Delete an org-level model.

The model must not be enabled in any namespaces. If it is still enabled,
you must disable it in all namespaces first before deleting.

### Example


```python
import mixpeek
from mixpeek.models.org_model_delete_response import OrgModelDeleteResponse
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
    api_instance = mixpeek.ModelsApi(api_client)
    model_id = 'model_id_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Delete model
        api_response = api_instance.delete_model(model_id, authorization=authorization)
        print("The response of ModelsApi->delete_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->delete_model: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **str**|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**OrgModelDeleteResponse**](OrgModelDeleteResponse.md)

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

# **generate_upload_url_models**
> ModelPresignedURLResponse generate_upload_url_models(create_model_upload_request, authorization=authorization)

Generate presigned URL for model upload

Generate a presigned URL for uploading a custom model archive.

This is step 1 of the presigned URL workflow:
1. POST /models/uploads → Returns presigned_url + upload_id
2. PUT presigned_url with model archive (client uploads directly to S3)
3. POST /models/uploads/{upload_id}/confirm → Validates and creates model

The model will be stored at the organization level and can be enabled
in any namespace within the organization.

### Example


```python
import mixpeek
from mixpeek.models.create_model_upload_request import CreateModelUploadRequest
from mixpeek.models.model_presigned_url_response import ModelPresignedURLResponse
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
    api_instance = mixpeek.ModelsApi(api_client)
    create_model_upload_request = mixpeek.CreateModelUploadRequest() # CreateModelUploadRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Generate presigned URL for model upload
        api_response = api_instance.generate_upload_url_models(create_model_upload_request, authorization=authorization)
        print("The response of ModelsApi->generate_upload_url_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->generate_upload_url_models: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_model_upload_request** | [**CreateModelUploadRequest**](CreateModelUploadRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**ModelPresignedURLResponse**](ModelPresignedURLResponse.md)

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

# **get_model**
> OrgModelDetailResponse get_model(model_id, authorization=authorization)

Get model details

Get detailed information about an org-level model.

### Example


```python
import mixpeek
from mixpeek.models.org_model_detail_response import OrgModelDetailResponse
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
    api_instance = mixpeek.ModelsApi(api_client)
    model_id = 'model_id_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Get model details
        api_response = api_instance.get_model(model_id, authorization=authorization)
        print("The response of ModelsApi->get_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->get_model: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **str**|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**OrgModelDetailResponse**](OrgModelDetailResponse.md)

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

# **list_models**
> OrgModelListResponse list_models(authorization=authorization)

List organization models

List all custom models registered at the organization level.

These models can be enabled in any namespace within the organization
using the namespace-level enable endpoint.

### Example


```python
import mixpeek
from mixpeek.models.org_model_list_response import OrgModelListResponse
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
    api_instance = mixpeek.ModelsApi(api_client)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # List organization models
        api_response = api_instance.list_models(authorization=authorization)
        print("The response of ModelsApi->list_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->list_models: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**OrgModelListResponse**](OrgModelListResponse.md)

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

