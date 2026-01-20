# NotificationChannelConfig

Configuration for a notification channel.  Channels define where notifications are sent when an alert is triggered. Supports multiple channel types including webhooks, Slack, and email.  Attributes:     channel_type: Type of notification channel (webhook, slack, email)     channel_id: Optional reference to a pre-configured channel in the organization     config: Optional channel-specific configuration overrides

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_type** | **str** | Type of notification channel: &#39;webhook&#39;, &#39;slack&#39;, &#39;email&#39; | 
**channel_id** | **str** | Reference to a pre-configured notification channel in the organization | [optional] 
**config** | **object** | Channel-specific configuration overrides (e.g., webhook URL, Slack channel) | [optional] 

## Example

```python
from mixpeek.models.notification_channel_config import NotificationChannelConfig

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationChannelConfig from a JSON string
notification_channel_config_instance = NotificationChannelConfig.from_json(json)
# print the JSON string representation of the object
print(NotificationChannelConfig.to_json())

# convert the object into a dict
notification_channel_config_dict = notification_channel_config_instance.to_dict()
# create an instance of NotificationChannelConfig from a dict
notification_channel_config_from_dict = NotificationChannelConfig.from_dict(notification_channel_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


