# OrgModelDeleteResponse

Response model for org model deletion.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] [default to True]
**model_id** | **str** |  | 
**message** | **str** |  | 

## Example

```python
from mixpeek.models.org_model_delete_response import OrgModelDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrgModelDeleteResponse from a JSON string
org_model_delete_response_instance = OrgModelDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(OrgModelDeleteResponse.to_json())

# convert the object into a dict
org_model_delete_response_dict = org_model_delete_response_instance.to_dict()
# create an instance of OrgModelDeleteResponse from a dict
org_model_delete_response_from_dict = OrgModelDeleteResponse.from_dict(org_model_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


