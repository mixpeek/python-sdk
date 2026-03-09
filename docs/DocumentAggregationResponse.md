# DocumentAggregationResponse

Response containing document aggregation results.  Returns aggregated statistics grouped by specified fields.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[AggregationResult]**](AggregationResult.md) | List of aggregation results, one per group. | 
**total_groups** | **int** | Total number of unique groups returned. | 
**query_info** | **Dict[str, object]** | Additional information about the query execution. May include collection info, pipeline stages, execution time, etc. | [optional] 

## Example

```python
from mixpeek.models.document_aggregation_response import DocumentAggregationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentAggregationResponse from a JSON string
document_aggregation_response_instance = DocumentAggregationResponse.from_json(json)
# print the JSON string representation of the object
print(DocumentAggregationResponse.to_json())

# convert the object into a dict
document_aggregation_response_dict = document_aggregation_response_instance.to_dict()
# create an instance of DocumentAggregationResponse from a dict
document_aggregation_response_from_dict = DocumentAggregationResponse.from_dict(document_aggregation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


