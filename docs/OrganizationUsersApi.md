# mixpeek.OrganizationUsersApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user_organizations**](OrganizationUsersApi.md#create_user_organizations) | **POST** /v1/organizations/users | Create User
[**delete_user_organizations_email**](OrganizationUsersApi.md#delete_user_organizations_email) | **DELETE** /v1/organizations/users/{user_email} | Delete User
[**get_user_organizations_email**](OrganizationUsersApi.md#get_user_organizations_email) | **GET** /v1/organizations/users/{user_email} | Get User
[**list_users_organizations**](OrganizationUsersApi.md#list_users_organizations) | **GET** /v1/organizations/users | List Users
[**update_user_organizations_email**](OrganizationUsersApi.md#update_user_organizations_email) | **PATCH** /v1/organizations/users/{user_email} | Update User


# **create_user_organizations**
> object create_user_organizations(user_create_request, authorization=authorization)

Create User

Create a new organization user.

### Example


```python
import mixpeek
from mixpeek.models.user_create_request import UserCreateRequest
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
    api_instance = mixpeek.OrganizationUsersApi(api_client)
    user_create_request = mixpeek.UserCreateRequest() # UserCreateRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Create User
        api_response = api_instance.create_user_organizations(user_create_request, authorization=authorization)
        print("The response of OrganizationUsersApi->create_user_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationUsersApi->create_user_organizations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_create_request** | [**UserCreateRequest**](UserCreateRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

**object**

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

# **delete_user_organizations_email**
> GenericSuccessResponse delete_user_organizations_email(user_email, authorization=authorization)

Delete User

Delete a user and revoke their API keys.

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
    api_instance = mixpeek.OrganizationUsersApi(api_client)
    user_email = 'user_email_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Delete User
        api_response = api_instance.delete_user_organizations_email(user_email, authorization=authorization)
        print("The response of OrganizationUsersApi->delete_user_organizations_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationUsersApi->delete_user_organizations_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_email** | **str**|  | 
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

# **get_user_organizations_email**
> object get_user_organizations_email(user_email, authorization=authorization)

Get User

Return a user by email address.

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
    api_instance = mixpeek.OrganizationUsersApi(api_client)
    user_email = 'user_email_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Get User
        api_response = api_instance.get_user_organizations_email(user_email, authorization=authorization)
        print("The response of OrganizationUsersApi->get_user_organizations_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationUsersApi->get_user_organizations_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_email** | **str**|  | 
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

# **list_users_organizations**
> object list_users_organizations(skip=skip, limit=limit, role=role, status=status, authorization=authorization)

List Users

List organization users with pagination and optional filters.

### Example


```python
import mixpeek
from mixpeek.models.user_role import UserRole
from mixpeek.models.user_status import UserStatus
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
    api_instance = mixpeek.OrganizationUsersApi(api_client)
    skip = 0 # int |  (optional) (default to 0)
    limit = 50 # int |  (optional) (default to 50)
    role = mixpeek.UserRole() # UserRole |  (optional)
    status = mixpeek.UserStatus() # UserStatus |  (optional)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # List Users
        api_response = api_instance.list_users_organizations(skip=skip, limit=limit, role=role, status=status, authorization=authorization)
        print("The response of OrganizationUsersApi->list_users_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationUsersApi->list_users_organizations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 50]
 **role** | [**UserRole**](.md)|  | [optional] 
 **status** | [**UserStatus**](.md)|  | [optional] 
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

# **update_user_organizations_email**
> object update_user_organizations_email(user_email, user_update_request, authorization=authorization)

Update User

Apply partial updates to an existing user.

### Example


```python
import mixpeek
from mixpeek.models.user_update_request import UserUpdateRequest
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
    api_instance = mixpeek.OrganizationUsersApi(api_client)
    user_email = 'user_email_example' # str | 
    user_update_request = mixpeek.UserUpdateRequest() # UserUpdateRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Update User
        api_response = api_instance.update_user_organizations_email(user_email, user_update_request, authorization=authorization)
        print("The response of OrganizationUsersApi->update_user_organizations_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationUsersApi->update_user_organizations_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_email** | **str**|  | 
 **user_update_request** | [**UserUpdateRequest**](UserUpdateRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

**object**

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

