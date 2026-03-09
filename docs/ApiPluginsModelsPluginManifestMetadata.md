# ApiPluginsModelsPluginManifestMetadata

Metadata extracted from plugin manifest.py.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_extractor_name** | **str** | Plugin name | 
**version** | **str** | Plugin version | 
**description** | **str** | Plugin description | [optional] 
**input_schema** | **Dict[str, object]** | Input schema JSON | [optional] 
**output_schema** | **Dict[str, object]** | Output schema JSON | [optional] 
**parameter_schema** | **Dict[str, object]** | Parameter schema JSON | [optional] 
**required_vector_indexes** | **List[Dict[str, object]]** | Required vector indexes | [optional] 
**features** | **List[Dict[str, object]]** | Features defined by the plugin (embeddings, scalars) | [optional] 
**dependencies** | **List[str]** | Python package dependencies | [optional] 
**feature_uri** | **str** | Feature URI for realtime inference (e.g., mixpeek://text_extractor@v1/multilingual_e5_large_instruct_v1) | [optional] 

## Example

```python
from mixpeek.models.api_plugins_models_plugin_manifest_metadata import ApiPluginsModelsPluginManifestMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPluginsModelsPluginManifestMetadata from a JSON string
api_plugins_models_plugin_manifest_metadata_instance = ApiPluginsModelsPluginManifestMetadata.from_json(json)
# print the JSON string representation of the object
print(ApiPluginsModelsPluginManifestMetadata.to_json())

# convert the object into a dict
api_plugins_models_plugin_manifest_metadata_dict = api_plugins_models_plugin_manifest_metadata_instance.to_dict()
# create an instance of ApiPluginsModelsPluginManifestMetadata from a dict
api_plugins_models_plugin_manifest_metadata_from_dict = ApiPluginsModelsPluginManifestMetadata.from_dict(api_plugins_models_plugin_manifest_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


