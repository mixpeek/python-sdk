# mixpeek.RetrieverInteractionsApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_interaction_retrievers**](RetrieverInteractionsApi.md#create_interaction_retrievers) | **POST** /v1/retrievers/interactions | Create Interaction
[**delete_interaction_retrievers**](RetrieverInteractionsApi.md#delete_interaction_retrievers) | **DELETE** /v1/retrievers/interactions/{interaction_id} | Delete Interaction
[**get_interaction_retrievers**](RetrieverInteractionsApi.md#get_interaction_retrievers) | **GET** /v1/retrievers/interactions/{interaction_id} | Get Interaction
[**list_interactions_retrievers**](RetrieverInteractionsApi.md#list_interactions_retrievers) | **POST** /v1/retrievers/interactions/list | List Interactions


# **create_interaction_retrievers**
> InteractionResponse create_interaction_retrievers(search_interaction, authorization=authorization, x_namespace=x_namespace)

Create Interaction

Record a search interaction (view, click, feedback, etc.).

### Example


```python
import mixpeek
from mixpeek.models.interaction_response import InteractionResponse
from mixpeek.models.search_interaction import SearchInteraction
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
    api_instance = mixpeek.RetrieverInteractionsApi(api_client)
    search_interaction = mixpeek.SearchInteraction() # SearchInteraction | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Create Interaction
        api_response = api_instance.create_interaction_retrievers(search_interaction, authorization=authorization, x_namespace=x_namespace)
        print("The response of RetrieverInteractionsApi->create_interaction_retrievers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrieverInteractionsApi->create_interaction_retrievers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_interaction** | [**SearchInteraction**](SearchInteraction.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**InteractionResponse**](InteractionResponse.md)

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

# **delete_interaction_retrievers**
> object delete_interaction_retrievers(interaction_id, authorization=authorization, x_namespace=x_namespace)

Delete Interaction

Delete a specific interaction (idempotent - succeeds even if already deleted).

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
    api_instance = mixpeek.RetrieverInteractionsApi(api_client)
    interaction_id = 'interaction_id_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Delete Interaction
        api_response = api_instance.delete_interaction_retrievers(interaction_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of RetrieverInteractionsApi->delete_interaction_retrievers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrieverInteractionsApi->delete_interaction_retrievers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interaction_id** | **str**|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

**object**

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

# **get_interaction_retrievers**
> InteractionResponse get_interaction_retrievers(interaction_id, authorization=authorization, x_namespace=x_namespace)

Get Interaction

Get a specific interaction.

### Example


```python
import mixpeek
from mixpeek.models.interaction_response import InteractionResponse
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
    api_instance = mixpeek.RetrieverInteractionsApi(api_client)
    interaction_id = 'interaction_id_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Interaction
        api_response = api_instance.get_interaction_retrievers(interaction_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of RetrieverInteractionsApi->get_interaction_retrievers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrieverInteractionsApi->get_interaction_retrievers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interaction_id** | **str**|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**InteractionResponse**](InteractionResponse.md)

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

# **list_interactions_retrievers**
> ListInteractionsResponse list_interactions_retrievers(limit=limit, offset=offset, cursor=cursor, include_total=include_total, authorization=authorization, x_namespace=x_namespace, list_interactions_request=list_interactions_request)

List Interactions

List interactions with optional filters and pagination.

Supports hybrid filtering: simple fields + advanced LogicalOperator.

### Example


```python
import mixpeek
from mixpeek.models.list_interactions_request import ListInteractionsRequest
from mixpeek.models.list_interactions_response import ListInteractionsResponse
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
    api_instance = mixpeek.RetrieverInteractionsApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    cursor = 'cursor_example' # str |  (optional)
    include_total = False # bool |  (optional) (default to False)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)
    list_interactions_request = mixpeek.ListInteractionsRequest() # ListInteractionsRequest |  (optional)

    try:
        # List Interactions
        api_response = api_instance.list_interactions_retrievers(limit=limit, offset=offset, cursor=cursor, include_total=include_total, authorization=authorization, x_namespace=x_namespace, list_interactions_request=list_interactions_request)
        print("The response of RetrieverInteractionsApi->list_interactions_retrievers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrieverInteractionsApi->list_interactions_retrievers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **cursor** | **str**|  | [optional] 
 **include_total** | **bool**|  | [optional] [default to False]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 
 **list_interactions_request** | [**ListInteractionsRequest**](ListInteractionsRequest.md)|  | [optional] 

### Return type

[**ListInteractionsResponse**](ListInteractionsResponse.md)

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

