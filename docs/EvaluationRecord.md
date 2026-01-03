# EvaluationRecord

Complete evaluation record with results.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evaluation_id** | **str** | Unique evaluation identifier | 
**retriever_id** | **str** | ID of retriever being evaluated | 
**dataset_id** | **str** | ID of dataset used for evaluation | 
**dataset_name** | **str** | Name of dataset | 
**config** | [**EvaluationConfig**](EvaluationConfig.md) | Evaluation configuration | 
**status** | [**EvaluationStatus**](EvaluationStatus.md) | Current status | 
**created_at** | **datetime** | When evaluation was created | 
**updated_at** | **datetime** | Last update timestamp | 
**completed_at** | **datetime** | When evaluation completed | [optional] 
**namespace_id** | **str** | Namespace ID | 
**internal_id** | **str** | Internal organization ID | 
**query_count** | **int** | Number of queries evaluated | 
**overall_metrics** | **Dict[str, float]** | Aggregated metrics across all queries | [optional] 
**metrics_by_k** | **Dict[str, Dict[str, float]]** | Metrics broken down by K value (keys are string K values like &#39;5&#39;, &#39;10&#39;, &#39;20&#39;) | [optional] 
**error_message** | **str** | Error message if failed | [optional] 

## Example

```python
from mixpeek.models.evaluation_record import EvaluationRecord

# TODO update the JSON string below
json = "{}"
# create an instance of EvaluationRecord from a JSON string
evaluation_record_instance = EvaluationRecord.from_json(json)
# print the JSON string representation of the object
print(EvaluationRecord.to_json())

# convert the object into a dict
evaluation_record_dict = evaluation_record_instance.to_dict()
# create an instance of EvaluationRecord from a dict
evaluation_record_from_dict = EvaluationRecord.from_dict(evaluation_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


