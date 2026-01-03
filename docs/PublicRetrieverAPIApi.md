# mixpeek.PublicRetrieverAPIApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_retriever_name**](PublicRetrieverAPIApi.md#execute_retriever_name) | **POST** /v1/public/retrievers/{public_name}/execute | Execute Public Retriever
[**get_retriever_config_name**](PublicRetrieverAPIApi.md#get_retriever_config_name) | **GET** /v1/public/retrievers/{public_name}/config | Get Public Retriever Config
[**get_retriever_template_name**](PublicRetrieverAPIApi.md#get_retriever_template_name) | **GET** /v1/public/retrievers/{public_name}/template | Get Public Retriever Template
[**list_retrievers**](PublicRetrieverAPIApi.md#list_retrievers) | **GET** /v1/public/retrievers/ | List Public Retrievers
[**track_interaction_batch_retrievers_name**](PublicRetrieverAPIApi.md#track_interaction_batch_retrievers_name) | **POST** /v1/public/retrievers/{public_name}/interactions/batch | Track Interaction Batch
[**track_interaction_retrievers_name**](PublicRetrieverAPIApi.md#track_interaction_retrievers_name) | **POST** /v1/public/retrievers/{public_name}/interactions | Track Interaction
[**verify_password_retrievers_name**](PublicRetrieverAPIApi.md#verify_password_retrievers_name) | **POST** /v1/public/retrievers/{public_name}/verify | Verify Password


# **execute_retriever_name**
> object execute_retriever_name(public_name, x_public_api_key, retriever_execution_request, return_presigned_urls=return_presigned_urls, x_retriever_password=x_retriever_password)

Execute Public Retriever

Execute a published retriever (public endpoint).

**Authentication:**
- Requires `X-Public-API-Key` header with the retriever's public API key
- If password-protected, also requires `X-Retriever-Password` header

**Rate Limiting:**
- Subject to per-retriever rate limits (per minute/hour/day)
- May also have IP-based rate limits

**Response:**
- Only returns fields specified in `exposed_fields` configuration
- Internal metadata is stripped from results
- Includes `execution_id` for interaction tracking
- Presigned URLs returned by default (return_presigned_urls=true) for media rendering

**Example:**
```bash
curl -X POST "https://api.mixpeek.com/v1/public/retrievers/video-search/execute" \
  -H "X-Public-API-Key: prk_abc123..." \
  -H "Content-Type: application/json" \
  -d '{
    "inputs": {"query": "red car"},
    "pagination": {"method": "offset", "page_number": 1, "page_size": 10}
  }'
```

**Example with return_presigned_urls disabled:**
```bash
curl -X POST "https://api.mixpeek.com/v1/public/retrievers/video-search/execute?return_presigned_urls=false" \
  -H "X-Public-API-Key: prk_abc123..." \
  -H "Content-Type: application/json" \
  -d '{
    "inputs": {"query": "red car"},
    "pagination": {"method": "offset", "page_number": 1, "page_size": 10}
  }'
```

### Example


```python
import mixpeek
from mixpeek.models.retriever_execution_request import RetrieverExecutionRequest
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
    api_instance = mixpeek.PublicRetrieverAPIApi(api_client)
    public_name = 'public_name_example' # str | Public name of the published retriever
    x_public_api_key = 'x_public_api_key_example' # str | 
    retriever_execution_request = mixpeek.RetrieverExecutionRequest() # RetrieverExecutionRequest | 
    return_presigned_urls = True # bool | Generate fresh presigned download URLs for all blobs with S3 storage. Default: True for public retrievers to enable media rendering. Set to False if you only need metadata without URLs. (optional) (default to True)
    x_retriever_password = 'x_retriever_password_example' # str |  (optional)

    try:
        # Execute Public Retriever
        api_response = api_instance.execute_retriever_name(public_name, x_public_api_key, retriever_execution_request, return_presigned_urls=return_presigned_urls, x_retriever_password=x_retriever_password)
        print("The response of PublicRetrieverAPIApi->execute_retriever_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicRetrieverAPIApi->execute_retriever_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_name** | **str**| Public name of the published retriever | 
 **x_public_api_key** | **str**|  | 
 **retriever_execution_request** | [**RetrieverExecutionRequest**](RetrieverExecutionRequest.md)|  | 
 **return_presigned_urls** | **bool**| Generate fresh presigned download URLs for all blobs with S3 storage. Default: True for public retrievers to enable media rendering. Set to False if you only need metadata without URLs. | [optional] [default to True]
 **x_retriever_password** | **str**|  | [optional] 

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

# **get_retriever_config_name**
> PublicRetrieverConfigResponse get_retriever_config_name(public_name)

Get Public Retriever Config

Get display configuration for public page rendering.

Returns the UI configuration needed to render the public search interface.
Used by the frontend app at apps.mixpeek.com to dynamically build the UI.

**Authentication:**
- NO authentication required - this endpoint is public
- Anyone can access the config if they know the public_name
- The config includes the public_api_key needed for execute/interact endpoints

**Response includes:**
- Display config (logo, theme, components, field rendering)
- Title and description
- Password protection status
- Public API key for subsequent authenticated requests

**Example:**
```bash
curl -X GET "https://api.mixpeek.com/v1/public/retrievers/video-search/config"
```

### Example


```python
import mixpeek
from mixpeek.models.public_retriever_config_response import PublicRetrieverConfigResponse
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
    api_instance = mixpeek.PublicRetrieverAPIApi(api_client)
    public_name = 'public_name_example' # str | Public name of the published retriever

    try:
        # Get Public Retriever Config
        api_response = api_instance.get_retriever_config_name(public_name)
        print("The response of PublicRetrieverAPIApi->get_retriever_config_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicRetrieverAPIApi->get_retriever_config_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_name** | **str**| Public name of the published retriever | 

### Return type

[**PublicRetrieverConfigResponse**](PublicRetrieverConfigResponse.md)

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

# **get_retriever_template_name**
> PublicRetrieverTemplateResponse get_retriever_template_name(public_name)

Get Public Retriever Template

Get retriever configuration as a reusable template.

Returns the published retriever's configuration in a format that can be
directly used to create your own retriever. This is perfect for discovering
patterns and adapting them to your own data.

**Authentication:**
- NO authentication required - this endpoint is completely public
- Anyone can get the template if they know the public_name

**Use Case:**
1. Browse public retrievers to find patterns you like
2. GET this endpoint to get the full configuration
3. Copy the config and modify for your needs (especially `collection_identifiers`)
4. POST to `/v1/retrievers` to create your own retriever
5. Optionally publish it with the same display_config

**What's included:**
- Retriever configuration (stages, input_schema, budget_limits)
- Display configuration (for publishing with similar UI)
- Original metadata for reference

**What you need to change:**
- `collection_identifiers`: Replace with your own collection IDs
- `retriever_name`: Give it a unique name
- Optionally modify stages, inputs, display_config as needed

**Example:**
```bash
# 1. Get the template
curl -X GET "https://api.mixpeek.com/v1/public/retrievers/video-search/template"

# 2. Modify the response and create your own retriever
curl -X POST "https://api.mixpeek.com/v1/retrievers" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "retriever_name": "my_video_search",
    "collection_identifiers": ["my_videos"],
    "stages": [...],  # From template
    "input_schema": {...},  # From template
    "budget_limits": {...},  # From template
    "display_config": {...}  # From template (optional)
  }'
```

**Response includes:**
- All retriever configuration fields
- Display config for publishing (optional to use)
- Source reference (where this template came from)

### Example


```python
import mixpeek
from mixpeek.models.public_retriever_template_response import PublicRetrieverTemplateResponse
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
    api_instance = mixpeek.PublicRetrieverAPIApi(api_client)
    public_name = 'public_name_example' # str | Public name of the published retriever

    try:
        # Get Public Retriever Template
        api_response = api_instance.get_retriever_template_name(public_name)
        print("The response of PublicRetrieverAPIApi->get_retriever_template_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicRetrieverAPIApi->get_retriever_template_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_name** | **str**| Public name of the published retriever | 

### Return type

[**PublicRetrieverTemplateResponse**](PublicRetrieverTemplateResponse.md)

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

# **list_retrievers**
> ListPublicRetrieversResponse list_retrievers(page=page, page_size=page_size, include_inactive=include_inactive, search=search)

List Public Retrievers

List all public retrievers with pagination and search.

This endpoint allows browsing and discovering all published retrievers
across all organizations. No authentication required.

**Authentication:**
- NO authentication required - completely public endpoint
- Discover retrievers created by all Mixpeek users

**Pagination:**
- Default: page=1, page_size=20
- Maximum page_size: 100
- Returns total count and total pages

**Search:**
- Search across retriever titles and descriptions
- Case-insensitive regex matching
- Combine with pagination

**Filtering:**
- By default, only active retrievers are shown
- Set `include_inactive=true` to see all retrievers

**Response includes:**
- List of public retrievers with basic info
- Pagination details (page, page_size, total_count, total_pages)
- Aggregate statistics (total active, password protected, open)

**What's NOT exposed:**
- API keys (except in individual config endpoint)
- Internal IDs or organization details
- Full retriever configuration (use template endpoint for that)
- Password values (only password_protected: true/false)

**Example:**
```bash
# List all public retrievers (first page)
curl -X GET "https://api.mixpeek.com/v1/public/retrievers/"

# Search for video-related retrievers
curl -X GET "https://api.mixpeek.com/v1/public/retrievers/?search=video&page_size=50"

# Get page 2 with custom page size
curl -X GET "https://api.mixpeek.com/v1/public/retrievers/?page=2&page_size=50"
```

**Use Cases:**
- Browse available public retrievers
- Discover search patterns and implementations
- Find retrievers to use as templates
- Explore what others have built

### Example


```python
import mixpeek
from mixpeek.models.list_public_retrievers_response import ListPublicRetrieversResponse
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
    api_instance = mixpeek.PublicRetrieverAPIApi(api_client)
    page = 1 # int | Page number (1-indexed) (optional) (default to 1)
    page_size = 20 # int | Results per page (optional) (default to 20)
    include_inactive = False # bool | Include inactive retrievers in results (optional) (default to False)
    search = 'search_example' # str | Search query for filtering by title or description (optional)

    try:
        # List Public Retrievers
        api_response = api_instance.list_retrievers(page=page, page_size=page_size, include_inactive=include_inactive, search=search)
        print("The response of PublicRetrieverAPIApi->list_retrievers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicRetrieverAPIApi->list_retrievers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number (1-indexed) | [optional] [default to 1]
 **page_size** | **int**| Results per page | [optional] [default to 20]
 **include_inactive** | **bool**| Include inactive retrievers in results | [optional] [default to False]
 **search** | **str**| Search query for filtering by title or description | [optional] 

### Return type

[**ListPublicRetrieversResponse**](ListPublicRetrieversResponse.md)

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

# **track_interaction_batch_retrievers_name**
> object track_interaction_batch_retrievers_name(public_name, x_public_api_key, public_interaction_batch_request, x_session_id=x_session_id)

Track Interaction Batch

Track multiple interactions in a single request (batching).

More efficient than sending individual interaction requests.
Use this for batching viewport visibility, bulk actions, etc.

**Authentication:**
- Requires `X-Public-API-Key` header
- Password NOT required (tracking should work even without auth)

**Recommended Headers:**
- `X-Session-ID`: Applied to all interactions in the batch

**Limits:**
- Maximum 100 interactions per batch

**Example:**
```bash
curl -X POST "https://api.mixpeek.com/v1/public/retrievers/video-search/interactions/batch" \
  -H "X-Public-API-Key: prk_abc123..." \
  -H "X-Session-ID: sess_xyz..." \
  -H "Content-Type: application/json" \
  -d '{
    "interactions": [
      {
        "document_id": "doc_123",
        "interaction_type": ["VIEW"],
        "position": 0,
        "execution_id": "exec_abc"
      },
      {
        "document_id": "doc_456",
        "interaction_type": ["VIEW"],
        "position": 1,
        "execution_id": "exec_abc"
      }
    ]
  }'
```

### Example


```python
import mixpeek
from mixpeek.models.public_interaction_batch_request import PublicInteractionBatchRequest
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
    api_instance = mixpeek.PublicRetrieverAPIApi(api_client)
    public_name = 'public_name_example' # str | Public name of the published retriever
    x_public_api_key = 'x_public_api_key_example' # str | 
    public_interaction_batch_request = mixpeek.PublicInteractionBatchRequest() # PublicInteractionBatchRequest | 
    x_session_id = 'x_session_id_example' # str |  (optional)

    try:
        # Track Interaction Batch
        api_response = api_instance.track_interaction_batch_retrievers_name(public_name, x_public_api_key, public_interaction_batch_request, x_session_id=x_session_id)
        print("The response of PublicRetrieverAPIApi->track_interaction_batch_retrievers_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicRetrieverAPIApi->track_interaction_batch_retrievers_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_name** | **str**| Public name of the published retriever | 
 **x_public_api_key** | **str**|  | 
 **public_interaction_batch_request** | [**PublicInteractionBatchRequest**](PublicInteractionBatchRequest.md)|  | 
 **x_session_id** | **str**|  | [optional] 

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

# **track_interaction_retrievers_name**
> object track_interaction_retrievers_name(public_name, x_public_api_key, public_interaction_request, x_session_id=x_session_id)

Track Interaction

Track user interaction with search results.

Records user engagement (clicks, views, etc.) for analytics and
potential search optimization (Learning to Rank).

**Authentication:**
- Requires `X-Public-API-Key` header
- Password NOT required (tracking should work even without auth)

**Recommended Headers:**
- `X-Session-ID`: Session identifier for tracking user journey

**Interaction Types:**
- `VIEW`: Result was visible in viewport
- `CLICK`: User clicked on result
- `POSITIVE_FEEDBACK`: User explicitly liked result
- `NEGATIVE_FEEDBACK`: User explicitly disliked result
- `PURCHASE`: User purchased/converted
- `ADD_TO_CART`: User added to cart
- `WISHLIST`: User added to wishlist
- `LONG_VIEW`: User spent significant time viewing
- `SHARE`: User shared result
- `BOOKMARK`: User bookmarked result

**Example:**
```bash
curl -X POST "https://api.mixpeek.com/v1/public/retrievers/video-search/interactions" \
  -H "X-Public-API-Key: prk_abc123..." \
  -H "X-Session-ID: sess_xyz..." \
  -H "Content-Type: application/json" \
  -d '{
    "document_id": "doc_123",
    "interaction_type": ["CLICK"],
    "position": 2,
    "execution_id": "exec_abc",
    "query_snapshot": {"query": "red car"}
  }'
```

### Example


```python
import mixpeek
from mixpeek.models.public_interaction_request import PublicInteractionRequest
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
    api_instance = mixpeek.PublicRetrieverAPIApi(api_client)
    public_name = 'public_name_example' # str | Public name of the published retriever
    x_public_api_key = 'x_public_api_key_example' # str | 
    public_interaction_request = mixpeek.PublicInteractionRequest() # PublicInteractionRequest | 
    x_session_id = 'x_session_id_example' # str |  (optional)

    try:
        # Track Interaction
        api_response = api_instance.track_interaction_retrievers_name(public_name, x_public_api_key, public_interaction_request, x_session_id=x_session_id)
        print("The response of PublicRetrieverAPIApi->track_interaction_retrievers_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicRetrieverAPIApi->track_interaction_retrievers_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_name** | **str**| Public name of the published retriever | 
 **x_public_api_key** | **str**|  | 
 **public_interaction_request** | [**PublicInteractionRequest**](PublicInteractionRequest.md)|  | 
 **x_session_id** | **str**|  | [optional] 

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

# **verify_password_retrievers_name**
> VerifyPasswordResponse verify_password_retrievers_name(public_name, verify_password_request)

Verify Password

Verify password for a password-protected retriever.

Allows the frontend to check if a password is valid before attempting to execute
a password-protected retriever. Returns the public API key if the password is valid.

**Authentication:**
- NO authentication required - this endpoint is public
- The password is verified against the retriever's configured password

**Use Case:**
1. Frontend detects that a retriever is password-protected (from /config endpoint)
2. User enters password in the UI
3. Frontend calls this endpoint to verify the password
4. If valid, frontend receives the public_api_key to use for subsequent requests

**Response:**
- `valid`: Whether the password is correct
- `public_api_key`: The API key to use for execute/interact endpoints (only if valid)

**Example:**
```bash
curl -X POST "https://api.mixpeek.com/v1/public/retrievers/private-search/verify" \
  -H "Content-Type: application/json" \
  -d '{"password": "secret123"}'
```

**Response if valid:**
```json
{
  "valid": true,
  "public_api_key": "prk_abc123..."
}
```

**Response if invalid:**
```json
{
  "valid": false,
  "public_api_key": null
}
```

### Example


```python
import mixpeek
from mixpeek.models.verify_password_request import VerifyPasswordRequest
from mixpeek.models.verify_password_response import VerifyPasswordResponse
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
    api_instance = mixpeek.PublicRetrieverAPIApi(api_client)
    public_name = 'public_name_example' # str | Public name of the published retriever
    verify_password_request = mixpeek.VerifyPasswordRequest() # VerifyPasswordRequest | 

    try:
        # Verify Password
        api_response = api_instance.verify_password_retrievers_name(public_name, verify_password_request)
        print("The response of PublicRetrieverAPIApi->verify_password_retrievers_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicRetrieverAPIApi->verify_password_retrievers_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_name** | **str**| Public name of the published retriever | 
 **verify_password_request** | [**VerifyPasswordRequest**](VerifyPasswordRequest.md)|  | 

### Return type

[**VerifyPasswordResponse**](VerifyPasswordResponse.md)

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

