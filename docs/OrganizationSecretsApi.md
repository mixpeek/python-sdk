# mixpeek.OrganizationSecretsApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_secret_organizations**](OrganizationSecretsApi.md#create_secret_organizations) | **POST** /v1/organizations/secrets | Create Secret
[**delete_secret_organizations_name**](OrganizationSecretsApi.md#delete_secret_organizations_name) | **DELETE** /v1/organizations/secrets/{secret_name} | Delete Secret
[**list_secrets_organizations**](OrganizationSecretsApi.md#list_secrets_organizations) | **GET** /v1/organizations/secrets | List Secrets
[**update_secret_organizations_name**](OrganizationSecretsApi.md#update_secret_organizations_name) | **PUT** /v1/organizations/secrets/{secret_name} | Update Secret


# **create_secret_organizations**
> SecretResponse create_secret_organizations(create_secret_request, authorization=authorization)

Create Secret

Create a new secret in organization vault.

**Security**:
- Secret value is encrypted at rest using Fernet encryption
- Encrypted using ENCRYPTION_KEY from environment
- Decrypted value is NEVER returned in API responses
- Only secret names are exposed in list operations

**Use Cases**:
- Store API keys for external services (Stripe, GitHub, etc.)
- Store authentication tokens for api_call retriever stage
- Store credentials for third-party integrations

**Important**:
- Secret names must be unique within organization
- Use update endpoint to modify existing secrets
- Delete and recreate if you forget the value

### Example


```python
import mixpeek
from mixpeek.models.create_secret_request import CreateSecretRequest
from mixpeek.models.secret_response import SecretResponse
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
    api_instance = mixpeek.OrganizationSecretsApi(api_client)
    create_secret_request = mixpeek.CreateSecretRequest() # CreateSecretRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Create Secret
        api_response = api_instance.create_secret_organizations(create_secret_request, authorization=authorization)
        print("The response of OrganizationSecretsApi->create_secret_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationSecretsApi->create_secret_organizations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_secret_request** | [**CreateSecretRequest**](CreateSecretRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**SecretResponse**](SecretResponse.md)

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

# **delete_secret_organizations_name**
> SecretResponse delete_secret_organizations_name(secret_name, authorization=authorization)

Delete Secret

Delete a secret from organization vault.

**Warning**:
- Deletion is permanent and immediate
- Any api_call stages using this secret will fail
- No confirmation prompt - use with caution

**Use Cases**:
- Remove unused credentials
- Clean up after service decommissioning
- Security incident response

### Example


```python
import mixpeek
from mixpeek.models.secret_response import SecretResponse
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
    api_instance = mixpeek.OrganizationSecretsApi(api_client)
    secret_name = 'secret_name_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Delete Secret
        api_response = api_instance.delete_secret_organizations_name(secret_name, authorization=authorization)
        print("The response of OrganizationSecretsApi->delete_secret_organizations_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationSecretsApi->delete_secret_organizations_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_name** | **str**|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**SecretResponse**](SecretResponse.md)

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

# **list_secrets_organizations**
> SecretsListResponse list_secrets_organizations(authorization=authorization)

List Secrets

List all secret names in organization vault.

**Security**:
- Returns ONLY secret names, never values
- Use for discovering which secrets are configured
- Secret values can only be retrieved by internal services

**Response**:
- List of secret names (e.g., ['stripe_api_key', 'github_token'])
- Total count of secrets

### Example


```python
import mixpeek
from mixpeek.models.secrets_list_response import SecretsListResponse
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
    api_instance = mixpeek.OrganizationSecretsApi(api_client)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # List Secrets
        api_response = api_instance.list_secrets_organizations(authorization=authorization)
        print("The response of OrganizationSecretsApi->list_secrets_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationSecretsApi->list_secrets_organizations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**SecretsListResponse**](SecretsListResponse.md)

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

# **update_secret_organizations_name**
> SecretResponse update_secret_organizations_name(secret_name, update_secret_request, authorization=authorization)

Update Secret

Update an existing secret in organization vault.

**Security**:
- Replaces existing encrypted value with new encrypted value
- Old value is permanently overwritten
- No history or audit trail of previous values

**Use Cases**:
- Rotate API keys periodically
- Update expired tokens
- Change credentials after security incident

### Example


```python
import mixpeek
from mixpeek.models.secret_response import SecretResponse
from mixpeek.models.update_secret_request import UpdateSecretRequest
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
    api_instance = mixpeek.OrganizationSecretsApi(api_client)
    secret_name = 'secret_name_example' # str | 
    update_secret_request = mixpeek.UpdateSecretRequest() # UpdateSecretRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Update Secret
        api_response = api_instance.update_secret_organizations_name(secret_name, update_secret_request, authorization=authorization)
        print("The response of OrganizationSecretsApi->update_secret_organizations_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationSecretsApi->update_secret_organizations_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_name** | **str**|  | 
 **update_secret_request** | [**UpdateSecretRequest**](UpdateSecretRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**SecretResponse**](SecretResponse.md)

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

