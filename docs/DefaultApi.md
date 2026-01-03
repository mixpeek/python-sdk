# mixpeek.DefaultApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_trigger**](DefaultApi.md#create_trigger) | **POST** /v1/triggers | Create Trigger
[**delete_trigger**](DefaultApi.md#delete_trigger) | **DELETE** /v1/triggers/{trigger_id} | Delete Trigger
[**execute_trigger_now**](DefaultApi.md#execute_trigger_now) | **POST** /v1/triggers/{trigger_id}/execute | Execute Trigger Now
[**get_trigger**](DefaultApi.md#get_trigger) | **GET** /v1/triggers/{trigger_id} | Get Trigger
[**get_trigger_history**](DefaultApi.md#get_trigger_history) | **GET** /v1/triggers/{trigger_id}/history | Get Trigger Execution History
[**list_triggers**](DefaultApi.md#list_triggers) | **POST** /v1/triggers/list | List Triggers
[**pause_trigger**](DefaultApi.md#pause_trigger) | **POST** /v1/triggers/{trigger_id}/pause | Pause Trigger
[**resume_trigger**](DefaultApi.md#resume_trigger) | **POST** /v1/triggers/{trigger_id}/resume | Resume Trigger
[**update_trigger**](DefaultApi.md#update_trigger) | **PATCH** /v1/triggers/{trigger_id} | Update Trigger


# **create_trigger**
> SharedTriggersModelsTriggerModel create_trigger(shared_triggers_models_create_trigger_request, authorization=authorization, x_namespace=x_namespace)

Create Trigger

Create a new trigger for scheduled job execution.

    **Action Types:**
    - `cluster`: Execute clustering on a cluster definition
    - `taxonomy_enrichment`: Apply taxonomy enrichment to a collection

    **Schedule Types:**
    - `cron`: Execute at specific times using cron expressions (e.g., "0 2 * * *" for daily at 2am)
    - `interval`: Execute at fixed intervals (e.g., every 6 hours)
    - `event`: Execute when specific events occur (e.g., after 100 documents added)
    - `conditional`: Execute when conditions are met (e.g., drift threshold exceeded)

    **Examples:**

    Cluster trigger (daily at 2am):
    ```json
    {
      "action_type": "cluster",
      "action_config": {"cluster_id": "clust_abc123"},
      "trigger_type": "cron",
      "schedule_config": {"cron_expression": "0 2 * * *", "timezone": "UTC"},
      "description": "Daily clustering at 2am"
    }
    ```

    Taxonomy enrichment trigger (every 6 hours):
    ```json
    {
      "action_type": "taxonomy_enrichment",
      "action_config": {
        "taxonomy_id": "tax_products",
        "collection_id": "col_inventory",
        "batch_size": 1000
      },
      "trigger_type": "interval",
      "schedule_config": {"interval_seconds": 21600},
      "description": "Re-enrich products every 6 hours"
    }
    ```

### Example


```python
import mixpeek
from mixpeek.models.shared_triggers_models_create_trigger_request import SharedTriggersModelsCreateTriggerRequest
from mixpeek.models.shared_triggers_models_trigger_model import SharedTriggersModelsTriggerModel
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
    api_instance = mixpeek.DefaultApi(api_client)
    shared_triggers_models_create_trigger_request = mixpeek.SharedTriggersModelsCreateTriggerRequest() # SharedTriggersModelsCreateTriggerRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Create Trigger
        api_response = api_instance.create_trigger(shared_triggers_models_create_trigger_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of DefaultApi->create_trigger:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_trigger: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_triggers_models_create_trigger_request** | [**SharedTriggersModelsCreateTriggerRequest**](SharedTriggersModelsCreateTriggerRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**SharedTriggersModelsTriggerModel**](SharedTriggersModelsTriggerModel.md)

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

# **delete_trigger**
> delete_trigger(trigger_id, authorization=authorization, x_namespace=x_namespace)

Delete Trigger

Delete a trigger (soft delete - sets status to disabled).

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
    api_instance = mixpeek.DefaultApi(api_client)
    trigger_id = 'trigger_id_example' # str | Trigger ID
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Delete Trigger
        api_instance.delete_trigger(trigger_id, authorization=authorization, x_namespace=x_namespace)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_trigger: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trigger_id** | **str**| Trigger ID | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_trigger_now**
> TaskResponse execute_trigger_now(trigger_id, authorization=authorization, x_namespace=x_namespace)

Execute Trigger Now

Manually execute a trigger immediately.

    This bypasses the schedule and executes the trigger's action right away.
    Useful for testing trigger configuration or forcing immediate execution.

    Returns a task response that can be used to monitor execution progress.

### Example


```python
import mixpeek
from mixpeek.models.task_response import TaskResponse
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
    api_instance = mixpeek.DefaultApi(api_client)
    trigger_id = 'trigger_id_example' # str | Trigger ID
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Execute Trigger Now
        api_response = api_instance.execute_trigger_now(trigger_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of DefaultApi->execute_trigger_now:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->execute_trigger_now: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trigger_id** | **str**| Trigger ID | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**TaskResponse**](TaskResponse.md)

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

# **get_trigger**
> SharedTriggersModelsTriggerModel get_trigger(trigger_id, authorization=authorization, x_namespace=x_namespace)

Get Trigger

Get a trigger by ID.

### Example


```python
import mixpeek
from mixpeek.models.shared_triggers_models_trigger_model import SharedTriggersModelsTriggerModel
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
    api_instance = mixpeek.DefaultApi(api_client)
    trigger_id = 'trigger_id_example' # str | Trigger ID
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Trigger
        api_response = api_instance.get_trigger(trigger_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of DefaultApi->get_trigger:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_trigger: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trigger_id** | **str**| Trigger ID | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**SharedTriggersModelsTriggerModel**](SharedTriggersModelsTriggerModel.md)

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

# **get_trigger_history**
> SharedTriggersModelsTriggerHistoryResponse get_trigger_history(trigger_id, offset=offset, limit=limit, authorization=authorization, x_namespace=x_namespace)

Get Trigger Execution History

Get execution history for a trigger with pagination.

### Example


```python
import mixpeek
from mixpeek.models.shared_triggers_models_trigger_history_response import SharedTriggersModelsTriggerHistoryResponse
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
    api_instance = mixpeek.DefaultApi(api_client)
    trigger_id = 'trigger_id_example' # str | Trigger ID
    offset = 0 # int | Pagination offset (optional) (default to 0)
    limit = 50 # int | Results per page (optional) (default to 50)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Trigger Execution History
        api_response = api_instance.get_trigger_history(trigger_id, offset=offset, limit=limit, authorization=authorization, x_namespace=x_namespace)
        print("The response of DefaultApi->get_trigger_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_trigger_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trigger_id** | **str**| Trigger ID | 
 **offset** | **int**| Pagination offset | [optional] [default to 0]
 **limit** | **int**| Results per page | [optional] [default to 50]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**SharedTriggersModelsTriggerHistoryResponse**](SharedTriggersModelsTriggerHistoryResponse.md)

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

# **list_triggers**
> SharedTriggersModelsListTriggersResponse list_triggers(authorization=authorization, x_namespace=x_namespace, shared_triggers_models_list_triggers_request=shared_triggers_models_list_triggers_request)

List Triggers

List triggers with filters and pagination.

    **Filters:**
    - `action_type`: Filter by action type (cluster, taxonomy_enrichment)
    - `trigger_type`: Filter by trigger type (cron, interval, event, conditional)
    - `status`: Filter by status (active, paused, disabled, failed)
    - `resource_id`: Filter by resource ID (cluster_id or taxonomy_id)

### Example


```python
import mixpeek
from mixpeek.models.shared_triggers_models_list_triggers_request import SharedTriggersModelsListTriggersRequest
from mixpeek.models.shared_triggers_models_list_triggers_response import SharedTriggersModelsListTriggersResponse
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
    api_instance = mixpeek.DefaultApi(api_client)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)
    shared_triggers_models_list_triggers_request = mixpeek.SharedTriggersModelsListTriggersRequest() # SharedTriggersModelsListTriggersRequest |  (optional)

    try:
        # List Triggers
        api_response = api_instance.list_triggers(authorization=authorization, x_namespace=x_namespace, shared_triggers_models_list_triggers_request=shared_triggers_models_list_triggers_request)
        print("The response of DefaultApi->list_triggers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_triggers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 
 **shared_triggers_models_list_triggers_request** | [**SharedTriggersModelsListTriggersRequest**](SharedTriggersModelsListTriggersRequest.md)|  | [optional] 

### Return type

[**SharedTriggersModelsListTriggersResponse**](SharedTriggersModelsListTriggersResponse.md)

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

# **pause_trigger**
> SharedTriggersModelsTriggerModel pause_trigger(trigger_id, authorization=authorization, x_namespace=x_namespace)

Pause Trigger

Pause trigger execution. Paused triggers retain configuration but do not execute.

### Example


```python
import mixpeek
from mixpeek.models.shared_triggers_models_trigger_model import SharedTriggersModelsTriggerModel
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
    api_instance = mixpeek.DefaultApi(api_client)
    trigger_id = 'trigger_id_example' # str | Trigger ID
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Pause Trigger
        api_response = api_instance.pause_trigger(trigger_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of DefaultApi->pause_trigger:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->pause_trigger: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trigger_id** | **str**| Trigger ID | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**SharedTriggersModelsTriggerModel**](SharedTriggersModelsTriggerModel.md)

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

# **resume_trigger**
> SharedTriggersModelsTriggerModel resume_trigger(trigger_id, authorization=authorization, x_namespace=x_namespace)

Resume Trigger

Resume a paused trigger. Next execution time is recalculated from current time.

### Example


```python
import mixpeek
from mixpeek.models.shared_triggers_models_trigger_model import SharedTriggersModelsTriggerModel
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
    api_instance = mixpeek.DefaultApi(api_client)
    trigger_id = 'trigger_id_example' # str | Trigger ID
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Resume Trigger
        api_response = api_instance.resume_trigger(trigger_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of DefaultApi->resume_trigger:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->resume_trigger: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trigger_id** | **str**| Trigger ID | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**SharedTriggersModelsTriggerModel**](SharedTriggersModelsTriggerModel.md)

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

# **update_trigger**
> SharedTriggersModelsTriggerModel update_trigger(trigger_id, shared_triggers_models_update_trigger_request, authorization=authorization, x_namespace=x_namespace)

Update Trigger

Update a trigger.

    **Allowed updates:**
    - `schedule_config`: Modify trigger schedule
    - `description`: Update description
    - `status`: Change status (prefer using pause/resume endpoints)

    **Not allowed:**
    - `action_type`: Must delete and recreate
    - `trigger_type`: Must delete and recreate
    - `action_config`: Must delete and recreate

### Example


```python
import mixpeek
from mixpeek.models.shared_triggers_models_trigger_model import SharedTriggersModelsTriggerModel
from mixpeek.models.shared_triggers_models_update_trigger_request import SharedTriggersModelsUpdateTriggerRequest
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
    api_instance = mixpeek.DefaultApi(api_client)
    trigger_id = 'trigger_id_example' # str | Trigger ID
    shared_triggers_models_update_trigger_request = mixpeek.SharedTriggersModelsUpdateTriggerRequest() # SharedTriggersModelsUpdateTriggerRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Update Trigger
        api_response = api_instance.update_trigger(trigger_id, shared_triggers_models_update_trigger_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of DefaultApi->update_trigger:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_trigger: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trigger_id** | **str**| Trigger ID | 
 **shared_triggers_models_update_trigger_request** | [**SharedTriggersModelsUpdateTriggerRequest**](SharedTriggersModelsUpdateTriggerRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**SharedTriggersModelsTriggerModel**](SharedTriggersModelsTriggerModel.md)

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

