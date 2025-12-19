# SlackConfig

Configuration for Slack notifications.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_url** | **str** | Slack webhook URL | 
**channel** | **str** | Slack channel to send to | [optional] 
**username** | **str** | Username to use for the message | [optional] 
**icon_emoji** | **str** | Emoji to use as the icon | [optional] 
**icon_url** | **str** | URL to an image to use as the icon | [optional] 
**blocks_template** | **str** | Template for Slack blocks | [optional] 

## Example

```python
from mixpeek.models.slack_config import SlackConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SlackConfig from a JSON string
slack_config_instance = SlackConfig.from_json(json)
# print the JSON string representation of the object
print(SlackConfig.to_json())

# convert the object into a dict
slack_config_dict = slack_config_instance.to_dict()
# create an instance of SlackConfig from a dict
slack_config_from_dict = SlackConfig.from_dict(slack_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


