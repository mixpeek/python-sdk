# OPTICSParams

Parameters for OPTICS clustering algorithm.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_samples** | **int** | Number of samples in a neighborhood for a point to be considered a core point | [optional] [default to 5]
**max_eps** | **float** | Maximum distance between two samples. Default (None) means no maximum distance | [optional] 
**metric** | **str** | Metric to use for distance computation | [optional] [default to 'minkowski']
**p** | **float** | Parameter for the Minkowski metric | [optional] [default to 2]
**metric_params** | **object** | Additional keyword arguments for the metric function | [optional] 
**cluster_method** | **str** | Method to extract clusters (&#39;xi&#39; or &#39;dbscan&#39;) | [optional] [default to 'xi']
**eps** | **float** | Maximum distance for DBSCAN cluster extraction method | [optional] 
**xi** | **float** | Minimum steepness on the reachability plot for cluster boundary (xi method) | [optional] [default to 0.05]
**predecessor_correction** | **bool** | Correct clusters based on predecessors (xi method) | [optional] [default to True]
**min_cluster_size** | **float** | Minimum number of samples in a cluster. Can be a fraction if &lt; 1.0 | [optional] 
**algorithm** | **str** | Algorithm to compute pointwise distances (&#39;auto&#39;, &#39;ball_tree&#39;, &#39;kd_tree&#39;, &#39;brute&#39;) | [optional] [default to 'auto']
**leaf_size** | **int** | Leaf size passed to BallTree or KDTree | [optional] [default to 30]
**n_jobs** | **int** | Number of parallel jobs to run (-1 means using all processors) | [optional] [default to 1]

## Example

```python
from mixpeek.models.optics_params import OPTICSParams

# TODO update the JSON string below
json = "{}"
# create an instance of OPTICSParams from a JSON string
optics_params_instance = OPTICSParams.from_json(json)
# print the JSON string representation of the object
print(OPTICSParams.to_json())

# convert the object into a dict
optics_params_dict = optics_params_instance.to_dict()
# create an instance of OPTICSParams from a dict
optics_params_from_dict = OPTICSParams.from_dict(optics_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


