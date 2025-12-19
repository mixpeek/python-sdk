# GenericSuccessResponse

GenericSuccessResponse.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] [default to 'Successfully completed']
**success** | **bool** |  | [optional] [default to True]

## Example

```python
from mixpeek.models.generic_success_response import GenericSuccessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GenericSuccessResponse from a JSON string
generic_success_response_instance = GenericSuccessResponse.from_json(json)
# print the JSON string representation of the object
print(GenericSuccessResponse.to_json())

# convert the object into a dict
generic_success_response_dict = generic_success_response_instance.to_dict()
# create an instance of GenericSuccessResponse from a dict
generic_success_response_from_dict = GenericSuccessResponse.from_dict(generic_success_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


