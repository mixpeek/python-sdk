# WebhookConfig

Configuration for webhook notifications.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL to which the webhook will be sent. | 
**headers** | **Dict[str, str]** | Custom headers to include in the webhook request. | [optional] 
**payload_template** | **Dict[str, object]** | A Jinja2 template for the JSON payload. | [optional] 
**timeout** | **float** | Request timeout in seconds. | [optional] [default to 10.0]

## Example

```python
from mixpeek.models.webhook_config import WebhookConfig

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookConfig from a JSON string
webhook_config_instance = WebhookConfig.from_json(json)
# print the JSON string representation of the object
print(WebhookConfig.to_json())

# convert the object into a dict
webhook_config_dict = webhook_config_instance.to_dict()
# create an instance of WebhookConfig from a dict
webhook_config_from_dict = WebhookConfig.from_dict(webhook_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


