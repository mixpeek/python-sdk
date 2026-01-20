# mixpeek.PublicNotificationsAPIApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**unsubscribe_from_nudges_notifications**](PublicNotificationsAPIApi.md#unsubscribe_from_nudges_notifications) | **GET** /v1/public/notifications/unsubscribe | Unsubscribe From Nudges


# **unsubscribe_from_nudges_notifications**
> object unsubscribe_from_nudges_notifications(token)

Unsubscribe From Nudges

Unsubscribe from nudge emails using a signed token.

This is a public endpoint (no auth required) for one-click unsubscribe
from email links. The token is cryptographically signed and contains
the organization ID and nudge type.

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
    api_instance = mixpeek.PublicNotificationsAPIApi(api_client)
    token = 'token_example' # str | Signed unsubscribe token from email

    try:
        # Unsubscribe From Nudges
        api_response = api_instance.unsubscribe_from_nudges_notifications(token)
        print("The response of PublicNotificationsAPIApi->unsubscribe_from_nudges_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicNotificationsAPIApi->unsubscribe_from_nudges_notifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Signed unsubscribe token from email | 

### Return type

**object**

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

