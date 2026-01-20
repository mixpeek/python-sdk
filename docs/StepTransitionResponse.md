# StepTransitionResponse

API response model for step transition analytics.  Contains comprehensive statistics about the A→B transition including conversion metrics, duration analysis, and predictor insights.  Example Response:     ```json     {         \"from_step\": \"inquiry\",         \"to_step\": \"closed_won\",         \"count\": 1000,         \"converted\": 350,         \"conversion_rate\": 0.35,         \"durations_sec\": {             \"mean\": 432000.0,             \"median\": 345600.0,             \"p50\": 345600.0,             \"p90\": 691200.0,             \"p95\": 864000.0,             \"std_dev\": 172800.0,             \"min\": 86400.0,             \"max\": 1209600.0         },         \"top_predictors\": [             {                 \"field\": \"Sender Domain\",                 \"value\": \"enterprise.com\",                 \"count\": 150,                 \"conversion_rate\": 0.75,                 \"lift\": 2.14             }         ],         \"metadata\": {             \"collection_id\": \"col_emails\",             \"taxonomy_id\": \"tax_sales_stages\",             \"total_events_analyzed\": 5432         }     }     ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_step** | **str** | Starting step | 
**to_step** | **str** | Ending step | 
**count** | **int** | Total number of sequences starting at from_step | 
**converted** | **int** | Number of sequences that reached to_step | 
**conversion_rate** | **float** | Percentage that converted (converted / count) | 
**durations_sec** | [**DurationStats**](DurationStats.md) | Duration statistics (None if no conversions) | [optional] 
**top_predictors** | [**List[PredictorLift]**](PredictorLift.md) | Covariates with highest lift (sorted by absolute lift) | [optional] 
**metadata** | **object** | Additional metadata (collection_id, event counts, etc.) | [optional] 

## Example

```python
from mixpeek.models.step_transition_response import StepTransitionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StepTransitionResponse from a JSON string
step_transition_response_instance = StepTransitionResponse.from_json(json)
# print the JSON string representation of the object
print(StepTransitionResponse.to_json())

# convert the object into a dict
step_transition_response_dict = step_transition_response_instance.to_dict()
# create an instance of StepTransitionResponse from a dict
step_transition_response_from_dict = StepTransitionResponse.from_dict(step_transition_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


