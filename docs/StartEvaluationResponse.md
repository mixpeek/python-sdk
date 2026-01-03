# StartEvaluationResponse

Response when starting an evaluation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** | Task ID for tracking progress | 
**evaluation_id** | **str** | Evaluation ID | 
**task_type** | **str** | Task type | [optional] [default to 'retriever.evaluation']
**status** | **str** | Initial status | [optional] [default to 'pending']
**created_at** | **str** | Creation timestamp | 

## Example

```python
from mixpeek.models.start_evaluation_response import StartEvaluationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StartEvaluationResponse from a JSON string
start_evaluation_response_instance = StartEvaluationResponse.from_json(json)
# print the JSON string representation of the object
print(StartEvaluationResponse.to_json())

# convert the object into a dict
start_evaluation_response_dict = start_evaluation_response_instance.to_dict()
# create an instance of StartEvaluationResponse from a dict
start_evaluation_response_from_dict = StartEvaluationResponse.from_dict(start_evaluation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


