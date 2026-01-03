# mixpeek.ScaffoldTemplatesApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**instantiate_scaffold_template**](ScaffoldTemplatesApi.md#instantiate_scaffold_template) | **POST** /v1/templates/scaffolds/{template_id}/instantiate | Instantiate Scaffold Template


# **instantiate_scaffold_template**
> InstantiatedScaffoldResponse instantiate_scaffold_template(template_id, instantiate_scaffold_request, authorization=authorization)

Instantiate Scaffold Template

Create complete infrastructure from scaffold template.

Creates all resources atomically:
1. **Namespace** with configured feature extractors
2. **Bucket** with schema for your data structure
3. **Collection** linked to bucket with feature config
4. **Retriever** with search pipeline stages

All resources are empty, ready for data upload.

**Next Steps:**
1. Upload data: `POST /v1/buckets/{bucket_id}/objects`
2. Process batch: `POST /v1/collections/{collection_id}/batches`
3. Search: `POST /v1/retrievers/{retriever_id}/retrieve`

**Example Request:**
```json
{
    "namespace_name": "my_video_app",
    "namespace_description": "Video search application"
}
```

### Example


```python
import mixpeek
from mixpeek.models.instantiate_scaffold_request import InstantiateScaffoldRequest
from mixpeek.models.instantiated_scaffold_response import InstantiatedScaffoldResponse
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
    api_instance = mixpeek.ScaffoldTemplatesApi(api_client)
    template_id = 'template_id_example' # str | Scaffold template ID
    instantiate_scaffold_request = mixpeek.InstantiateScaffoldRequest() # InstantiateScaffoldRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Instantiate Scaffold Template
        api_response = api_instance.instantiate_scaffold_template(template_id, instantiate_scaffold_request, authorization=authorization)
        print("The response of ScaffoldTemplatesApi->instantiate_scaffold_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScaffoldTemplatesApi->instantiate_scaffold_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| Scaffold template ID | 
 **instantiate_scaffold_request** | [**InstantiateScaffoldRequest**](InstantiateScaffoldRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**InstantiatedScaffoldResponse**](InstantiatedScaffoldResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

