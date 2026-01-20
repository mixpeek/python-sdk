# CustomModelDocument

Custom model document stored in MongoDB.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_id** | **str** | Unique model identifier | 
**namespace_id** | **str** | Owner namespace ID | 
**name** | **str** | Model name | 
**version** | **str** | Model version | 
**model_archive_url** | **str** | S3 URL to model archive | 
**model_format** | **str** | Model format/framework | 
**model_hash** | **str** | SHA256 hash of model file | 
**deployed** | **bool** | Whether model is deployed | [optional] [default to False]
**deployment_info** | [**ModelDeploymentInfo**](ModelDeploymentInfo.md) | Deployment details | [optional] 
**framework** | **str** | ML framework (e.g., sentence-transformers) | [optional] 
**task_type** | **str** | Task type (e.g., embedding, classification) | [optional] 
**input_schema** | **object** | Input schema JSON | [optional] 
**output_schema** | **object** | Output schema JSON | [optional] 
**resource_requirements** | [**ModelResourceRequirements**](ModelResourceRequirements.md) | Resource requirements for deployment | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 

## Example

```python
from mixpeek.models.custom_model_document import CustomModelDocument

# TODO update the JSON string below
json = "{}"
# create an instance of CustomModelDocument from a JSON string
custom_model_document_instance = CustomModelDocument.from_json(json)
# print the JSON string representation of the object
print(CustomModelDocument.to_json())

# convert the object into a dict
custom_model_document_dict = custom_model_document_instance.to_dict()
# create an instance of CustomModelDocument from a dict
custom_model_document_from_dict = CustomModelDocument.from_dict(custom_model_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


