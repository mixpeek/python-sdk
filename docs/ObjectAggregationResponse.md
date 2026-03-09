# ObjectAggregationResponse

Response containing object aggregation results.  Returns aggregated statistics grouped by specified fields.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[AggregationResult]**](AggregationResult.md) | List of aggregation results, one per group. | 
**total_groups** | **int** | Total number of unique groups returned. | 
**query_info** | **Dict[str, object]** | Additional information about the query execution. May include pipeline stages, execution time, etc. | [optional] 

## Example

```python
from mixpeek.models.object_aggregation_response import ObjectAggregationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectAggregationResponse from a JSON string
object_aggregation_response_instance = ObjectAggregationResponse.from_json(json)
# print the JSON string representation of the object
print(ObjectAggregationResponse.to_json())

# convert the object into a dict
object_aggregation_response_dict = object_aggregation_response_instance.to_dict()
# create an instance of ObjectAggregationResponse from a dict
object_aggregation_response_from_dict = ObjectAggregationResponse.from_dict(object_aggregation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


