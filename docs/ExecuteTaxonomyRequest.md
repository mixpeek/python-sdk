# ExecuteTaxonomyRequest

Request model for on-demand taxonomy validation and testing ONLY.  ⚠️ IMPORTANT: This endpoint is ONLY for testing taxonomy configuration with sample documents.  DO NOT USE THIS FOR BATCH ENRICHMENT: ❌ Do NOT use this to enrich an entire collection ❌ Do NOT use source_collection_id expecting batch processing ❌ Do NOT use target_collection_id expecting persistence  HOW TAXONOMY ENRICHMENT ACTUALLY WORKS: ✅ Automatic during ingestion: Attach taxonomies to collections via `taxonomy_applications` ✅ On-the-fly in retrieval: Add `taxonomy_join` stage to retriever pipelines  This endpoint validates: - Taxonomy configuration is correct - Retriever can find matching taxonomy nodes - Enrichment fields are properly applied  For production enrichment, see: - Collections API: attach taxonomies via `taxonomy_applications` field - Retrievers API: add `taxonomy_join` stage for on-the-fly enrichment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taxonomy** | [**TaxonomyModelInput**](TaxonomyModelInput.md) | Full taxonomy model with configuration (fetched from DB by controller) | 
**retriever** | [**RetrieverModelInput**](RetrieverModelInput.md) | Optional retriever configuration override for testing. If omitted, uses the retriever configured in the taxonomy. | [optional] 
**source_documents** | **List[Dict[str, object]]** | Sample documents to test enrichment (typically 1-5 docs). Results are returned immediately, not persisted. ⚠️ Do NOT pass collection_id expecting batch processing! | [optional] 
**source_collection_id** | **str** | ⚠️ IGNORED IN ON_DEMAND MODE. This field exists for legacy compatibility only. To enrich collections, use taxonomy_applications on the collection. | [optional] 
**target_collection_id** | **str** | ⚠️ IGNORED IN ON_DEMAND MODE. This field exists for legacy compatibility only. Results are never persisted via this endpoint. | [optional] 
**join_mode** | [**JoinMode**](JoinMode.md) | Must be &#39;on_demand&#39;. BATCH mode is NOT supported via API. Batch enrichment is automatic (triggered by engine during ingestion). | [optional] 
**batch_size** | **int** | Batch size for the scroll iterator | [optional] [default to 1000]
**scroll_filters** | [**LogicalOperatorInput**](LogicalOperatorInput.md) | Additional filters applied to the source collection prior to enrichment. | [optional] 

## Example

```python
from mixpeek.models.execute_taxonomy_request import ExecuteTaxonomyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExecuteTaxonomyRequest from a JSON string
execute_taxonomy_request_instance = ExecuteTaxonomyRequest.from_json(json)
# print the JSON string representation of the object
print(ExecuteTaxonomyRequest.to_json())

# convert the object into a dict
execute_taxonomy_request_dict = execute_taxonomy_request_instance.to_dict()
# create an instance of ExecuteTaxonomyRequest from a dict
execute_taxonomy_request_from_dict = ExecuteTaxonomyRequest.from_dict(execute_taxonomy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


