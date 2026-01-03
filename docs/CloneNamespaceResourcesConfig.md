# CloneNamespaceResourcesConfig

Configuration for which resources to include in clone.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collections** | **bool** | Include collections (with all embeddings/vectors) | [optional] [default to True]
**retrievers** | **bool** | Include retrievers | [optional] [default to True]
**taxonomies** | **bool** | Include taxonomies | [optional] [default to False]

## Example

```python
from mixpeek.models.clone_namespace_resources_config import CloneNamespaceResourcesConfig

# TODO update the JSON string below
json = "{}"
# create an instance of CloneNamespaceResourcesConfig from a JSON string
clone_namespace_resources_config_instance = CloneNamespaceResourcesConfig.from_json(json)
# print the JSON string representation of the object
print(CloneNamespaceResourcesConfig.to_json())

# convert the object into a dict
clone_namespace_resources_config_dict = clone_namespace_resources_config_instance.to_dict()
# create an instance of CloneNamespaceResourcesConfig from a dict
clone_namespace_resources_config_from_dict = CloneNamespaceResourcesConfig.from_dict(clone_namespace_resources_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


