# GenericDeleteResponse

GenericDeleteResponse.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] [default to 'Successfully deleted']
**success** | **bool** |  | [optional] [default to True]

## Example

```python
from mixpeek.models.generic_delete_response import GenericDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GenericDeleteResponse from a JSON string
generic_delete_response_instance = GenericDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(GenericDeleteResponse.to_json())

# convert the object into a dict
generic_delete_response_dict = generic_delete_response_instance.to_dict()
# create an instance of GenericDeleteResponse from a dict
generic_delete_response_from_dict = GenericDeleteResponse.from_dict(generic_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


