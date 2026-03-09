# mixpeek.PagesApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_page**](PagesApi.md#create_page) | **POST** /v1/pages | Create a Page
[**delete_page**](PagesApi.md#delete_page) | **DELETE** /v1/pages/{page_id} | Delete a Page
[**get_page**](PagesApi.md#get_page) | **GET** /v1/pages/{page_id} | Get a Page
[**list_pages**](PagesApi.md#list_pages) | **GET** /v1/pages | List Pages
[**update_page**](PagesApi.md#update_page) | **PATCH** /v1/pages/{page_id} | Update a Page


# **create_page**
> PageResponse create_page(create_page_request, authorization=authorization, authorization2=authorization2, x_namespace=x_namespace)

Create a Page

Create a new branded Page served at `https://mxp.co/p/{slug}`.

Pages are multi-tab search interfaces that combine retrievers, a hero section,
featured galleries, stats bars, and custom SEO — all served from a globally
unique slug. Each tab can route to an internal retriever (`retriever_id`) or a
marketplace catalog entry (`public_name`).

**Rendering modes (in priority order):**
1. `custom_html` — raw HTML/CSS/JS in a sandboxed iframe (full control)
2. `sections[]` — slot-based composition with typed blocks (`template: "generic"`)
3. Named presets — `template: "brand-compliance"` etc. (legacy)

**Slugs** are globally unique across all organizations. The page will be
accessible at `https://mxp.co/p/{slug}` immediately after creation.

When a retriever is published via `POST /v1/retrievers/{id}/publish`, a
companion Page is auto-created at `/p/{public_name}` — you don't need to call
this endpoint manually unless you want to customize the page further.

### Example


```python
import mixpeek
from mixpeek.models.create_page_request import CreatePageRequest
from mixpeek.models.page_response import PageResponse
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
    api_instance = mixpeek.PagesApi(api_client)
    create_page_request = mixpeek.CreatePageRequest() # CreatePageRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    authorization2 = 'authorization_example' # str |  (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Create a Page
        api_response = api_instance.create_page(create_page_request, authorization=authorization, authorization2=authorization2, x_namespace=x_namespace)
        print("The response of PagesApi->create_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PagesApi->create_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_page_request** | [**CreatePageRequest**](CreatePageRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **authorization2** | **str**|  | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**PageResponse**](PageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created Page configuration |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_page**
> GenericDeleteResponse delete_page(page_id, authorization=authorization, authorization2=authorization2, x_namespace=x_namespace)

Delete a Page

Delete a Page permanently.

The slug is freed immediately and can be reused. The page will stop
being served at `https://mxp.co/p/{slug}` within seconds.

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
    api_instance = mixpeek.PagesApi(api_client)
    page_id = 'page_id_example' # str | Page ID (e.g. pg_abc123def456)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    authorization2 = 'authorization_example' # str |  (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Delete a Page
        api_response = api_instance.delete_page(page_id, authorization=authorization, authorization2=authorization2, x_namespace=x_namespace)
        print("The response of PagesApi->delete_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PagesApi->delete_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page ID (e.g. pg_abc123def456) | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **authorization2** | **str**|  | [optional] 
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
**200** | Deletion confirmation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page**
> PageResponse get_page(page_id, authorization=authorization, authorization2=authorization2, x_namespace=x_namespace)

Get a Page

Get a Page by its `page_id`.

Returns the full configuration including tabs, sections, hero, gallery,
theme, and SEO settings.

### Example


```python
import mixpeek
from mixpeek.models.page_response import PageResponse
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
    api_instance = mixpeek.PagesApi(api_client)
    page_id = 'page_id_example' # str | Page ID (e.g. pg_abc123def456)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    authorization2 = 'authorization_example' # str |  (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get a Page
        api_response = api_instance.get_page(page_id, authorization=authorization, authorization2=authorization2, x_namespace=x_namespace)
        print("The response of PagesApi->get_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PagesApi->get_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page ID (e.g. pg_abc123def456) | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **authorization2** | **str**|  | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**PageResponse**](PageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Full Page configuration |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pages**
> ListPagesResponse list_pages(limit=limit, offset=offset, template=template, authorization=authorization, authorization2=authorization2, x_namespace=x_namespace)

List Pages

List all Pages for this organization.

Returns Pages scoped to your organization and namespace. Use `template` to
filter to a specific rendering mode (e.g. `generic` for sections-based pages
or `brand-compliance` for the legacy compliance template).

### Example


```python
import mixpeek
from mixpeek.models.list_pages_response import ListPagesResponse
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
    api_instance = mixpeek.PagesApi(api_client)
    limit = 100 # int | Maximum number of results to return (optional) (default to 100)
    offset = 0 # int | Number of results to skip for pagination (optional) (default to 0)
    template = 'template_example' # str | Filter by template type (e.g. 'generic', 'brand-compliance') (optional)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    authorization2 = 'authorization_example' # str |  (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # List Pages
        api_response = api_instance.list_pages(limit=limit, offset=offset, template=template, authorization=authorization, authorization2=authorization2, x_namespace=x_namespace)
        print("The response of PagesApi->list_pages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PagesApi->list_pages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of results to return | [optional] [default to 100]
 **offset** | **int**| Number of results to skip for pagination | [optional] [default to 0]
 **template** | **str**| Filter by template type (e.g. &#39;generic&#39;, &#39;brand-compliance&#39;) | [optional] 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **authorization2** | **str**|  | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**ListPagesResponse**](ListPagesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated list of Pages for this organization |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_page**
> PageResponse update_page(page_id, update_page_request, authorization=authorization, authorization2=authorization2, x_namespace=x_namespace)

Update a Page

Partially update a Page configuration.

All fields are optional — only the fields you provide are updated. Omitted
fields retain their current values.

If you update `slug`, it must be globally unique. If you update `tabs`, all
`retriever_id` references are re-validated against your organization.

### Example


```python
import mixpeek
from mixpeek.models.page_response import PageResponse
from mixpeek.models.update_page_request import UpdatePageRequest
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
    api_instance = mixpeek.PagesApi(api_client)
    page_id = 'page_id_example' # str | Page ID (e.g. pg_abc123def456)
    update_page_request = mixpeek.UpdatePageRequest() # UpdatePageRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    authorization2 = 'authorization_example' # str |  (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Update a Page
        api_response = api_instance.update_page(page_id, update_page_request, authorization=authorization, authorization2=authorization2, x_namespace=x_namespace)
        print("The response of PagesApi->update_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PagesApi->update_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page ID (e.g. pg_abc123def456) | 
 **update_page_request** | [**UpdatePageRequest**](UpdatePageRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **authorization2** | **str**|  | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**PageResponse**](PageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated Page configuration |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

