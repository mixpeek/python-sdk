# SharedNamespacesMigrationsModelsFeatureExtractorConfig

Configuration for a feature extractor in migration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_extractor_name** | **str** | Name of the extractor | 
**version** | **str** | Version to use | [optional] 
**parameters** | **Dict[str, object]** | Extractor parameters | [optional] 

## Example

```python
from mixpeek.models.shared_namespaces_migrations_models_feature_extractor_config import SharedNamespacesMigrationsModelsFeatureExtractorConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SharedNamespacesMigrationsModelsFeatureExtractorConfig from a JSON string
shared_namespaces_migrations_models_feature_extractor_config_instance = SharedNamespacesMigrationsModelsFeatureExtractorConfig.from_json(json)
# print the JSON string representation of the object
print(SharedNamespacesMigrationsModelsFeatureExtractorConfig.to_json())

# convert the object into a dict
shared_namespaces_migrations_models_feature_extractor_config_dict = shared_namespaces_migrations_models_feature_extractor_config_instance.to_dict()
# create an instance of SharedNamespacesMigrationsModelsFeatureExtractorConfig from a dict
shared_namespaces_migrations_models_feature_extractor_config_from_dict = SharedNamespacesMigrationsModelsFeatureExtractorConfig.from_dict(shared_namespaces_migrations_models_feature_extractor_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


