# OrgModelDocument

Org-level model document stored in MongoDB.  Org-scoped: Uses organization_id instead of namespace_id. Models belong to an organization and can be enabled in any namespace within that org.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_id** | **str** | Unique model identifier | 
**organization_id** | **str** | Owner organization ID | 
**name** | **str** | Model name | 
**version** | **str** | Model version (semver) | 
**description** | **str** | Model description | [optional] 
**s3_archive_url** | **str** | S3 URL to model archive | 
**model_format** | **str** | Model format/framework | 
**model_hash** | **str** | SHA256 hash of model archive | 
**validation_status** | **str** | Validation status | 
**validation_errors** | **List[str]** | Validation error messages | [optional] 
**deployed** | **bool** | Whether model has been deployed to any namespace | [optional] [default to False]
**deployment_info** | [**OrgModelDeploymentInfo**](OrgModelDeploymentInfo.md) | Deployment details | [optional] 
**framework** | **str** | ML framework (e.g., sentence-transformers) | [optional] 
**task_type** | **str** | Task type (e.g., embedding, classification) | [optional] 
**input_schema** | **Dict[str, object]** | Input schema JSON | [optional] 
**output_schema** | **Dict[str, object]** | Output schema JSON | [optional] 
**resource_requirements** | [**ModelResourceRequirements**](ModelResourceRequirements.md) | Resource requirements for deployment | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 

## Example

```python
from mixpeek.models.org_model_document import OrgModelDocument

# TODO update the JSON string below
json = "{}"
# create an instance of OrgModelDocument from a JSON string
org_model_document_instance = OrgModelDocument.from_json(json)
# print the JSON string representation of the object
print(OrgModelDocument.to_json())

# convert the object into a dict
org_model_document_dict = org_model_document_instance.to_dict()
# create an instance of OrgModelDocument from a dict
org_model_document_from_dict = OrgModelDocument.from_dict(org_model_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


