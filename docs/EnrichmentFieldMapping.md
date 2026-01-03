# EnrichmentFieldMapping

Maps a cluster result field to a document enrichment field.  Similar to InputMapping pattern used throughout Mixpeek.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_field** | **str** | Field from cluster results to include. Available fields: cluster_id, cluster_label, distance_to_centroid, member_count, keywords, x, y, z (visualization coords), metadata.* | 
**target_field** | **str** | Target field name in enriched document. Example: &#39;category_id&#39; for cluster_id, &#39;product_category&#39; for cluster_label | 

## Example

```python
from mixpeek.models.enrichment_field_mapping import EnrichmentFieldMapping

# TODO update the JSON string below
json = "{}"
# create an instance of EnrichmentFieldMapping from a JSON string
enrichment_field_mapping_instance = EnrichmentFieldMapping.from_json(json)
# print the JSON string representation of the object
print(EnrichmentFieldMapping.to_json())

# convert the object into a dict
enrichment_field_mapping_dict = enrichment_field_mapping_instance.to_dict()
# create an instance of EnrichmentFieldMapping from a dict
enrichment_field_mapping_from_dict = EnrichmentFieldMapping.from_dict(enrichment_field_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


