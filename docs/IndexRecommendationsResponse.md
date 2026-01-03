# IndexRecommendationsResponse

Response for index recommendations endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespace_id** | **str** | Namespace ID analyzed | 
**time_range_days** | **int** | Number of days analyzed | 
**recommendations** | [**List[IndexRecommendation]**](IndexRecommendation.md) | Index recommendations | 
**summary** | **Dict[str, int]** | Summary statistics (high_priority, medium_priority, low_priority counts) | 

## Example

```python
from mixpeek.models.index_recommendations_response import IndexRecommendationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IndexRecommendationsResponse from a JSON string
index_recommendations_response_instance = IndexRecommendationsResponse.from_json(json)
# print the JSON string representation of the object
print(IndexRecommendationsResponse.to_json())

# convert the object into a dict
index_recommendations_response_dict = index_recommendations_response_instance.to_dict()
# create an instance of IndexRecommendationsResponse from a dict
index_recommendations_response_from_dict = IndexRecommendationsResponse.from_dict(index_recommendations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


