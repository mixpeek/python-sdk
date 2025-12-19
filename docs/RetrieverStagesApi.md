# mixpeek.RetrieverStagesApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_stages_retrievers**](RetrieverStagesApi.md#list_stages_retrievers) | **GET** /v1/retrievers/stages | List available retriever stages


# **list_stages_retrievers**
> List[RetrieverStageDefinition] list_stages_retrievers(authorization=authorization, x_namespace=x_namespace)

List available retriever stages

List available retriever stages.

### Example


```python
import mixpeek
from mixpeek.models.retriever_stage_definition import RetrieverStageDefinition
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
    api_instance = mixpeek.RetrieverStagesApi(api_client)
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)
    x_namespace = 'x_namespace_example' # str | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. (optional)

    try:
        # List available retriever stages
        api_response = api_instance.list_stages_retrievers(authorization=authorization, x_namespace=x_namespace)
        print("The response of RetrieverStagesApi->list_stages_retrievers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrieverStagesApi->list_stages_retrievers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 
 **x_namespace** | **str**| Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: &#39;netflix_prod&#39; or &#39;ns_1234567890&#39;. To create a namespace, use the /namespaces endpoint. | [optional] 

### Return type

[**List[RetrieverStageDefinition]**](RetrieverStageDefinition.md)

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

