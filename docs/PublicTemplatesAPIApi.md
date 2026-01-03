# mixpeek.PublicTemplatesAPIApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_namespace_template**](PublicTemplatesAPIApi.md#get_namespace_template) | **GET** /v1/public/templates/namespaces/{template_id} | Get Public Namespace Template
[**get_retriever_template**](PublicTemplatesAPIApi.md#get_retriever_template) | **GET** /v1/public/templates/retrievers/{template_id} | Get Public Retriever Template
[**get_scaffold_templates**](PublicTemplatesAPIApi.md#get_scaffold_templates) | **GET** /v1/public/templates/scaffolds/{template_id} | Get Scaffold
[**list_namespace_templates**](PublicTemplatesAPIApi.md#list_namespace_templates) | **GET** /v1/public/templates/namespaces | List Public Namespace Templates
[**list_retriever_templates**](PublicTemplatesAPIApi.md#list_retriever_templates) | **GET** /v1/public/templates/retrievers | List Public Retriever Templates
[**list_scaffolds_templates**](PublicTemplatesAPIApi.md#list_scaffolds_templates) | **GET** /v1/public/templates/scaffolds | List Scaffolds


# **get_namespace_template**
> BaseTemplateModel get_namespace_template(template_id)

Get Public Namespace Template

Get public namespace template details (no authentication required).

Returns template only if marked as public.

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
    api_instance = mixpeek.PublicTemplatesAPIApi(api_client)
    template_id = 'template_id_example' # str | Template ID

    try:
        # Get Public Namespace Template
        api_response = api_instance.get_namespace_template(template_id)
        print("The response of PublicTemplatesAPIApi->get_namespace_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicTemplatesAPIApi->get_namespace_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| Template ID | 

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

# **get_retriever_template**
> BaseTemplateModel get_retriever_template(template_id)

Get Public Retriever Template

Get public retriever template details (no authentication required).

Returns template only if marked as public.

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
    api_instance = mixpeek.PublicTemplatesAPIApi(api_client)
    template_id = 'template_id_example' # str | Template ID

    try:
        # Get Public Retriever Template
        api_response = api_instance.get_retriever_template(template_id)
        print("The response of PublicTemplatesAPIApi->get_retriever_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicTemplatesAPIApi->get_retriever_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| Template ID | 

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

# **get_scaffold_templates**
> BaseTemplateModel get_scaffold_templates(template_id)

Get Scaffold

Get scaffold template details (public, no auth required).

Returns the complete configuration including:
- Namespace: feature extractors, payload indexes
- Bucket: name, description, schema
- Collection: feature extractor config
- Retriever: stages, input schema

**To instantiate (requires auth):**
```
POST /v1/templates/scaffolds/{template_id}/instantiate
{"namespace_name": "my_app"}
```

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
    api_instance = mixpeek.PublicTemplatesAPIApi(api_client)
    template_id = 'template_id_example' # str | Scaffold template ID

    try:
        # Get Scaffold
        api_response = api_instance.get_scaffold_templates(template_id)
        print("The response of PublicTemplatesAPIApi->get_scaffold_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicTemplatesAPIApi->get_scaffold_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| Scaffold template ID | 

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

# **list_namespace_templates**
> List[BaseTemplateModel] list_namespace_templates(category=category)

List Public Namespace Templates

List public namespace templates (no authentication required).

Returns only templates marked as public (is_public=True).

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
    api_instance = mixpeek.PublicTemplatesAPIApi(api_client)
    category = 'category_example' # str | Filter by category (optional)

    try:
        # List Public Namespace Templates
        api_response = api_instance.list_namespace_templates(category=category)
        print("The response of PublicTemplatesAPIApi->list_namespace_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicTemplatesAPIApi->list_namespace_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**| Filter by category | [optional] 

### Return type

[**List[BaseTemplateModel]**](BaseTemplateModel.md)

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

# **list_retriever_templates**
> List[BaseTemplateModel] list_retriever_templates(category=category)

List Public Retriever Templates

List public retriever templates (no authentication required).

Returns only templates marked as public (is_public=True).

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
    api_instance = mixpeek.PublicTemplatesAPIApi(api_client)
    category = 'category_example' # str | Filter by category (optional)

    try:
        # List Public Retriever Templates
        api_response = api_instance.list_retriever_templates(category=category)
        print("The response of PublicTemplatesAPIApi->list_retriever_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicTemplatesAPIApi->list_retriever_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**| Filter by category | [optional] 

### Return type

[**List[BaseTemplateModel]**](BaseTemplateModel.md)

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

# **list_scaffolds_templates**
> List[BaseTemplateModel] list_scaffolds_templates(category=category, is_active=is_active)

List Scaffolds

List available scaffold templates (public, no auth required).

Scaffolds are pre-configured templates that create complete infrastructure:
- Namespace with feature extractors
- Bucket with data schema
- Collection with processing config
- Retriever with search pipeline

**Categories:**
- `media` - Video, image, podcast search
- `documents` - Document Q&A, RAG
- `ecommerce` - Product catalog search

**To instantiate (requires auth):**
```
POST /v1/templates/scaffolds/{template_id}/instantiate
{"namespace_name": "my_app"}
```

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
    api_instance = mixpeek.PublicTemplatesAPIApi(api_client)
    category = 'category_example' # str | Filter by category (media, documents, ecommerce) (optional)
    is_active = True # bool | Only show active templates (optional) (default to True)

    try:
        # List Scaffolds
        api_response = api_instance.list_scaffolds_templates(category=category, is_active=is_active)
        print("The response of PublicTemplatesAPIApi->list_scaffolds_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicTemplatesAPIApi->list_scaffolds_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**| Filter by category (media, documents, ecommerce) | [optional] 
 **is_active** | **bool**| Only show active templates | [optional] [default to True]

### Return type

[**List[BaseTemplateModel]**](BaseTemplateModel.md)

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

