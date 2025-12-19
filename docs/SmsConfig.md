# SmsConfig

Configuration for SMS notifications.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_numbers** | **List[str]** | Phone numbers to send to | 
**message_template** | **str** | Template for SMS message | [optional] 

## Example

```python
from mixpeek.models.sms_config import SmsConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SmsConfig from a JSON string
sms_config_instance = SmsConfig.from_json(json)
# print the JSON string representation of the object
print(SmsConfig.to_json())

# convert the object into a dict
sms_config_dict = sms_config_instance.to_dict()
# create an instance of SmsConfig from a dict
sms_config_from_dict = SmsConfig.from_dict(sms_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


