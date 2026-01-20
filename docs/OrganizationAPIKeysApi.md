# mixpeek.OrganizationAPIKeysApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_key_organizations_users_email**](OrganizationAPIKeysApi.md#create_key_organizations_users_email) | **POST** /v1/organizations/users/{user_email}/api-keys | Create Api Key
[**delete_key_organizations_users_email_name**](OrganizationAPIKeysApi.md#delete_key_organizations_users_email_name) | **DELETE** /v1/organizations/users/{user_email}/api-keys/{key_name} | Delete Api Key
[**list_keys_organizations_users_email**](OrganizationAPIKeysApi.md#list_keys_organizations_users_email) | **GET** /v1/organizations/users/{user_email}/api-keys | List Api Keys
[**rotate_key_organizations_users_email_name**](OrganizationAPIKeysApi.md#rotate_key_organizations_users_email_name) | **POST** /v1/organizations/users/{user_email}/api-keys/{key_name}/rotate | Rotate Api Key
[**update_key_organizations_users_email_name**](OrganizationAPIKeysApi.md#update_key_organizations_users_email_name) | **PATCH** /v1/organizations/users/{user_email}/api-keys/{key_name} | Update Api Key


# **create_key_organizations_users_email**
> APIKeyCreateResponse create_key_organizations_users_email(user_email, api_key_create_request, authorization=authorization)

Create Api Key

Create a new API key for a user.

### Example


```python
import mixpeek
from mixpeek.models.api_key_create_request import APIKeyCreateRequest
from mixpeek.models.api_key_create_response import APIKeyCreateResponse
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
    api_instance = mixpeek.OrganizationAPIKeysApi(api_client)
    user_email = 'user_email_example' # str | 
    api_key_create_request = mixpeek.APIKeyCreateRequest() # APIKeyCreateRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Create Api Key
        api_response = api_instance.create_key_organizations_users_email(user_email, api_key_create_request, authorization=authorization)
        print("The response of OrganizationAPIKeysApi->create_key_organizations_users_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationAPIKeysApi->create_key_organizations_users_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_email** | **str**|  | 
 **api_key_create_request** | [**APIKeyCreateRequest**](APIKeyCreateRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**APIKeyCreateResponse**](APIKeyCreateResponse.md)

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

# **delete_key_organizations_users_email_name**
> GenericSuccessResponse delete_key_organizations_users_email_name(user_email, key_name, authorization=authorization)

Delete Api Key

Revoke an API key.

🔒 The "admin-key" is protected and cannot be deleted.

### Example


```python
import mixpeek
from mixpeek.models.generic_success_response import GenericSuccessResponse
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
    api_instance = mixpeek.OrganizationAPIKeysApi(api_client)
    user_email = 'user_email_example' # str | 
    key_name = 'key_name_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Delete Api Key
        api_response = api_instance.delete_key_organizations_users_email_name(user_email, key_name, authorization=authorization)
        print("The response of OrganizationAPIKeysApi->delete_key_organizations_users_email_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationAPIKeysApi->delete_key_organizations_users_email_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_email** | **str**|  | 
 **key_name** | **str**|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**GenericSuccessResponse**](GenericSuccessResponse.md)

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

# **list_keys_organizations_users_email**
> object list_keys_organizations_users_email(user_email, include_revoked=include_revoked, authorization=authorization)

List Api Keys

List API keys for a user.

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
    api_instance = mixpeek.OrganizationAPIKeysApi(api_client)
    user_email = 'user_email_example' # str | 
    include_revoked = False # bool |  (optional) (default to False)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # List Api Keys
        api_response = api_instance.list_keys_organizations_users_email(user_email, include_revoked=include_revoked, authorization=authorization)
        print("The response of OrganizationAPIKeysApi->list_keys_organizations_users_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationAPIKeysApi->list_keys_organizations_users_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_email** | **str**|  | 
 **include_revoked** | **bool**|  | [optional] [default to False]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

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

# **rotate_key_organizations_users_email_name**
> APIKeyCreateResponse rotate_key_organizations_users_email_name(user_email, key_name, authorization=authorization)

Rotate Api Key

Rotate an API key and return the new secret.

🔒 The "admin-key" is protected and cannot be rotated.

### Example


```python
import mixpeek
from mixpeek.models.api_key_create_response import APIKeyCreateResponse
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
    api_instance = mixpeek.OrganizationAPIKeysApi(api_client)
    user_email = 'user_email_example' # str | 
    key_name = 'key_name_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Rotate Api Key
        api_response = api_instance.rotate_key_organizations_users_email_name(user_email, key_name, authorization=authorization)
        print("The response of OrganizationAPIKeysApi->rotate_key_organizations_users_email_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationAPIKeysApi->rotate_key_organizations_users_email_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_email** | **str**|  | 
 **key_name** | **str**|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**APIKeyCreateResponse**](APIKeyCreateResponse.md)

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

# **update_key_organizations_users_email_name**
> APIKeyModel update_key_organizations_users_email_name(user_email, key_name, api_key_update_request, authorization=authorization)

Update Api Key

Update an API key's metadata or permissions.

🔒 The "admin-key" is protected and cannot be modified.

### Example


```python
import mixpeek
from mixpeek.models.api_key_model import APIKeyModel
from mixpeek.models.api_key_update_request import APIKeyUpdateRequest
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
    api_instance = mixpeek.OrganizationAPIKeysApi(api_client)
    user_email = 'user_email_example' # str | 
    key_name = 'key_name_example' # str | 
    api_key_update_request = mixpeek.APIKeyUpdateRequest() # APIKeyUpdateRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Update Api Key
        api_response = api_instance.update_key_organizations_users_email_name(user_email, key_name, api_key_update_request, authorization=authorization)
        print("The response of OrganizationAPIKeysApi->update_key_organizations_users_email_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationAPIKeysApi->update_key_organizations_users_email_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_email** | **str**|  | 
 **key_name** | **str**|  | 
 **api_key_update_request** | [**APIKeyUpdateRequest**](APIKeyUpdateRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**APIKeyModel**](APIKeyModel.md)

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

