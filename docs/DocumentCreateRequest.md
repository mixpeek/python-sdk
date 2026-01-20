# DocumentCreateRequest

Request model for creating a document.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_id** | **str** | ID of the collection the document belongs to. | 
**root_object_id** | **str** | Optional denormalized root object identifier provided during creation. | [optional] 
**root_bucket_id** | **str** | Optional denormalized bucket identifier provided during creation. | [optional] 
**source_type** | **str** | Optional immediate parent type for the document. | [optional] 
**source_collection_id** | **str** | Optional parent collection identifier when sourced from a collection. | [optional] 
**source_document_id** | **str** | Optional parent document identifier when sourced from a collection. | [optional] 
**source_object_id** | **str** | Optional parent object identifier when sourced directly from a bucket. | [optional] 
**lineage_path** | **str** | Optional materialized lineage path to set during creation. | [optional] 
**lineage_chain** | [**List[LineageStep]**](LineageStep.md) | Processing steps from root object to this document. Recommended for decomposition trees. | [optional] 
**document_schema_version** | **str** | Optional document schema version (v1 or v2). If not provided, uses system default. | [optional] 
**metadata** | **object** | Optional metadata dictionary for user-defined fields and custom attributes. | [optional] 
**features** | [**List[FeatureModel]**](FeatureModel.md) | Features to associate with the document | [optional] 

## Example

```python
from mixpeek.models.document_create_request import DocumentCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentCreateRequest from a JSON string
document_create_request_instance = DocumentCreateRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentCreateRequest.to_json())

# convert the object into a dict
document_create_request_dict = document_create_request_instance.to_dict()
# create an instance of DocumentCreateRequest from a dict
document_create_request_from_dict = DocumentCreateRequest.from_dict(document_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


