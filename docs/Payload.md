# Payload


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
from mixpeek.models.payload import Payload

# TODO update the JSON string below
json = "{}"
# create an instance of Payload from a JSON string
payload_instance = Payload.from_json(json)
# print the JSON string representation of the object
print(Payload.to_json())

# convert the object into a dict
payload_dict = payload_instance.to_dict()
# create an instance of Payload from a dict
payload_from_dict = Payload.from_dict(payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


