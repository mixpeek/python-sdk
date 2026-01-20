# mixpeek.PublishedRetrieversApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_name_availability_retrievers_id_publish**](PublishedRetrieversApi.md#check_name_availability_retrievers_id_publish) | **GET** /v1/retrievers/{retriever_id}/publish/availability | Check Name Availability
[**get_organization_publish_stats_retrievers**](PublishedRetrieversApi.md#get_organization_publish_stats_retrievers) | **GET** /v1/retrievers/publish/stats | Get Organization Publish Stats
[**get_published_retriever_id_publish**](PublishedRetrieversApi.md#get_published_retriever_id_publish) | **GET** /v1/retrievers/{retriever_id}/publish | Get Published Retriever
[**list_published_retrievers**](PublishedRetrieversApi.md#list_published_retrievers) | **GET** /v1/retrievers/published | List Published Retrievers
[**publish_retriever**](PublishedRetrieversApi.md#publish_retriever) | **POST** /v1/retrievers/{retriever_id}/publish | Publish Retriever
[**unpublish_retriever_id_publish**](PublishedRetrieversApi.md#unpublish_retriever_id_publish) | **DELETE** /v1/retrievers/{retriever_id}/publish | Unpublish Retriever
[**update_published_retriever_id_publish**](PublishedRetrieversApi.md#update_published_retriever_id_publish) | **PATCH** /v1/retrievers/{retriever_id}/publish | Update Published Retriever


# **check_name_availability_retrievers_id_publish**
> PublicNameAvailabilityResponse check_name_availability_retrievers_id_publish(retriever_id, name, authorization=authorization, x_namespace=x_namespace)

Check Name Availability

Check if a public name is available.

Public names must be globally unique across all organizations.
Use this endpoint before publishing to ensure your desired name is available.

### Example


```python
import mixpeek
from mixpeek.models.public_name_availability_response import PublicNameAvailabilityResponse
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
    api_instance = mixpeek.PublishedRetrieversApi(api_client)
    retriever_id = 'retriever_id_example' # str | ID of the retriever
    name = 'name_example' # str | Public name to check
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Check Name Availability
        api_response = api_instance.check_name_availability_retrievers_id_publish(retriever_id, name, authorization=authorization, x_namespace=x_namespace)
        print("The response of PublishedRetrieversApi->check_name_availability_retrievers_id_publish:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublishedRetrieversApi->check_name_availability_retrievers_id_publish: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retriever_id** | **str**| ID of the retriever | 
 **name** | **str**| Public name to check | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**PublicNameAvailabilityResponse**](PublicNameAvailabilityResponse.md)

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

# **get_organization_publish_stats_retrievers**
> OrganizationPublishStatsResponse get_organization_publish_stats_retrievers(authorization=authorization, x_namespace=x_namespace)

Get Organization Publish Stats

Get organization publish statistics.

### Example


```python
import mixpeek
from mixpeek.models.organization_publish_stats_response import OrganizationPublishStatsResponse
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
    api_instance = mixpeek.PublishedRetrieversApi(api_client)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Organization Publish Stats
        api_response = api_instance.get_organization_publish_stats_retrievers(authorization=authorization, x_namespace=x_namespace)
        print("The response of PublishedRetrieversApi->get_organization_publish_stats_retrievers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublishedRetrieversApi->get_organization_publish_stats_retrievers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**OrganizationPublishStatsResponse**](OrganizationPublishStatsResponse.md)

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

# **get_published_retriever_id_publish**
> PublishedRetrieverResponse get_published_retriever_id_publish(retriever_id, authorization=authorization, x_namespace=x_namespace)

Get Published Retriever

Get published retriever details.

Returns configuration including public URL, display settings, and rate limits.
The public API key is not returned (it was shown only once during publishing).

### Example


```python
import mixpeek
from mixpeek.models.published_retriever_response import PublishedRetrieverResponse
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
    api_instance = mixpeek.PublishedRetrieversApi(api_client)
    retriever_id = 'retriever_id_example' # str | ID of the retriever
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Published Retriever
        api_response = api_instance.get_published_retriever_id_publish(retriever_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of PublishedRetrieversApi->get_published_retriever_id_publish:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublishedRetrieversApi->get_published_retriever_id_publish: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retriever_id** | **str**| ID of the retriever | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**PublishedRetrieverResponse**](PublishedRetrieverResponse.md)

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

# **list_published_retrievers**
> object list_published_retrievers(limit=limit, offset=offset, authorization=authorization, x_namespace=x_namespace)

List Published Retrievers

List all published retrievers for the organization.

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
    api_instance = mixpeek.PublishedRetrieversApi(api_client)
    limit = 100 # int | Maximum number of results (optional) (default to 100)
    offset = 0 # int | Number of results to skip (optional) (default to 0)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # List Published Retrievers
        api_response = api_instance.list_published_retrievers(limit=limit, offset=offset, authorization=authorization, x_namespace=x_namespace)
        print("The response of PublishedRetrieversApi->list_published_retrievers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublishedRetrieversApi->list_published_retrievers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of results | [optional] [default to 100]
 **offset** | **int**| Number of results to skip | [optional] [default to 0]
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

# **publish_retriever**
> PublishRetrieverResponse publish_retriever(retriever_id, publish_retriever_request, authorization=authorization, x_namespace=x_namespace)

Publish Retriever

Publish a retriever as a public search interface.

Creates a public API endpoint and branded page for the retriever.
Returns a public API key that should be stored securely (shown only once).

**Limits:**
- Maximum 10 published retrievers per organization
- Public name must be globally unique

**Security:**
- Public API key is required for all requests
- Optional password protection via organization secrets
- Configurable rate limits per retriever
- Field masking ensures only approved fields are exposed

### Example


```python
import mixpeek
from mixpeek.models.publish_retriever_request import PublishRetrieverRequest
from mixpeek.models.publish_retriever_response import PublishRetrieverResponse
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
    api_instance = mixpeek.PublishedRetrieversApi(api_client)
    retriever_id = 'retriever_id_example' # str | ID of the retriever to publish
    publish_retriever_request = mixpeek.PublishRetrieverRequest() # PublishRetrieverRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Publish Retriever
        api_response = api_instance.publish_retriever(retriever_id, publish_retriever_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of PublishedRetrieversApi->publish_retriever:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublishedRetrieversApi->publish_retriever: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retriever_id** | **str**| ID of the retriever to publish | 
 **publish_retriever_request** | [**PublishRetrieverRequest**](PublishRetrieverRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**PublishRetrieverResponse**](PublishRetrieverResponse.md)

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

# **unpublish_retriever_id_publish**
> GenericDeleteResponse unpublish_retriever_id_publish(retriever_id, authorization=authorization, x_namespace=x_namespace)

Unpublish Retriever

Unpublish a retriever.

Removes the public API endpoint and deletes the short URL redirect.
The public API key will immediately stop working.
This action cannot be undone (you'll need to republish to get a new API key).

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
    api_instance = mixpeek.PublishedRetrieversApi(api_client)
    retriever_id = 'retriever_id_example' # str | ID of the retriever to unpublish
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Unpublish Retriever
        api_response = api_instance.unpublish_retriever_id_publish(retriever_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of PublishedRetrieversApi->unpublish_retriever_id_publish:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublishedRetrieversApi->unpublish_retriever_id_publish: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retriever_id** | **str**| ID of the retriever to unpublish | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

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

# **update_published_retriever_id_publish**
> PublishedRetrieverResponse update_published_retriever_id_publish(retriever_id, update_published_retriever_request, authorization=authorization, x_namespace=x_namespace)

Update Published Retriever

Update published retriever configuration.

Allows updating display config, rate limits, exposed fields, and password protection.
The public API key and public name cannot be changed (unpublish and republish instead).

### Example


```python
import mixpeek
from mixpeek.models.published_retriever_response import PublishedRetrieverResponse
from mixpeek.models.update_published_retriever_request import UpdatePublishedRetrieverRequest
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
    api_instance = mixpeek.PublishedRetrieversApi(api_client)
    retriever_id = 'retriever_id_example' # str | ID of the retriever
    update_published_retriever_request = mixpeek.UpdatePublishedRetrieverRequest() # UpdatePublishedRetrieverRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Update Published Retriever
        api_response = api_instance.update_published_retriever_id_publish(retriever_id, update_published_retriever_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of PublishedRetrieversApi->update_published_retriever_id_publish:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublishedRetrieversApi->update_published_retriever_id_publish: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retriever_id** | **str**| ID of the retriever | 
 **update_published_retriever_request** | [**UpdatePublishedRetrieverRequest**](UpdatePublishedRetrieverRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**PublishedRetrieverResponse**](PublishedRetrieverResponse.md)

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

