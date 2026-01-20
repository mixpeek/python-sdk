# UpdateReminderPreferencesRequest

Request model for updating reminder preferences.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Master toggle for all reminders | [optional] 
**onboarding_nudges** | **bool** | Enable/disable onboarding nudges | [optional] 
**engagement_reminders** | **bool** | Enable/disable engagement reminders | [optional] 
**feature_tips** | **bool** | Enable/disable feature tips | [optional] 
**quiet_hours_start** | **int** | Hour (0-23) to start quiet period (UTC) | [optional] 
**quiet_hours_end** | **int** | Hour (0-23) to end quiet period (UTC) | [optional] 

## Example

```python
from mixpeek.models.update_reminder_preferences_request import UpdateReminderPreferencesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateReminderPreferencesRequest from a JSON string
update_reminder_preferences_request_instance = UpdateReminderPreferencesRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateReminderPreferencesRequest.to_json())

# convert the object into a dict
update_reminder_preferences_request_dict = update_reminder_preferences_request_instance.to_dict()
# create an instance of UpdateReminderPreferencesRequest from a dict
update_reminder_preferences_request_from_dict = UpdateReminderPreferencesRequest.from_dict(update_reminder_preferences_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


