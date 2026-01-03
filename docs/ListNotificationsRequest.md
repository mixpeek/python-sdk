# ListNotificationsRequest

Request model for listing notifications.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notification_type** | [**NotificationType**](NotificationType.md) | Filter by notification type | [optional] 
**priority** | [**NotificationPriority**](NotificationPriority.md) | Filter by priority | [optional] 
**read** | **bool** | Filter by read status | [optional] 
**user_id** | **str** | Filter by user ID | [optional] 

## Example

```python
from mixpeek.models.list_notifications_request import ListNotificationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListNotificationsRequest from a JSON string
list_notifications_request_instance = ListNotificationsRequest.from_json(json)
# print the JSON string representation of the object
print(ListNotificationsRequest.to_json())

# convert the object into a dict
list_notifications_request_dict = list_notifications_request_instance.to_dict()
# create an instance of ListNotificationsRequest from a dict
list_notifications_request_from_dict = ListNotificationsRequest.from_dict(list_notifications_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


