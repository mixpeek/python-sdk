# ModelDeployResponse

Response model for model deployment.  Deploying a model pre-loads the weights into the Ray object store, making them available for zero-copy access by plugins.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether deployment succeeded | 
**model_id** | **str** | Model identifier | 
**namespace_id** | **str** | Namespace ID | 
**deployment_status** | **str** | Deployment status (deployed, failed) | 
**cached** | **bool** | Whether model is cached in object store | [optional] [default to False]
**message** | **str** | Status message | 

## Example

```python
from mixpeek.models.model_deploy_response import ModelDeployResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModelDeployResponse from a JSON string
model_deploy_response_instance = ModelDeployResponse.from_json(json)
# print the JSON string representation of the object
print(ModelDeployResponse.to_json())

# convert the object into a dict
model_deploy_response_dict = model_deploy_response_instance.to_dict()
# create an instance of ModelDeployResponse from a dict
model_deploy_response_from_dict = ModelDeployResponse.from_dict(model_deploy_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


