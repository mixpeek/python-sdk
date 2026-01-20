# OrgModelListResponse

Response model for listing org models.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] [default to True]
**models** | [**List[OrgModelListItem]**](OrgModelListItem.md) |  | 
**total** | **int** |  | 
**organization_id** | **str** |  | 

## Example

```python
from mixpeek.models.org_model_list_response import OrgModelListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrgModelListResponse from a JSON string
org_model_list_response_instance = OrgModelListResponse.from_json(json)
# print the JSON string representation of the object
print(OrgModelListResponse.to_json())

# convert the object into a dict
org_model_list_response_dict = org_model_list_response_instance.to_dict()
# create an instance of OrgModelListResponse from a dict
org_model_list_response_from_dict = OrgModelListResponse.from_dict(org_model_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


