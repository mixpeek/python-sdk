# WebhookOutput

Represents a configured webhook for an organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_id** | **str** | Unique identifier for the webhook. | [optional] 
**webhook_name** | **str** | Human-readable name for the webhook. | 
**event_types** | [**List[WebhookEventType]**](WebhookEventType.md) | A list of event types that this webhook subscribes to. | 
**channels** | [**List[WebhookChannelOutput]**](WebhookChannelOutput.md) | A list of channels to notify for the subscribed events. | 
**is_active** | **bool** | Whether the webhook is currently active and should send notifications. | [optional] [default to True]
**created_at** | **datetime** | Timestamp of when the webhook was created. | [optional] 
**updated_at** | **datetime** | Timestamp of the last update. | [optional] 

## Example

```python
from mixpeek.models.webhook_output import WebhookOutput

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookOutput from a JSON string
webhook_output_instance = WebhookOutput.from_json(json)
# print the JSON string representation of the object
print(WebhookOutput.to_json())

# convert the object into a dict
webhook_output_dict = webhook_output_instance.to_dict()
# create an instance of WebhookOutput from a dict
webhook_output_from_dict = WebhookOutput.from_dict(webhook_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


