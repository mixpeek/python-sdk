# EnrichmentHistoryResponse

Taxonomy enrichment history response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taxonomy_id** | **str** |  | 
**time_range** | [**ApiAnalyticsTaxonomiesModelsTimeRange**](ApiAnalyticsTaxonomiesModelsTimeRange.md) |  | 
**metrics** | [**List[EnrichmentMetric]**](EnrichmentMetric.md) |  | 
**summary** | **object** |  | [optional] 

## Example

```python
from mixpeek.models.enrichment_history_response import EnrichmentHistoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnrichmentHistoryResponse from a JSON string
enrichment_history_response_instance = EnrichmentHistoryResponse.from_json(json)
# print the JSON string representation of the object
print(EnrichmentHistoryResponse.to_json())

# convert the object into a dict
enrichment_history_response_dict = enrichment_history_response_instance.to_dict()
# create an instance of EnrichmentHistoryResponse from a dict
enrichment_history_response_from_dict = EnrichmentHistoryResponse.from_dict(enrichment_history_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


