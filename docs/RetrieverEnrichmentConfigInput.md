# RetrieverEnrichmentConfigInput

Configuration for attaching a retriever enrichment to a collection.  Retriever enrichments run a retriever pipeline on each document during post-processing and write selected result fields back to the document.  Attributes:     retriever_id: ID of the retriever to execute     input_mappings: How to map document fields to retriever inputs     write_back_fields: Which result fields to write back to the document     execution_phase: Which post-processing phase to run in (default: RETRIEVER_ENRICHMENT)     priority: Priority within the execution phase (higher = runs first)     scroll_filters: Optional filters to select which documents to enrich     enabled: Whether this enrichment is active

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retriever_id** | **str** | ID of the retriever to execute | 
**input_mappings** | [**List[EnrichmentInputMapping]**](EnrichmentInputMapping.md) | Map document fields or constants to retriever input parameters | 
**write_back_fields** | [**List[WriteBackFieldMapping]**](WriteBackFieldMapping.md) | Which retriever result fields to write back to the document | 
**execution_phase** | [**PostProcessingPhase**](PostProcessingPhase.md) | Which phase this enrichment runs in. Default: RETRIEVER_ENRICHMENT (phase 4, after taxonomies, clusters, and alerts) | [optional] 
**priority** | **int** | Priority within the execution phase (higher &#x3D; runs first) | [optional] [default to 0]
**scroll_filters** | [**LogicalOperatorInput**](LogicalOperatorInput.md) | Optional filters to select which documents to enrich | [optional] 
**enabled** | **bool** | Whether this enrichment is active | [optional] [default to True]

## Example

```python
from mixpeek.models.retriever_enrichment_config_input import RetrieverEnrichmentConfigInput

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieverEnrichmentConfigInput from a JSON string
retriever_enrichment_config_input_instance = RetrieverEnrichmentConfigInput.from_json(json)
# print the JSON string representation of the object
print(RetrieverEnrichmentConfigInput.to_json())

# convert the object into a dict
retriever_enrichment_config_input_dict = retriever_enrichment_config_input_instance.to_dict()
# create an instance of RetrieverEnrichmentConfigInput from a dict
retriever_enrichment_config_input_from_dict = RetrieverEnrichmentConfigInput.from_dict(retriever_enrichment_config_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


