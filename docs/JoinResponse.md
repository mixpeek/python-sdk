# JoinResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stats** | [**JoinStats**](JoinStats.md) |  | 
**results** | **List[Dict[str, object]]** |  | [optional] 

## Example

```python
from mixpeek.models.join_response import JoinResponse

# TODO update the JSON string below
json = "{}"
# create an instance of JoinResponse from a JSON string
join_response_instance = JoinResponse.from_json(json)
# print the JSON string representation of the object
print(JoinResponse.to_json())

# convert the object into a dict
join_response_dict = join_response_instance.to_dict()
# create an instance of JoinResponse from a dict
join_response_from_dict = JoinResponse.from_dict(join_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


