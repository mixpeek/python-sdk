# WebhookChannelOutput

Notification channel configuration for webhook delivery.  Defines how and where webhook event notifications should be delivered. Each webhook can have multiple channels configured for redundancy or different notification audiences.  Supported Channels:     - EMAIL: Send notifications via email to specified recipients     - SLACK: Post messages to Slack channels or direct messages     - WEBHOOK: HTTP POST to external endpoints (standard webhooks)  Use Cases:     - Route critical alerts to Slack and email simultaneously     - Send audit trail events to external webhook endpoints     - Notify team members via email for object lifecycle events     - Post cluster completion status to Slack channels  Requirements:     - Channel type must match the config type (discriminated union)     - Each config must have valid credentials/endpoints configured     - Channel configs are validated at webhook creation time

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | [**NotificationChannel**](NotificationChannel.md) | REQUIRED. The notification channel type for delivery. Determines which delivery mechanism is used (email, Slack, webhook). Must match the type of the configs field. | 
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


