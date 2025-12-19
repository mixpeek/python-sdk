# WebhookInput

Represents a configured webhook for an organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_id** | **str** | Unique identifier for the webhook. | [optional] 
**webhook_name** | **str** | Human-readable name for the webhook. | 
**internal_id** | **str** | The internal ID of the organization that owns this webhook. | [optional] 
**event_types** | [**List[WebhookEventType]**](WebhookEventType.md) | A list of event types that this webhook subscribes to. | 
**channels** | [**List[WebhookChannelInput]**](WebhookChannelInput.md) | A list of channels to notify for the subscribed events. | 
**is_active** | **bool** | Whether the webhook is currently active and should send notifications. | [optional] [default to True]
**created_at** | **datetime** | Timestamp of when the webhook was created. | [optional] 
**updated_at** | **datetime** | Timestamp of the last update. | [optional] 

## Example

```python
from mixpeek.models.webhook_input import WebhookInput

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookInput from a JSON string
webhook_input_instance = WebhookInput.from_json(json)
# print the JSON string representation of the object
print(WebhookInput.to_json())

# convert the object into a dict
webhook_input_dict = webhook_input_instance.to_dict()
# create an instance of WebhookInput from a dict
webhook_input_from_dict = WebhookInput.from_dict(webhook_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


