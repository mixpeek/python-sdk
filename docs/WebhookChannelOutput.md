# WebhookChannelOutput

Model for a single notification channel configuration within a webhook.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | [**NotificationChannel**](NotificationChannel.md) | The channel through which notifications are sent. | 
**configs** | [**Configs**](Configs.md) |  | 

## Example

```python
from mixpeek.models.webhook_channel_output import WebhookChannelOutput

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookChannelOutput from a JSON string
webhook_channel_output_instance = WebhookChannelOutput.from_json(json)
# print the JSON string representation of the object
print(WebhookChannelOutput.to_json())

# convert the object into a dict
webhook_channel_output_dict = webhook_channel_output_instance.to_dict()
# create an instance of WebhookChannelOutput from a dict
webhook_channel_output_from_dict = WebhookChannelOutput.from_dict(webhook_channel_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


