# mixpeek.PublicScaffoldsApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_scaffold_templates**](PublicScaffoldsApi.md#get_scaffold_templates) | **GET** /v1/public/templates/scaffolds/{template_id} | Get Scaffold
[**list_scaffolds_templates**](PublicScaffoldsApi.md#list_scaffolds_templates) | **GET** /v1/public/templates/scaffolds | List Scaffolds


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
    api_instance = mixpeek.PublicScaffoldsApi(api_client)
    template_id = 'template_id_example' # str | Scaffold template ID

    try:
        # Get Scaffold
        api_response = api_instance.get_scaffold_templates(template_id)
        print("The response of PublicScaffoldsApi->get_scaffold_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicScaffoldsApi->get_scaffold_templates: %s\n" % e)
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
    api_instance = mixpeek.PublicScaffoldsApi(api_client)
    category = 'category_example' # str | Filter by category (media, documents, ecommerce) (optional)
    is_active = True # bool | Only show active templates (optional) (default to True)

    try:
        # List Scaffolds
        api_response = api_instance.list_scaffolds_templates(category=category, is_active=is_active)
        print("The response of PublicScaffoldsApi->list_scaffolds_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicScaffoldsApi->list_scaffolds_templates: %s\n" % e)
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

