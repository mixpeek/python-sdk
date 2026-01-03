# mixpeek.ResourceSearchApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_resources**](ResourceSearchApi.md#search_resources) | **POST** /v1/resources/search | Search Resources


# **search_resources**
> SearchResponse search_resources(search_request, authorization=authorization, x_namespace=x_namespace)

Search Resources

Search across all resource names and IDs within your namespace.

    This endpoint performs a case-insensitive search across:
    - Buckets (bucket_name, bucket_id)
    - Collections (collection_name, collection_id)
    - Retrievers (retriever_name, retriever_id)
    - Taxonomies (taxonomy_name, taxonomy_id)
    - Clusters (cluster_name, cluster_id)
    - Namespaces (namespace_name, namespace_id)

    Results are sorted by relevance (exact matches first) and creation time (newest first).
    Use the resource_types parameter to filter searches to specific resource types.
    Pagination is supported via limit and offset parameters.

### Example


```python
import mixpeek
from mixpeek.models.search_request import SearchRequest
from mixpeek.models.search_response import SearchResponse
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
    api_instance = mixpeek.ResourceSearchApi(api_client)
    search_request = mixpeek.SearchRequest() # SearchRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Search Resources
        api_response = api_instance.search_resources(search_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of ResourceSearchApi->search_resources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceSearchApi->search_resources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_request** | [**SearchRequest**](SearchRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**SearchResponse**](SearchResponse.md)

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

