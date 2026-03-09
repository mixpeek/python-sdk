# CloneCollectionRequest

Request to clone a collection with optional modifications.  **Purpose:** Cloning creates a NEW collection (with new ID) based on an existing one, allowing you to make changes that aren't allowed via PATCH (source, feature_extractor, field_passthrough). This is the recommended way to iterate on collection designs.  **Clone vs Template vs Version:** - **Clone**: Copy THIS collection and modify it (for iteration/fixes) - **Template**: Create collection from a reusable pattern (for new projects) - **Version**: (Not implemented) - Use clone instead  **Use Cases:** - Change feature extractor configuration without breaking production - Modify field_passthrough to include/exclude fields - Switch to different source (bucket or collection) - Test modifications before replacing production collection - Create variants (e.g., different embedding models)  **All fields are OPTIONAL:** - Omit a field to keep the original value - Provide a field to override the original value - collection_name is REQUIRED (clones must have unique names)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_name** | **str** | REQUIRED. Name for the cloned collection. Must be unique and different from the source collection. | 
**description** | **str** | OPTIONAL. Description override. If omitted, copies from source collection. | [optional] 
**source** | [**SourceConfigInput**](SourceConfigInput.md) | OPTIONAL. Override source configuration. If omitted, copies from source collection. Allows switching between buckets or collections. | [optional] 
**feature_extractor** | [**SharedCollectionFeaturesExtractorsModelsFeatureExtractorConfigInput**](SharedCollectionFeaturesExtractorsModelsFeatureExtractorConfigInput.md) | OPTIONAL. Override feature extractor configuration. If omitted, copies from source collection. This is where you&#39;d change models, parameters, or field_passthrough. | [optional] 
**enabled** | **bool** | OPTIONAL. Override enabled status. If omitted, copies from source collection. | [optional] 
**metadata** | **Dict[str, object]** | OPTIONAL. Override metadata. If omitted, copies from source collection. | [optional] 
**taxonomy_applications** | [**List[TaxonomyApplicationConfigInput]**](TaxonomyApplicationConfigInput.md) | OPTIONAL. Override taxonomy applications. If omitted, copies from source collection. | [optional] 

## Example

```python
from mixpeek.models.clone_collection_request import CloneCollectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CloneCollectionRequest from a JSON string
clone_collection_request_instance = CloneCollectionRequest.from_json(json)
# print the JSON string representation of the object
print(CloneCollectionRequest.to_json())

# convert the object into a dict
clone_collection_request_dict = clone_collection_request_instance.to_dict()
# create an instance of CloneCollectionRequest from a dict
clone_collection_request_from_dict = CloneCollectionRequest.from_dict(clone_collection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


