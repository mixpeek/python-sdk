# ReminderPreferencesResponse

Response model for reminder preferences.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reminders** | [**ReminderPreferences**](ReminderPreferences.md) | Reminder/nudge email preferences | 

## Example

```python
from mixpeek.models.reminder_preferences_response import ReminderPreferencesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReminderPreferencesResponse from a JSON string
reminder_preferences_response_instance = ReminderPreferencesResponse.from_json(json)
# print the JSON string representation of the object
print(ReminderPreferencesResponse.to_json())

# convert the object into a dict
reminder_preferences_response_dict = reminder_preferences_response_instance.to_dict()
# create an instance of ReminderPreferencesResponse from a dict
reminder_preferences_response_from_dict = ReminderPreferencesResponse.from_dict(reminder_preferences_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


