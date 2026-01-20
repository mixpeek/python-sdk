# EnableOrgModelResponse

Response from enabling an org-level model for a namespace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether operation succeeded | 
**model_id** | **str** | Model identifier | 
**namespace_id** | **str** | Namespace where model was enabled | 
**deployment_status** | **str** | Deployment status (deployed, pending, skipped) | 
**message** | **str** | Status message | 

## Example

```python
from mixpeek.models.enable_org_model_response import EnableOrgModelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnableOrgModelResponse from a JSON string
enable_org_model_response_instance = EnableOrgModelResponse.from_json(json)
# print the JSON string representation of the object
print(EnableOrgModelResponse.to_json())

# convert the object into a dict
enable_org_model_response_dict = enable_org_model_response_instance.to_dict()
# create an instance of EnableOrgModelResponse from a dict
enable_org_model_response_from_dict = EnableOrgModelResponse.from_dict(enable_org_model_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


