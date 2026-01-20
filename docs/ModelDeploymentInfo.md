# ModelDeploymentInfo

Deployment information for a model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ray_cluster_url** | **str** | Ray cluster URL where model is deployed | [optional] 
**ray_deployment_name** | **str** | Ray deployment name | [optional] 
**endpoint** | **str** | HTTP endpoint for model inference | 
**base_image** | **str** | Docker image used for deployment | 
**deployed_at** | **datetime** | When the model was deployed | [optional] 

## Example

```python
from mixpeek.models.model_deployment_info import ModelDeploymentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ModelDeploymentInfo from a JSON string
model_deployment_info_instance = ModelDeploymentInfo.from_json(json)
# print the JSON string representation of the object
print(ModelDeploymentInfo.to_json())

# convert the object into a dict
model_deployment_info_dict = model_deployment_info_instance.to_dict()
# create an instance of ModelDeploymentInfo from a dict
model_deployment_info_from_dict = ModelDeploymentInfo.from_dict(model_deployment_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


