# ReminderPreferences

User preferences for reminder/nudge emails.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Master toggle for all reminder emails | [optional] [default to True]
**onboarding_nudges** | **bool** | Funnel progression nudges | [optional] [default to True]
**engagement_reminders** | **bool** | Re-engagement emails for inactivity | [optional] [default to True]
**feature_tips** | **bool** | Helpful tips and inspiration | [optional] [default to True]
**quiet_hours_start** | **int** | Hour (0-23) to start quiet period (UTC) | [optional] 
**quiet_hours_end** | **int** | Hour (0-23) to end quiet period (UTC) | [optional] 

## Example

```python
from mixpeek.models.reminder_preferences import ReminderPreferences

# TODO update the JSON string below
json = "{}"
# create an instance of ReminderPreferences from a JSON string
reminder_preferences_instance = ReminderPreferences.from_json(json)
# print the JSON string representation of the object
print(ReminderPreferences.to_json())

# convert the object into a dict
reminder_preferences_dict = reminder_preferences_instance.to_dict()
# create an instance of ReminderPreferences from a dict
reminder_preferences_from_dict = ReminderPreferences.from_dict(reminder_preferences_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


