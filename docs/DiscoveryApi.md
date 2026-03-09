# mixpeek.DiscoveryApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_discovery**](DiscoveryApi.md#get_all_discovery) | **GET** /v1/discovery | Get All Discovery Information
[**get_manifest_schema_discovery**](DiscoveryApi.md#get_manifest_schema_discovery) | **GET** /v1/discovery/schema | Get Manifest Schema for Agent Configuration
[**list_extractors_discovery**](DiscoveryApi.md#list_extractors_discovery) | **GET** /v1/discovery/extractors | List Available Feature Extractors
[**list_stages_with_examples_discovery**](DiscoveryApi.md#list_stages_with_examples_discovery) | **GET** /v1/discovery/stages | List Available Retriever Stages with Examples


# **get_all_discovery**
> DiscoveryResponse get_all_discovery()

Get All Discovery Information

Returns combined discovery information including extractors, stages, and manifest schema in a single request. Use this for comprehensive capability discovery.

### Example


```python
import mixpeek
from mixpeek.models.discovery_response import DiscoveryResponse
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
    api_instance = mixpeek.DiscoveryApi(api_client)

    try:
        # Get All Discovery Information
        api_response = api_instance.get_all_discovery()
        print("The response of DiscoveryApi->get_all_discovery:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscoveryApi->get_all_discovery: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DiscoveryResponse**](DiscoveryResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manifest_schema_discovery**
> ManifestSchemaDiscovery get_manifest_schema_discovery()

Get Manifest Schema for Agent Configuration

Returns the complete manifest schema including all resource types, their JSON schemas, dependency graph, and YAML examples. Use this for programmatic manifest generation and validation.

### Example


```python
import mixpeek
from mixpeek.models.manifest_schema_discovery import ManifestSchemaDiscovery
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
    api_instance = mixpeek.DiscoveryApi(api_client)

    try:
        # Get Manifest Schema for Agent Configuration
        api_response = api_instance.get_manifest_schema_discovery()
        print("The response of DiscoveryApi->get_manifest_schema_discovery:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscoveryApi->get_manifest_schema_discovery: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ManifestSchemaDiscovery**](ManifestSchemaDiscovery.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_extractors_discovery**
> List[ExtractorDiscovery] list_extractors_discovery()

List Available Feature Extractors

Discover all available feature extractors with their capabilities, supported modalities, output features, and example usage. Use this to understand what extractors are available when configuring namespaces and collections in manifests.

### Example


```python
import mixpeek
from mixpeek.models.extractor_discovery import ExtractorDiscovery
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
    api_instance = mixpeek.DiscoveryApi(api_client)

    try:
        # List Available Feature Extractors
        api_response = api_instance.list_extractors_discovery()
        print("The response of DiscoveryApi->list_extractors_discovery:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscoveryApi->list_extractors_discovery: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ExtractorDiscovery]**](ExtractorDiscovery.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_stages_with_examples_discovery**
> List[StageDiscovery] list_stages_with_examples_discovery()

List Available Retriever Stages with Examples

Discover all available retriever stages with extended information including example configurations, common use cases, and cost tiers. This endpoint provides more context than /v1/retrievers/stages for agent-driven configuration.

### Example


```python
import mixpeek
from mixpeek.models.stage_discovery import StageDiscovery
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
    api_instance = mixpeek.DiscoveryApi(api_client)

    try:
        # List Available Retriever Stages with Examples
        api_response = api_instance.list_stages_with_examples_discovery()
        print("The response of DiscoveryApi->list_stages_with_examples_discovery:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscoveryApi->list_stages_with_examples_discovery: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[StageDiscovery]**](StageDiscovery.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

