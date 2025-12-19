# mixpeek.OrganizationsApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_key_organizations_users_email**](OrganizationsApi.md#create_key_organizations_users_email) | **POST** /v1/organizations/users/{user_email}/api-keys | Create Api Key
[**delete_key_organizations_users_email_name**](OrganizationsApi.md#delete_key_organizations_users_email_name) | **DELETE** /v1/organizations/users/{user_email}/api-keys/{key_name} | Delete Api Key
[**delete_user_organizations_email**](OrganizationsApi.md#delete_user_organizations_email) | **DELETE** /v1/organizations/users/{user_email} | Delete User
[**get_organization**](OrganizationsApi.md#get_organization) | **GET** /v1/organizations | Get Organization
[**get_user_organizations_email**](OrganizationsApi.md#get_user_organizations_email) | **GET** /v1/organizations/users/{user_email} | Get User
[**update_key_organizations_users_email_name**](OrganizationsApi.md#update_key_organizations_users_email_name) | **PATCH** /v1/organizations/users/{user_email}/api-keys/{key_name} | Update Api Key


# **create_key_organizations_users_email**
> APIKey create_key_organizations_users_email(user_email, key_name=key_name, authorization=authorization)

Create Api Key

Create a new API key for a specific user.

### Example


```python
import mixpeek
from mixpeek.models.api_key import APIKey
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
    api_instance = mixpeek.OrganizationsApi(api_client)
    user_email = 'user_email_example' # str | 
    key_name = 'default' # str |  (optional) (default to 'default')
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)

    try:
        # Create Api Key
        api_response = api_instance.create_key_organizations_users_email(user_email, key_name=key_name, authorization=authorization)
        print("The response of OrganizationsApi->create_key_organizations_users_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->create_key_organizations_users_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_email** | **str**|  | 
 **key_name** | **str**|  | [optional] [default to &#39;default&#39;]
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 

### Return type

[**APIKey**](APIKey.md)

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

# **delete_key_organizations_users_email_name**
> GenericSuccessResponse delete_key_organizations_users_email_name(user_email, key_name, authorization=authorization)

Delete Api Key

Delete a specific API key for a user.

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
    api_instance = mixpeek.OrganizationsApi(api_client)
    user_email = 'user_email_example' # str | 
    key_name = 'key_name_example' # str | 
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)

    try:
        # Delete Api Key
        api_response = api_instance.delete_key_organizations_users_email_name(user_email, key_name, authorization=authorization)
        print("The response of OrganizationsApi->delete_key_organizations_users_email_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->delete_key_organizations_users_email_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_email** | **str**|  | 
 **key_name** | **str**|  | 
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 

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

# **delete_user_organizations_email**
> GenericSuccessResponse delete_user_organizations_email(user_email, authorization=authorization)

Delete User

Delete a user.

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
    api_instance = mixpeek.OrganizationsApi(api_client)
    user_email = 'user_email_example' # str | 
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)

    try:
        # Delete User
        api_response = api_instance.delete_user_organizations_email(user_email, authorization=authorization)
        print("The response of OrganizationsApi->delete_user_organizations_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->delete_user_organizations_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_email** | **str**|  | 
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 

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

# **get_organization**
> OrganizationModelResponse get_organization(authorization=authorization)

Get Organization

Get an organization.

### Example


```python
import mixpeek
from mixpeek.models.organization_model_response import OrganizationModelResponse
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
    api_instance = mixpeek.OrganizationsApi(api_client)
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)

    try:
        # Get Organization
        api_response = api_instance.get_organization(authorization=authorization)
        print("The response of OrganizationsApi->get_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 

### Return type

[**OrganizationModelResponse**](OrganizationModelResponse.md)

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

# **get_user_organizations_email**
> UserModelOutput get_user_organizations_email(user_email, authorization=authorization)

Get User

Get a user.

### Example


```python
import mixpeek
from mixpeek.models.user_model_output import UserModelOutput
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
    api_instance = mixpeek.OrganizationsApi(api_client)
    user_email = 'user_email_example' # str | 
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)

    try:
        # Get User
        api_response = api_instance.get_user_organizations_email(user_email, authorization=authorization)
        print("The response of OrganizationsApi->get_user_organizations_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_user_organizations_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_email** | **str**|  | 
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 

### Return type

[**UserModelOutput**](UserModelOutput.md)

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
> APIKey update_key_organizations_users_email_name(user_email, key_name, api_key_update, authorization=authorization)

Update Api Key

Update an API key's name or permissions.

### Example


```python
import mixpeek
from mixpeek.models.api_key import APIKey
from mixpeek.models.api_key_update import APIKeyUpdate
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
    api_instance = mixpeek.OrganizationsApi(api_client)
    user_email = 'user_email_example' # str | 
    key_name = 'key_name_example' # str | 
    api_key_update = mixpeek.APIKeyUpdate() # APIKeyUpdate | 
    authorization = 'authorization_example' # str | Bearer token authentication using your API key. Format: 'Bearer your_api_key'. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: 'Bearer sk_1234567890abcdef' (optional)

    try:
        # Update Api Key
        api_response = api_instance.update_key_organizations_users_email_name(user_email, key_name, api_key_update, authorization=authorization)
        print("The response of OrganizationsApi->update_key_organizations_users_email_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->update_key_organizations_users_email_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_email** | **str**|  | 
 **key_name** | **str**|  | 
 **api_key_update** | [**APIKeyUpdate**](APIKeyUpdate.md)|  | 
 **authorization** | **str**| Bearer token authentication using your API key. Format: &#39;Bearer your_api_key&#39;. To get an API key, create an account at mixpeek.com/start and generate a key in your account settings. Example: &#39;Bearer sk_1234567890abcdef&#39; | [optional] 

### Return type

[**APIKey**](APIKey.md)

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

