# ResponseShape3

Optional structured extraction schema. Natural language or JSON schema. Example: 'Extract API version, deprecated methods, and example code'

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from mixpeek.models.response_shape3 import ResponseShape3

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseShape3 from a JSON string
response_shape3_instance = ResponseShape3.from_json(json)
# print the JSON string representation of the object
print(ResponseShape3.to_json())

# convert the object into a dict
response_shape3_dict = response_shape3_instance.to_dict()
# create an instance of ResponseShape3 from a dict
response_shape3_from_dict = ResponseShape3.from_dict(response_shape3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


