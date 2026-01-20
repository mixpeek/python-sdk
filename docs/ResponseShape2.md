# ResponseShape2

Define custom structured output using LLM extraction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from mixpeek.models.response_shape2 import ResponseShape2

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseShape2 from a JSON string
response_shape2_instance = ResponseShape2.from_json(json)
# print the JSON string representation of the object
print(ResponseShape2.to_json())

# convert the object into a dict
response_shape2_dict = response_shape2_instance.to_dict()
# create an instance of ResponseShape2 from a dict
response_shape2_from_dict = ResponseShape2.from_dict(response_shape2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


