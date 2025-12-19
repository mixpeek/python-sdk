# mixpeek.TaxonomiesApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_taxonomy_taxonomies**](TaxonomiesApi.md#create_taxonomy_taxonomies) | **POST** /v1/taxonomies | Create Taxonomy
[**create_taxonomy_version_taxonomies**](TaxonomiesApi.md#create_taxonomy_version_taxonomies) | **POST** /v1/taxonomies/{taxonomy_id}/versions | Create Taxonomy Version
[**delete_taxonomy_taxonomies**](TaxonomiesApi.md#delete_taxonomy_taxonomies) | **DELETE** /v1/taxonomies/{taxonomy_identifier} | Delete Taxonomy
[**execute_taxonomy_taxonomies**](TaxonomiesApi.md#execute_taxonomy_taxonomies) | **POST** /v1/taxonomies/execute/{taxonomy_identifier} | Execute Taxonomy
[**get_taxonomy_taxonomies**](TaxonomiesApi.md#get_taxonomy_taxonomies) | **GET** /v1/taxonomies/{taxonomy_identifier} | Get Taxonomy
[**list_taxonomies**](TaxonomiesApi.md#list_taxonomies) | **POST** /v1/taxonomies/list | List Taxonomies
[**list_taxonomy_versions_taxonomies**](TaxonomiesApi.md#list_taxonomy_versions_taxonomies) | **GET** /v1/taxonomies/{taxonomy_id}/versions | List Taxonomy Versions


# **create_taxonomy_taxonomies**
> TaxonomyResponse create_taxonomy_taxonomies(create_taxonomy_request, authorization=authorization, x_namespace=x_namespace)

Create Taxonomy

Create a taxonomy and return the created resource.

### Example


```python
import mixpeek
from mixpeek.models.create_taxonomy_request import CreateTaxonomyRequest
from mixpeek.models.taxonomy_response import TaxonomyResponse
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
    api_instance = mixpeek.TaxonomiesApi(api_client)
    create_taxonomy_request = mixpeek.CreateTaxonomyRequest() # CreateTaxonomyRequest | 
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)
    x_namespace = 'x_namespace_example' # str | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. (optional)

    try:
        # Create Taxonomy
        api_response = api_instance.create_taxonomy_taxonomies(create_taxonomy_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of TaxonomiesApi->create_taxonomy_taxonomies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomiesApi->create_taxonomy_taxonomies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_taxonomy_request** | [**CreateTaxonomyRequest**](CreateTaxonomyRequest.md)|  | 
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 
 **x_namespace** | **str**| Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: &#39;netflix_prod&#39; or &#39;ns_1234567890&#39;. To create a namespace, use the /namespaces endpoint. | [optional] 

### Return type

[**TaxonomyResponse**](TaxonomyResponse.md)

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

# **create_taxonomy_version_taxonomies**
> TaxonomyResponse create_taxonomy_version_taxonomies(taxonomy_id, request_body, authorization=authorization, x_namespace=x_namespace)

Create Taxonomy Version

Create a new version for a taxonomy with a new config snapshot.

### Example


```python
import mixpeek
from mixpeek.models.taxonomy_response import TaxonomyResponse
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
    api_instance = mixpeek.TaxonomiesApi(api_client)
    taxonomy_id = 'taxonomy_id_example' # str | Taxonomy ID (tax_...)
    request_body = None # Dict[str, object] | 
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)
    x_namespace = 'x_namespace_example' # str | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. (optional)

    try:
        # Create Taxonomy Version
        api_response = api_instance.create_taxonomy_version_taxonomies(taxonomy_id, request_body, authorization=authorization, x_namespace=x_namespace)
        print("The response of TaxonomiesApi->create_taxonomy_version_taxonomies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomiesApi->create_taxonomy_version_taxonomies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxonomy_id** | **str**| Taxonomy ID (tax_...) | 
 **request_body** | [**Dict[str, object]**](object.md)|  | 
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 
 **x_namespace** | **str**| Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: &#39;netflix_prod&#39; or &#39;ns_1234567890&#39;. To create a namespace, use the /namespaces endpoint. | [optional] 

### Return type

[**TaxonomyResponse**](TaxonomyResponse.md)

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

# **delete_taxonomy_taxonomies**
> GenericDeleteResponse delete_taxonomy_taxonomies(taxonomy_identifier, authorization=authorization, x_namespace=x_namespace)

Delete Taxonomy

Delete a taxonomy by ID or name.

### Example


```python
import mixpeek
from mixpeek.models.generic_delete_response import GenericDeleteResponse
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
    api_instance = mixpeek.TaxonomiesApi(api_client)
    taxonomy_identifier = 'taxonomy_identifier_example' # str | Taxonomy ID or name
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)
    x_namespace = 'x_namespace_example' # str | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. (optional)

    try:
        # Delete Taxonomy
        api_response = api_instance.delete_taxonomy_taxonomies(taxonomy_identifier, authorization=authorization, x_namespace=x_namespace)
        print("The response of TaxonomiesApi->delete_taxonomy_taxonomies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomiesApi->delete_taxonomy_taxonomies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxonomy_identifier** | **str**| Taxonomy ID or name | 
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 
 **x_namespace** | **str**| Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: &#39;netflix_prod&#39; or &#39;ns_1234567890&#39;. To create a namespace, use the /namespaces endpoint. | [optional] 

### Return type

[**GenericDeleteResponse**](GenericDeleteResponse.md)

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

# **execute_taxonomy_taxonomies**
> JoinResponse execute_taxonomy_taxonomies(taxonomy_identifier, payload, version=version, authorization=authorization, x_namespace=x_namespace)

Execute Taxonomy

Execute on-demand taxonomy validation/testing.

This endpoint is for testing taxonomy configuration only.
It validates the taxonomy by calling the engine with empty documents.

NOTE: Batch taxonomy materialization is NOT triggered via API.
It's automatically triggered by the engine after feature extraction,
based on collection configuration (taxonomy_applications).

Real on-demand taxonomy enrichment happens within retriever pipelines.

### Example


```python
import mixpeek
from mixpeek.models.join_response import JoinResponse
from mixpeek.models.payload import Payload
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
    api_instance = mixpeek.TaxonomiesApi(api_client)
    taxonomy_identifier = 'taxonomy_identifier_example' # str | Taxonomy ID or name
    payload = mixpeek.Payload() # Payload | 
    version = 56 # int | Optional taxonomy version to execute (optional)
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)
    x_namespace = 'x_namespace_example' # str | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. (optional)

    try:
        # Execute Taxonomy
        api_response = api_instance.execute_taxonomy_taxonomies(taxonomy_identifier, payload, version=version, authorization=authorization, x_namespace=x_namespace)
        print("The response of TaxonomiesApi->execute_taxonomy_taxonomies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomiesApi->execute_taxonomy_taxonomies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxonomy_identifier** | **str**| Taxonomy ID or name | 
 **payload** | [**Payload**](Payload.md)|  | 
 **version** | **int**| Optional taxonomy version to execute | [optional] 
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 
 **x_namespace** | **str**| Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: &#39;netflix_prod&#39; or &#39;ns_1234567890&#39;. To create a namespace, use the /namespaces endpoint. | [optional] 

### Return type

[**JoinResponse**](JoinResponse.md)

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

# **get_taxonomy_taxonomies**
> TaxonomyResponse get_taxonomy_taxonomies(taxonomy_identifier, version=version, authorization=authorization, x_namespace=x_namespace)

Get Taxonomy

Get a taxonomy by ID or name.

### Example


```python
import mixpeek
from mixpeek.models.taxonomy_response import TaxonomyResponse
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
    api_instance = mixpeek.TaxonomiesApi(api_client)
    taxonomy_identifier = 'taxonomy_identifier_example' # str | Taxonomy ID or name
    version = 56 # int | Optional taxonomy version to fetch (optional)
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)
    x_namespace = 'x_namespace_example' # str | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. (optional)

    try:
        # Get Taxonomy
        api_response = api_instance.get_taxonomy_taxonomies(taxonomy_identifier, version=version, authorization=authorization, x_namespace=x_namespace)
        print("The response of TaxonomiesApi->get_taxonomy_taxonomies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomiesApi->get_taxonomy_taxonomies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxonomy_identifier** | **str**| Taxonomy ID or name | 
 **version** | **int**| Optional taxonomy version to fetch | [optional] 
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 
 **x_namespace** | **str**| Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: &#39;netflix_prod&#39; or &#39;ns_1234567890&#39;. To create a namespace, use the /namespaces endpoint. | [optional] 

### Return type

[**TaxonomyResponse**](TaxonomyResponse.md)

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

# **list_taxonomies**
> ListTaxonomiesResponse list_taxonomies(limit=limit, offset=offset, authorization=authorization, x_namespace=x_namespace, list_taxonomies_request=list_taxonomies_request)

List Taxonomies

List taxonomies with optional filters and pagination.

### Example


```python
import mixpeek
from mixpeek.models.list_taxonomies_request import ListTaxonomiesRequest
from mixpeek.models.list_taxonomies_response import ListTaxonomiesResponse
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
    api_instance = mixpeek.TaxonomiesApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)
    x_namespace = 'x_namespace_example' # str | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. (optional)
    list_taxonomies_request = mixpeek.ListTaxonomiesRequest() # ListTaxonomiesRequest |  (optional)

    try:
        # List Taxonomies
        api_response = api_instance.list_taxonomies(limit=limit, offset=offset, authorization=authorization, x_namespace=x_namespace, list_taxonomies_request=list_taxonomies_request)
        print("The response of TaxonomiesApi->list_taxonomies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomiesApi->list_taxonomies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 
 **x_namespace** | **str**| Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: &#39;netflix_prod&#39; or &#39;ns_1234567890&#39;. To create a namespace, use the /namespaces endpoint. | [optional] 
 **list_taxonomies_request** | [**ListTaxonomiesRequest**](ListTaxonomiesRequest.md)|  | [optional] 

### Return type

[**ListTaxonomiesResponse**](ListTaxonomiesResponse.md)

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

# **list_taxonomy_versions_taxonomies**
> ListTaxonomiesResponse list_taxonomy_versions_taxonomies(taxonomy_id, authorization=authorization, x_namespace=x_namespace)

List Taxonomy Versions

List all versions for a taxonomy (head included as latest).

### Example


```python
import mixpeek
from mixpeek.models.list_taxonomies_response import ListTaxonomiesResponse
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
    api_instance = mixpeek.TaxonomiesApi(api_client)
    taxonomy_id = 'taxonomy_id_example' # str | Taxonomy ID (tax_...)
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)
    x_namespace = 'x_namespace_example' # str | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. (optional)

    try:
        # List Taxonomy Versions
        api_response = api_instance.list_taxonomy_versions_taxonomies(taxonomy_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of TaxonomiesApi->list_taxonomy_versions_taxonomies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomiesApi->list_taxonomy_versions_taxonomies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxonomy_id** | **str**| Taxonomy ID (tax_...) | 
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 
 **x_namespace** | **str**| Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: &#39;netflix_prod&#39; or &#39;ns_1234567890&#39;. To create a namespace, use the /namespaces endpoint. | [optional] 

### Return type

[**ListTaxonomiesResponse**](ListTaxonomiesResponse.md)

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

