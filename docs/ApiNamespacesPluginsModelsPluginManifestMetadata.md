# ApiNamespacesPluginsModelsPluginManifestMetadata

Metadata extracted from plugin manifest.py.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_extractor_name** | **str** | Plugin name | [optional] 
**version** | **str** | Plugin version | [optional] 
**description** | **str** | Plugin description | [optional] 
**input_schema** | **Dict[str, object]** | Input schema JSON | [optional] 
**output_schema** | **Dict[str, object]** | Output schema JSON | [optional] 
**parameter_schema** | **Dict[str, object]** | Parameter schema JSON | [optional] 
**required_vector_indexes** | **List[Dict[str, object]]** | Required vector indexes | [optional] 
**features** | **List[Dict[str, object]]** | Features defined by the plugin (embeddings, scalars) | [optional] 
**dependencies** | **List[str]** | Python package dependencies | [optional] 
**compute_profile** | **Dict[str, object]** | Compute resource requirements for this plugin&#39;s pipeline steps. Keys: resource_type (cpu/gpu/api), gpu_memory_gb, actor_memory_gb, batch_size, max_concurrency. Validated into ComputeProfile at pipeline build time. | [optional] 
**serve_config** | **Dict[str, object]** | Ray Serve deployment configuration for realtime inference. Keys: num_replicas, min_replicas, max_replicas, target_ongoing_requests, num_cpus, num_gpus, memory_gb. Validated into ServeConfig at deploy time. Takes precedence over compute_profile for Serve resource allocation. | [optional] 
**feature_uri** | **str** | Feature URI for realtime inference (e.g., mixpeek://text_extractor@v1/multilingual_e5_large_instruct_v1) | [optional] 
**cost_rates** | **List[Dict[str, object]]** | Custom credit cost rates for this plugin. When present, the billing system uses these rates instead of ComputeProfile-based pricing. Format: [{\&quot;unit\&quot;: \&quot;minute\&quot;, \&quot;credits_per_unit\&quot;: 50}, ...]. Valid units: minute, image, 1k_tokens, page, face, extraction. | [optional] 

## Example

```python
from mixpeek.models.api_namespaces_plugins_models_plugin_manifest_metadata import ApiNamespacesPluginsModelsPluginManifestMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNamespacesPluginsModelsPluginManifestMetadata from a JSON string
api_namespaces_plugins_models_plugin_manifest_metadata_instance = ApiNamespacesPluginsModelsPluginManifestMetadata.from_json(json)
# print the JSON string representation of the object
print(ApiNamespacesPluginsModelsPluginManifestMetadata.to_json())

# convert the object into a dict
api_namespaces_plugins_models_plugin_manifest_metadata_dict = api_namespaces_plugins_models_plugin_manifest_metadata_instance.to_dict()
# create an instance of ApiNamespacesPluginsModelsPluginManifestMetadata from a dict
api_namespaces_plugins_models_plugin_manifest_metadata_from_dict = ApiNamespacesPluginsModelsPluginManifestMetadata.from_dict(api_namespaces_plugins_models_plugin_manifest_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


