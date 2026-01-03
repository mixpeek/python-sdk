# mixpeek.BucketTemplatesApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bucket_template_from**](BucketTemplatesApi.md#create_bucket_template_from) | **POST** /v1/templates/buckets/from-bucket/{bucket_id} | Create Bucket Template
[**get_bucket_template**](BucketTemplatesApi.md#get_bucket_template) | **GET** /v1/templates/buckets/{template_id} | Get Bucket Template
[**instantiate_bucket_template**](BucketTemplatesApi.md#instantiate_bucket_template) | **POST** /v1/templates/buckets/{template_id}/instantiate | Instantiate Bucket Template
[**list_bucket_templates**](BucketTemplatesApi.md#list_bucket_templates) | **POST** /v1/templates/buckets | List Bucket Templates


# **create_bucket_template_from**
> CreateTemplateFromResourceResponse create_bucket_template_from(bucket_id, create_template_from_resource_request, authorization=authorization, x_namespace=x_namespace)

Create Bucket Template

Create template from existing bucket.

Supports three template scopes:
- **organization**: Available to all users in your organization (default)
- **user**: Available only to you
- **system**: Available to all organizations (requires Mixpeek admin email)

### Example


```python
import mixpeek
from mixpeek.models.create_template_from_resource_request import CreateTemplateFromResourceRequest
from mixpeek.models.create_template_from_resource_response import CreateTemplateFromResourceResponse
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
    api_instance = mixpeek.BucketTemplatesApi(api_client)
    bucket_id = 'bucket_id_example' # str | Bucket ID
    create_template_from_resource_request = mixpeek.CreateTemplateFromResourceRequest() # CreateTemplateFromResourceRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Create Bucket Template
        api_response = api_instance.create_bucket_template_from(bucket_id, create_template_from_resource_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of BucketTemplatesApi->create_bucket_template_from:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketTemplatesApi->create_bucket_template_from: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **str**| Bucket ID | 
 **create_template_from_resource_request** | [**CreateTemplateFromResourceRequest**](CreateTemplateFromResourceRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**CreateTemplateFromResourceResponse**](CreateTemplateFromResourceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bucket_template**
> BaseTemplateModel get_bucket_template(template_id, authorization=authorization, x_namespace=x_namespace)

Get Bucket Template

Get bucket template details.

### Example


```python
import mixpeek
from mixpeek.models.base_template_model import BaseTemplateModel
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
    api_instance = mixpeek.BucketTemplatesApi(api_client)
    template_id = 'template_id_example' # str | Template ID
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Bucket Template
        api_response = api_instance.get_bucket_template(template_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of BucketTemplatesApi->get_bucket_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketTemplatesApi->get_bucket_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| Template ID | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**BaseTemplateModel**](BaseTemplateModel.md)

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

# **instantiate_bucket_template**
> InstantiatedBucketTemplateResponse instantiate_bucket_template(template_id, instantiate_bucket_template_request, authorization=authorization, x_namespace=x_namespace)

Instantiate Bucket Template

Instantiate bucket template.

### Example


```python
import mixpeek
from mixpeek.models.instantiate_bucket_template_request import InstantiateBucketTemplateRequest
from mixpeek.models.instantiated_bucket_template_response import InstantiatedBucketTemplateResponse
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
    api_instance = mixpeek.BucketTemplatesApi(api_client)
    template_id = 'template_id_example' # str | Template ID
    instantiate_bucket_template_request = mixpeek.InstantiateBucketTemplateRequest() # InstantiateBucketTemplateRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Instantiate Bucket Template
        api_response = api_instance.instantiate_bucket_template(template_id, instantiate_bucket_template_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of BucketTemplatesApi->instantiate_bucket_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketTemplatesApi->instantiate_bucket_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| Template ID | 
 **instantiate_bucket_template_request** | [**InstantiateBucketTemplateRequest**](InstantiateBucketTemplateRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**InstantiatedBucketTemplateResponse**](InstantiatedBucketTemplateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_bucket_templates**
> ListTemplatesResponse list_bucket_templates(authorization=authorization, x_namespace=x_namespace, list_templates_request=list_templates_request)

List Bucket Templates

List bucket templates (system + organization + user).

Supports filtering, sorting, and search like other list operations.

### Example


```python
import mixpeek
from mixpeek.models.list_templates_request import ListTemplatesRequest
from mixpeek.models.list_templates_response import ListTemplatesResponse
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
    api_instance = mixpeek.BucketTemplatesApi(api_client)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)
    list_templates_request = mixpeek.ListTemplatesRequest() # ListTemplatesRequest |  (optional)

    try:
        # List Bucket Templates
        api_response = api_instance.list_bucket_templates(authorization=authorization, x_namespace=x_namespace, list_templates_request=list_templates_request)
        print("The response of BucketTemplatesApi->list_bucket_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketTemplatesApi->list_bucket_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 
 **list_templates_request** | [**ListTemplatesRequest**](ListTemplatesRequest.md)|  | [optional] 

### Return type

[**ListTemplatesResponse**](ListTemplatesResponse.md)

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

