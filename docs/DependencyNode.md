# DependencyNode

Node in dependency graph.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | Resource ID | 
**resource_type** | [**SharedNamespacesMigrationsModelsResourceType**](SharedNamespacesMigrationsModelsResourceType.md) | Resource type | 
**dependencies** | **List[str]** | IDs of resources this depends on | [optional] 
**tier** | **int** | Dependency tier (0&#x3D;no deps) | [optional] [default to 0]

## Example

```python
from mixpeek.models.dependency_node import DependencyNode

# TODO update the JSON string below
json = "{}"
# create an instance of DependencyNode from a JSON string
dependency_node_instance = DependencyNode.from_json(json)
# print the JSON string representation of the object
print(DependencyNode.to_json())

# convert the object into a dict
dependency_node_dict = dependency_node_instance.to_dict()
# create an instance of DependencyNode from a dict
dependency_node_from_dict = DependencyNode.from_dict(dependency_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


