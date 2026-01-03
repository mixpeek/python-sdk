# InteractionTuningRecommendation

Recommendation for interaction tuning.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recommendation_type** | **str** | Type of recommendation | 
**current_value** | **object** |  | [optional] 
**recommended_value** | **object** |  | 
**expected_impact** | **str** | Expected performance impact | 
**confidence** | **float** | Confidence score | 
**reasoning** | **str** | Explanation of recommendation | 

## Example

```python
from mixpeek.models.interaction_tuning_recommendation import InteractionTuningRecommendation

# TODO update the JSON string below
json = "{}"
# create an instance of InteractionTuningRecommendation from a JSON string
interaction_tuning_recommendation_instance = InteractionTuningRecommendation.from_json(json)
# print the JSON string representation of the object
print(InteractionTuningRecommendation.to_json())

# convert the object into a dict
interaction_tuning_recommendation_dict = interaction_tuning_recommendation_instance.to_dict()
# create an instance of InteractionTuningRecommendation from a dict
interaction_tuning_recommendation_from_dict = InteractionTuningRecommendation.from_dict(interaction_tuning_recommendation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


