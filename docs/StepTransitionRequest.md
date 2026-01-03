# StepTransitionRequest

API request model for step transition analytics.  This model extends the engine query model with API-specific validation and documentation.  Use this to analyze how documents transition from one taxonomy step to another, computing conversion rates, durations, and predictor lifts.  Example:     ```json     {         \"collection_id\": \"col_emails\",         \"taxonomy_id\": \"tax_sales_stages\",         \"from_step\": \"inquiry\",         \"to_step\": \"closed_won\",         \"max_window_days\": 90,         \"min_support\": 10     }     ```  Response includes:     - Conversion rate (% reaching to_step)     - Duration statistics (mean, median, p90, p95)     - Top predictors (covariates with highest lift)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_id** | **str** | Collection to analyze for step transitions | 
**taxonomy_id** | **str** | Taxonomy ID (each taxonomy_id is immutable, clone creates new ID) | 
**from_step** | **str** | Starting step label (e.g., &#39;inquiry&#39;, &#39;draft&#39;) | 
**to_step** | **str** | Ending step label (e.g., &#39;closed_won&#39;, &#39;published&#39;) | 
**max_window_days** | **int** | Maximum days between from_step and to_step. Sequences exceeding this are excluded. | [optional] 
**filters** | **Dict[str, object]** | Optional filters for events (e.g., {&#39;metadata.region&#39;: &#39;US&#39;}) | [optional] 
**override_step_analytics** | [**StepAnalyticsConfigInput**](StepAnalyticsConfigInput.md) | Override taxonomy&#39;s default step_analytics config for this query | [optional] 
**min_support** | **int** | Minimum number of sequences required for valid analysis | [optional] [default to 10]

## Example

```python
from mixpeek.models.step_transition_request import StepTransitionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StepTransitionRequest from a JSON string
step_transition_request_instance = StepTransitionRequest.from_json(json)
# print the JSON string representation of the object
print(StepTransitionRequest.to_json())

# convert the object into a dict
step_transition_request_dict = step_transition_request_instance.to_dict()
# create an instance of StepTransitionRequest from a dict
step_transition_request_from_dict = StepTransitionRequest.from_dict(step_transition_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


