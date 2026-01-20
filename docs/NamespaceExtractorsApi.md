# mixpeek.NamespaceExtractorsApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_extractor_namespaces**](NamespaceExtractorsApi.md#get_extractor_namespaces) | **GET** /v1/namespaces/{namespace_id}/extractors/{extractor_id} | Get extractor details
[**list_extractors_namespaces**](NamespaceExtractorsApi.md#list_extractors_namespaces) | **GET** /v1/namespaces/{namespace_id}/extractors | List all extractors available to namespace


# **get_extractor_namespaces**
> UnifiedExtractorResponse get_extractor_namespaces(namespace_id, extractor_id, authorization=authorization, x_namespace=x_namespace)

Get extractor details

Get detailed information about a specific extractor.

Works for both builtin extractors and custom plugins.

**Parameters:**
- `extractor_id`: Extractor identifier (e.g., 'text_extractor_v1', 'my_custom_plugin_1_0_0')

**Response includes:**
- Full schema information (input, output, parameters)
- Vector index configuration
- For custom plugins: deployment status, validation status

### Example


```python
import mixpeek
from mixpeek.models.unified_extractor_response import UnifiedExtractorResponse
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
    api_instance = mixpeek.NamespaceExtractorsApi(api_client)
    namespace_id = 'namespace_id_example' # str | 
    extractor_id = 'extractor_id_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get extractor details
        api_response = api_instance.get_extractor_namespaces(namespace_id, extractor_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of NamespaceExtractorsApi->get_extractor_namespaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NamespaceExtractorsApi->get_extractor_namespaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_id** | **str**|  | 
 **extractor_id** | **str**|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**UnifiedExtractorResponse**](UnifiedExtractorResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Extractor details |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Extractor not found |  -  |
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_extractors_namespaces**
> UnifiedExtractorListResponse list_extractors_namespaces(namespace_id, source=source, include_disabled=include_disabled, authorization=authorization, x_namespace=x_namespace)

List all extractors available to namespace

List all feature extractors available for use in this namespace.

This endpoint returns a **unified view** combining:
- **Builtin extractors**: Core extractors shipped with Mixpeek (text_extractor, image_extractor, etc.)
- **Custom plugins**: User-uploaded plugins at org or namespace level (Enterprise)

Each extractor includes:
- `input_schema`: JSON schema for input data validation
- `output_schema`: JSON schema for output document structure
- `parameter_schema`: JSON schema for configurable parameters
- `required_vector_indexes`: Vector indexes produced by this extractor
- `feature_uri`: URI to reference this extractor in collections

**Use Cases:**
- Discover available extractors when creating collections
- Get schema information for SDK code generation
- Check which custom plugins are deployed

**Filtering:**
- `source=builtin`: Only builtin extractors
- `source=custom`: Only custom plugins
- `source=all` (default): All extractors

### Example


```python
import mixpeek
from mixpeek.models.unified_extractor_list_response import UnifiedExtractorListResponse
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
    api_instance = mixpeek.NamespaceExtractorsApi(api_client)
    namespace_id = 'namespace_id_example' # str | 
    source = 'source_example' # str | Filter by extractor source (builtin, custom, or all) (optional)
    include_disabled = False # bool | Include disabled/undeployed custom plugins (optional) (default to False)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # List all extractors available to namespace
        api_response = api_instance.list_extractors_namespaces(namespace_id, source=source, include_disabled=include_disabled, authorization=authorization, x_namespace=x_namespace)
        print("The response of NamespaceExtractorsApi->list_extractors_namespaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NamespaceExtractorsApi->list_extractors_namespaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_id** | **str**|  | 
 **source** | **str**| Filter by extractor source (builtin, custom, or all) | [optional] 
 **include_disabled** | **bool**| Include disabled/undeployed custom plugins | [optional] [default to False]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**UnifiedExtractorListResponse**](UnifiedExtractorListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all available extractors |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

