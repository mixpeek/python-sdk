# UuidIndexParams

Configuration for UUID index.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'uuid']
**is_tenant** | **bool** |  | [optional] [default to False]

## Example

```python
from mixpeek.models.uuid_index_params import UuidIndexParams

# TODO update the JSON string below
json = "{}"
# create an instance of UuidIndexParams from a JSON string
uuid_index_params_instance = UuidIndexParams.from_json(json)
# print the JSON string representation of the object
print(UuidIndexParams.to_json())

# convert the object into a dict
uuid_index_params_dict = uuid_index_params_instance.to_dict()
# create an instance of UuidIndexParams from a dict
uuid_index_params_from_dict = UuidIndexParams.from_dict(uuid_index_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


