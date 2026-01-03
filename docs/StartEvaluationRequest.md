# StartEvaluationRequest

Request to start an evaluation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset_name** | **str** | Name of the evaluation dataset to use | 
**evaluation_config** | [**EvaluationConfig**](EvaluationConfig.md) | Optional evaluation configuration (uses defaults if not provided) | [optional] 

## Example

```python
from mixpeek.models.start_evaluation_request import StartEvaluationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StartEvaluationRequest from a JSON string
start_evaluation_request_instance = StartEvaluationRequest.from_json(json)
# print the JSON string representation of the object
print(StartEvaluationRequest.to_json())

# convert the object into a dict
start_evaluation_request_dict = start_evaluation_request_instance.to_dict()
# create an instance of StartEvaluationRequest from a dict
start_evaluation_request_from_dict = StartEvaluationRequest.from_dict(start_evaluation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


