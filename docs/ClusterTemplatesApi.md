# mixpeek.ClusterTemplatesApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cluster_template_from**](ClusterTemplatesApi.md#create_cluster_template_from) | **POST** /v1/templates/clusters/from-cluster/{cluster_id} | Create Cluster Template
[**get_cluster_template**](ClusterTemplatesApi.md#get_cluster_template) | **GET** /v1/templates/clusters/{template_id} | Get Cluster Template
[**instantiate_cluster_template**](ClusterTemplatesApi.md#instantiate_cluster_template) | **POST** /v1/templates/clusters/{template_id}/instantiate | Instantiate Cluster Template
[**list_cluster_templates**](ClusterTemplatesApi.md#list_cluster_templates) | **POST** /v1/templates/clusters | List Cluster Templates


# **create_cluster_template_from**
> CreateTemplateFromResourceResponse create_cluster_template_from(cluster_id, create_template_from_resource_request, authorization=authorization, x_namespace=x_namespace)

Create Cluster Template

Create template from existing cluster.

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
    api_instance = mixpeek.ClusterTemplatesApi(api_client)
    cluster_id = 'cluster_id_example' # str | Cluster ID
    create_template_from_resource_request = mixpeek.CreateTemplateFromResourceRequest() # CreateTemplateFromResourceRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Create Cluster Template
        api_response = api_instance.create_cluster_template_from(cluster_id, create_template_from_resource_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of ClusterTemplatesApi->create_cluster_template_from:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterTemplatesApi->create_cluster_template_from: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Cluster ID | 
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

# **get_cluster_template**
> BaseTemplateModel get_cluster_template(template_id, authorization=authorization, x_namespace=x_namespace)

Get Cluster Template

Get cluster template details.

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
    api_instance = mixpeek.ClusterTemplatesApi(api_client)
    template_id = 'template_id_example' # str | Template ID
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Cluster Template
        api_response = api_instance.get_cluster_template(template_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of ClusterTemplatesApi->get_cluster_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterTemplatesApi->get_cluster_template: %s\n" % e)
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

# **instantiate_cluster_template**
> InstantiatedClusterTemplateResponse instantiate_cluster_template(template_id, instantiate_cluster_template_request, authorization=authorization, x_namespace=x_namespace)

Instantiate Cluster Template

Instantiate cluster template.

### Example


```python
import mixpeek
from mixpeek.models.instantiate_cluster_template_request import InstantiateClusterTemplateRequest
from mixpeek.models.instantiated_cluster_template_response import InstantiatedClusterTemplateResponse
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
    api_instance = mixpeek.ClusterTemplatesApi(api_client)
    template_id = 'template_id_example' # str | Template ID
    instantiate_cluster_template_request = mixpeek.InstantiateClusterTemplateRequest() # InstantiateClusterTemplateRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Instantiate Cluster Template
        api_response = api_instance.instantiate_cluster_template(template_id, instantiate_cluster_template_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of ClusterTemplatesApi->instantiate_cluster_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterTemplatesApi->instantiate_cluster_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| Template ID | 
 **instantiate_cluster_template_request** | [**InstantiateClusterTemplateRequest**](InstantiateClusterTemplateRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**InstantiatedClusterTemplateResponse**](InstantiatedClusterTemplateResponse.md)

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

# **list_cluster_templates**
> ListTemplatesResponse list_cluster_templates(authorization=authorization, x_namespace=x_namespace, list_templates_request=list_templates_request)

List Cluster Templates

List cluster templates (system + organization + user).

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
    api_instance = mixpeek.ClusterTemplatesApi(api_client)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)
    list_templates_request = mixpeek.ListTemplatesRequest() # ListTemplatesRequest |  (optional)

    try:
        # List Cluster Templates
        api_response = api_instance.list_cluster_templates(authorization=authorization, x_namespace=x_namespace, list_templates_request=list_templates_request)
        print("The response of ClusterTemplatesApi->list_cluster_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterTemplatesApi->list_cluster_templates: %s\n" % e)
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

