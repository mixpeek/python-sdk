# ReturnVectorNames

Controls vector data in the response. Pass `true` to get a `_vectors` field listing available vector names (no embedding data). Pass a list of vector names (e.g. `[\"fashionsiglip_v1_embedding\"]`) to return the actual float arrays for those specific vectors, keyed by name.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from mixpeek.models.return_vector_names import ReturnVectorNames

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnVectorNames from a JSON string
return_vector_names_instance = ReturnVectorNames.from_json(json)
# print the JSON string representation of the object
print(ReturnVectorNames.to_json())

# convert the object into a dict
return_vector_names_dict = return_vector_names_instance.to_dict()
# create an instance of ReturnVectorNames from a dict
return_vector_names_from_dict = ReturnVectorNames.from_dict(return_vector_names_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


