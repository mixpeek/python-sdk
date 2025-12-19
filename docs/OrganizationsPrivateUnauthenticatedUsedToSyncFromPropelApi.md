# mixpeek.OrganizationsPrivateUnauthenticatedUsedToSyncFromPropelApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_to_organization**](OrganizationsPrivateUnauthenticatedUsedToSyncFromPropelApi.md#add_user_to_organization) | **POST** /v1/private/organizations/add-user | Add User To Organization Private
[**create_organization**](OrganizationsPrivateUnauthenticatedUsedToSyncFromPropelApi.md#create_organization) | **POST** /v1/private/organizations | Create Organization Private
[**delete_organization**](OrganizationsPrivateUnauthenticatedUsedToSyncFromPropelApi.md#delete_organization) | **DELETE** /v1/private/organizations/{organization_identifier} | Delete Organization Private
[**get_organization**](OrganizationsPrivateUnauthenticatedUsedToSyncFromPropelApi.md#get_organization) | **GET** /v1/private/organizations/{organization_identifier} | Get Organization Private
[**update_organization**](OrganizationsPrivateUnauthenticatedUsedToSyncFromPropelApi.md#update_organization) | **PATCH** /v1/private/organizations/{organization_identifier} | Update Organization Private


# **add_user_to_organization**
> OrganizationModelResponse add_user_to_organization(add_user_to_organization_request)

Add User To Organization Private

Add a user to a private organization.

### Example


```python
import mixpeek
from mixpeek.models.add_user_to_organization_request import AddUserToOrganizationRequest
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
    api_instance = mixpeek.OrganizationsPrivateUnauthenticatedUsedToSyncFromPropelApi(api_client)
    add_user_to_organization_request = mixpeek.AddUserToOrganizationRequest() # AddUserToOrganizationRequest | 

    try:
        # Add User To Organization Private
        api_response = api_instance.add_user_to_organization(add_user_to_organization_request)
        print("The response of OrganizationsPrivateUnauthenticatedUsedToSyncFromPropelApi->add_user_to_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsPrivateUnauthenticatedUsedToSyncFromPropelApi->add_user_to_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_user_to_organization_request** | [**AddUserToOrganizationRequest**](AddUserToOrganizationRequest.md)|  | 

### Return type

[**OrganizationModelResponse**](OrganizationModelResponse.md)

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

# **create_organization**
> OrganizationModelResponse create_organization(create_organization_request)

Create Organization Private

Create a new private organization.

### Example


```python
import mixpeek
from mixpeek.models.create_organization_request import CreateOrganizationRequest
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
    api_instance = mixpeek.OrganizationsPrivateUnauthenticatedUsedToSyncFromPropelApi(api_client)
    create_organization_request = mixpeek.CreateOrganizationRequest() # CreateOrganizationRequest | 

    try:
        # Create Organization Private
        api_response = api_instance.create_organization(create_organization_request)
        print("The response of OrganizationsPrivateUnauthenticatedUsedToSyncFromPropelApi->create_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsPrivateUnauthenticatedUsedToSyncFromPropelApi->create_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_organization_request** | [**CreateOrganizationRequest**](CreateOrganizationRequest.md)|  | 

### Return type

[**OrganizationModelResponse**](OrganizationModelResponse.md)

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

# **delete_organization**
> GenericDeleteResponse delete_organization(organization_identifier)

Delete Organization Private

Delete a private organization.

### Example


```python
import mixpeek
from mixpeek.models.generic_delete_response import GenericDeleteResponse
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
    api_instance = mixpeek.OrganizationsPrivateUnauthenticatedUsedToSyncFromPropelApi(api_client)
    organization_identifier = 'organization_identifier_example' # str | 

    try:
        # Delete Organization Private
        api_response = api_instance.delete_organization(organization_identifier)
        print("The response of OrganizationsPrivateUnauthenticatedUsedToSyncFromPropelApi->delete_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsPrivateUnauthenticatedUsedToSyncFromPropelApi->delete_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_identifier** | **str**|  | 

### Return type

[**GenericDeleteResponse**](GenericDeleteResponse.md)

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
> OrganizationModelResponse get_organization(organization_identifier)

Get Organization Private

Get a private organization by ID or name.

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
    api_instance = mixpeek.OrganizationsPrivateUnauthenticatedUsedToSyncFromPropelApi(api_client)
    organization_identifier = 'organization_identifier_example' # str | 

    try:
        # Get Organization Private
        api_response = api_instance.get_organization(organization_identifier)
        print("The response of OrganizationsPrivateUnauthenticatedUsedToSyncFromPropelApi->get_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsPrivateUnauthenticatedUsedToSyncFromPropelApi->get_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_identifier** | **str**|  | 

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

# **update_organization**
> OrganizationModelResponse update_organization(organization_identifier, organization_admin_update_request)

Update Organization Private

Admin-only: update organization tier and/or rate limits.

### Example


```python
import mixpeek
from mixpeek.models.organization_admin_update_request import OrganizationAdminUpdateRequest
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
    api_instance = mixpeek.OrganizationsPrivateUnauthenticatedUsedToSyncFromPropelApi(api_client)
    organization_identifier = 'organization_identifier_example' # str | 
    organization_admin_update_request = mixpeek.OrganizationAdminUpdateRequest() # OrganizationAdminUpdateRequest | 

    try:
        # Update Organization Private
        api_response = api_instance.update_organization(organization_identifier, organization_admin_update_request)
        print("The response of OrganizationsPrivateUnauthenticatedUsedToSyncFromPropelApi->update_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsPrivateUnauthenticatedUsedToSyncFromPropelApi->update_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_identifier** | **str**|  | 
 **organization_admin_update_request** | [**OrganizationAdminUpdateRequest**](OrganizationAdminUpdateRequest.md)|  | 

### Return type

[**OrganizationModelResponse**](OrganizationModelResponse.md)

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

