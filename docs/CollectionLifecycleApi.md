# mixpeek.CollectionLifecycleApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_lifecycle**](CollectionLifecycleApi.md#get_lifecycle) | **GET** /v1/collections/{collection_identifier}/lifecycle | Get Lifecycle Status
[**transition_lifecycle**](CollectionLifecycleApi.md#transition_lifecycle) | **PATCH** /v1/collections/{collection_identifier}/lifecycle | Transition Lifecycle


# **get_lifecycle**
> LifecycleStatusResponse get_lifecycle(collection_identifier, authorization=authorization, authorization2=authorization2, x_namespace=x_namespace)

Get Lifecycle Status

Get the storage lifecycle status of a collection including vector counts.

### Example


```python
import mixpeek
from mixpeek.models.lifecycle_status_response import LifecycleStatusResponse
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
    api_instance = mixpeek.CollectionLifecycleApi(api_client)
    collection_identifier = 'collection_identifier_example' # str | Collection ID or name
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    authorization2 = 'authorization_example' # str |  (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Lifecycle Status
        api_response = api_instance.get_lifecycle(collection_identifier, authorization=authorization, authorization2=authorization2, x_namespace=x_namespace)
        print("The response of CollectionLifecycleApi->get_lifecycle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionLifecycleApi->get_lifecycle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_identifier** | **str**| Collection ID or name | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **authorization2** | **str**|  | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**LifecycleStatusResponse**](LifecycleStatusResponse.md)

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
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transition_lifecycle**
> LifecycleStatusResponse transition_lifecycle(collection_identifier, transition_lifecycle_request, authorization=authorization, authorization2=authorization2, x_namespace=x_namespace)

Transition Lifecycle

Transition a collection's storage tier. 'cold' evicts from Qdrant (vectors searchable via S3 Vectors). 'active' rehydrates back to Qdrant. 'archived' permanently removes vectors.

### Example


```python
import mixpeek
from mixpeek.models.lifecycle_status_response import LifecycleStatusResponse
from mixpeek.models.transition_lifecycle_request import TransitionLifecycleRequest
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
    api_instance = mixpeek.CollectionLifecycleApi(api_client)
    collection_identifier = 'collection_identifier_example' # str | Collection ID or name
    transition_lifecycle_request = mixpeek.TransitionLifecycleRequest() # TransitionLifecycleRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    authorization2 = 'authorization_example' # str |  (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Transition Lifecycle
        api_response = api_instance.transition_lifecycle(collection_identifier, transition_lifecycle_request, authorization=authorization, authorization2=authorization2, x_namespace=x_namespace)
        print("The response of CollectionLifecycleApi->transition_lifecycle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionLifecycleApi->transition_lifecycle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_identifier** | **str**| Collection ID or name | 
 **transition_lifecycle_request** | [**TransitionLifecycleRequest**](TransitionLifecycleRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **authorization2** | **str**|  | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**LifecycleStatusResponse**](LifecycleStatusResponse.md)

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
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

