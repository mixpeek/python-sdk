# mixpeek.NamespaceCloneApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clone_namespace**](NamespaceCloneApi.md#clone_namespace) | **POST** /v1/namespaces/{namespace_identifier}/clone | Clone Namespace


# **clone_namespace**
> CloneNamespaceResponse clone_namespace(namespace_identifier, clone_namespace_request, authorization=authorization)

Clone Namespace

Clone a namespace with all its data.

    **What gets cloned:**
    - Namespace configuration (extractors, payload indexes)
    - Buckets (metadata, references same S3 files)
    - Collections (full copy of all vectors/embeddings)
    - Retrievers (pipeline configuration)

    **Use Cases:**
    - Create staging environment from production
    - Backup namespace with all data
    - Fork namespace for experimentation

    **For config-only copy (no data), use templates instead:**
    - POST /templates/namespaces/from-namespace/{id}
    - POST /templates/namespaces/{template_id}/instantiate

### Example


```python
import mixpeek
from mixpeek.models.clone_namespace_request import CloneNamespaceRequest
from mixpeek.models.clone_namespace_response import CloneNamespaceResponse
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
    api_instance = mixpeek.NamespaceCloneApi(api_client)
    namespace_identifier = 'namespace_identifier_example' # str | Source namespace ID or name to clone from
    clone_namespace_request = mixpeek.CloneNamespaceRequest() # CloneNamespaceRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Clone Namespace
        api_response = api_instance.clone_namespace(namespace_identifier, clone_namespace_request, authorization=authorization)
        print("The response of NamespaceCloneApi->clone_namespace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NamespaceCloneApi->clone_namespace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_identifier** | **str**| Source namespace ID or name to clone from | 
 **clone_namespace_request** | [**CloneNamespaceRequest**](CloneNamespaceRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**CloneNamespaceResponse**](CloneNamespaceResponse.md)

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

