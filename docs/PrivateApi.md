# mixpeek.PrivateApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_to_organization**](PrivateApi.md#add_user_to_organization) | **POST** /v1/private/organizations/add-user | Add User To Organization Private
[**configure_storage_cors_configurations**](PrivateApi.md#configure_storage_cors_configurations) | **POST** /v1/private/configurations/storage/cors | Configure CORS for Object Storage
[**create_bootstrap_key_organizations_id_users_email**](PrivateApi.md#create_bootstrap_key_organizations_id_users_email) | **POST** /v1/private/organizations/{organization_id}/users/{user_email}/bootstrap-key | Create Bootstrap Api Key
[**create_organization**](PrivateApi.md#create_organization) | **POST** /v1/private/organizations | Create Organization Private
[**delete_organization**](PrivateApi.md#delete_organization) | **DELETE** /v1/private/organizations/{organization_identifier} | Delete Organization Private
[**diagnose_clickhouse_configurations_diagnostics**](PrivateApi.md#diagnose_clickhouse_configurations_diagnostics) | **GET** /v1/private/configurations/clickhouse/diagnostics | Diagnose ClickHouse Configuration
[**get_organization**](PrivateApi.md#get_organization) | **GET** /v1/private/organizations/{organization_identifier} | Get Organization Private
[**get_storage_cors_configurations**](PrivateApi.md#get_storage_cors_configurations) | **GET** /v1/private/configurations/storage/cors | Get Current CORS Configuration
[**trigger_next_tier_internal_batches_batch_id_num**](PrivateApi.md#trigger_next_tier_internal_batches_batch_id_num) | **POST** /v1/internal/batches/{batch_id}/trigger-tier/{tier_num} | Trigger next tier processing (Internal - Engine callback)
[**update_organization**](PrivateApi.md#update_organization) | **PATCH** /v1/private/organizations/{organization_identifier} | Update Organization Private


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
    api_instance = mixpeek.PrivateApi(api_client)
    add_user_to_organization_request = mixpeek.AddUserToOrganizationRequest() # AddUserToOrganizationRequest | 

    try:
        # Add User To Organization Private
        api_response = api_instance.add_user_to_organization(add_user_to_organization_request)
        print("The response of PrivateApi->add_user_to_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateApi->add_user_to_organization: %s\n" % e)
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

# **configure_storage_cors_configurations**
> CORSConfigurationResponse configure_storage_cors_configurations(configure_cors_request)

Configure CORS for Object Storage

Configure CORS (Cross-Origin Resource Sharing) on the object storage bucket.

    **Why is this needed?**
    When using presigned URLs for browser-based uploads, browsers enforce CORS policies.
    Without proper CORS configuration, uploads from the frontend will fail with CORS errors.

    **When to use this:**
    - During initial setup of the Mixpeek platform
    - When adding new frontend domains (development, staging, production)
    - When troubleshooting browser upload failures

    **Important notes:**
    - This is an admin-only operation (requires admin API key)
    - CORS is configured on the entire object storage bucket (not per-namespace)
    - Changes take effect immediately but may be cached by browsers
    - This works for any object storage provider (S3, LocalStack, GCS)

    **Common use cases:**
    1. Local development: Configure localhost origins
    2. Production: Configure production domain origins
    3. Multi-environment: Configure multiple origins for dev/staging/prod

### Example


```python
import mixpeek
from mixpeek.models.cors_configuration_response import CORSConfigurationResponse
from mixpeek.models.configure_cors_request import ConfigureCORSRequest
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
    api_instance = mixpeek.PrivateApi(api_client)
    configure_cors_request = mixpeek.ConfigureCORSRequest() # ConfigureCORSRequest | 

    try:
        # Configure CORS for Object Storage
        api_response = api_instance.configure_storage_cors_configurations(configure_cors_request)
        print("The response of PrivateApi->configure_storage_cors_configurations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateApi->configure_storage_cors_configurations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configure_cors_request** | [**ConfigureCORSRequest**](ConfigureCORSRequest.md)|  | 

### Return type

[**CORSConfigurationResponse**](CORSConfigurationResponse.md)

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

# **create_bootstrap_key_organizations_id_users_email**
> Dict[str, object] create_bootstrap_key_organizations_id_users_email(organization_id, user_email)

Create Bootstrap Api Key

Create the organization's primary API key (requires MIXPEEK_PRIVATE_KEY).

🔑 IMPORTANT - Two Different Keys (DO NOT CONFUSE):

1. MIXPEEK_PRIVATE_KEY (what you use to call THIS endpoint):
   - Static, hardcoded token shared between studio proxy and backend
   - Used ONLY for server-to-server /v1/private/* endpoint calls
   - Never changes, never stored in database
   - Never used by frontend UI
   - Example: xnefritAiaKQiddNL3ZHWEN4cHWLsCkwEycUDLU2wLekQEuf

2. Organization API Key (what THIS endpoint creates and returns):
   - Created ONCE per organization with ADMIN permissions
   - Used by frontend UI for ALL /v1/* API calls
   - Named "admin-key" and stored in database (hashed)
   - Plaintext returned ONCE on creation
   - 🔒 PROTECTED: Users CANNOT delete, rotate, or change permissions on this key
   - Example: sk_kbHvXHAySDUrzrPo2ajwmqBAXJ...

This endpoint creates an Organization API key (type #2) that the frontend will use.
It does NOT create, modify, or touch the MIXPEEK_PRIVATE_KEY (type #1).

⚠️ The plaintext key is only returned ONCE on creation - store it in localStorage!
✅ If called when key exists: Revokes old key and returns a new one (idempotent)

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
    api_instance = mixpeek.PrivateApi(api_client)
    organization_id = 'organization_id_example' # str | 
    user_email = 'user_email_example' # str | 

    try:
        # Create Bootstrap Api Key
        api_response = api_instance.create_bootstrap_key_organizations_id_users_email(organization_id, user_email)
        print("The response of PrivateApi->create_bootstrap_key_organizations_id_users_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateApi->create_bootstrap_key_organizations_id_users_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 
 **user_email** | **str**|  | 

### Return type

**Dict[str, object]**

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
    api_instance = mixpeek.PrivateApi(api_client)
    create_organization_request = mixpeek.CreateOrganizationRequest() # CreateOrganizationRequest | 

    try:
        # Create Organization Private
        api_response = api_instance.create_organization(create_organization_request)
        print("The response of PrivateApi->create_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateApi->create_organization: %s\n" % e)
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
    api_instance = mixpeek.PrivateApi(api_client)
    organization_identifier = 'organization_identifier_example' # str | 

    try:
        # Delete Organization Private
        api_response = api_instance.delete_organization(organization_identifier)
        print("The response of PrivateApi->delete_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateApi->delete_organization: %s\n" % e)
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

# **diagnose_clickhouse_configurations_diagnostics**
> object diagnose_clickhouse_configurations_diagnostics()

Diagnose ClickHouse Configuration

Run diagnostics on ClickHouse to check version, settings, and data type behavior.

    This is useful for:
    - Debugging differences between local and production environments
    - Verifying ClickHouse configuration
    - Checking if COUNT() returns strings or integers

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
    api_instance = mixpeek.PrivateApi(api_client)

    try:
        # Diagnose ClickHouse Configuration
        api_response = api_instance.diagnose_clickhouse_configurations_diagnostics()
        print("The response of PrivateApi->diagnose_clickhouse_configurations_diagnostics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateApi->diagnose_clickhouse_configurations_diagnostics: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
    api_instance = mixpeek.PrivateApi(api_client)
    organization_identifier = 'organization_identifier_example' # str | 

    try:
        # Get Organization Private
        api_response = api_instance.get_organization(organization_identifier)
        print("The response of PrivateApi->get_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateApi->get_organization: %s\n" % e)
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

# **get_storage_cors_configurations**
> CORSConfigurationInfo get_storage_cors_configurations()

Get Current CORS Configuration

Retrieve the current CORS configuration for the object storage bucket.

    **Use this to:**
    - Verify CORS is properly configured
    - Check which origins are currently allowed
    - Troubleshoot CORS-related issues
    - Audit current security settings

### Example


```python
import mixpeek
from mixpeek.models.cors_configuration_info import CORSConfigurationInfo
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
    api_instance = mixpeek.PrivateApi(api_client)

    try:
        # Get Current CORS Configuration
        api_response = api_instance.get_storage_cors_configurations()
        print("The response of PrivateApi->get_storage_cors_configurations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateApi->get_storage_cors_configurations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CORSConfigurationInfo**](CORSConfigurationInfo.md)

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

# **trigger_next_tier_internal_batches_batch_id_num**
> object trigger_next_tier_internal_batches_batch_id_num(batch_id, tier_num, trigger_tier_request, authorization=authorization)

Trigger next tier processing (Internal - Engine callback)

Called by Engine/BatchPoller when a tier completes to trigger next tier

### Example


```python
import mixpeek
from mixpeek.models.trigger_tier_request import TriggerTierRequest
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
    api_instance = mixpeek.PrivateApi(api_client)
    batch_id = 'batch_id_example' # str | 
    tier_num = 56 # int | 
    trigger_tier_request = mixpeek.TriggerTierRequest() # TriggerTierRequest | 
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Trigger next tier processing (Internal - Engine callback)
        api_response = api_instance.trigger_next_tier_internal_batches_batch_id_num(batch_id, tier_num, trigger_tier_request, authorization=authorization)
        print("The response of PrivateApi->trigger_next_tier_internal_batches_batch_id_num:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateApi->trigger_next_tier_internal_batches_batch_id_num: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_id** | **str**|  | 
 **tier_num** | **int**|  | 
 **trigger_tier_request** | [**TriggerTierRequest**](TriggerTierRequest.md)|  | 
 **authorization** | **str**|  | [optional] 

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

# **update_organization**
> OrganizationModelResponse update_organization(organization_identifier, organization_admin_update_request)

Update Organization Private

Admin-only: update organization tier, rate limits, and infrastructure.

Security: This endpoint is ONLY accessible with MIXPEEK_PRIVATE_TOKEN.
It allows updating infrastructure configuration (Qdrant/Ray URLs) for ENTERPRISE customers.

Infrastructure updates require Mixpeek admin privileges and are logged for audit.

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
    api_instance = mixpeek.PrivateApi(api_client)
    organization_identifier = 'organization_identifier_example' # str | 
    organization_admin_update_request = mixpeek.OrganizationAdminUpdateRequest() # OrganizationAdminUpdateRequest | 

    try:
        # Update Organization Private
        api_response = api_instance.update_organization(organization_identifier, organization_admin_update_request)
        print("The response of PrivateApi->update_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateApi->update_organization: %s\n" % e)
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

