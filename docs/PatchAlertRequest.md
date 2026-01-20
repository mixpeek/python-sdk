# PatchAlertRequest

Request model to update an alert.  All fields are optional - provide only what you want to update. Core fields (retriever_id, notification_config) can be updated since alerts don't have join history like taxonomies.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Updated name for the alert | [optional] 
**description** | **str** | Updated description for the alert | [optional] 
**retriever_id** | **str** | Updated retriever ID | [optional] 
**notification_config** | [**AlertNotificationConfig**](AlertNotificationConfig.md) | Updated notification configuration | [optional] 
**enabled** | **bool** | Updated enabled status | [optional] 
**metadata** | **object** | Updated metadata | [optional] 

## Example

```python
from mixpeek.models.patch_alert_request import PatchAlertRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchAlertRequest from a JSON string
patch_alert_request_instance = PatchAlertRequest.from_json(json)
# print the JSON string representation of the object
print(PatchAlertRequest.to_json())

# convert the object into a dict
patch_alert_request_dict = patch_alert_request_instance.to_dict()
# create an instance of PatchAlertRequest from a dict
patch_alert_request_from_dict = PatchAlertRequest.from_dict(patch_alert_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


