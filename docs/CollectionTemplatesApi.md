# mixpeek.CollectionTemplatesApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_collection_template_from**](CollectionTemplatesApi.md#create_collection_template_from) | **POST** /v1/templates/collections/from-collection/{collection_id} | Create Collection Template
[**get_collection_template**](CollectionTemplatesApi.md#get_collection_template) | **GET** /v1/templates/collections/{template_id} | Get Collection Template
[**instantiate_collection_template**](CollectionTemplatesApi.md#instantiate_collection_template) | **POST** /v1/templates/collections/{template_id}/instantiate | Instantiate Collection Template
[**list_collection_templates**](CollectionTemplatesApi.md#list_collection_templates) | **POST** /v1/templates/collections | List Collection Templates


# **create_collection_template_from**
> CreateTemplateFromResourceResponse create_collection_template_from(collection_id, create_template_from_resource_request, authorization=authorization, x_namespace=x_namespace)

Create Collection Template

Create template from existing collection.

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
    api_instance = mixpeek.CollectionTemplatesApi(api_client)
    collection_id = 'collection_id_example' # str | Collection ID
    create_template_from_resource_request = mixpeek.CreateTemplateFromResourceRequest() # CreateTemplateFromResourceRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Create Collection Template
        api_response = api_instance.create_collection_template_from(collection_id, create_template_from_resource_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of CollectionTemplatesApi->create_collection_template_from:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionTemplatesApi->create_collection_template_from: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| Collection ID | 
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

# **get_collection_template**
> BaseTemplateModel get_collection_template(template_id, authorization=authorization, x_namespace=x_namespace)

Get Collection Template

Get collection template details.

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
    api_instance = mixpeek.CollectionTemplatesApi(api_client)
    template_id = 'template_id_example' # str | Template ID
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Collection Template
        api_response = api_instance.get_collection_template(template_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of CollectionTemplatesApi->get_collection_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionTemplatesApi->get_collection_template: %s\n" % e)
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

# **instantiate_collection_template**
> InstantiatedCollectionTemplateResponse instantiate_collection_template(template_id, instantiate_collection_template_request, authorization=authorization, x_namespace=x_namespace)

Instantiate Collection Template

Instantiate collection template.

### Example


```python
import mixpeek
from mixpeek.models.instantiate_collection_template_request import InstantiateCollectionTemplateRequest
from mixpeek.models.instantiated_collection_template_response import InstantiatedCollectionTemplateResponse
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
    api_instance = mixpeek.CollectionTemplatesApi(api_client)
    template_id = 'template_id_example' # str | Template ID
    instantiate_collection_template_request = mixpeek.InstantiateCollectionTemplateRequest() # InstantiateCollectionTemplateRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Instantiate Collection Template
        api_response = api_instance.instantiate_collection_template(template_id, instantiate_collection_template_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of CollectionTemplatesApi->instantiate_collection_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionTemplatesApi->instantiate_collection_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| Template ID | 
 **instantiate_collection_template_request** | [**InstantiateCollectionTemplateRequest**](InstantiateCollectionTemplateRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**InstantiatedCollectionTemplateResponse**](InstantiatedCollectionTemplateResponse.md)

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

# **list_collection_templates**
> ListTemplatesResponse list_collection_templates(authorization=authorization, x_namespace=x_namespace, list_templates_request=list_templates_request)

List Collection Templates

List collection templates (system + organization + user).

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
    api_instance = mixpeek.CollectionTemplatesApi(api_client)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)
    list_templates_request = mixpeek.ListTemplatesRequest() # ListTemplatesRequest |  (optional)

    try:
        # List Collection Templates
        api_response = api_instance.list_collection_templates(authorization=authorization, x_namespace=x_namespace, list_templates_request=list_templates_request)
        print("The response of CollectionTemplatesApi->list_collection_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionTemplatesApi->list_collection_templates: %s\n" % e)
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

