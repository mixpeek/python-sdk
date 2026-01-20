# DBSCANParams

Parameters for DBSCAN clustering algorithm.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eps** | **float** | Maximum distance between two samples for one to be considered in the neighborhood of the other | [optional] [default to 0.5]
**min_samples** | **int** | Number of samples in a neighborhood for a point to be considered a core point | [optional] [default to 5]
**metric** | **str** | Metric to use for distance computation | [optional] [default to 'euclidean']
**metric_params** | **object** | Additional keyword arguments for the metric function | [optional] 
**algorithm** | **str** | Algorithm to compute pointwise distances and find nearest neighbors (&#39;auto&#39;, &#39;ball_tree&#39;, &#39;kd_tree&#39;, &#39;brute&#39;) | [optional] [default to 'auto']
**leaf_size** | **int** | Leaf size passed to BallTree or KDTree | [optional] [default to 30]
**p** | **float** | The power of the Minkowski metric to be used to calculate distance between points | [optional] [default to 2]
**n_jobs** | **int** | The number of parallel jobs to run (-1 means using all processors) | [optional] [default to 1]

## Example

```python
from mixpeek.models.dbscan_params import DBSCANParams

# TODO update the JSON string below
json = "{}"
# create an instance of DBSCANParams from a JSON string
dbscan_params_instance = DBSCANParams.from_json(json)
# print the JSON string representation of the object
print(DBSCANParams.to_json())

# convert the object into a dict
dbscan_params_dict = dbscan_params_instance.to_dict()
# create an instance of DBSCANParams from a dict
dbscan_params_from_dict = DBSCANParams.from_dict(dbscan_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


