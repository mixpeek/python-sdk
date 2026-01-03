# SourceEnrichmentConfig

Configuration for enriching source collection documents with cluster assignments.  When enrich_source_collection=True, cluster assignments are written back to the original source documents, similar to taxonomy enrichment.  Uses flexible field mapping pattern to support any cluster result fields.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_mappings** | [**List[EnrichmentFieldMapping]**](EnrichmentFieldMapping.md) | List of field mappings from cluster results to document fields. Default includes cluster_id and cluster_label. Can include: distance_to_centroid, member_count, keywords, visualization coords (x, y, z), etc. | [optional] 

## Example

```python
from mixpeek.models.source_enrichment_config import SourceEnrichmentConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SourceEnrichmentConfig from a JSON string
source_enrichment_config_instance = SourceEnrichmentConfig.from_json(json)
# print the JSON string representation of the object
print(SourceEnrichmentConfig.to_json())

# convert the object into a dict
source_enrichment_config_dict = source_enrichment_config_instance.to_dict()
# create an instance of SourceEnrichmentConfig from a dict
source_enrichment_config_from_dict = SourceEnrichmentConfig.from_dict(source_enrichment_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


