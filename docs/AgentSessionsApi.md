# mixpeek.AgentSessionsApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_session_agents**](AgentSessionsApi.md#create_session_agents) | **POST** /v1/agents/sessions | Create Session
[**detect_intent_agents_sessions**](AgentSessionsApi.md#detect_intent_agents_sessions) | **POST** /v1/agents/sessions/intent/detect | Detect Intent
[**get_history_agents_sessions**](AgentSessionsApi.md#get_history_agents_sessions) | **GET** /v1/agents/sessions/{session_id}/history | Get History
[**get_session_agents**](AgentSessionsApi.md#get_session_agents) | **GET** /v1/agents/sessions/{session_id} | Get Session
[**list_sessions_agents**](AgentSessionsApi.md#list_sessions_agents) | **POST** /v1/agents/sessions/list | List Sessions
[**list_tools_agents_sessions**](AgentSessionsApi.md#list_tools_agents_sessions) | **GET** /v1/agents/sessions/tools | List Tools
[**patch_session_agents**](AgentSessionsApi.md#patch_session_agents) | **PATCH** /v1/agents/sessions/{session_id} | Patch Session
[**send_message_agents_sessions**](AgentSessionsApi.md#send_message_agents_sessions) | **POST** /v1/agents/sessions/{session_id}/messages | Send Message
[**submit_feedback_agents_sessions**](AgentSessionsApi.md#submit_feedback_agents_sessions) | **POST** /v1/agents/sessions/{session_id}/feedback | Submit Feedback
[**terminate_session_agents**](AgentSessionsApi.md#terminate_session_agents) | **DELETE** /v1/agents/sessions/{session_id} | Terminate Session


# **create_session_agents**
> CreateSessionResponse create_session_agents(create_session_request, authorization=authorization, x_namespace=x_namespace)

Create Session

Create a new agent session.

A session represents a stateful conversation with an AI agent that can
call tools to search data, filter results, and perform multi-step reasoning.

Args:
    request: FastAPI request with tenant context
    payload: Session creation request

Returns:
    CreateSessionResponse with session metadata

Example:
    ```bash
    curl -X POST http://localhost:8000/v1/agents/sessions \
      -H "Authorization: Bearer {api_key}" \
      -H "X-Namespace: {namespace_id}" \
      -H "Content-Type: application/json" \
      -d '{
        "agent_config": {
          "model": "claude-3-5-sonnet-20241022",
          "temperature": 0.7,
          "available_tools": ["search_retrievers", "execute_retriever"]
        },
        "quotas": {
          "max_messages": 100,
          "max_tokens_total": 100000
        }
      }'
    ```

### Example


```python
import mixpeek
from mixpeek.models.create_session_request import CreateSessionRequest
from mixpeek.models.create_session_response import CreateSessionResponse
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
    api_instance = mixpeek.AgentSessionsApi(api_client)
    create_session_request = mixpeek.CreateSessionRequest() # CreateSessionRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Create Session
        api_response = api_instance.create_session_agents(create_session_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of AgentSessionsApi->create_session_agents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentSessionsApi->create_session_agents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_session_request** | [**CreateSessionRequest**](CreateSessionRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**CreateSessionResponse**](CreateSessionResponse.md)

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

# **detect_intent_agents_sessions**
> IntentClassification detect_intent_agents_sessions(detect_intent_request, authorization=authorization, x_namespace=x_namespace)

Detect Intent

Detect user intent from natural language request.

This endpoint analyzes a user's request to determine whether they want to:
- Execute queries on existing data (execution mode)
- Create new resources/infrastructure (setup mode)
- Or if the request is ambiguous and needs clarification

It performs keyword analysis and checks existing collections to provide
intelligent classification and recommendations.

Args:
    request: FastAPI request with tenant context
    payload: Intent detection request with user's input

Returns:
    IntentClassification with detected intent and recommendations

Example:
    ```bash
    curl -X POST http://localhost:8000/v1/agents/intent/detect \
      -H "Authorization: Bearer {api_key}" \
      -H "X-Namespace: {namespace_id}" \
      -H "Content-Type: application/json" \
      -d '{
        "user_request": "I want to search videos by faces",
        "include_collection_analysis": true
      }'
    ```

### Example


```python
import mixpeek
from mixpeek.models.detect_intent_request import DetectIntentRequest
from mixpeek.models.intent_classification import IntentClassification
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
    api_instance = mixpeek.AgentSessionsApi(api_client)
    detect_intent_request = mixpeek.DetectIntentRequest() # DetectIntentRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Detect Intent
        api_response = api_instance.detect_intent_agents_sessions(detect_intent_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of AgentSessionsApi->detect_intent_agents_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentSessionsApi->detect_intent_agents_sessions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **detect_intent_request** | [**DetectIntentRequest**](DetectIntentRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**IntentClassification**](IntentClassification.md)

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

# **get_history_agents_sessions**
> GetHistoryResponse get_history_agents_sessions(session_id, limit=limit, offset=offset, authorization=authorization, x_namespace=x_namespace)

Get History

Get conversation history for a session.

Returns messages in chronological order (oldest first).

Args:
    request: FastAPI request with tenant context
    session_id: Session identifier
    limit: Maximum messages to return (default: 50, max: 200)
    offset: Pagination offset (default: 0)

Returns:
    GetHistoryResponse with message history

Raises:
    NotFoundError: If session not found

Example:
    ```bash
    curl -X GET "http://localhost:8000/v1/agents/sessions/ses_abc123/history?limit=20&offset=0" \
      -H "Authorization: Bearer {api_key}" \
      -H "X-Namespace: {namespace_id}"
    ```

### Example


```python
import mixpeek
from mixpeek.models.get_history_response import GetHistoryResponse
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
    api_instance = mixpeek.AgentSessionsApi(api_client)
    session_id = 'session_id_example' # str | Session ID
    limit = 50 # int | Maximum messages to return (optional) (default to 50)
    offset = 0 # int | Pagination offset (optional) (default to 0)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get History
        api_response = api_instance.get_history_agents_sessions(session_id, limit=limit, offset=offset, authorization=authorization, x_namespace=x_namespace)
        print("The response of AgentSessionsApi->get_history_agents_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentSessionsApi->get_history_agents_sessions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| Session ID | 
 **limit** | **int**| Maximum messages to return | [optional] [default to 50]
 **offset** | **int**| Pagination offset | [optional] [default to 0]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**GetHistoryResponse**](GetHistoryResponse.md)

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

# **get_session_agents**
> GetSessionResponse get_session_agents(session_id, authorization=authorization, x_namespace=x_namespace)

Get Session

Get session metadata by ID.

Args:
    request: FastAPI request with tenant context
    session_id: Session identifier

Returns:
    GetSessionResponse with session metadata

Raises:
    NotFoundError: If session not found

Example:
    ```bash
    curl -X GET http://localhost:8000/v1/agents/sessions/ses_abc123 \
      -H "Authorization: Bearer {api_key}" \
      -H "X-Namespace: {namespace_id}"
    ```

### Example


```python
import mixpeek
from mixpeek.models.get_session_response import GetSessionResponse
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
    api_instance = mixpeek.AgentSessionsApi(api_client)
    session_id = 'session_id_example' # str | Session ID
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Session
        api_response = api_instance.get_session_agents(session_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of AgentSessionsApi->get_session_agents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentSessionsApi->get_session_agents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| Session ID | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**GetSessionResponse**](GetSessionResponse.md)

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

# **list_sessions_agents**
> ListSessionsResponse list_sessions_agents(limit=limit, offset=offset, cursor=cursor, include_total=include_total, authorization=authorization, x_namespace=x_namespace, list_sessions_request=list_sessions_request)

List Sessions

List agent sessions in the namespace.

Args:
    request: FastAPI request with tenant context
    list_request: Optional filters and sorting
    pagination: Pagination parameters

Returns:
    ListSessionsResponse with session list

Example:
    ```bash
    curl -X POST http://localhost:8000/v1/agents/sessions/list \
      -H "Authorization: Bearer {api_key}" \
      -H "X-Namespace: {namespace_id}" \
      -H "Content-Type: application/json" \
      -d '{"status": "active"}'
    ```

### Example


```python
import mixpeek
from mixpeek.models.list_sessions_request import ListSessionsRequest
from mixpeek.models.list_sessions_response import ListSessionsResponse
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
    api_instance = mixpeek.AgentSessionsApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    cursor = 'cursor_example' # str |  (optional)
    include_total = False # bool |  (optional) (default to False)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)
    list_sessions_request = mixpeek.ListSessionsRequest() # ListSessionsRequest |  (optional)

    try:
        # List Sessions
        api_response = api_instance.list_sessions_agents(limit=limit, offset=offset, cursor=cursor, include_total=include_total, authorization=authorization, x_namespace=x_namespace, list_sessions_request=list_sessions_request)
        print("The response of AgentSessionsApi->list_sessions_agents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentSessionsApi->list_sessions_agents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **cursor** | **str**|  | [optional] 
 **include_total** | **bool**|  | [optional] [default to False]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 
 **list_sessions_request** | [**ListSessionsRequest**](ListSessionsRequest.md)|  | [optional] 

### Return type

[**ListSessionsResponse**](ListSessionsResponse.md)

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

# **list_tools_agents_sessions**
> ListToolsResponse list_tools_agents_sessions(category=category, authorization=authorization, x_namespace=x_namespace)

List Tools

List all available agent tools.

Use this endpoint to discover available tools before creating a session.
Pass tool names to `available_tools` in AgentConfig when creating a session.

Tool Categories:
- search: Tools for searching data (smart_search, execute_retriever, execute_adhoc_retriever)
- read: Tools for reading resources (list_*, get_*)
- create: Tools for creating resources (create_*)
- analyze: Tools for analyzing content (analyze_sample_with_pipeline, transcribe_with_pipeline)
- upload: Tools for file uploads (create_upload, confirm_upload, get_upload_status)
- memory: Tools for agent memory (search_feedback)
- recommendations: Tools for getting recommendations

Args:
    request: FastAPI request with tenant context
    category: Optional filter by tool category

Returns:
    ListToolsResponse with available tools

Example:
    ```bash
    # List all tools
    curl -X GET http://localhost:8000/v1/agents/tools \
      -H "Authorization: Bearer {api_key}" \
      -H "X-Namespace: {namespace_id}"

    # List only search tools
    curl -X GET "http://localhost:8000/v1/agents/tools?category=search" \
      -H "Authorization: Bearer {api_key}" \
      -H "X-Namespace: {namespace_id}"
    ```

### Example


```python
import mixpeek
from mixpeek.models.list_tools_response import ListToolsResponse
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
    api_instance = mixpeek.AgentSessionsApi(api_client)
    category = 'category_example' # str | Filter by tool category (optional)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # List Tools
        api_response = api_instance.list_tools_agents_sessions(category=category, authorization=authorization, x_namespace=x_namespace)
        print("The response of AgentSessionsApi->list_tools_agents_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentSessionsApi->list_tools_agents_sessions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**| Filter by tool category | [optional] 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**ListToolsResponse**](ListToolsResponse.md)

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

# **patch_session_agents**
> PatchSessionResponse patch_session_agents(session_id, patch_session_request, authorization=authorization, x_namespace=x_namespace)

Patch Session

Update session metadata.

Only user_memory can be updated. To change agent configuration,
create a new session.

Args:
    request: FastAPI request with tenant context
    session_id: Session identifier
    payload: Update request

Returns:
    PatchSessionResponse with update timestamp

Raises:
    NotFoundError: If session not found

Example:
    ```bash
    curl -X PATCH http://localhost:8000/v1/agents/sessions/ses_abc123 \
      -H "Authorization: Bearer {api_key}" \
      -H "X-Namespace: {namespace_id}" \
      -H "Content-Type: application/json" \
      -d '{
        "user_memory": {
          "preferences": {"language": "en", "domain": "tech"}
        }
      }'
    ```

### Example


```python
import mixpeek
from mixpeek.models.patch_session_request import PatchSessionRequest
from mixpeek.models.patch_session_response import PatchSessionResponse
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
    api_instance = mixpeek.AgentSessionsApi(api_client)
    session_id = 'session_id_example' # str | Session ID
    patch_session_request = mixpeek.PatchSessionRequest() # PatchSessionRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Patch Session
        api_response = api_instance.patch_session_agents(session_id, patch_session_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of AgentSessionsApi->patch_session_agents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentSessionsApi->patch_session_agents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| Session ID | 
 **patch_session_request** | [**PatchSessionRequest**](PatchSessionRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**PatchSessionResponse**](PatchSessionResponse.md)

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

# **send_message_agents_sessions**
> object send_message_agents_sessions(session_id, send_message_request, authorization=authorization, x_namespace=x_namespace)

Send Message

Send a message to the agent and stream the response.

This endpoint streams Server-Sent Events (SSE) back to the client as
the agent processes the message through its workflow.

## SSE Event Types

**Core Events:**
- `intent`: Intent classification result (emitted first)
    - `{intent, confidence, category, reasoning, context_scope}`
- `thinking`: Agent is analyzing/planning
    - `{step, message}`
- `tool_call`: Agent is calling a tool
    - `{tool_name, tool_call_id, inputs}`
- `tool_result`: Tool execution completed
    - `{tool_name, tool_call_id, success, output, latency_ms}`
- `token`: Response token (streaming)
    - `{content}`
- `message`: Final response content
    - `{content, message_id, is_final}`
- `session_name`: Auto-generated session name (first message only)
    - `{session_name}`
- `done`: Processing complete
    - `{latency_ms, tool_calls_made, message_id, retriever_summary, data_accessed_via_retriever}`
- `error`: Error occurred
    - `{message, recoverable}`

**Retriever Events (IMPORTANT - Primary Data Pathway):**
- `retriever_execution`: Retriever was used for data access
    - `{tool_name, execution_id, retriever_id, is_adhoc, documents_returned, latency_ms, message}`
    - Emitted whenever data is accessed via retriever (saved or ad-hoc)
- `pipeline_config`: Ad-hoc retriever configuration
    - `{tool_name, config, message}`
    - Contains the exact pipeline config users can save as a named retriever

**Retriever Summary in `done` Event:**
```json
{
  "retriever_summary": {
    "used_retrievers": true,
    "retriever_count": 2,
    "saved_retrievers": 1,
    "adhoc_retrievers": 1,
    "total_documents": 25,
    "executions": [...]
  },
  "data_accessed_via_retriever": true
}
```

Args:
    request: FastAPI request with tenant context
    session_id: Session identifier
    payload: Message request

Returns:
    StreamingResponse with SSE events

Raises:
    NotFoundError: If session not found

Example:
    ```bash
    curl -N -X POST http://localhost:8000/v1/agents/sessions/ses_abc123/messages \
      -H "Authorization: Bearer {api_key}" \
      -H "X-Namespace: {namespace_id}" \
      -H "Content-Type: application/json" \
      -d '{
        "content": "Find videos about machine learning",
        "stream": true
      }'

    # SSE Output:
    event: intent
    data: {"intent": "retriever_search", "confidence": 0.92, "category": "retriever"}

    event: thinking
    data: {"step": "processing", "message": "Analyzing your request..."}

    event: tool_call
    data: {"tool_name": "execute_retriever", "tool_call_id": "run_abc", "inputs": {...}}

    event: tool_result
    data: {"tool_name": "execute_retriever", "success": true, "output": {...}}

    event: retriever_execution
    data: {"tool_name": "execute_retriever", "is_adhoc": false, "documents_returned": 5}

    event: message
    data: {"content": "I found 5 videos about machine learning...", "is_final": true}

    event: done
    data: {"latency_ms": 1250.5, "data_accessed_via_retriever": true, "retriever_summary": {...}}
    ```

### Example


```python
import mixpeek
from mixpeek.models.send_message_request import SendMessageRequest
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
    api_instance = mixpeek.AgentSessionsApi(api_client)
    session_id = 'session_id_example' # str | Session ID
    send_message_request = mixpeek.SendMessageRequest() # SendMessageRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Send Message
        api_response = api_instance.send_message_agents_sessions(session_id, send_message_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of AgentSessionsApi->send_message_agents_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentSessionsApi->send_message_agents_sessions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| Session ID | 
 **send_message_request** | [**SendMessageRequest**](SendMessageRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

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

# **submit_feedback_agents_sessions**
> SubmitFeedbackResponse submit_feedback_agents_sessions(session_id, submit_feedback_request, authorization=authorization, x_namespace=x_namespace)

Submit Feedback

Submit feedback on an assistant message.

When positive feedback is received, the conversation exchange is stored
to memory for future context. When negative feedback is received, the
exchange is NOT stored. This enables learning from quality interactions.

Args:
    request: FastAPI request with tenant context
    session_id: Session identifier
    payload: Feedback request

Returns:
    SubmitFeedbackResponse with feedback status

Raises:
    NotFoundError: If session or message not found

Example:
    ```bash
    curl -X POST http://localhost:8000/v1/agents/sessions/ses_abc123/feedback \
      -H "Authorization: Bearer {api_key}" \
      -H "X-Namespace: {namespace_id}" \
      -H "Content-Type: application/json" \
      -d '{
        "message_id": "msg_xyz789",
        "rating": "positive",
        "feedback_text": "Very helpful response!"
      }'
    ```

### Example


```python
import mixpeek
from mixpeek.models.submit_feedback_request import SubmitFeedbackRequest
from mixpeek.models.submit_feedback_response import SubmitFeedbackResponse
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
    api_instance = mixpeek.AgentSessionsApi(api_client)
    session_id = 'session_id_example' # str | Session ID
    submit_feedback_request = mixpeek.SubmitFeedbackRequest() # SubmitFeedbackRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Submit Feedback
        api_response = api_instance.submit_feedback_agents_sessions(session_id, submit_feedback_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of AgentSessionsApi->submit_feedback_agents_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentSessionsApi->submit_feedback_agents_sessions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| Session ID | 
 **submit_feedback_request** | [**SubmitFeedbackRequest**](SubmitFeedbackRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**SubmitFeedbackResponse**](SubmitFeedbackResponse.md)

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

# **terminate_session_agents**
> TerminateSessionResponse terminate_session_agents(session_id, authorization=authorization, x_namespace=x_namespace)

Terminate Session

Terminate a session and kill its actor.

This permanently ends the session and releases all associated resources.

Args:
    request: FastAPI request with tenant context
    session_id: Session identifier

Returns:
    TerminateSessionResponse with termination timestamp

Raises:
    NotFoundError: If session not found

Example:
    ```bash
    curl -X DELETE http://localhost:8000/v1/agents/sessions/ses_abc123 \
      -H "Authorization: Bearer {api_key}" \
      -H "X-Namespace: {namespace_id}"
    ```

### Example


```python
import mixpeek
from mixpeek.models.terminate_session_response import TerminateSessionResponse
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
    api_instance = mixpeek.AgentSessionsApi(api_client)
    session_id = 'session_id_example' # str | Session ID
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Terminate Session
        api_response = api_instance.terminate_session_agents(session_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of AgentSessionsApi->terminate_session_agents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentSessionsApi->terminate_session_agents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| Session ID | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**TerminateSessionResponse**](TerminateSessionResponse.md)

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

