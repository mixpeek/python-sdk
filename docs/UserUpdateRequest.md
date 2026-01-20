# UserUpdateRequest

Partial update payload for a user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_name** | **str** | Updated display name. | [optional] 
**avatar_url** | **str** | Updated profile image URL (e.g., custom avatar to override Gravatar). | [optional] 
**role** | [**UserRole**](UserRole.md) | Updated organization role. | [optional] 
**status** | [**UserStatus**](UserStatus.md) | Lifecycle status update (active, suspended, pending). | [optional] 
**metadata** | **object** | Replaces metadata with the provided dictionary when set. | [optional] 

## Example

```python
from mixpeek.models.user_update_request import UserUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserUpdateRequest from a JSON string
user_update_request_instance = UserUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(UserUpdateRequest.to_json())

# convert the object into a dict
user_update_request_dict = user_update_request_instance.to_dict()
# create an instance of UserUpdateRequest from a dict
user_update_request_from_dict = UserUpdateRequest.from_dict(user_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


