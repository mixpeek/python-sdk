# ClusteringEnrichmentResponse

Response after applying clustering enrichment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**processed** | **int** | Number of processed points | 
**enriched** | **int** | Number of enriched points | 
**failed** | **int** | Number of failed points | 
**batches** | **int** | Batches processed | 

## Example

```python
from mixpeek.models.clustering_enrichment_response import ClusteringEnrichmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClusteringEnrichmentResponse from a JSON string
clustering_enrichment_response_instance = ClusteringEnrichmentResponse.from_json(json)
# print the JSON string representation of the object
print(ClusteringEnrichmentResponse.to_json())

# convert the object into a dict
clustering_enrichment_response_dict = clustering_enrichment_response_instance.to_dict()
# create an instance of ClusteringEnrichmentResponse from a dict
clustering_enrichment_response_from_dict = ClusteringEnrichmentResponse.from_dict(clustering_enrichment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


