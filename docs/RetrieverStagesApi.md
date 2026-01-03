# mixpeek.RetrieverStagesApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_stages_retrievers**](RetrieverStagesApi.md#list_stages_retrievers) | **GET** /v1/retrievers/stages | List Available Retriever Stages


# **list_stages_retrievers**
> List[RetrieverStageDefinition] list_stages_retrievers()

List Available Retriever Stages

List all registered retriever stages with their configurations. Use this endpoint to discover available stages before creating retrievers. Each stage includes its ID, description, category, and full parameter schema. The parameter_schema field contains complete Pydantic JSON Schema with validation rules, descriptions, and examples for all stage parameters.

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

    try:
        # List Available Retriever Stages
        api_response = api_instance.list_stages_retrievers()
        print("The response of RetrieverStagesApi->list_stages_retrievers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrieverStagesApi->list_stages_retrievers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | List of retriever stage definitions with complete parameter schemas. Each stage includes: - stage_id: Unique identifier to use in retriever configurations - description: Human-readable purpose and behavior - category: Transformation type (filter/sort/reduce/apply) - icon: UI icon identifier - parameter_schema: Full JSON Schema for stage parameters (null if no params) |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

