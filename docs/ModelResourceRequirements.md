# ModelResourceRequirements

Resource requirements for model deployment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_cpus** | **float** | Number of CPUs | [optional] [default to 1.0]
**num_gpus** | **int** | Number of GPUs | [optional] [default to 0]
**memory** | **int** | Memory in bytes (default 4GB) | [optional] [default to 4294967296]

## Example

```python
from mixpeek.models.model_resource_requirements import ModelResourceRequirements

# TODO update the JSON string below
json = "{}"
# create an instance of ModelResourceRequirements from a JSON string
model_resource_requirements_instance = ModelResourceRequirements.from_json(json)
# print the JSON string representation of the object
print(ModelResourceRequirements.to_json())

# convert the object into a dict
model_resource_requirements_dict = model_resource_requirements_instance.to_dict()
# create an instance of ModelResourceRequirements from a dict
model_resource_requirements_from_dict = ModelResourceRequirements.from_dict(model_resource_requirements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


