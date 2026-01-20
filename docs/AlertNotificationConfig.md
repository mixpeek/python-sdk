# AlertNotificationConfig

How and where to send notifications when an alert is triggered.  Defines the notification channels and what information to include in the notification payload.  Attributes:     channels: List of channels to send notifications to     include_matches: Whether to include matched documents in the payload     include_scores: Whether to include similarity scores in the payload     template_id: Optional template for formatting the notification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channels** | [**List[NotificationChannelConfig]**](NotificationChannelConfig.md) | List of notification channels to send alerts to | 
**include_matches** | **bool** | Include matched documents in notification payload | [optional] [default to True]
**include_scores** | **bool** | Include similarity scores in notification payload | [optional] [default to True]
**template_id** | **str** | Optional notification template for formatting | [optional] 

## Example

```python
from mixpeek.models.alert_notification_config import AlertNotificationConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AlertNotificationConfig from a JSON string
alert_notification_config_instance = AlertNotificationConfig.from_json(json)
# print the JSON string representation of the object
print(AlertNotificationConfig.to_json())

# convert the object into a dict
alert_notification_config_dict = alert_notification_config_instance.to_dict()
# create an instance of AlertNotificationConfig from a dict
alert_notification_config_from_dict = AlertNotificationConfig.from_dict(alert_notification_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


