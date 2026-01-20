# Notification

Model for a notification instance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID | [optional] 
**type** | [**NotificationType**](NotificationType.md) | Notification type | 
**priority** | [**NotificationPriority**](NotificationPriority.md) | Priority level | 
**title** | **str** | Notification title | 
**content** | **str** | Notification content | 
**created_at** | **datetime** | Creation timestamp | [optional] 
**organization_id** | **str** | Organization ID | 
**user_id** | **str** | User ID (if applicable) | [optional] 
**metadata** | **object** | Additional metadata | [optional] 
**delivery_status** | **Dict[str, str]** | Delivery status by channel | [optional] 
**read** | **bool** | Whether the notification has been read | [optional] [default to False]
**read_at** | **datetime** | When the notification was read | [optional] 

## Example

```python
from mixpeek.models.notification import Notification

# TODO update the JSON string below
json = "{}"
# create an instance of Notification from a JSON string
notification_instance = Notification.from_json(json)
# print the JSON string representation of the object
print(Notification.to_json())

# convert the object into a dict
notification_dict = notification_instance.to_dict()
# create an instance of Notification from a dict
notification_from_dict = Notification.from_dict(notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


