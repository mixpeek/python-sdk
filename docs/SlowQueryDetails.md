# SlowQueryDetails

Details of a slow query.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retriever_id** | **str** | Retriever that executed the query | 
**query** | **str** | Query input string | 
**latency_ms** | **float** | Query latency in milliseconds | 
**results_count** | **int** | Number of results returned | 
**queried_fields** | **List[str]** | List of metadata fields queried | 

## Example

```python
from mixpeek.models.slow_query_details import SlowQueryDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SlowQueryDetails from a JSON string
slow_query_details_instance = SlowQueryDetails.from_json(json)
# print the JSON string representation of the object
print(SlowQueryDetails.to_json())

# convert the object into a dict
slow_query_details_dict = slow_query_details_instance.to_dict()
# create an instance of SlowQueryDetails from a dict
slow_query_details_from_dict = SlowQueryDetails.from_dict(slow_query_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


