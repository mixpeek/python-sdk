# OrgModelDetailResponse

Response model for org model details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] [default to True]
**model** | [**OrgModelDocument**](OrgModelDocument.md) |  | 

## Example

```python
from mixpeek.models.org_model_detail_response import OrgModelDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrgModelDetailResponse from a JSON string
org_model_detail_response_instance = OrgModelDetailResponse.from_json(json)
# print the JSON string representation of the object
print(OrgModelDetailResponse.to_json())

# convert the object into a dict
org_model_detail_response_dict = org_model_detail_response_instance.to_dict()
# create an instance of OrgModelDetailResponse from a dict
org_model_detail_response_from_dict = OrgModelDetailResponse.from_dict(org_model_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


