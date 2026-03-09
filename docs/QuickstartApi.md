# mixpeek.QuickstartApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**provision_docs_search_quickstart**](QuickstartApi.md#provision_docs_search_quickstart) | **POST** /v1/quickstart/docs-search | Provision Docs Search


# **provision_docs_search_quickstart**
> DocsSearchResponse provision_docs_search_quickstart(docs_search_request, authorization=authorization)

Provision Docs Search

One-call provisioning of a complete documentation search pipeline. Creates a namespace, bucket, web crawl collection, retriever with semantic + code search, publishes it, and generates a scoped API key. Returns everything needed to embed the search widget.

### Example


```python
import mixpeek
from mixpeek.models.docs_search_request import DocsSearchRequest
from mixpeek.models.docs_search_response import DocsSearchResponse
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
    api_instance = mixpeek.QuickstartApi(api_client)
    docs_search_request = mixpeek.DocsSearchRequest() # DocsSearchRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Provision Docs Search
        api_response = api_instance.provision_docs_search_quickstart(docs_search_request, authorization=authorization)
        print("The response of QuickstartApi->provision_docs_search_quickstart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuickstartApi->provision_docs_search_quickstart: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **docs_search_request** | [**DocsSearchRequest**](DocsSearchRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**DocsSearchResponse**](DocsSearchResponse.md)

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

