# Payload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taxonomy** | [**TaxonomyModel**](TaxonomyModel.md) | Full taxonomy model with configuration (fetched from DB by controller) | 
**retriever** | [**RetrieverModelInput**](RetrieverModelInput.md) | Optional retriever configuration override for testing. If omitted, uses the retriever configured in the taxonomy. | [optional] 
**source_documents** | **List[Dict[str, object]]** | Optional documents to enrich for testing. If omitted, validates configuration without processing documents. | [optional] 
**source_collection_id** | **str** | Collection reference (for context/logging only in ON_DEMAND mode) | [optional] 
**target_collection_id** | **str** | Not used in ON_DEMAND mode. | [optional] 
**join_mode** | [**JoinMode**](JoinMode.md) | Must be &#x60;on_demand&#x60;. Batch mode is not supported via API. | [optional] 
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


