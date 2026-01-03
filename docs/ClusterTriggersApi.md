# mixpeek.ClusterTriggersApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_trigger_clusters**](ClusterTriggersApi.md#create_trigger_clusters) | **POST** /v1/clusters/triggers | Create Cluster Trigger
[**delete_trigger_clusters**](ClusterTriggersApi.md#delete_trigger_clusters) | **DELETE** /v1/clusters/triggers/{trigger_id} | Delete Cluster Trigger
[**get_trigger_clusters**](ClusterTriggersApi.md#get_trigger_clusters) | **GET** /v1/clusters/triggers/{trigger_id} | Get Cluster Trigger
[**get_trigger_history_clusters**](ClusterTriggersApi.md#get_trigger_history_clusters) | **POST** /v1/clusters/triggers/{trigger_id}/history | Get Trigger Execution History
[**list_triggers_clusters**](ClusterTriggersApi.md#list_triggers_clusters) | **POST** /v1/clusters/triggers/list | List Cluster Triggers
[**pause_trigger_clusters**](ClusterTriggersApi.md#pause_trigger_clusters) | **POST** /v1/clusters/triggers/{trigger_id}/pause | Pause Cluster Trigger
[**resume_trigger_clusters**](ClusterTriggersApi.md#resume_trigger_clusters) | **POST** /v1/clusters/triggers/{trigger_id}/resume | Resume Cluster Trigger
[**update_trigger_clusters**](ClusterTriggersApi.md#update_trigger_clusters) | **PATCH** /v1/clusters/triggers/{trigger_id} | Update Cluster Trigger


# **create_trigger_clusters**
> SharedClustersTriggersModelsTriggerModel create_trigger_clusters(shared_clusters_triggers_models_create_trigger_request, authorization=authorization, x_namespace=x_namespace)

Create Cluster Trigger

Create a new trigger for automated cluster execution.

    Supports multiple trigger types:
    - **cron**: Execute at specific times using cron expressions
    - **interval**: Execute at fixed intervals
    - **event**: Execute when specific events occur (e.g., documents added)
    - **conditional**: Execute when conditions are met (e.g., drift threshold)

### Example


```python
import mixpeek
from mixpeek.models.shared_clusters_triggers_models_create_trigger_request import SharedClustersTriggersModelsCreateTriggerRequest
from mixpeek.models.shared_clusters_triggers_models_trigger_model import SharedClustersTriggersModelsTriggerModel
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
    api_instance = mixpeek.ClusterTriggersApi(api_client)
    shared_clusters_triggers_models_create_trigger_request = mixpeek.SharedClustersTriggersModelsCreateTriggerRequest() # SharedClustersTriggersModelsCreateTriggerRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Create Cluster Trigger
        api_response = api_instance.create_trigger_clusters(shared_clusters_triggers_models_create_trigger_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of ClusterTriggersApi->create_trigger_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterTriggersApi->create_trigger_clusters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_clusters_triggers_models_create_trigger_request** | [**SharedClustersTriggersModelsCreateTriggerRequest**](SharedClustersTriggersModelsCreateTriggerRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**SharedClustersTriggersModelsTriggerModel**](SharedClustersTriggersModelsTriggerModel.md)

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

# **delete_trigger_clusters**
> delete_trigger_clusters(trigger_id, authorization=authorization, x_namespace=x_namespace)

Delete Cluster Trigger

Delete a cluster trigger (soft delete).

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
    api_instance = mixpeek.ClusterTriggersApi(api_client)
    trigger_id = 'trigger_id_example' # str | Trigger ID
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Delete Cluster Trigger
        api_instance.delete_trigger_clusters(trigger_id, authorization=authorization, x_namespace=x_namespace)
    except Exception as e:
        print("Exception when calling ClusterTriggersApi->delete_trigger_clusters: %s\n" % e)
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

# **get_trigger_clusters**
> SharedClustersTriggersModelsTriggerModel get_trigger_clusters(trigger_id, authorization=authorization, x_namespace=x_namespace)

Get Cluster Trigger

Get a cluster trigger by ID.

### Example


```python
import mixpeek
from mixpeek.models.shared_clusters_triggers_models_trigger_model import SharedClustersTriggersModelsTriggerModel
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
    api_instance = mixpeek.ClusterTriggersApi(api_client)
    trigger_id = 'trigger_id_example' # str | Trigger ID
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Cluster Trigger
        api_response = api_instance.get_trigger_clusters(trigger_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of ClusterTriggersApi->get_trigger_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterTriggersApi->get_trigger_clusters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trigger_id** | **str**| Trigger ID | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**SharedClustersTriggersModelsTriggerModel**](SharedClustersTriggersModelsTriggerModel.md)

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

# **get_trigger_history_clusters**
> SharedClustersTriggersModelsTriggerHistoryResponse get_trigger_history_clusters(trigger_id, trigger_history_request, authorization=authorization, x_namespace=x_namespace)

Get Trigger Execution History

Get execution history for a trigger with pagination.

### Example


```python
import mixpeek
from mixpeek.models.shared_clusters_triggers_models_trigger_history_response import SharedClustersTriggersModelsTriggerHistoryResponse
from mixpeek.models.trigger_history_request import TriggerHistoryRequest
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
    api_instance = mixpeek.ClusterTriggersApi(api_client)
    trigger_id = 'trigger_id_example' # str | Trigger ID
    trigger_history_request = mixpeek.TriggerHistoryRequest() # TriggerHistoryRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Trigger Execution History
        api_response = api_instance.get_trigger_history_clusters(trigger_id, trigger_history_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of ClusterTriggersApi->get_trigger_history_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterTriggersApi->get_trigger_history_clusters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trigger_id** | **str**| Trigger ID | 
 **trigger_history_request** | [**TriggerHistoryRequest**](TriggerHistoryRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**SharedClustersTriggersModelsTriggerHistoryResponse**](SharedClustersTriggersModelsTriggerHistoryResponse.md)

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

# **list_triggers_clusters**
> SharedClustersTriggersModelsListTriggersResponse list_triggers_clusters(shared_clusters_triggers_models_list_triggers_request, authorization=authorization, x_namespace=x_namespace)

List Cluster Triggers

List cluster triggers with filters and pagination.

### Example


```python
import mixpeek
from mixpeek.models.shared_clusters_triggers_models_list_triggers_request import SharedClustersTriggersModelsListTriggersRequest
from mixpeek.models.shared_clusters_triggers_models_list_triggers_response import SharedClustersTriggersModelsListTriggersResponse
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
    api_instance = mixpeek.ClusterTriggersApi(api_client)
    shared_clusters_triggers_models_list_triggers_request = mixpeek.SharedClustersTriggersModelsListTriggersRequest() # SharedClustersTriggersModelsListTriggersRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # List Cluster Triggers
        api_response = api_instance.list_triggers_clusters(shared_clusters_triggers_models_list_triggers_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of ClusterTriggersApi->list_triggers_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterTriggersApi->list_triggers_clusters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_clusters_triggers_models_list_triggers_request** | [**SharedClustersTriggersModelsListTriggersRequest**](SharedClustersTriggersModelsListTriggersRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**SharedClustersTriggersModelsListTriggersResponse**](SharedClustersTriggersModelsListTriggersResponse.md)

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

# **pause_trigger_clusters**
> SharedClustersTriggersModelsTriggerModel pause_trigger_clusters(trigger_id, authorization=authorization, x_namespace=x_namespace)

Pause Cluster Trigger

Pause trigger execution. Paused triggers retain configuration but do not execute.

### Example


```python
import mixpeek
from mixpeek.models.shared_clusters_triggers_models_trigger_model import SharedClustersTriggersModelsTriggerModel
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
    api_instance = mixpeek.ClusterTriggersApi(api_client)
    trigger_id = 'trigger_id_example' # str | Trigger ID
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Pause Cluster Trigger
        api_response = api_instance.pause_trigger_clusters(trigger_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of ClusterTriggersApi->pause_trigger_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterTriggersApi->pause_trigger_clusters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trigger_id** | **str**| Trigger ID | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**SharedClustersTriggersModelsTriggerModel**](SharedClustersTriggersModelsTriggerModel.md)

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

# **resume_trigger_clusters**
> SharedClustersTriggersModelsTriggerModel resume_trigger_clusters(trigger_id, authorization=authorization, x_namespace=x_namespace)

Resume Cluster Trigger

Resume paused trigger. Next execution time is recalculated from current time.

### Example


```python
import mixpeek
from mixpeek.models.shared_clusters_triggers_models_trigger_model import SharedClustersTriggersModelsTriggerModel
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
    api_instance = mixpeek.ClusterTriggersApi(api_client)
    trigger_id = 'trigger_id_example' # str | Trigger ID
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Resume Cluster Trigger
        api_response = api_instance.resume_trigger_clusters(trigger_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of ClusterTriggersApi->resume_trigger_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterTriggersApi->resume_trigger_clusters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trigger_id** | **str**| Trigger ID | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**SharedClustersTriggersModelsTriggerModel**](SharedClustersTriggersModelsTriggerModel.md)

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

# **update_trigger_clusters**
> SharedClustersTriggersModelsTriggerModel update_trigger_clusters(trigger_id, shared_clusters_triggers_models_update_trigger_request, authorization=authorization, x_namespace=x_namespace)

Update Cluster Trigger

Update a cluster trigger.

    Allowed updates:
    - schedule_config: Modify trigger schedule
    - description: Update description
    - status: Change status (use pause/resume endpoints instead)

    Not allowed:
    - trigger_type: Must delete and recreate
    - cluster_id: Immutable
    - execution_config: Immutable

### Example


```python
import mixpeek
from mixpeek.models.shared_clusters_triggers_models_trigger_model import SharedClustersTriggersModelsTriggerModel
from mixpeek.models.shared_clusters_triggers_models_update_trigger_request import SharedClustersTriggersModelsUpdateTriggerRequest
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
    api_instance = mixpeek.ClusterTriggersApi(api_client)
    trigger_id = 'trigger_id_example' # str | Trigger ID
    shared_clusters_triggers_models_update_trigger_request = mixpeek.SharedClustersTriggersModelsUpdateTriggerRequest() # SharedClustersTriggersModelsUpdateTriggerRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Update Cluster Trigger
        api_response = api_instance.update_trigger_clusters(trigger_id, shared_clusters_triggers_models_update_trigger_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of ClusterTriggersApi->update_trigger_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterTriggersApi->update_trigger_clusters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trigger_id** | **str**| Trigger ID | 
 **shared_clusters_triggers_models_update_trigger_request** | [**SharedClustersTriggersModelsUpdateTriggerRequest**](SharedClustersTriggersModelsUpdateTriggerRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**SharedClustersTriggersModelsTriggerModel**](SharedClustersTriggersModelsTriggerModel.md)

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

