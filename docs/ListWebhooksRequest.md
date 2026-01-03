# ListWebhooksRequest

Request for listing webhooks with filters.  Filters webhooks by various criteria.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **str** | Filter by event type | [optional] 
**is_active** | **bool** | Filter by active status | [optional] 

## Example

```python
from mixpeek.models.list_webhooks_request import ListWebhooksRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListWebhooksRequest from a JSON string
list_webhooks_request_instance = ListWebhooksRequest.from_json(json)
# print the JSON string representation of the object
print(ListWebhooksRequest.to_json())

# convert the object into a dict
list_webhooks_request_dict = list_webhooks_request_instance.to_dict()
# create an instance of ListWebhooksRequest from a dict
list_webhooks_request_from_dict = ListWebhooksRequest.from_dict(list_webhooks_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


