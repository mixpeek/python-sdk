# mixpeek.TaxonomyTemplatesApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_taxonomy_template_taxonomies_from**](TaxonomyTemplatesApi.md#create_taxonomy_template_taxonomies_from) | **POST** /v1/templates/taxonomies/from-taxonomy/{taxonomy_id} | Create Taxonomy Template
[**get_taxonomy_template_taxonomies**](TaxonomyTemplatesApi.md#get_taxonomy_template_taxonomies) | **GET** /v1/templates/taxonomies/{template_id} | Get Taxonomy Template
[**instantiate_taxonomy_template_taxonomies**](TaxonomyTemplatesApi.md#instantiate_taxonomy_template_taxonomies) | **POST** /v1/templates/taxonomies/{template_id}/instantiate | Instantiate Taxonomy Template
[**list_taxonomy_templates_taxonomies**](TaxonomyTemplatesApi.md#list_taxonomy_templates_taxonomies) | **POST** /v1/templates/taxonomies | List Taxonomy Templates


# **create_taxonomy_template_taxonomies_from**
> CreateTemplateFromResourceResponse create_taxonomy_template_taxonomies_from(taxonomy_id, create_template_from_resource_request, authorization=authorization, x_namespace=x_namespace)

Create Taxonomy Template

Create template from existing taxonomy.

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
    api_instance = mixpeek.TaxonomyTemplatesApi(api_client)
    taxonomy_id = 'taxonomy_id_example' # str | Taxonomy ID
    create_template_from_resource_request = mixpeek.CreateTemplateFromResourceRequest() # CreateTemplateFromResourceRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Create Taxonomy Template
        api_response = api_instance.create_taxonomy_template_taxonomies_from(taxonomy_id, create_template_from_resource_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of TaxonomyTemplatesApi->create_taxonomy_template_taxonomies_from:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomyTemplatesApi->create_taxonomy_template_taxonomies_from: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxonomy_id** | **str**| Taxonomy ID | 
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

# **get_taxonomy_template_taxonomies**
> BaseTemplateModel get_taxonomy_template_taxonomies(template_id, authorization=authorization, x_namespace=x_namespace)

Get Taxonomy Template

Get taxonomy template details.

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
    api_instance = mixpeek.TaxonomyTemplatesApi(api_client)
    template_id = 'template_id_example' # str | Template ID
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Taxonomy Template
        api_response = api_instance.get_taxonomy_template_taxonomies(template_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of TaxonomyTemplatesApi->get_taxonomy_template_taxonomies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomyTemplatesApi->get_taxonomy_template_taxonomies: %s\n" % e)
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

# **instantiate_taxonomy_template_taxonomies**
> InstantiatedTaxonomyTemplateResponse instantiate_taxonomy_template_taxonomies(template_id, instantiate_taxonomy_template_request, authorization=authorization, x_namespace=x_namespace)

Instantiate Taxonomy Template

Instantiate taxonomy template.

### Example


```python
import mixpeek
from mixpeek.models.instantiate_taxonomy_template_request import InstantiateTaxonomyTemplateRequest
from mixpeek.models.instantiated_taxonomy_template_response import InstantiatedTaxonomyTemplateResponse
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
    api_instance = mixpeek.TaxonomyTemplatesApi(api_client)
    template_id = 'template_id_example' # str | Template ID
    instantiate_taxonomy_template_request = mixpeek.InstantiateTaxonomyTemplateRequest() # InstantiateTaxonomyTemplateRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Instantiate Taxonomy Template
        api_response = api_instance.instantiate_taxonomy_template_taxonomies(template_id, instantiate_taxonomy_template_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of TaxonomyTemplatesApi->instantiate_taxonomy_template_taxonomies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomyTemplatesApi->instantiate_taxonomy_template_taxonomies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| Template ID | 
 **instantiate_taxonomy_template_request** | [**InstantiateTaxonomyTemplateRequest**](InstantiateTaxonomyTemplateRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**InstantiatedTaxonomyTemplateResponse**](InstantiatedTaxonomyTemplateResponse.md)

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

# **list_taxonomy_templates_taxonomies**
> ListTemplatesResponse list_taxonomy_templates_taxonomies(authorization=authorization, x_namespace=x_namespace, list_templates_request=list_templates_request)

List Taxonomy Templates

List taxonomy templates (system + organization + user).

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
    api_instance = mixpeek.TaxonomyTemplatesApi(api_client)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)
    list_templates_request = mixpeek.ListTemplatesRequest() # ListTemplatesRequest |  (optional)

    try:
        # List Taxonomy Templates
        api_response = api_instance.list_taxonomy_templates_taxonomies(authorization=authorization, x_namespace=x_namespace, list_templates_request=list_templates_request)
        print("The response of TaxonomyTemplatesApi->list_taxonomy_templates_taxonomies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomyTemplatesApi->list_taxonomy_templates_taxonomies: %s\n" % e)
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

