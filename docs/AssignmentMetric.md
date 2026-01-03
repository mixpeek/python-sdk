# AssignmentMetric

Taxonomy assignment metrics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_bucket** | **datetime** |  | 
**assignment_count** | **int** |  | 
**avg_confidence** | **float** |  | 
**unique_labels** | **int** |  | 

## Example

```python
from mixpeek.models.assignment_metric import AssignmentMetric

# TODO update the JSON string below
json = "{}"
# create an instance of AssignmentMetric from a JSON string
assignment_metric_instance = AssignmentMetric.from_json(json)
# print the JSON string representation of the object
print(AssignmentMetric.to_json())

# convert the object into a dict
assignment_metric_dict = assignment_metric_instance.to_dict()
# create an instance of AssignmentMetric from a dict
assignment_metric_from_dict = AssignmentMetric.from_dict(assignment_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


