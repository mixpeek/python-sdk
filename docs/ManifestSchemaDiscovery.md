# ManifestSchemaDiscovery

Manifest schema discovery for agent-driven configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manifest_version** | **str** | Current manifest schema version | 
**resource_types** | **List[str]** | List of supported resource types | 
**schemas** | **Dict[str, object]** | JSON Schema for each resource type | 
**dependency_graph** | **Dict[str, List[str]]** | Resource dependencies (key depends on values) | 
**examples** | **Dict[str, str]** | YAML example for each resource type | [optional] 

## Example

```python
from mixpeek.models.manifest_schema_discovery import ManifestSchemaDiscovery

# TODO update the JSON string below
json = "{}"
# create an instance of ManifestSchemaDiscovery from a JSON string
manifest_schema_discovery_instance = ManifestSchemaDiscovery.from_json(json)
# print the JSON string representation of the object
print(ManifestSchemaDiscovery.to_json())

# convert the object into a dict
manifest_schema_discovery_dict = manifest_schema_discovery_instance.to_dict()
# create an instance of ManifestSchemaDiscovery from a dict
manifest_schema_discovery_from_dict = ManifestSchemaDiscovery.from_dict(manifest_schema_discovery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


