# MigrationConfig

Configuration for a namespace migration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**migration_type** | [**MigrationType**](MigrationType.md) | Type of migration to perform | 
**source_namespace_id** | **str** | Source namespace ID | 
**target_namespace_id** | **str** | Target namespace ID (auto-generated if not provided) | [optional] 
**target_namespace_name** | **str** | Name for target namespace | [optional] 
**feature_extractors** | [**List[SharedNamespacesMigrationsModelsFeatureExtractorConfig]**](SharedNamespacesMigrationsModelsFeatureExtractorConfig.md) | New extractors to use (RE_EXTRACT only) | [optional] 
**filters** | [**ResourceFilter**](ResourceFilter.md) | Resource selection filters | [optional] 
**batch_options** | [**BatchOptions**](BatchOptions.md) | Batch processing options | [optional] 
**taxonomy_options** | [**TaxonomyOptions**](TaxonomyOptions.md) | Taxonomy migration options | [optional] 
**cluster_options** | [**ClusterOptions**](ClusterOptions.md) | Cluster migration options | [optional] 
**retriever_options** | [**RetrieverOptions**](RetrieverOptions.md) | Retriever migration options | [optional] 
**preserve_resource_ids** | **bool** | Preserve original resource IDs in target | [optional] [default to False]
**dry_run** | **bool** | Validate only, don&#39;t execute | [optional] [default to False]
**webhook_url** | **str** | Webhook URL for status notifications | [optional] 

## Example

```python
from mixpeek.models.migration_config import MigrationConfig

# TODO update the JSON string below
json = "{}"
# create an instance of MigrationConfig from a JSON string
migration_config_instance = MigrationConfig.from_json(json)
# print the JSON string representation of the object
print(MigrationConfig.to_json())

# convert the object into a dict
migration_config_dict = migration_config_instance.to_dict()
# create an instance of MigrationConfig from a dict
migration_config_from_dict = MigrationConfig.from_dict(migration_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


