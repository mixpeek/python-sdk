# UpdatePreferencesRequest

Request model for updating notification preferences.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preferences** | **object** | Updated notification preferences | 

## Example

```python
from mixpeek.models.update_preferences_request import UpdatePreferencesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePreferencesRequest from a JSON string
update_preferences_request_instance = UpdatePreferencesRequest.from_json(json)
# print the JSON string representation of the object
print(UpdatePreferencesRequest.to_json())

# convert the object into a dict
update_preferences_request_dict = update_preferences_request_instance.to_dict()
# create an instance of UpdatePreferencesRequest from a dict
update_preferences_request_from_dict = UpdatePreferencesRequest.from_dict(update_preferences_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


