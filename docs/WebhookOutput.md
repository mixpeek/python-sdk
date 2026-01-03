# WebhookOutput

Configured webhook subscription for organization event notifications.  Webhooks enable real-time notifications when events occur in the system. Each webhook subscribes to specific event types and delivers notifications via one or more configured channels (Slack, email, HTTP, SMS).  Webhook Lifecycle:     1. Created with event_types and channels configured     2. is_active=True enables notification delivery     3. Events matching event_types trigger notifications to all channels     4. is_active=False temporarily pauses notifications without deletion     5. Webhook can be updated to add/remove event types or channels     6. Permanent deletion removes the webhook configuration  Use Cases:     - Integrate Mixpeek events with external systems via HTTP webhooks     - Notify teams in Slack when ingestion jobs complete     - Send email alerts when critical failures occur     - Trigger automated workflows based on state changes     - Maintain audit trails by forwarding events to SIEM systems  Best Practices:     - Subscribe only to events you need (reduces noise)     - Use descriptive webhook_name for identification     - Configure multiple channels for critical events (redundancy)     - Set is_active=False to temporarily disable without losing config     - Monitor webhook delivery failures via last_error tracking

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_id** | **str** | Unique identifier for the webhook. Auto-generated with &#39;wh_&#39; prefix followed by secure random token. Format: wh_{10-character alphanumeric}. Used for API operations and event tracking. | [optional] 
**webhook_name** | **str** | REQUIRED. Human-readable name for the webhook. Displayed in dashboards, logs, and notification metadata. Should describe the webhook&#39;s purpose or destination. Format: 1-200 characters. | 
**event_types** | [**List[WebhookEventType]**](WebhookEventType.md) | REQUIRED. List of event types that trigger this webhook. When any of these events occur, notifications are sent to all channels. Must contain at least one event type. Common patterns: - [&#39;object.created&#39;, &#39;object.updated&#39;] for object lifecycle tracking - [&#39;cluster.execution.completed&#39;, &#39;cluster.execution.failed&#39;] for job monitoring - [&#39;*&#39;] for all events (use cautiously, high volume) | 
**channels** | [**List[WebhookChannelOutput]**](WebhookChannelOutput.md) | REQUIRED. List of notification channels for event delivery. When an event occurs, notifications are sent to ALL configured channels. Must contain at least one channel. Multiple channels provide redundancy and multi-audience delivery. Example: Send to both Slack (team) and email (manager) for critical events. | 
**is_active** | **bool** | Whether the webhook is currently active and should send notifications. True: Events trigger notifications to channels. False: Webhook is paused, no notifications sent but config preserved. Use to temporarily disable webhooks without losing configuration. Default: True | [optional] [default to True]
**created_at** | **datetime** | UTC timestamp when the webhook was created. Auto-generated at creation time. Immutable after creation. Format: ISO 8601 datetime. | [optional] 
**updated_at** | **datetime** | UTC timestamp of the most recent webhook update. Updated automatically when event_types, channels, or is_active changes. Tracks configuration modifications. Format: ISO 8601 datetime. | [optional] 

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


