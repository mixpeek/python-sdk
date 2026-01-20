# CreateAlertRequest

Request model to create an alert.  Creates a new alert that can be attached to collections to monitor for matching content and send notifications when matches are found.  Note: The alert references a retriever that contains all query logic (filters, min_score, limits, collection targeting). The alert's job is simply to run that retriever and notify if results exist.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Human-readable name for the alert | 
**description** | **str** | Optional description of what this alert monitors | [optional] 
**retriever_id** | **str** | ID of the retriever to execute. The retriever defines filters, scoring, limits. | 
**notification_config** | [**AlertNotificationConfig**](AlertNotificationConfig.md) | How and where to send notifications when alert triggers | 
**enabled** | **bool** | Whether the alert is active and will execute | [optional] [default to True]
**metadata** | **object** | Additional user-defined metadata for the alert | [optional] 

## Example

```python
from mixpeek.models.create_alert_request import CreateAlertRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAlertRequest from a JSON string
create_alert_request_instance = CreateAlertRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAlertRequest.to_json())

# convert the object into a dict
create_alert_request_dict = create_alert_request_instance.to_dict()
# create an instance of CreateAlertRequest from a dict
create_alert_request_from_dict = CreateAlertRequest.from_dict(create_alert_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


