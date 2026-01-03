# TransitionPath

Represents a multi-step path between two steps.  Tracks the intermediate steps documents take when transitioning from from_step to to_step.  Attributes:     path: Ordered sequence of steps (e.g., [\"inquiry\", \"followup\", \"proposal\", \"closed_won\"])     count: Number of sequences that followed this exact path     percentage: Percentage of all completing sequences that used this path     avg_duration_sec: Average time to complete this path  Example:     ```python     # 30% of successful conversions took this 4-step path     TransitionPath(         path=[\"inquiry\", \"followup\", \"proposal\", \"closed_won\"],         count=120,         percentage=34.3,         avg_duration_sec=604800.0  # 7 days average     )     ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **List[str]** | Ordered sequence of steps | 
**count** | **int** | Number of sequences following this path | 
**percentage** | **float** | Percentage of total completing sequences | 
**avg_duration_sec** | **float** | Average time to complete this path (seconds) | [optional] 

## Example

```python
from mixpeek.models.transition_path import TransitionPath

# TODO update the JSON string below
json = "{}"
# create an instance of TransitionPath from a JSON string
transition_path_instance = TransitionPath.from_json(json)
# print the JSON string representation of the object
print(TransitionPath.to_json())

# convert the object into a dict
transition_path_dict = transition_path_instance.to_dict()
# create an instance of TransitionPath from a dict
transition_path_from_dict = TransitionPath.from_dict(transition_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


