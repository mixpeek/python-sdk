# OrgModelDeploymentInfo

Deployment information for an org-level model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ray_cluster_url** | **str** | Ray cluster URL where model is deployed | [optional] 
**ray_deployment_name** | **str** | Ray deployment name | [optional] 
**deployed_at** | **datetime** | When the model was deployed | [optional] 

## Example

```python
from mixpeek.models.org_model_deployment_info import OrgModelDeploymentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OrgModelDeploymentInfo from a JSON string
org_model_deployment_info_instance = OrgModelDeploymentInfo.from_json(json)
# print the JSON string representation of the object
print(OrgModelDeploymentInfo.to_json())

# convert the object into a dict
org_model_deployment_info_dict = org_model_deployment_info_instance.to_dict()
# create an instance of OrgModelDeploymentInfo from a dict
org_model_deployment_info_from_dict = OrgModelDeploymentInfo.from_dict(org_model_deployment_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


