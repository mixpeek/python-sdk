# mixpeek.TemplatesApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bucket_template_from**](TemplatesApi.md#create_bucket_template_from) | **POST** /v1/templates/buckets/from-bucket/{bucket_id} | Create Bucket Template
[**create_cluster_template_from**](TemplatesApi.md#create_cluster_template_from) | **POST** /v1/templates/clusters/from-cluster/{cluster_id} | Create Cluster Template
[**create_collection_template_from**](TemplatesApi.md#create_collection_template_from) | **POST** /v1/templates/collections/from-collection/{collection_id} | Create Collection Template
[**create_namespace_template_from**](TemplatesApi.md#create_namespace_template_from) | **POST** /v1/templates/namespaces/from-namespace/{namespace_id} | Create Namespace Template
[**create_retriever_template_from**](TemplatesApi.md#create_retriever_template_from) | **POST** /v1/templates/retrievers/from-retriever/{retriever_id} | Create Retriever Template
[**create_taxonomy_template_taxonomies_from**](TemplatesApi.md#create_taxonomy_template_taxonomies_from) | **POST** /v1/templates/taxonomies/from-taxonomy/{taxonomy_id} | Create Taxonomy Template
[**get_bucket_template**](TemplatesApi.md#get_bucket_template) | **GET** /v1/templates/buckets/{template_id} | Get Bucket Template
[**get_cluster_template**](TemplatesApi.md#get_cluster_template) | **GET** /v1/templates/clusters/{template_id} | Get Cluster Template
[**get_collection_template**](TemplatesApi.md#get_collection_template) | **GET** /v1/templates/collections/{template_id} | Get Collection Template
[**get_namespace_template**](TemplatesApi.md#get_namespace_template) | **GET** /v1/templates/namespaces/{template_id} | Get Namespace Template
[**get_retriever_template**](TemplatesApi.md#get_retriever_template) | **GET** /v1/templates/retrievers/{template_id} | Get Retriever Template
[**get_taxonomy_template_taxonomies**](TemplatesApi.md#get_taxonomy_template_taxonomies) | **GET** /v1/templates/taxonomies/{template_id} | Get Taxonomy Template
[**instantiate_bucket_template**](TemplatesApi.md#instantiate_bucket_template) | **POST** /v1/templates/buckets/{template_id}/instantiate | Instantiate Bucket Template
[**instantiate_cluster_template**](TemplatesApi.md#instantiate_cluster_template) | **POST** /v1/templates/clusters/{template_id}/instantiate | Instantiate Cluster Template
[**instantiate_collection_template**](TemplatesApi.md#instantiate_collection_template) | **POST** /v1/templates/collections/{template_id}/instantiate | Instantiate Collection Template
[**instantiate_namespace_template**](TemplatesApi.md#instantiate_namespace_template) | **POST** /v1/templates/namespaces/{template_id}/instantiate | Instantiate Namespace Template
[**instantiate_retriever_template**](TemplatesApi.md#instantiate_retriever_template) | **POST** /v1/templates/retrievers/{template_id}/instantiate | Instantiate Retriever Template
[**instantiate_taxonomy_template_taxonomies**](TemplatesApi.md#instantiate_taxonomy_template_taxonomies) | **POST** /v1/templates/taxonomies/{template_id}/instantiate | Instantiate Taxonomy Template
[**list_bucket_templates**](TemplatesApi.md#list_bucket_templates) | **POST** /v1/templates/buckets | List Bucket Templates
[**list_cluster_templates**](TemplatesApi.md#list_cluster_templates) | **POST** /v1/templates/clusters | List Cluster Templates
[**list_collection_templates**](TemplatesApi.md#list_collection_templates) | **POST** /v1/templates/collections | List Collection Templates
[**list_namespace_templates**](TemplatesApi.md#list_namespace_templates) | **GET** /v1/templates/namespaces | List Namespace Templates
[**list_retriever_templates**](TemplatesApi.md#list_retriever_templates) | **POST** /v1/templates/retrievers | List Retriever Templates
[**list_taxonomy_templates_taxonomies**](TemplatesApi.md#list_taxonomy_templates_taxonomies) | **POST** /v1/templates/taxonomies | List Taxonomy Templates


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
    api_instance = mixpeek.TemplatesApi(api_client)
    bucket_id = 'bucket_id_example' # str | Bucket ID
    create_template_from_resource_request = mixpeek.CreateTemplateFromResourceRequest() # CreateTemplateFromResourceRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Create Bucket Template
        api_response = api_instance.create_bucket_template_from(bucket_id, create_template_from_resource_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of TemplatesApi->create_bucket_template_from:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->create_bucket_template_from: %s\n" % e)
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
    api_instance = mixpeek.TemplatesApi(api_client)
    cluster_id = 'cluster_id_example' # str | Cluster ID
    create_template_from_resource_request = mixpeek.CreateTemplateFromResourceRequest() # CreateTemplateFromResourceRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Create Cluster Template
        api_response = api_instance.create_cluster_template_from(cluster_id, create_template_from_resource_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of TemplatesApi->create_cluster_template_from:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->create_cluster_template_from: %s\n" % e)
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
    api_instance = mixpeek.TemplatesApi(api_client)
    collection_id = 'collection_id_example' # str | Collection ID
    create_template_from_resource_request = mixpeek.CreateTemplateFromResourceRequest() # CreateTemplateFromResourceRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Create Collection Template
        api_response = api_instance.create_collection_template_from(collection_id, create_template_from_resource_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of TemplatesApi->create_collection_template_from:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->create_collection_template_from: %s\n" % e)
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

# **create_namespace_template_from**
> CreateTemplateFromResourceResponse create_namespace_template_from(namespace_id, create_template_from_resource_request, authorization=authorization, x_namespace=x_namespace)

Create Namespace Template

Create template from existing namespace.

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
    api_instance = mixpeek.TemplatesApi(api_client)
    namespace_id = 'namespace_id_example' # str | Namespace ID
    create_template_from_resource_request = mixpeek.CreateTemplateFromResourceRequest() # CreateTemplateFromResourceRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Create Namespace Template
        api_response = api_instance.create_namespace_template_from(namespace_id, create_template_from_resource_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of TemplatesApi->create_namespace_template_from:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->create_namespace_template_from: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_id** | **str**| Namespace ID | 
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

# **create_retriever_template_from**
> CreateTemplateFromResourceResponse create_retriever_template_from(retriever_id, create_template_from_resource_request, authorization=authorization, x_namespace=x_namespace)

Create Retriever Template

Create template from existing retriever.

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
    api_instance = mixpeek.TemplatesApi(api_client)
    retriever_id = 'retriever_id_example' # str | Retriever ID
    create_template_from_resource_request = mixpeek.CreateTemplateFromResourceRequest() # CreateTemplateFromResourceRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Create Retriever Template
        api_response = api_instance.create_retriever_template_from(retriever_id, create_template_from_resource_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of TemplatesApi->create_retriever_template_from:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->create_retriever_template_from: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retriever_id** | **str**| Retriever ID | 
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
    api_instance = mixpeek.TemplatesApi(api_client)
    taxonomy_id = 'taxonomy_id_example' # str | Taxonomy ID
    create_template_from_resource_request = mixpeek.CreateTemplateFromResourceRequest() # CreateTemplateFromResourceRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Create Taxonomy Template
        api_response = api_instance.create_taxonomy_template_taxonomies_from(taxonomy_id, create_template_from_resource_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of TemplatesApi->create_taxonomy_template_taxonomies_from:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->create_taxonomy_template_taxonomies_from: %s\n" % e)
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
    api_instance = mixpeek.TemplatesApi(api_client)
    template_id = 'template_id_example' # str | Template ID
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Bucket Template
        api_response = api_instance.get_bucket_template(template_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of TemplatesApi->get_bucket_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->get_bucket_template: %s\n" % e)
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
    api_instance = mixpeek.TemplatesApi(api_client)
    template_id = 'template_id_example' # str | Template ID
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Cluster Template
        api_response = api_instance.get_cluster_template(template_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of TemplatesApi->get_cluster_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->get_cluster_template: %s\n" % e)
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
    api_instance = mixpeek.TemplatesApi(api_client)
    template_id = 'template_id_example' # str | Template ID
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Collection Template
        api_response = api_instance.get_collection_template(template_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of TemplatesApi->get_collection_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->get_collection_template: %s\n" % e)
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

# **get_namespace_template**
> BaseTemplateModel get_namespace_template(template_id, authorization=authorization, x_namespace=x_namespace)

Get Namespace Template

Get namespace template details.

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
    api_instance = mixpeek.TemplatesApi(api_client)
    template_id = 'template_id_example' # str | Template ID
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Namespace Template
        api_response = api_instance.get_namespace_template(template_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of TemplatesApi->get_namespace_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->get_namespace_template: %s\n" % e)
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

# **get_retriever_template**
> BaseTemplateModel get_retriever_template(template_id, authorization=authorization, x_namespace=x_namespace)

Get Retriever Template

Get retriever template details.

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
    api_instance = mixpeek.TemplatesApi(api_client)
    template_id = 'template_id_example' # str | Template ID
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Retriever Template
        api_response = api_instance.get_retriever_template(template_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of TemplatesApi->get_retriever_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->get_retriever_template: %s\n" % e)
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
    api_instance = mixpeek.TemplatesApi(api_client)
    template_id = 'template_id_example' # str | Template ID
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Taxonomy Template
        api_response = api_instance.get_taxonomy_template_taxonomies(template_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of TemplatesApi->get_taxonomy_template_taxonomies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->get_taxonomy_template_taxonomies: %s\n" % e)
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
    api_instance = mixpeek.TemplatesApi(api_client)
    template_id = 'template_id_example' # str | Template ID
    instantiate_bucket_template_request = mixpeek.InstantiateBucketTemplateRequest() # InstantiateBucketTemplateRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Instantiate Bucket Template
        api_response = api_instance.instantiate_bucket_template(template_id, instantiate_bucket_template_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of TemplatesApi->instantiate_bucket_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->instantiate_bucket_template: %s\n" % e)
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
    api_instance = mixpeek.TemplatesApi(api_client)
    template_id = 'template_id_example' # str | Template ID
    instantiate_cluster_template_request = mixpeek.InstantiateClusterTemplateRequest() # InstantiateClusterTemplateRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Instantiate Cluster Template
        api_response = api_instance.instantiate_cluster_template(template_id, instantiate_cluster_template_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of TemplatesApi->instantiate_cluster_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->instantiate_cluster_template: %s\n" % e)
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
    api_instance = mixpeek.TemplatesApi(api_client)
    template_id = 'template_id_example' # str | Template ID
    instantiate_collection_template_request = mixpeek.InstantiateCollectionTemplateRequest() # InstantiateCollectionTemplateRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Instantiate Collection Template
        api_response = api_instance.instantiate_collection_template(template_id, instantiate_collection_template_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of TemplatesApi->instantiate_collection_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->instantiate_collection_template: %s\n" % e)
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

# **instantiate_namespace_template**
> InstantiatedTemplateResponse instantiate_namespace_template(template_id, instantiate_template_request, authorization=authorization, x_namespace=x_namespace)

Instantiate Namespace Template

Instantiate namespace template.

### Example


```python
import mixpeek
from mixpeek.models.instantiate_template_request import InstantiateTemplateRequest
from mixpeek.models.instantiated_template_response import InstantiatedTemplateResponse
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
    api_instance = mixpeek.TemplatesApi(api_client)
    template_id = 'template_id_example' # str | Template ID
    instantiate_template_request = mixpeek.InstantiateTemplateRequest() # InstantiateTemplateRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Instantiate Namespace Template
        api_response = api_instance.instantiate_namespace_template(template_id, instantiate_template_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of TemplatesApi->instantiate_namespace_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->instantiate_namespace_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| Template ID | 
 **instantiate_template_request** | [**InstantiateTemplateRequest**](InstantiateTemplateRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**InstantiatedTemplateResponse**](InstantiatedTemplateResponse.md)

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

# **instantiate_retriever_template**
> InstantiatedRetrieverTemplateResponse instantiate_retriever_template(template_id, instantiate_retriever_template_request, authorization=authorization, x_namespace=x_namespace)

Instantiate Retriever Template

Instantiate retriever template.

### Example


```python
import mixpeek
from mixpeek.models.instantiate_retriever_template_request import InstantiateRetrieverTemplateRequest
from mixpeek.models.instantiated_retriever_template_response import InstantiatedRetrieverTemplateResponse
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
    api_instance = mixpeek.TemplatesApi(api_client)
    template_id = 'template_id_example' # str | Template ID
    instantiate_retriever_template_request = mixpeek.InstantiateRetrieverTemplateRequest() # InstantiateRetrieverTemplateRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Instantiate Retriever Template
        api_response = api_instance.instantiate_retriever_template(template_id, instantiate_retriever_template_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of TemplatesApi->instantiate_retriever_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->instantiate_retriever_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| Template ID | 
 **instantiate_retriever_template_request** | [**InstantiateRetrieverTemplateRequest**](InstantiateRetrieverTemplateRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**InstantiatedRetrieverTemplateResponse**](InstantiatedRetrieverTemplateResponse.md)

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
    api_instance = mixpeek.TemplatesApi(api_client)
    template_id = 'template_id_example' # str | Template ID
    instantiate_taxonomy_template_request = mixpeek.InstantiateTaxonomyTemplateRequest() # InstantiateTaxonomyTemplateRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Instantiate Taxonomy Template
        api_response = api_instance.instantiate_taxonomy_template_taxonomies(template_id, instantiate_taxonomy_template_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of TemplatesApi->instantiate_taxonomy_template_taxonomies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->instantiate_taxonomy_template_taxonomies: %s\n" % e)
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
    api_instance = mixpeek.TemplatesApi(api_client)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)
    list_templates_request = mixpeek.ListTemplatesRequest() # ListTemplatesRequest |  (optional)

    try:
        # List Bucket Templates
        api_response = api_instance.list_bucket_templates(authorization=authorization, x_namespace=x_namespace, list_templates_request=list_templates_request)
        print("The response of TemplatesApi->list_bucket_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->list_bucket_templates: %s\n" % e)
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
    api_instance = mixpeek.TemplatesApi(api_client)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)
    list_templates_request = mixpeek.ListTemplatesRequest() # ListTemplatesRequest |  (optional)

    try:
        # List Cluster Templates
        api_response = api_instance.list_cluster_templates(authorization=authorization, x_namespace=x_namespace, list_templates_request=list_templates_request)
        print("The response of TemplatesApi->list_cluster_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->list_cluster_templates: %s\n" % e)
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
    api_instance = mixpeek.TemplatesApi(api_client)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)
    list_templates_request = mixpeek.ListTemplatesRequest() # ListTemplatesRequest |  (optional)

    try:
        # List Collection Templates
        api_response = api_instance.list_collection_templates(authorization=authorization, x_namespace=x_namespace, list_templates_request=list_templates_request)
        print("The response of TemplatesApi->list_collection_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->list_collection_templates: %s\n" % e)
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

# **list_namespace_templates**
> List[BaseTemplateModel] list_namespace_templates(category=category, scope=scope, is_active=is_active, authorization=authorization, x_namespace=x_namespace)

List Namespace Templates

List namespace templates (system + organization + user).

### Example


```python
import mixpeek
from mixpeek.models.base_template_model import BaseTemplateModel
from mixpeek.models.template_scope import TemplateScope
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
    api_instance = mixpeek.TemplatesApi(api_client)
    category = 'category_example' # str | Filter by category (optional)
    scope = mixpeek.TemplateScope() # TemplateScope | Filter by scope (system, organization, or user) (optional)
    is_active = True # bool | Show only active templates (optional) (default to True)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # List Namespace Templates
        api_response = api_instance.list_namespace_templates(category=category, scope=scope, is_active=is_active, authorization=authorization, x_namespace=x_namespace)
        print("The response of TemplatesApi->list_namespace_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->list_namespace_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**| Filter by category | [optional] 
 **scope** | [**TemplateScope**](.md)| Filter by scope (system, organization, or user) | [optional] 
 **is_active** | **bool**| Show only active templates | [optional] [default to True]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

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
> ListTemplatesResponse list_retriever_templates(authorization=authorization, x_namespace=x_namespace, list_templates_request=list_templates_request)

List Retriever Templates

List retriever templates (system + organization + user).

Supports filtering, sorting, and search like other list operations.

**Request Body (optional):**
- `filters`: Attribute-based filters `{"AND": [{"field": "category", "operator": "eq", "value": "semantic_search"}]}`
- `sort`: Sort options `{"field": "name", "direction": "asc"}`
- `search`: Wildcard search across template_id, name, description, tags
- `scope`: Filter by scope (system, organization, user)
- `category`: Filter by category
- `is_active`: Show only active templates (default: true)
- `tags`: Filter by tags (templates must have ALL specified tags)

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
    api_instance = mixpeek.TemplatesApi(api_client)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)
    list_templates_request = mixpeek.ListTemplatesRequest() # ListTemplatesRequest |  (optional)

    try:
        # List Retriever Templates
        api_response = api_instance.list_retriever_templates(authorization=authorization, x_namespace=x_namespace, list_templates_request=list_templates_request)
        print("The response of TemplatesApi->list_retriever_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->list_retriever_templates: %s\n" % e)
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
    api_instance = mixpeek.TemplatesApi(api_client)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)
    list_templates_request = mixpeek.ListTemplatesRequest() # ListTemplatesRequest |  (optional)

    try:
        # List Taxonomy Templates
        api_response = api_instance.list_taxonomy_templates_taxonomies(authorization=authorization, x_namespace=x_namespace, list_templates_request=list_templates_request)
        print("The response of TemplatesApi->list_taxonomy_templates_taxonomies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->list_taxonomy_templates_taxonomies: %s\n" % e)
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

