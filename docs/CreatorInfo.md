# CreatorInfo

Information about who created or updated a resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | User identifier | 
**email** | **str** | User email address | [optional] 
**name** | **str** | User display name | [optional] 

## Example

```python
from mixpeek.models.creator_info import CreatorInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CreatorInfo from a JSON string
creator_info_instance = CreatorInfo.from_json(json)
# print the JSON string representation of the object
print(CreatorInfo.to_json())

# convert the object into a dict
creator_info_dict = creator_info_instance.to_dict()
# create an instance of CreatorInfo from a dict
creator_info_from_dict = CreatorInfo.from_dict(creator_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


