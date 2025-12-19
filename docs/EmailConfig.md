# EmailConfig

Configuration for email notifications.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to_addresses** | **List[str]** | Email addresses to send to | 
**subject_template** | **str** | Template for email subject | [optional] 
**body_template** | **str** | Template for email body | [optional] 
**content_type** | [**NotificationContentType**](NotificationContentType.md) | Format of the email body | [optional] 
**cc_addresses** | **List[str]** | CC addresses | [optional] 
**bcc_addresses** | **List[str]** | BCC addresses | [optional] 

## Example

```python
from mixpeek.models.email_config import EmailConfig

# TODO update the JSON string below
json = "{}"
# create an instance of EmailConfig from a JSON string
email_config_instance = EmailConfig.from_json(json)
# print the JSON string representation of the object
print(EmailConfig.to_json())

# convert the object into a dict
email_config_dict = email_config_instance.to_dict()
# create an instance of EmailConfig from a dict
email_config_from_dict = EmailConfig.from_dict(email_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


