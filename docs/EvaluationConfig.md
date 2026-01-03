# EvaluationConfig

Configuration for an evaluation run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**k_values** | **List[int]** | K values for Precision@K, Recall@K, NDCG@K, etc. | [optional] [default to [1, 5, 10, 20]]
**metrics** | **List[str]** | List of metrics to calculate. Available: precision, recall, f1, map, ndcg, mrr | [optional] [default to [precision, recall, f1, map, ndcg, mrr]]

## Example

```python
from mixpeek.models.evaluation_config import EvaluationConfig

# TODO update the JSON string below
json = "{}"
# create an instance of EvaluationConfig from a JSON string
evaluation_config_instance = EvaluationConfig.from_json(json)
# print the JSON string representation of the object
print(EvaluationConfig.to_json())

# convert the object into a dict
evaluation_config_dict = evaluation_config_instance.to_dict()
# create an instance of EvaluationConfig from a dict
evaluation_config_from_dict = EvaluationConfig.from_dict(evaluation_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


