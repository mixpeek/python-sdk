# EnableOrgModelRequest

Request to enable an org-level model for a namespace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deploy** | **bool** | Whether to deploy the model to Ray immediately after enabling | [optional] [default to False]
**resource_overrides** | [**ModelResourceRequirements**](ModelResourceRequirements.md) | Override resource requirements for this namespace deployment | [optional] 

## Example

```python
from mixpeek.models.enable_org_model_request import EnableOrgModelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EnableOrgModelRequest from a JSON string
enable_org_model_request_instance = EnableOrgModelRequest.from_json(json)
# print the JSON string representation of the object
print(EnableOrgModelRequest.to_json())

# convert the object into a dict
enable_org_model_request_dict = enable_org_model_request_instance.to_dict()
# create an instance of EnableOrgModelRequest from a dict
enable_org_model_request_from_dict = EnableOrgModelRequest.from_dict(enable_org_model_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


