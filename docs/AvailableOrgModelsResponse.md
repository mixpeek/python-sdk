# AvailableOrgModelsResponse

Response for listing available org models.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] [default to True]
**models** | [**List[AvailableOrgModelItem]**](AvailableOrgModelItem.md) |  | 
**total** | **int** |  | 
**namespace_id** | **str** |  | 

## Example

```python
from mixpeek.models.available_org_models_response import AvailableOrgModelsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableOrgModelsResponse from a JSON string
available_org_models_response_instance = AvailableOrgModelsResponse.from_json(json)
# print the JSON string representation of the object
print(AvailableOrgModelsResponse.to_json())

# convert the object into a dict
available_org_models_response_dict = available_org_models_response_instance.to_dict()
# create an instance of AvailableOrgModelsResponse from a dict
available_org_models_response_from_dict = AvailableOrgModelsResponse.from_dict(available_org_models_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


