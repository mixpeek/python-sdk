# TaxonomyApplicationConfigOutput

Configuration block that attaches a taxonomy to a collection.  Supports execution phase ordering for unified post-processing with taxonomies, clusters, and alerts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taxonomy_id** | **str** | ID of the &#x60;TaxonomyModel&#x60; to execute. | 
**execution_mode** | [**TaxonomyExecutionMode**](TaxonomyExecutionMode.md) | Execution mode for taxonomy enrichment. Materializes results during ingestion. | [optional] 
**target_collection_id** | **str** | Optional collection to persist results into when &#x60;execution_mode&#x60; is &#39;materialize&#39;. If omitted, the source collection is updated in-place. | [optional] 
**scroll_filters** | [**LogicalOperatorOutput**](LogicalOperatorOutput.md) | Additional filters applied when scrolling the source collection before enrichment. | [optional] 
**execution_phase** | **int** | Which phase this taxonomy runs in. Default: 1 (TAXONOMY phase, runs first). Valid values: 1&#x3D;TAXONOMY, 2&#x3D;CLUSTER, 3&#x3D;ALERT. Lower phases run earlier. | [optional] [default to 1]
**priority** | **int** | Priority within the execution phase (higher &#x3D; runs first) | [optional] [default to 0]
**hierarchical_enrichment_style** | [**HierarchicalEnrichmentStyle**](HierarchicalEnrichmentStyle.md) | For hierarchical taxonomies, controls how enrichment fields are structured. &#39;full_chain&#39;: Each tier writes to tier-prefixed fields (tier1_id, tier2_id, etc.). &#39;best_match&#39;: Only deepest match stored (category_id, category_name, path[]). &#39;combined&#39; (default): Both full chain AND best match summary fields. | [optional] 

## Example

```python
from mixpeek.models.taxonomy_application_config_output import TaxonomyApplicationConfigOutput

# TODO update the JSON string below
json = "{}"
# create an instance of TaxonomyApplicationConfigOutput from a JSON string
taxonomy_application_config_output_instance = TaxonomyApplicationConfigOutput.from_json(json)
# print the JSON string representation of the object
print(TaxonomyApplicationConfigOutput.to_json())

# convert the object into a dict
taxonomy_application_config_output_dict = taxonomy_application_config_output_instance.to_dict()
# create an instance of TaxonomyApplicationConfigOutput from a dict
taxonomy_application_config_output_from_dict = TaxonomyApplicationConfigOutput.from_dict(taxonomy_application_config_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


