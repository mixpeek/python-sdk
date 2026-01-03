# IndexRecommendation

MongoDB index recommendation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** | Field to index | 
**query_count** | **int** | Number of queries using this field | 
**avg_latency_ms** | **float** | Average latency | 
**p95_latency_ms** | **float** | 95th percentile latency | 
**slow_query_count** | **int** | Queries slower than 500ms | 
**very_slow_query_count** | **int** | Queries slower than 1000ms | 
**priority_score** | **float** | Priority score for indexing | 
**recommendation** | **str** | Human-readable recommendation level | 
**mongodb_index_command** | **str** | Ready-to-use MongoDB index command | 

## Example

```python
from mixpeek.models.index_recommendation import IndexRecommendation

# TODO update the JSON string below
json = "{}"
# create an instance of IndexRecommendation from a JSON string
index_recommendation_instance = IndexRecommendation.from_json(json)
# print the JSON string representation of the object
print(IndexRecommendation.to_json())

# convert the object into a dict
index_recommendation_dict = index_recommendation_instance.to_dict()
# create an instance of IndexRecommendation from a dict
index_recommendation_from_dict = IndexRecommendation.from_dict(index_recommendation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


