# mixpeek.NotificationsApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_notification**](NotificationsApi.md#delete_notification) | **DELETE** /v1/notifications/{notification_id} | Delete Notification
[**get_funnel_state_notifications**](NotificationsApi.md#get_funnel_state_notifications) | **GET** /v1/notifications/funnel/state | Get Funnel State
[**get_notification**](NotificationsApi.md#get_notification) | **GET** /v1/notifications/{notification_id} | Get Notification
[**get_preferences_notifications**](NotificationsApi.md#get_preferences_notifications) | **GET** /v1/notifications/preferences | Get Preferences
[**get_reminder_preferences_notifications**](NotificationsApi.md#get_reminder_preferences_notifications) | **GET** /v1/notifications/preferences/reminders | Get Reminder Preferences
[**get_unread_count_notifications**](NotificationsApi.md#get_unread_count_notifications) | **GET** /v1/notifications/unread/count | Get Unread Count
[**list_notifications**](NotificationsApi.md#list_notifications) | **POST** /v1/notifications/list | List Notifications
[**mark_all_as_read_notifications**](NotificationsApi.md#mark_all_as_read_notifications) | **POST** /v1/notifications/read/all | Mark All As Read
[**mark_as_read_notifications**](NotificationsApi.md#mark_as_read_notifications) | **POST** /v1/notifications/{notification_id}/read | Mark As Read
[**update_preferences_notifications**](NotificationsApi.md#update_preferences_notifications) | **PUT** /v1/notifications/preferences | Update Preferences
[**update_reminder_preferences_notifications**](NotificationsApi.md#update_reminder_preferences_notifications) | **PUT** /v1/notifications/preferences/reminders | Update Reminder Preferences


# **delete_notification**
> delete_notification(notification_id, authorization=authorization)

Delete Notification

Delete a notification (idempotent - succeeds even if already deleted).

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
    api_instance = mixpeek.NotificationsApi(api_client)
    notification_id = 'notification_id_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Delete Notification
        api_instance.delete_notification(notification_id, authorization=authorization)
    except Exception as e:
        print("Exception when calling NotificationsApi->delete_notification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **str**|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

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

# **get_funnel_state_notifications**
> object get_funnel_state_notifications(authorization=authorization)

Get Funnel State

Get the current funnel state for the organization.

Returns the user's position in the onboarding funnel, including:
- Current stage
- When each stage was reached
- Nudges that have been sent
- Last activity timestamp

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
    api_instance = mixpeek.NotificationsApi(api_client)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Get Funnel State
        api_response = api_instance.get_funnel_state_notifications(authorization=authorization)
        print("The response of NotificationsApi->get_funnel_state_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->get_funnel_state_notifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_notification**
> Notification get_notification(notification_id, authorization=authorization)

Get Notification

Get a single notification by its ID.

### Example


```python
import mixpeek
from mixpeek.models.notification import Notification
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
    api_instance = mixpeek.NotificationsApi(api_client)
    notification_id = 'notification_id_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Get Notification
        api_response = api_instance.get_notification(notification_id, authorization=authorization)
        print("The response of NotificationsApi->get_notification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->get_notification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **str**|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**Notification**](Notification.md)

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

# **get_preferences_notifications**
> object get_preferences_notifications(authorization=authorization)

Get Preferences

Get notification preferences for the organization.

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
    api_instance = mixpeek.NotificationsApi(api_client)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Get Preferences
        api_response = api_instance.get_preferences_notifications(authorization=authorization)
        print("The response of NotificationsApi->get_preferences_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->get_preferences_notifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_reminder_preferences_notifications**
> ReminderPreferencesResponse get_reminder_preferences_notifications(authorization=authorization)

Get Reminder Preferences

Get reminder/nudge email preferences for the organization.

These preferences control funnel-based onboarding nudges,
re-engagement emails, and feature tips.

### Example


```python
import mixpeek
from mixpeek.models.reminder_preferences_response import ReminderPreferencesResponse
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
    api_instance = mixpeek.NotificationsApi(api_client)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Get Reminder Preferences
        api_response = api_instance.get_reminder_preferences_notifications(authorization=authorization)
        print("The response of NotificationsApi->get_reminder_preferences_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->get_reminder_preferences_notifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**ReminderPreferencesResponse**](ReminderPreferencesResponse.md)

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

# **get_unread_count_notifications**
> object get_unread_count_notifications(user_id=user_id, authorization=authorization)

Get Unread Count

Get count of unread notifications.

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
    api_instance = mixpeek.NotificationsApi(api_client)
    user_id = 'user_id_example' # str |  (optional)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Get Unread Count
        api_response = api_instance.get_unread_count_notifications(user_id=user_id, authorization=authorization)
        print("The response of NotificationsApi->get_unread_count_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->get_unread_count_notifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | [optional] 
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

# **list_notifications**
> ListNotificationsResponse list_notifications(limit=limit, offset=offset, cursor=cursor, include_total=include_total, authorization=authorization, list_notifications_request=list_notifications_request)

List Notifications

List all notifications for the user's organization.

### Example


```python
import mixpeek
from mixpeek.models.list_notifications_request import ListNotificationsRequest
from mixpeek.models.list_notifications_response import ListNotificationsResponse
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
    api_instance = mixpeek.NotificationsApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    cursor = 'cursor_example' # str |  (optional)
    include_total = False # bool |  (optional) (default to False)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    list_notifications_request = mixpeek.ListNotificationsRequest() # ListNotificationsRequest |  (optional)

    try:
        # List Notifications
        api_response = api_instance.list_notifications(limit=limit, offset=offset, cursor=cursor, include_total=include_total, authorization=authorization, list_notifications_request=list_notifications_request)
        print("The response of NotificationsApi->list_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->list_notifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **cursor** | **str**|  | [optional] 
 **include_total** | **bool**|  | [optional] [default to False]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **list_notifications_request** | [**ListNotificationsRequest**](ListNotificationsRequest.md)|  | [optional] 

### Return type

[**ListNotificationsResponse**](ListNotificationsResponse.md)

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

# **mark_all_as_read_notifications**
> object mark_all_as_read_notifications(authorization=authorization, mark_as_read_request=mark_as_read_request)

Mark All As Read

Mark all notifications as read for a user.

### Example


```python
import mixpeek
from mixpeek.models.mark_as_read_request import MarkAsReadRequest
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
    api_instance = mixpeek.NotificationsApi(api_client)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    mark_as_read_request = mixpeek.MarkAsReadRequest() # MarkAsReadRequest |  (optional)

    try:
        # Mark All As Read
        api_response = api_instance.mark_all_as_read_notifications(authorization=authorization, mark_as_read_request=mark_as_read_request)
        print("The response of NotificationsApi->mark_all_as_read_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->mark_all_as_read_notifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **mark_as_read_request** | [**MarkAsReadRequest**](MarkAsReadRequest.md)|  | [optional] 

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

# **mark_as_read_notifications**
> Notification mark_as_read_notifications(notification_id, authorization=authorization)

Mark As Read

Mark a notification as read.

### Example


```python
import mixpeek
from mixpeek.models.notification import Notification
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
    api_instance = mixpeek.NotificationsApi(api_client)
    notification_id = 'notification_id_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Mark As Read
        api_response = api_instance.mark_as_read_notifications(notification_id, authorization=authorization)
        print("The response of NotificationsApi->mark_as_read_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->mark_as_read_notifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **str**|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**Notification**](Notification.md)

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

# **update_preferences_notifications**
> object update_preferences_notifications(update_preferences_request, authorization=authorization)

Update Preferences

Update notification preferences for the organization.

### Example


```python
import mixpeek
from mixpeek.models.update_preferences_request import UpdatePreferencesRequest
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
    api_instance = mixpeek.NotificationsApi(api_client)
    update_preferences_request = mixpeek.UpdatePreferencesRequest() # UpdatePreferencesRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Update Preferences
        api_response = api_instance.update_preferences_notifications(update_preferences_request, authorization=authorization)
        print("The response of NotificationsApi->update_preferences_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->update_preferences_notifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_preferences_request** | [**UpdatePreferencesRequest**](UpdatePreferencesRequest.md)|  | 
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

# **update_reminder_preferences_notifications**
> ReminderPreferencesResponse update_reminder_preferences_notifications(update_reminder_preferences_request, authorization=authorization)

Update Reminder Preferences

Update reminder/nudge email preferences for the organization.

You can update individual preferences without affecting others:
- enabled: Master toggle for all reminder emails
- onboarding_nudges: Funnel progression nudges
- engagement_reminders: Re-engagement emails for inactivity
- feature_tips: Helpful tips and inspiration
- quiet_hours_start/end: Hours (0-23 UTC) when no emails are sent

### Example


```python
import mixpeek
from mixpeek.models.reminder_preferences_response import ReminderPreferencesResponse
from mixpeek.models.update_reminder_preferences_request import UpdateReminderPreferencesRequest
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
    api_instance = mixpeek.NotificationsApi(api_client)
    update_reminder_preferences_request = mixpeek.UpdateReminderPreferencesRequest() # UpdateReminderPreferencesRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Update Reminder Preferences
        api_response = api_instance.update_reminder_preferences_notifications(update_reminder_preferences_request, authorization=authorization)
        print("The response of NotificationsApi->update_reminder_preferences_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->update_reminder_preferences_notifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_reminder_preferences_request** | [**UpdateReminderPreferencesRequest**](UpdateReminderPreferencesRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**ReminderPreferencesResponse**](ReminderPreferencesResponse.md)

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

