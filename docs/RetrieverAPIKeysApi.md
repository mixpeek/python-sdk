# mixpeek.RetrieverAPIKeysApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_retriever_key**](RetrieverAPIKeysApi.md#create_retriever_key) | **POST** /v1/retrievers/{retriever_id}/api-keys | Create Retriever API Key
[**list_retriever_keys**](RetrieverAPIKeysApi.md#list_retriever_keys) | **GET** /v1/retrievers/{retriever_id}/api-keys | List Retriever API Keys
[**revoke_retriever_key**](RetrieverAPIKeysApi.md#revoke_retriever_key) | **DELETE** /v1/retrievers/{retriever_id}/api-keys/{key_id} | Revoke Retriever API Key


# **create_retriever_key**
> RetrieverAPIKeyResponse create_retriever_key(retriever_id, create_retriever_api_key_request, authorization=authorization, authorization2=authorization2, x_namespace=x_namespace)

Create Retriever API Key

Generate a scoped API key for executing this specific retriever.

    **Use Cases:**
    - Provide external services with execution-only access
    - Embed retriever calls in customer applications
    - Create separate keys for staging vs production
    - Implement per-customer access keys for SaaS products

    **Security:**
    - Keys grant EXECUTE_RETRIEVER permission only
    - Keys are scoped to single retriever (cannot access others)
    - Keys inherit org's rate limits
    - Keys can be revoked instantly
    - Key prefix (ret_sk_abc...) shown in UI for identification

    **Ownership:**
    - Only the organization that owns the retriever can create keys
    - Verified by matching internal_id + namespace_id

    **Key Format:**
    - Prefix: ret_sk_
    - Length: 60 characters
    - Example: ret_sk_abcdefghijklmnopqrstuvwxyz123456789...

    **Response:**
    - Plaintext key shown ONLY ONCE in response
    - Save the key immediately - it cannot be retrieved later
    - Key prefix stored for identification in UI

### Example


```python
import mixpeek
from mixpeek.models.create_retriever_api_key_request import CreateRetrieverAPIKeyRequest
from mixpeek.models.retriever_api_key_response import RetrieverAPIKeyResponse
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
    api_instance = mixpeek.RetrieverAPIKeysApi(api_client)
    retriever_id = 'retriever_id_example' # str | 
    create_retriever_api_key_request = mixpeek.CreateRetrieverAPIKeyRequest() # CreateRetrieverAPIKeyRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    authorization2 = 'authorization_example' # str |  (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Create Retriever API Key
        api_response = api_instance.create_retriever_key(retriever_id, create_retriever_api_key_request, authorization=authorization, authorization2=authorization2, x_namespace=x_namespace)
        print("The response of RetrieverAPIKeysApi->create_retriever_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrieverAPIKeysApi->create_retriever_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retriever_id** | **str**|  | 
 **create_retriever_api_key_request** | [**CreateRetrieverAPIKeyRequest**](CreateRetrieverAPIKeyRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **authorization2** | **str**|  | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**RetrieverAPIKeyResponse**](RetrieverAPIKeyResponse.md)

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
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_retriever_keys**
> RetrieverAPIKeyListResponse list_retriever_keys(retriever_id, include_revoked=include_revoked, authorization=authorization, authorization2=authorization2, x_namespace=x_namespace)

List Retriever API Keys

List all API keys for this retriever.

    **Fields:**
    - key_id: Public identifier for the key
    - key_prefix: First 10 characters + "..." for identification (e.g., "ret_sk_abc...")
    - name: Human-friendly label
    - created_at: When the key was created
    - last_used_at: When the key was last used (if ever)
    - status: ACTIVE, REVOKED, or EXPIRED
    - expires_at: Expiration timestamp (if set)

    **Note:**
    - Plaintext key is NEVER returned in list responses
    - Only shown once in creation response
    - Use key_prefix to identify keys in the UI

### Example


```python
import mixpeek
from mixpeek.models.retriever_api_key_list_response import RetrieverAPIKeyListResponse
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
    api_instance = mixpeek.RetrieverAPIKeysApi(api_client)
    retriever_id = 'retriever_id_example' # str | 
    include_revoked = False # bool | Include revoked and expired keys in the response (optional) (default to False)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    authorization2 = 'authorization_example' # str |  (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # List Retriever API Keys
        api_response = api_instance.list_retriever_keys(retriever_id, include_revoked=include_revoked, authorization=authorization, authorization2=authorization2, x_namespace=x_namespace)
        print("The response of RetrieverAPIKeysApi->list_retriever_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrieverAPIKeysApi->list_retriever_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retriever_id** | **str**|  | 
 **include_revoked** | **bool**| Include revoked and expired keys in the response | [optional] [default to False]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **authorization2** | **str**|  | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**RetrieverAPIKeyListResponse**](RetrieverAPIKeyListResponse.md)

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
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_retriever_key**
> GenericSuccessResponse revoke_retriever_key(retriever_id, key_id, authorization=authorization, authorization2=authorization2, x_namespace=x_namespace)

Revoke Retriever API Key

Revoke a retriever-scoped API key.

    **Effect:**
    - Key status is set to REVOKED
    - Key can no longer be used for authentication
    - Revocation is immediate (no grace period)
    - Auth cache is invalidated immediately
    - Cannot be undone (create a new key if needed)

    **Audit:**
    - Revocation is logged in the retriever's audit trail
    - Includes actor user ID and timestamp

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
    api_instance = mixpeek.RetrieverAPIKeysApi(api_client)
    retriever_id = 'retriever_id_example' # str | 
    key_id = 'key_id_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    authorization2 = 'authorization_example' # str |  (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Revoke Retriever API Key
        api_response = api_instance.revoke_retriever_key(retriever_id, key_id, authorization=authorization, authorization2=authorization2, x_namespace=x_namespace)
        print("The response of RetrieverAPIKeysApi->revoke_retriever_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrieverAPIKeysApi->revoke_retriever_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retriever_id** | **str**|  | 
 **key_id** | **str**|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **authorization2** | **str**|  | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

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
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

