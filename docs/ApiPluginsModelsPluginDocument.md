# ApiPluginsModelsPluginDocument

Plugin document stored in MongoDB.  Org-scoped: Uses organization_id instead of namespace_id. Plugins belong to an organization and can be used by any namespace within that org.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plugin_id** | **str** | Unique plugin identifier | 
**organization_id** | **str** | Owner organization ID | 
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
**manifest** | [**ApiPluginsModelsPluginManifestMetadata**](ApiPluginsModelsPluginManifestMetadata.md) | Metadata extracted from manifest.py | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 
**deployed_at** | **datetime** | When plugin was last deployed | [optional] 
**resolved_inference_name** | **str** | Resolved inference service name (from realtime.py or feature_uri) | [optional] 

## Example

```python
from mixpeek.models.api_plugins_models_plugin_document import ApiPluginsModelsPluginDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPluginsModelsPluginDocument from a JSON string
api_plugins_models_plugin_document_instance = ApiPluginsModelsPluginDocument.from_json(json)
# print the JSON string representation of the object
print(ApiPluginsModelsPluginDocument.to_json())

# convert the object into a dict
api_plugins_models_plugin_document_dict = api_plugins_models_plugin_document_instance.to_dict()
# create an instance of ApiPluginsModelsPluginDocument from a dict
api_plugins_models_plugin_document_from_dict = ApiPluginsModelsPluginDocument.from_dict(api_plugins_models_plugin_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


