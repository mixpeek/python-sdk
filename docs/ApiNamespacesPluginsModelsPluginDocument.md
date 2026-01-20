# ApiNamespacesPluginsModelsPluginDocument

Plugin document stored in MongoDB.  Supports both namespace-level and org-level plugins: - Namespace plugins have namespace_id - Org plugins have organization_id

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plugin_id** | **str** | Unique plugin identifier | 
**namespace_id** | **str** | Owner namespace ID (for namespace-level plugins) | [optional] 
**organization_id** | **str** | Owner organization ID (for org-level plugins) | [optional] 
**name** | **str** | Plugin name | 
**version** | **str** | Plugin version (semver) | 
**description** | **str** | Plugin description | [optional] 
**s3_archive_url** | **str** | S3 URL to plugin archive | 
**code_hash** | **str** | SHA256 hash of plugin code | 
**validation_status** | **str** | Validation status | 
**validation_errors** | **List[str]** | Validation error messages | [optional] 
**security_scan_passed** | **bool** | Whether security scan passed | [optional] [default to False]
**deployed** | **bool** | Whether plugin is deployed | [optional] [default to False]
**deployment_info** | [**PluginDeploymentInfo**](PluginDeploymentInfo.md) | Deployment details | [optional] 
**manifest** | [**ApiNamespacesPluginsModelsPluginManifestMetadata**](ApiNamespacesPluginsModelsPluginManifestMetadata.md) | Metadata extracted from manifest.py | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 
**deployed_at** | **datetime** | When plugin was last deployed | [optional] 
**resolved_inference_name** | **str** | Resolved inference service name (from realtime.py or feature_uri) | [optional] 

## Example

```python
from mixpeek.models.api_namespaces_plugins_models_plugin_document import ApiNamespacesPluginsModelsPluginDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNamespacesPluginsModelsPluginDocument from a JSON string
api_namespaces_plugins_models_plugin_document_instance = ApiNamespacesPluginsModelsPluginDocument.from_json(json)
# print the JSON string representation of the object
print(ApiNamespacesPluginsModelsPluginDocument.to_json())

# convert the object into a dict
api_namespaces_plugins_models_plugin_document_dict = api_namespaces_plugins_models_plugin_document_instance.to_dict()
# create an instance of ApiNamespacesPluginsModelsPluginDocument from a dict
api_namespaces_plugins_models_plugin_document_from_dict = ApiNamespacesPluginsModelsPluginDocument.from_dict(api_namespaces_plugins_models_plugin_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


