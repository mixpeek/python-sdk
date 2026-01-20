# ModelDetailResponse

Response model for model details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] [default to True]
**model** | [**CustomModelDocument**](CustomModelDocument.md) |  | 

## Example

```python
from mixpeek.models.model_detail_response import ModelDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModelDetailResponse from a JSON string
model_detail_response_instance = ModelDetailResponse.from_json(json)
# print the JSON string representation of the object
print(ModelDetailResponse.to_json())

# convert the object into a dict
model_detail_response_dict = model_detail_response_instance.to_dict()
# create an instance of ModelDetailResponse from a dict
model_detail_response_from_dict = ModelDetailResponse.from_dict(model_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


