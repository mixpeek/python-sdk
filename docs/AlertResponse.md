# AlertResponse

Response model for a single alert.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_id** | **str** | Unique identifier for the alert | [optional] 
**namespace_id** | **str** | Namespace this alert belongs to | [optional] 
**name** | **str** | Human-readable name for the alert | 
**description** | **str** | Optional description of what this alert monitors | [optional] 
**retriever_id** | **str** | ID of the retriever to execute. The retriever defines filters, scoring, limits. | 
**notification_config** | [**AlertNotificationConfig**](AlertNotificationConfig.md) | How and where to send notifications when alert triggers | 
**enabled** | **bool** | Whether the alert is active and will execute | [optional] [default to True]
**created_at** | **datetime** | Timestamp when the alert was created | [optional] 
**updated_at** | **datetime** | Timestamp when the alert was last updated | [optional] 
**metadata** | **Dict[str, object]** | Additional user-defined metadata for the alert | [optional] 

## Example

```python
from mixpeek.models.alert_response import AlertResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AlertResponse from a JSON string
alert_response_instance = AlertResponse.from_json(json)
# print the JSON string representation of the object
print(AlertResponse.to_json())

# convert the object into a dict
alert_response_dict = alert_response_instance.to_dict()
# create an instance of AlertResponse from a dict
alert_response_from_dict = AlertResponse.from_dict(alert_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


