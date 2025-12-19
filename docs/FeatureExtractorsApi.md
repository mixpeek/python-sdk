# mixpeek.FeatureExtractorsApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_feature_extractor_by**](FeatureExtractorsApi.md#get_feature_extractor_by) | **GET** /v1/collections/features/extractors/{feature_extractor_id} | Get Feature Extractor by Name
[**list_feature_extractors**](FeatureExtractorsApi.md#list_feature_extractors) | **GET** /v1/collections/features/extractors | List Feature Extractors


# **get_feature_extractor_by**
> FeatureExtractorResponseModel get_feature_extractor_by(feature_extractor_id)

Get Feature Extractor by Name

Get detailed information about a specific feature extractor by its name

### Example


```python
import mixpeek
from mixpeek.models.feature_extractor_response_model import FeatureExtractorResponseModel
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
    api_instance = mixpeek.FeatureExtractorsApi(api_client)
    feature_extractor_id = 'feature_extractor_id_example' # str | 

    try:
        # Get Feature Extractor by Name
        api_response = api_instance.get_feature_extractor_by(feature_extractor_id)
        print("The response of FeatureExtractorsApi->get_feature_extractor_by:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeatureExtractorsApi->get_feature_extractor_by: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature_extractor_id** | **str**|  | 

### Return type

[**FeatureExtractorResponseModel**](FeatureExtractorResponseModel.md)

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

# **list_feature_extractors**
> List[FeatureExtractorResponseModel] list_feature_extractors()

List Feature Extractors

List all available feature extractors grouped by category

### Example


```python
import mixpeek
from mixpeek.models.feature_extractor_response_model import FeatureExtractorResponseModel
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
    api_instance = mixpeek.FeatureExtractorsApi(api_client)

    try:
        # List Feature Extractors
        api_response = api_instance.list_feature_extractors()
        print("The response of FeatureExtractorsApi->list_feature_extractors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeatureExtractorsApi->list_feature_extractors: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[FeatureExtractorResponseModel]**](FeatureExtractorResponseModel.md)

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

