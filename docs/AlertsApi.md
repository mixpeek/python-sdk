# mixpeek.AlertsApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_alert**](AlertsApi.md#create_alert) | **POST** /v1/alerts | Create Alert
[**create_alert_0**](AlertsApi.md#create_alert_0) | **POST** /v1/alerts | Create Alert
[**delete_alert**](AlertsApi.md#delete_alert) | **DELETE** /v1/alerts/{alert_identifier} | Delete Alert
[**delete_alert_0**](AlertsApi.md#delete_alert_0) | **DELETE** /v1/alerts/{alert_identifier} | Delete Alert
[**get_alert**](AlertsApi.md#get_alert) | **GET** /v1/alerts/{alert_identifier} | Get Alert
[**get_alert_0**](AlertsApi.md#get_alert_0) | **GET** /v1/alerts/{alert_identifier} | Get Alert
[**list_alert_executions**](AlertsApi.md#list_alert_executions) | **GET** /v1/alerts/{alert_identifier}/executions | List Alert Executions
[**list_alert_executions_0**](AlertsApi.md#list_alert_executions_0) | **GET** /v1/alerts/{alert_identifier}/executions | List Alert Executions
[**list_alerts**](AlertsApi.md#list_alerts) | **POST** /v1/alerts/list | List Alerts
[**list_alerts_0**](AlertsApi.md#list_alerts_0) | **POST** /v1/alerts/list | List Alerts
[**list_all_executions_alerts**](AlertsApi.md#list_all_executions_alerts) | **GET** /v1/alerts/executions | List All Executions
[**list_all_executions_alerts_0**](AlertsApi.md#list_all_executions_alerts_0) | **GET** /v1/alerts/executions | List All Executions
[**patch_alert**](AlertsApi.md#patch_alert) | **PATCH** /v1/alerts/{alert_identifier} | Update Alert
[**patch_alert_0**](AlertsApi.md#patch_alert_0) | **PATCH** /v1/alerts/{alert_identifier} | Update Alert


# **create_alert**
> AlertResponse create_alert(create_alert_request, authorization=authorization, x_namespace=x_namespace)

Create Alert

Create a new alert that monitors document ingestion and sends notifications.

    Alerts attach retrievers to collections. When new documents are ingested,
    the alert runs the retriever and sends notifications if matches are found.

    **Key Components:**
    - `retriever_id`: References a retriever that defines query logic (filters, scoring, limits)
    - `notification_config`: Defines where to send notifications (webhook, Slack, email)

    **Note:** The retriever owns all query semantics. The alert's job is simply
    to run the retriever and notify if results exist.

### Example


```python
import mixpeek
from mixpeek.models.alert_response import AlertResponse
from mixpeek.models.create_alert_request import CreateAlertRequest
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
    api_instance = mixpeek.AlertsApi(api_client)
    create_alert_request = mixpeek.CreateAlertRequest() # CreateAlertRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Create Alert
        api_response = api_instance.create_alert(create_alert_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of AlertsApi->create_alert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->create_alert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_alert_request** | [**CreateAlertRequest**](CreateAlertRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**AlertResponse**](AlertResponse.md)

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

# **create_alert_0**
> AlertResponse create_alert_0(create_alert_request, authorization=authorization, x_namespace=x_namespace)

Create Alert

Create a new alert that monitors document ingestion and sends notifications.

    Alerts attach retrievers to collections. When new documents are ingested,
    the alert runs the retriever and sends notifications if matches are found.

    **Key Components:**
    - `retriever_id`: References a retriever that defines query logic (filters, scoring, limits)
    - `notification_config`: Defines where to send notifications (webhook, Slack, email)

    **Note:** The retriever owns all query semantics. The alert's job is simply
    to run the retriever and notify if results exist.

### Example


```python
import mixpeek
from mixpeek.models.alert_response import AlertResponse
from mixpeek.models.create_alert_request import CreateAlertRequest
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
    api_instance = mixpeek.AlertsApi(api_client)
    create_alert_request = mixpeek.CreateAlertRequest() # CreateAlertRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Create Alert
        api_response = api_instance.create_alert_0(create_alert_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of AlertsApi->create_alert_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->create_alert_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_alert_request** | [**CreateAlertRequest**](CreateAlertRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**AlertResponse**](AlertResponse.md)

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

# **delete_alert**
> object delete_alert(alert_identifier, authorization=authorization, x_namespace=x_namespace)

Delete Alert

Delete an alert and its execution history.

    This operation:
    - Removes the alert from MongoDB
    - Deletes all execution history for this alert
    - Does NOT affect the referenced retriever

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
    api_instance = mixpeek.AlertsApi(api_client)
    alert_identifier = 'alert_identifier_example' # str | Alert ID (alt_...) or name
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Delete Alert
        api_response = api_instance.delete_alert(alert_identifier, authorization=authorization, x_namespace=x_namespace)
        print("The response of AlertsApi->delete_alert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->delete_alert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_identifier** | **str**| Alert ID (alt_...) or name | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

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

# **delete_alert_0**
> object delete_alert_0(alert_identifier, authorization=authorization, x_namespace=x_namespace)

Delete Alert

Delete an alert and its execution history.

    This operation:
    - Removes the alert from MongoDB
    - Deletes all execution history for this alert
    - Does NOT affect the referenced retriever

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
    api_instance = mixpeek.AlertsApi(api_client)
    alert_identifier = 'alert_identifier_example' # str | Alert ID (alt_...) or name
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Delete Alert
        api_response = api_instance.delete_alert_0(alert_identifier, authorization=authorization, x_namespace=x_namespace)
        print("The response of AlertsApi->delete_alert_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->delete_alert_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_identifier** | **str**| Alert ID (alt_...) or name | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

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

# **get_alert**
> AlertResponse get_alert(alert_identifier, authorization=authorization, x_namespace=x_namespace)

Get Alert

Get an alert by ID (alt_...) or name.

### Example


```python
import mixpeek
from mixpeek.models.alert_response import AlertResponse
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
    api_instance = mixpeek.AlertsApi(api_client)
    alert_identifier = 'alert_identifier_example' # str | Alert ID (alt_...) or name
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Alert
        api_response = api_instance.get_alert(alert_identifier, authorization=authorization, x_namespace=x_namespace)
        print("The response of AlertsApi->get_alert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->get_alert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_identifier** | **str**| Alert ID (alt_...) or name | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**AlertResponse**](AlertResponse.md)

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

# **get_alert_0**
> AlertResponse get_alert_0(alert_identifier, authorization=authorization, x_namespace=x_namespace)

Get Alert

Get an alert by ID (alt_...) or name.

### Example


```python
import mixpeek
from mixpeek.models.alert_response import AlertResponse
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
    api_instance = mixpeek.AlertsApi(api_client)
    alert_identifier = 'alert_identifier_example' # str | Alert ID (alt_...) or name
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Alert
        api_response = api_instance.get_alert_0(alert_identifier, authorization=authorization, x_namespace=x_namespace)
        print("The response of AlertsApi->get_alert_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->get_alert_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_identifier** | **str**| Alert ID (alt_...) or name | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**AlertResponse**](AlertResponse.md)

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

# **list_alert_executions**
> AlertExecutionListResponse list_alert_executions(alert_identifier, limit=limit, offset=offset, cursor=cursor, include_total=include_total, authorization=authorization, x_namespace=x_namespace)

List Alert Executions

List execution history for a specific alert.

### Example


```python
import mixpeek
from mixpeek.models.alert_execution_list_response import AlertExecutionListResponse
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
    api_instance = mixpeek.AlertsApi(api_client)
    alert_identifier = 'alert_identifier_example' # str | Alert ID (alt_...) or name
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    cursor = 'cursor_example' # str |  (optional)
    include_total = False # bool |  (optional) (default to False)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # List Alert Executions
        api_response = api_instance.list_alert_executions(alert_identifier, limit=limit, offset=offset, cursor=cursor, include_total=include_total, authorization=authorization, x_namespace=x_namespace)
        print("The response of AlertsApi->list_alert_executions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->list_alert_executions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_identifier** | **str**| Alert ID (alt_...) or name | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **cursor** | **str**|  | [optional] 
 **include_total** | **bool**|  | [optional] [default to False]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**AlertExecutionListResponse**](AlertExecutionListResponse.md)

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

# **list_alert_executions_0**
> AlertExecutionListResponse list_alert_executions_0(alert_identifier, limit=limit, offset=offset, cursor=cursor, include_total=include_total, authorization=authorization, x_namespace=x_namespace)

List Alert Executions

List execution history for a specific alert.

### Example


```python
import mixpeek
from mixpeek.models.alert_execution_list_response import AlertExecutionListResponse
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
    api_instance = mixpeek.AlertsApi(api_client)
    alert_identifier = 'alert_identifier_example' # str | Alert ID (alt_...) or name
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    cursor = 'cursor_example' # str |  (optional)
    include_total = False # bool |  (optional) (default to False)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # List Alert Executions
        api_response = api_instance.list_alert_executions_0(alert_identifier, limit=limit, offset=offset, cursor=cursor, include_total=include_total, authorization=authorization, x_namespace=x_namespace)
        print("The response of AlertsApi->list_alert_executions_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->list_alert_executions_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_identifier** | **str**| Alert ID (alt_...) or name | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **cursor** | **str**|  | [optional] 
 **include_total** | **bool**|  | [optional] [default to False]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**AlertExecutionListResponse**](AlertExecutionListResponse.md)

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

# **list_alerts**
> ListAlertsResponse list_alerts(limit=limit, offset=offset, cursor=cursor, include_total=include_total, authorization=authorization, x_namespace=x_namespace, list_alerts_request=list_alerts_request)

List Alerts

List all alerts in the namespace with optional filtering and pagination.

    **Filtering:**
    - Use `search` for wildcard text search across alert_id, name, description
    - Use `filters` for structured queries

    **Sorting:**
    - Default: created_at descending (newest first)

### Example


```python
import mixpeek
from mixpeek.models.list_alerts_request import ListAlertsRequest
from mixpeek.models.list_alerts_response import ListAlertsResponse
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
    api_instance = mixpeek.AlertsApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    cursor = 'cursor_example' # str |  (optional)
    include_total = False # bool |  (optional) (default to False)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)
    list_alerts_request = mixpeek.ListAlertsRequest() # ListAlertsRequest |  (optional)

    try:
        # List Alerts
        api_response = api_instance.list_alerts(limit=limit, offset=offset, cursor=cursor, include_total=include_total, authorization=authorization, x_namespace=x_namespace, list_alerts_request=list_alerts_request)
        print("The response of AlertsApi->list_alerts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->list_alerts: %s\n" % e)
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
 **list_alerts_request** | [**ListAlertsRequest**](ListAlertsRequest.md)|  | [optional] 

### Return type

[**ListAlertsResponse**](ListAlertsResponse.md)

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

# **list_alerts_0**
> ListAlertsResponse list_alerts_0(limit=limit, offset=offset, cursor=cursor, include_total=include_total, authorization=authorization, x_namespace=x_namespace, list_alerts_request=list_alerts_request)

List Alerts

List all alerts in the namespace with optional filtering and pagination.

    **Filtering:**
    - Use `search` for wildcard text search across alert_id, name, description
    - Use `filters` for structured queries

    **Sorting:**
    - Default: created_at descending (newest first)

### Example


```python
import mixpeek
from mixpeek.models.list_alerts_request import ListAlertsRequest
from mixpeek.models.list_alerts_response import ListAlertsResponse
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
    api_instance = mixpeek.AlertsApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    cursor = 'cursor_example' # str |  (optional)
    include_total = False # bool |  (optional) (default to False)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)
    list_alerts_request = mixpeek.ListAlertsRequest() # ListAlertsRequest |  (optional)

    try:
        # List Alerts
        api_response = api_instance.list_alerts_0(limit=limit, offset=offset, cursor=cursor, include_total=include_total, authorization=authorization, x_namespace=x_namespace, list_alerts_request=list_alerts_request)
        print("The response of AlertsApi->list_alerts_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->list_alerts_0: %s\n" % e)
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
 **list_alerts_request** | [**ListAlertsRequest**](ListAlertsRequest.md)|  | [optional] 

### Return type

[**ListAlertsResponse**](ListAlertsResponse.md)

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

# **list_all_executions_alerts**
> AlertExecutionListResponse list_all_executions_alerts(limit=limit, offset=offset, cursor=cursor, include_total=include_total, authorization=authorization, x_namespace=x_namespace)

List All Executions

List execution history for all alerts in the namespace.

### Example


```python
import mixpeek
from mixpeek.models.alert_execution_list_response import AlertExecutionListResponse
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
    api_instance = mixpeek.AlertsApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    cursor = 'cursor_example' # str |  (optional)
    include_total = False # bool |  (optional) (default to False)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # List All Executions
        api_response = api_instance.list_all_executions_alerts(limit=limit, offset=offset, cursor=cursor, include_total=include_total, authorization=authorization, x_namespace=x_namespace)
        print("The response of AlertsApi->list_all_executions_alerts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->list_all_executions_alerts: %s\n" % e)
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

### Return type

[**AlertExecutionListResponse**](AlertExecutionListResponse.md)

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

# **list_all_executions_alerts_0**
> AlertExecutionListResponse list_all_executions_alerts_0(limit=limit, offset=offset, cursor=cursor, include_total=include_total, authorization=authorization, x_namespace=x_namespace)

List All Executions

List execution history for all alerts in the namespace.

### Example


```python
import mixpeek
from mixpeek.models.alert_execution_list_response import AlertExecutionListResponse
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
    api_instance = mixpeek.AlertsApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    cursor = 'cursor_example' # str |  (optional)
    include_total = False # bool |  (optional) (default to False)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # List All Executions
        api_response = api_instance.list_all_executions_alerts_0(limit=limit, offset=offset, cursor=cursor, include_total=include_total, authorization=authorization, x_namespace=x_namespace)
        print("The response of AlertsApi->list_all_executions_alerts_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->list_all_executions_alerts_0: %s\n" % e)
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

### Return type

[**AlertExecutionListResponse**](AlertExecutionListResponse.md)

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

# **patch_alert**
> AlertResponse patch_alert(alert_identifier, patch_alert_request, authorization=authorization, x_namespace=x_namespace)

Update Alert

Partially update an alert's configuration.

    **All fields are optional** - provide only what you want to update.

    Unlike taxonomies, alerts can be fully updated including:
    - `name`: Rename the alert
    - `description`: Update documentation
    - `retriever_id`: Change the retriever
    - `notification_config`: Update notification channels
    - `enabled`: Enable/disable the alert
    - `metadata`: Update custom metadata

### Example


```python
import mixpeek
from mixpeek.models.alert_response import AlertResponse
from mixpeek.models.patch_alert_request import PatchAlertRequest
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
    api_instance = mixpeek.AlertsApi(api_client)
    alert_identifier = 'alert_identifier_example' # str | Alert ID (alt_...) or name
    patch_alert_request = mixpeek.PatchAlertRequest() # PatchAlertRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Update Alert
        api_response = api_instance.patch_alert(alert_identifier, patch_alert_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of AlertsApi->patch_alert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->patch_alert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_identifier** | **str**| Alert ID (alt_...) or name | 
 **patch_alert_request** | [**PatchAlertRequest**](PatchAlertRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**AlertResponse**](AlertResponse.md)

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

# **patch_alert_0**
> AlertResponse patch_alert_0(alert_identifier, patch_alert_request, authorization=authorization, x_namespace=x_namespace)

Update Alert

Partially update an alert's configuration.

    **All fields are optional** - provide only what you want to update.

    Unlike taxonomies, alerts can be fully updated including:
    - `name`: Rename the alert
    - `description`: Update documentation
    - `retriever_id`: Change the retriever
    - `notification_config`: Update notification channels
    - `enabled`: Enable/disable the alert
    - `metadata`: Update custom metadata

### Example


```python
import mixpeek
from mixpeek.models.alert_response import AlertResponse
from mixpeek.models.patch_alert_request import PatchAlertRequest
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
    api_instance = mixpeek.AlertsApi(api_client)
    alert_identifier = 'alert_identifier_example' # str | Alert ID (alt_...) or name
    patch_alert_request = mixpeek.PatchAlertRequest() # PatchAlertRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Update Alert
        api_response = api_instance.patch_alert_0(alert_identifier, patch_alert_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of AlertsApi->patch_alert_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->patch_alert_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_identifier** | **str**| Alert ID (alt_...) or name | 
 **patch_alert_request** | [**PatchAlertRequest**](PatchAlertRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**AlertResponse**](AlertResponse.md)

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

