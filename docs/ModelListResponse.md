# ModelListResponse

Response model for listing models.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] [default to True]
**models** | [**List[ModelListItem]**](ModelListItem.md) |  | 
**total** | **int** |  | 
**namespace_id** | **str** |  | 

## Example

```python
from mixpeek.models.model_list_response import ModelListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModelListResponse from a JSON string
model_list_response_instance = ModelListResponse.from_json(json)
# print the JSON string representation of the object
print(ModelListResponse.to_json())

# convert the object into a dict
model_list_response_dict = model_list_response_instance.to_dict()
# create an instance of ModelListResponse from a dict
model_list_response_from_dict = ModelListResponse.from_dict(model_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


