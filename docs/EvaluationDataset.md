# EvaluationDataset

Complete evaluation dataset with metadata.  An evaluation dataset is a collection of queries with ground truth relevance labels, used to measure retriever quality.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset_id** | **str** | Unique dataset identifier | 
**dataset_name** | **str** | Human-readable dataset name | 
**description** | **str** | Dataset description | [optional] 
**queries** | [**List[GroundTruthQuery]**](GroundTruthQuery.md) | List of queries with ground truth | 
**created_at** | **datetime** | When dataset was created | 
**updated_at** | **datetime** | Last update timestamp | 
**namespace_id** | **str** | Namespace this dataset belongs to | 
**internal_id** | **str** | Internal organization ID | 
**query_count** | **int** | Number of queries in dataset | 
**metadata** | **Dict[str, object]** | Additional metadata (e.g., labeling instructions, version info) | [optional] 

## Example

```python
from mixpeek.models.evaluation_dataset import EvaluationDataset

# TODO update the JSON string below
json = "{}"
# create an instance of EvaluationDataset from a JSON string
evaluation_dataset_instance = EvaluationDataset.from_json(json)
# print the JSON string representation of the object
print(EvaluationDataset.to_json())

# convert the object into a dict
evaluation_dataset_dict = evaluation_dataset_instance.to_dict()
# create an instance of EvaluationDataset from a dict
evaluation_dataset_from_dict = EvaluationDataset.from_dict(evaluation_dataset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


