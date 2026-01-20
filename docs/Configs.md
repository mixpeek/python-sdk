# Configs

REQUIRED. Channel-specific configuration for notification delivery. Type depends on the channel field: - EmailConfig for EMAIL channel (recipients, subject template, etc.) - SlackConfig for SLACK channel (workspace, channel, bot token) - WebhookConfig for WEBHOOK channel (URL, headers, auth). See respective config models for detailed field requirements.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to_addresses** | **List[str]** | Email addresses to send to | 
**subject_template** | **str** | Template for email subject | [optional] 
**body_template** | **str** | Template for email body | [optional] 
**content_type** | [**NotificationContentType**](NotificationContentType.md) | Format of the email body | [optional] 
**cc_addresses** | **List[str]** | CC addresses | [optional] 
**bcc_addresses** | **List[str]** | BCC addresses | [optional] 
**webhook_url** | **str** | Slack webhook URL | 
**channel** | **str** | Slack channel to send to | [optional] 
**username** | **str** | Username to use for the message | [optional] 
**icon_emoji** | **str** | Emoji to use as the icon | [optional] 
**icon_url** | **str** | URL to an image to use as the icon | [optional] 
**blocks_template** | **str** | Template for Slack blocks | [optional] 
**url** | **str** | The URL to which the webhook will be sent. | 
**headers** | **Dict[str, str]** | Custom headers to include in the webhook request. | [optional] 
**payload_template** | **object** | A Jinja2 template for the JSON payload. | [optional] 
**timeout** | **float** | Request timeout in seconds. | [optional] [default to 10.0]

## Example

```python
from mixpeek.models.configs import Configs

# TODO update the JSON string below
json = "{}"
# create an instance of Configs from a JSON string
configs_instance = Configs.from_json(json)
# print the JSON string representation of the object
print(Configs.to_json())

# convert the object into a dict
configs_dict = configs_instance.to_dict()
# create an instance of Configs from a dict
configs_from_dict = Configs.from_dict(configs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


