# mixpeek.WebhooksApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook_organizations**](WebhooksApi.md#create_webhook_organizations) | **POST** /v1/organizations/webhooks/ | Create Webhook
[**delete_webhook_organizations**](WebhooksApi.md#delete_webhook_organizations) | **DELETE** /v1/organizations/webhooks/{identifier} | Delete Webhook
[**get_webhook_organizations**](WebhooksApi.md#get_webhook_organizations) | **GET** /v1/organizations/webhooks/{identifier} | Get Webhook
[**list_webhooks_organizations**](WebhooksApi.md#list_webhooks_organizations) | **GET** /v1/organizations/webhooks/ | List Webhooks
[**update_webhook_organizations**](WebhooksApi.md#update_webhook_organizations) | **PUT** /v1/organizations/webhooks/{identifier} | Update Webhook


# **create_webhook_organizations**
> WebhookOutput create_webhook_organizations(webhook_input, authorization=authorization)

Create Webhook

Create a new webhook for the user's organization.

### Example


```python
import mixpeek
from mixpeek.models.webhook_input import WebhookInput
from mixpeek.models.webhook_output import WebhookOutput
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
    api_instance = mixpeek.WebhooksApi(api_client)
    webhook_input = mixpeek.WebhookInput() # WebhookInput | 
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)

    try:
        # Create Webhook
        api_response = api_instance.create_webhook_organizations(webhook_input, authorization=authorization)
        print("The response of WebhooksApi->create_webhook_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->create_webhook_organizations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_input** | [**WebhookInput**](WebhookInput.md)|  | 
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 

### Return type

[**WebhookOutput**](WebhookOutput.md)

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

# **delete_webhook_organizations**
> delete_webhook_organizations(identifier, authorization=authorization)

Delete Webhook

Delete a webhook.

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
    api_instance = mixpeek.WebhooksApi(api_client)
    identifier = 'identifier_example' # str | 
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)

    try:
        # Delete Webhook
        api_instance.delete_webhook_organizations(identifier, authorization=authorization)
    except Exception as e:
        print("Exception when calling WebhooksApi->delete_webhook_organizations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**|  | 
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook_organizations**
> WebhookOutput get_webhook_organizations(identifier, authorization=authorization)

Get Webhook

Get a single webhook by its ID.

### Example


```python
import mixpeek
from mixpeek.models.webhook_output import WebhookOutput
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
    api_instance = mixpeek.WebhooksApi(api_client)
    identifier = 'identifier_example' # str | 
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)

    try:
        # Get Webhook
        api_response = api_instance.get_webhook_organizations(identifier, authorization=authorization)
        print("The response of WebhooksApi->get_webhook_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->get_webhook_organizations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**|  | 
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 

### Return type

[**WebhookOutput**](WebhookOutput.md)

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

# **list_webhooks_organizations**
> List[WebhookOutput] list_webhooks_organizations(authorization=authorization)

List Webhooks

List all webhooks for the user's organization.

### Example


```python
import mixpeek
from mixpeek.models.webhook_output import WebhookOutput
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
    api_instance = mixpeek.WebhooksApi(api_client)
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)

    try:
        # List Webhooks
        api_response = api_instance.list_webhooks_organizations(authorization=authorization)
        print("The response of WebhooksApi->list_webhooks_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->list_webhooks_organizations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 

### Return type

[**List[WebhookOutput]**](WebhookOutput.md)

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

# **update_webhook_organizations**
> WebhookOutput update_webhook_organizations(identifier, webhook_input, authorization=authorization)

Update Webhook

Update an existing webhook.

### Example


```python
import mixpeek
from mixpeek.models.webhook_input import WebhookInput
from mixpeek.models.webhook_output import WebhookOutput
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
    api_instance = mixpeek.WebhooksApi(api_client)
    identifier = 'identifier_example' # str | 
    webhook_input = mixpeek.WebhookInput() # WebhookInput | 
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)

    try:
        # Update Webhook
        api_response = api_instance.update_webhook_organizations(identifier, webhook_input, authorization=authorization)
        print("The response of WebhooksApi->update_webhook_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->update_webhook_organizations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**|  | 
 **webhook_input** | [**WebhookInput**](WebhookInput.md)|  | 
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 

### Return type

[**WebhookOutput**](WebhookOutput.md)

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

