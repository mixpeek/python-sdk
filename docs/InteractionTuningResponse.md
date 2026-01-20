# InteractionTuningResponse

Response for interaction tuning analysis.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retriever_id** | **str** | Retriever identifier | 
**analysis_period** | [**ApiAnalyticsModelsTimeRange**](ApiAnalyticsModelsTimeRange.md) | Analysis period | 
**recommendations** | [**List[InteractionTuningRecommendation]**](InteractionTuningRecommendation.md) | Tuning recommendations | 
**current_performance** | **object** | Current performance baseline | 

## Example

```python
from mixpeek.models.interaction_tuning_response import InteractionTuningResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InteractionTuningResponse from a JSON string
interaction_tuning_response_instance = InteractionTuningResponse.from_json(json)
# print the JSON string representation of the object
print(InteractionTuningResponse.to_json())

# convert the object into a dict
interaction_tuning_response_dict = interaction_tuning_response_instance.to_dict()
# create an instance of InteractionTuningResponse from a dict
interaction_tuning_response_from_dict = InteractionTuningResponse.from_dict(interaction_tuning_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


