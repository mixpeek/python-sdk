# mixpeek.NamespacesApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_namespace**](NamespacesApi.md#create_namespace) | **POST** /v1/namespaces | Create Namespace
[**delete_namespace**](NamespacesApi.md#delete_namespace) | **DELETE** /v1/namespaces/{namespace_identifier} | Delete Namespace
[**get_namespace**](NamespacesApi.md#get_namespace) | **GET** /v1/namespaces/{namespace_identifier} | Get Namespace
[**list_namespaces**](NamespacesApi.md#list_namespaces) | **POST** /v1/namespaces/list | List Namespaces
[**update_namespace**](NamespacesApi.md#update_namespace) | **PUT** /v1/namespaces/{namespace_identifier} | Update Namespace


# **create_namespace**
> NamespaceModel create_namespace(create_namespace_request, authorization=authorization)

Create Namespace

Creates a new namespace with specified feature extractors and payload indexes.

### Example


```python
import mixpeek
from mixpeek.models.create_namespace_request import CreateNamespaceRequest
from mixpeek.models.namespace_model import NamespaceModel
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
    api_instance = mixpeek.NamespacesApi(api_client)
    create_namespace_request = mixpeek.CreateNamespaceRequest() # CreateNamespaceRequest | 
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)

    try:
        # Create Namespace
        api_response = api_instance.create_namespace(create_namespace_request, authorization=authorization)
        print("The response of NamespacesApi->create_namespace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NamespacesApi->create_namespace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_namespace_request** | [**CreateNamespaceRequest**](CreateNamespaceRequest.md)|  | 
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 

### Return type

[**NamespaceModel**](NamespaceModel.md)

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

# **delete_namespace**
> delete_namespace(namespace_identifier, authorization=authorization)

Delete Namespace

Deletes an existing namespace using either its name or ID

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
    api_instance = mixpeek.NamespacesApi(api_client)
    namespace_identifier = 'namespace_identifier_example' # str | Either the namespace name or namespace ID
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)

    try:
        # Delete Namespace
        api_instance.delete_namespace(namespace_identifier, authorization=authorization)
    except Exception as e:
        print("Exception when calling NamespacesApi->delete_namespace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_identifier** | **str**| Either the namespace name or namespace ID | 
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 

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

# **get_namespace**
> NamespaceModel get_namespace(namespace_identifier, authorization=authorization)

Get Namespace

Retrieve details of a specific namespace using either its name or ID

### Example


```python
import mixpeek
from mixpeek.models.namespace_model import NamespaceModel
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
    api_instance = mixpeek.NamespacesApi(api_client)
    namespace_identifier = 'namespace_identifier_example' # str | Either the namespace name or namespace ID
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)

    try:
        # Get Namespace
        api_response = api_instance.get_namespace(namespace_identifier, authorization=authorization)
        print("The response of NamespacesApi->get_namespace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NamespacesApi->get_namespace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_identifier** | **str**| Either the namespace name or namespace ID | 
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 

### Return type

[**NamespaceModel**](NamespaceModel.md)

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

# **list_namespaces**
> ListNamespacesResponse list_namespaces(limit=limit, offset=offset, authorization=authorization, list_namespaces_request=list_namespaces_request)

List Namespaces

List all namespaces for a user

### Example


```python
import mixpeek
from mixpeek.models.list_namespaces_request import ListNamespacesRequest
from mixpeek.models.list_namespaces_response import ListNamespacesResponse
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
    api_instance = mixpeek.NamespacesApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)
    list_namespaces_request = mixpeek.ListNamespacesRequest() # ListNamespacesRequest |  (optional)

    try:
        # List Namespaces
        api_response = api_instance.list_namespaces(limit=limit, offset=offset, authorization=authorization, list_namespaces_request=list_namespaces_request)
        print("The response of NamespacesApi->list_namespaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NamespacesApi->list_namespaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 
 **list_namespaces_request** | [**ListNamespacesRequest**](ListNamespacesRequest.md)|  | [optional] 

### Return type

[**ListNamespacesResponse**](ListNamespacesResponse.md)

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

# **update_namespace**
> NamespaceModel update_namespace(namespace_identifier, update_namespace_request, authorization=authorization)

Update Namespace

Fully updates an existing namespace (all fields required)

### Example


```python
import mixpeek
from mixpeek.models.namespace_model import NamespaceModel
from mixpeek.models.update_namespace_request import UpdateNamespaceRequest
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
    api_instance = mixpeek.NamespacesApi(api_client)
    namespace_identifier = 'namespace_identifier_example' # str | Either the namespace name or namespace ID
    update_namespace_request = mixpeek.UpdateNamespaceRequest() # UpdateNamespaceRequest | 
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)

    try:
        # Update Namespace
        api_response = api_instance.update_namespace(namespace_identifier, update_namespace_request, authorization=authorization)
        print("The response of NamespacesApi->update_namespace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NamespacesApi->update_namespace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_identifier** | **str**| Either the namespace name or namespace ID | 
 **update_namespace_request** | [**UpdateNamespaceRequest**](UpdateNamespaceRequest.md)|  | 
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 

### Return type

[**NamespaceModel**](NamespaceModel.md)

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

