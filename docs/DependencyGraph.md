# DependencyGraph

Dependency graph for migration ordering.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodes** | [**List[DependencyNode]**](DependencyNode.md) | All resource nodes | [optional] 
**execution_order** | **List[str]** | Topologically sorted execution order | [optional] 

## Example

```python
from mixpeek.models.dependency_graph import DependencyGraph

# TODO update the JSON string below
json = "{}"
# create an instance of DependencyGraph from a JSON string
dependency_graph_instance = DependencyGraph.from_json(json)
# print the JSON string representation of the object
print(DependencyGraph.to_json())

# convert the object into a dict
dependency_graph_dict = dependency_graph_instance.to_dict()
# create an instance of DependencyGraph from a dict
dependency_graph_from_dict = DependencyGraph.from_dict(dependency_graph_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


