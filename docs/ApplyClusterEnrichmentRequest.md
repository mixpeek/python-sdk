# ApplyClusterEnrichmentRequest

Request to apply clustering enrichment to a collection.  Supports applying multiple clustering results in one request via `clustering_ids`. For backward compatibility, a single `clustering_id` is also accepted and up-converted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clustering_ids** | **List[str]** | Clustering result IDs to apply | 
**source_collection_id** | **str** | Collection to enrich | 
**target_collection_id** | **str** | Target collection to write enriched docs to | [optional] 
**batch_size** | **int** | Batch size for processing | [optional] [default to 1000]
**parallelism** | **int** | Parallel workers | [optional] [default to 1]

## Example

```python
from mixpeek.models.apply_cluster_enrichment_request import ApplyClusterEnrichmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyClusterEnrichmentRequest from a JSON string
apply_cluster_enrichment_request_instance = ApplyClusterEnrichmentRequest.from_json(json)
# print the JSON string representation of the object
print(ApplyClusterEnrichmentRequest.to_json())

# convert the object into a dict
apply_cluster_enrichment_request_dict = apply_cluster_enrichment_request_instance.to_dict()
# create an instance of ApplyClusterEnrichmentRequest from a dict
apply_cluster_enrichment_request_from_dict = ApplyClusterEnrichmentRequest.from_dict(apply_cluster_enrichment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


