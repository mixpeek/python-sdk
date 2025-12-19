# UserModelOutput

User Model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | [optional] 
**user_name** | **str** |  | [optional] 
**email** | **str** |  | 
**api_keys** | [**List[APIKey]**](APIKey.md) |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from mixpeek.models.user_model_output import UserModelOutput

# TODO update the JSON string below
json = "{}"
# create an instance of UserModelOutput from a JSON string
user_model_output_instance = UserModelOutput.from_json(json)
# print the JSON string representation of the object
print(UserModelOutput.to_json())

# convert the object into a dict
user_model_output_dict = user_model_output_instance.to_dict()
# create an instance of UserModelOutput from a dict
user_model_output_from_dict = UserModelOutput.from_dict(user_model_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


