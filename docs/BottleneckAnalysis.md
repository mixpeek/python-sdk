# BottleneckAnalysis

Bottleneck analysis result.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stage_name** | **str** | Stage name | 
**component** | **str** | Component | 
**execution_count** | **int** | Number of executions | 
**total_time_ms** | **float** | Total time spent | 
**avg_time_ms** | **float** | Average time per execution | 
**pct_of_total** | **float** | Percentage of total execution time | 
**rank** | **int** | Bottleneck ranking (1 &#x3D; worst) | 

## Example

```python
from mixpeek.models.bottleneck_analysis import BottleneckAnalysis

# TODO update the JSON string below
json = "{}"
# create an instance of BottleneckAnalysis from a JSON string
bottleneck_analysis_instance = BottleneckAnalysis.from_json(json)
# print the JSON string representation of the object
print(BottleneckAnalysis.to_json())

# convert the object into a dict
bottleneck_analysis_dict = bottleneck_analysis_instance.to_dict()
# create an instance of BottleneckAnalysis from a dict
bottleneck_analysis_from_dict = BottleneckAnalysis.from_dict(bottleneck_analysis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


