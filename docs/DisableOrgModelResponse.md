# DisableOrgModelResponse

Response from disabling an org-level model for a namespace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether operation succeeded | 
**model_id** | **str** | Model identifier | 
**namespace_id** | **str** | Namespace where model was disabled | 
**message** | **str** | Status message | 

## Example

```python
from mixpeek.models.disable_org_model_response import DisableOrgModelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DisableOrgModelResponse from a JSON string
disable_org_model_response_instance = DisableOrgModelResponse.from_json(json)
# print the JSON string representation of the object
print(DisableOrgModelResponse.to_json())

# convert the object into a dict
disable_org_model_response_dict = disable_org_model_response_instance.to_dict()
# create an instance of DisableOrgModelResponse from a dict
disable_org_model_response_from_dict = DisableOrgModelResponse.from_dict(disable_org_model_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


