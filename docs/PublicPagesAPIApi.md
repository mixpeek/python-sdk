# mixpeek.PublicPagesAPIApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_page_search_slug**](PublicPagesAPIApi.md#execute_page_search_slug) | **POST** /v1/public/pages/{slug}/search | Execute a Page tab search
[**get_page_config_slug**](PublicPagesAPIApi.md#get_page_config_slug) | **GET** /v1/public/pages/{slug} | Get public Page config
[**get_page_gallery_slug**](PublicPagesAPIApi.md#get_page_gallery_slug) | **GET** /v1/public/pages/{slug}/gallery | Get Page featured gallery


# **execute_page_search_slug**
> object execute_page_search_slug(slug, public_page_search_request)

Execute a Page tab search

Execute a search on a specific tab of a public Page — no authentication required.

Routes `tab_id` → retriever → results. Each tab can be backed by either:
- An **internal retriever** (`retriever_id`) — org-scoped, requires the page
  to be in your namespace
- A **marketplace catalog entry** (`public_name`) — proxied to the public
  marketplace API, no org context needed

The `inputs` dict is passed directly to the retriever's `input_schema`. For
image-based searches, pass `{"query_image": "data:image/jpeg;base64,..."}`.

**Example request:**
```json
{
  "tab_id": "evaluate",
  "inputs": {
    "query_image": "data:image/jpeg;base64,/9j/4AAQ..."
  },
  "settings": {}
}
```

### Example


```python
import mixpeek
from mixpeek.models.public_page_search_request import PublicPageSearchRequest
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
    api_instance = mixpeek.PublicPagesAPIApi(api_client)
    slug = 'slug_example' # str | Globally unique page slug
    public_page_search_request = mixpeek.PublicPageSearchRequest() # PublicPageSearchRequest | 

    try:
        # Execute a Page tab search
        api_response = api_instance.execute_page_search_slug(slug, public_page_search_request)
        print("The response of PublicPagesAPIApi->execute_page_search_slug:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicPagesAPIApi->execute_page_search_slug: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**| Globally unique page slug | 
 **public_page_search_request** | [**PublicPageSearchRequest**](PublicPageSearchRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Search results from the tab&#39;s retriever |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_config_slug**
> PublicPageConfigResponse get_page_config_slug(slug)

Get public Page config

Fetch the full configuration for a public Page — no authentication required.

Used by the `mxp.co/p/{slug}` frontend to render the page. Returns tabs,
hero, stats, sections, theme, and SEO settings. Password-protected pages
return a `password_protected: true` flag and omit sensitive config until
the password is verified at the search endpoint.

This endpoint is called automatically by `mxp.co/p/{slug}` on page load.
You only need to call it directly if you are building a custom frontend.

### Example


```python
import mixpeek
from mixpeek.models.public_page_config_response import PublicPageConfigResponse
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
    api_instance = mixpeek.PublicPagesAPIApi(api_client)
    slug = 'slug_example' # str | Globally unique page slug (e.g. 'brand-compliance')

    try:
        # Get public Page config
        api_response = api_instance.get_page_config_slug(slug)
        print("The response of PublicPagesAPIApi->get_page_config_slug:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicPagesAPIApi->get_page_config_slug: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**| Globally unique page slug (e.g. &#39;brand-compliance&#39;) | 

### Return type

[**PublicPageConfigResponse**](PublicPageConfigResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Full page configuration for UI rendering |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_gallery_slug**
> object get_page_gallery_slug(slug)

Get Page featured gallery

Fetch featured gallery results for a public Page — no authentication required.

Executes the page's `featured_gallery` retriever using `default_inputs` defined
in the gallery configuration. Returns an empty result set if the gallery is
disabled or not configured.

Called automatically by `mxp.co/p/{slug}` on page load to pre-populate the
featured gallery section with curated results.

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
    api_instance = mixpeek.PublicPagesAPIApi(api_client)
    slug = 'slug_example' # str | Globally unique page slug

    try:
        # Get Page featured gallery
        api_response = api_instance.get_page_gallery_slug(slug)
        print("The response of PublicPagesAPIApi->get_page_gallery_slug:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicPagesAPIApi->get_page_gallery_slug: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**| Globally unique page slug | 

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
**200** | Featured gallery results using the gallery&#39;s default inputs |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

