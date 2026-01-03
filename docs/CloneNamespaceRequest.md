# CloneNamespaceRequest

Request to clone a namespace with all its data.  Clone creates a full copy of a namespace including: - Namespace configuration (extractors, indexes) - Buckets (metadata, references same S3 files) - Collections (full copy of all vectors/embeddings) - Retrievers (pipeline configuration)  **Use Cases:** - Create staging environment from production - Backup namespace with all data - Fork namespace for experimentation  **For config-only copy (no data), use templates instead:** - POST /templates/namespaces/from-namespace/{id} - POST /templates/namespaces/{template_id}/instantiate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespace_name** | **str** | Name for the cloned namespace (must be unique) | 
**include_resources** | [**CloneNamespaceResourcesConfig**](CloneNamespaceResourcesConfig.md) | Which resources to include. Defaults to collections + retrievers. | [optional] 
**description** | **str** | Override description. If omitted, copies from source. | [optional] 
**source_organization_id** | **str** | Source org ID for cross-org cloning (admin only). | [optional] 

## Example

```python
from mixpeek.models.clone_namespace_request import CloneNamespaceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CloneNamespaceRequest from a JSON string
clone_namespace_request_instance = CloneNamespaceRequest.from_json(json)
# print the JSON string representation of the object
print(CloneNamespaceRequest.to_json())

# convert the object into a dict
clone_namespace_request_dict = clone_namespace_request_instance.to_dict()
# create an instance of CloneNamespaceRequest from a dict
clone_namespace_request_from_dict = CloneNamespaceRequest.from_dict(clone_namespace_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


