# ApplyTaxonomyRequest

Request to apply a taxonomy to an existing collection.  This endpoint triggers retroactive taxonomy materialization on all documents in a collection using distributed Ray processing.  Use Cases:     - Apply taxonomy to documents that were ingested before the taxonomy was created     - Re-apply taxonomy after taxonomy configuration changes     - Backfill enrichment data for existing collections  Requirements:     - taxonomy_id: REQUIRED - Must be an existing, valid taxonomy     - The taxonomy must already be attached to the collection via taxonomy_applications     - Documents must exist in the collection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taxonomy_id** | **str** | ID of the taxonomy to apply. REQUIRED. Must be an existing taxonomy (tax_*). The taxonomy must already be in the collection&#39;s taxonomy_applications list. | 
**scroll_filters** | **object** | Optional Qdrant filters to limit which documents are enriched. NOT REQUIRED. If not provided, all documents in the collection will be enriched. Use to process specific subsets (e.g., documents missing enrichment). | [optional] 
**batch_size** | **int** | Number of documents to process in each parallel batch. NOT REQUIRED. Defaults to 1000. Larger batches &#x3D; fewer Ray tasks but more memory per task. Smaller batches &#x3D; more Ray tasks but lower memory per task. | [optional] [default to 1000]
**parallelism** | **int** | Number of parallel Ray workers to use for processing. NOT REQUIRED. Defaults to 4. Higher parallelism &#x3D; faster processing but more cluster resources. Set based on available Ray cluster capacity. | [optional] [default to 4]

## Example

```python
from mixpeek.models.apply_taxonomy_request import ApplyTaxonomyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyTaxonomyRequest from a JSON string
apply_taxonomy_request_instance = ApplyTaxonomyRequest.from_json(json)
# print the JSON string representation of the object
print(ApplyTaxonomyRequest.to_json())

# convert the object into a dict
apply_taxonomy_request_dict = apply_taxonomy_request_instance.to_dict()
# create an instance of ApplyTaxonomyRequest from a dict
apply_taxonomy_request_from_dict = ApplyTaxonomyRequest.from_dict(apply_taxonomy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


