# WebhookChannelInput

Model for a single notification channel configuration within a webhook.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | [**NotificationChannel**](NotificationChannel.md) | The channel through which notifications are sent. | 
**configs** | [**Configs**](Configs.md) |  | 

## Example

```python
from mixpeek.models.webhook_channel_input import WebhookChannelInput

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookChannelInput from a JSON string
webhook_channel_input_instance = WebhookChannelInput.from_json(json)
# print the JSON string representation of the object
print(WebhookChannelInput.to_json())

# convert the object into a dict
webhook_channel_input_dict = webhook_channel_input_instance.to_dict()
# create an instance of WebhookChannelInput from a dict
webhook_channel_input_from_dict = WebhookChannelInput.from_dict(webhook_channel_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


