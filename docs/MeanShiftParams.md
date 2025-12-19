# MeanShiftParams

Parameters for Mean Shift clustering algorithm.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bandwidth** | **float** | Bandwidth used in the RBF kernel. If None, estimated using sklearn.cluster.estimate_bandwidth | [optional] 
**seeds** | **List[List[float]]** | Seeds used to initialize kernels. If None, all points are used as seeds | [optional] 
**bin_seeding** | **bool** | If true, initial kernel locations are discretized into a grid to speed up algorithm | [optional] [default to False]
**min_bin_freq** | **int** | Minimum number of seeds within a bin for the bin to be considered | [optional] [default to 1]
**cluster_all** | **bool** | If true, all points are clustered, even orphans. If false, orphans are given label -1 | [optional] [default to True]
**n_jobs** | **int** | Number of parallel jobs to run (-1 means using all processors) | [optional] [default to 1]
**max_iter** | **int** | Maximum number of iterations per seed point before the algorithm stops | [optional] [default to 300]

## Example

```python
from mixpeek.models.mean_shift_params import MeanShiftParams

# TODO update the JSON string below
json = "{}"
# create an instance of MeanShiftParams from a JSON string
mean_shift_params_instance = MeanShiftParams.from_json(json)
# print the JSON string representation of the object
print(MeanShiftParams.to_json())

# convert the object into a dict
mean_shift_params_dict = mean_shift_params_instance.to_dict()
# create an instance of MeanShiftParams from a dict
mean_shift_params_from_dict = MeanShiftParams.from_dict(mean_shift_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


