# KmeansParameters

Parameters for K-means clustering (deprecated, use algorithm_params)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**n_clusters** | **int** | Number of clusters to form | [optional] [default to 8]
**max_iter** | **int** | Maximum number of iterations | [optional] [default to 300]
**random_state** | **int** | Random seed for reproducibility | [optional] [default to 42]
**n_init** | **int** | Number of times k-means will run with different centroid seeds | [optional] [default to 10]
**tol** | **float** | Tolerance for convergence | [optional] [default to 1.0E-4]
**init** | **str** | Method for initialization (&#39;k-means++&#39; or &#39;random&#39;) | [optional] [default to 'k-means++']
**verbose** | **int** | Verbosity mode | [optional] [default to 0]
**copy_x** | **bool** | If True, the original data is not modified | [optional] [default to True]
**algorithm** | **str** | K-means algorithm to use (&#39;lloyd&#39;, &#39;elkan&#39;, or &#39;auto&#39;) | [optional] [default to 'lloyd']

## Example

```python
from mixpeek.models.kmeans_parameters import KmeansParameters

# TODO update the JSON string below
json = "{}"
# create an instance of KmeansParameters from a JSON string
kmeans_parameters_instance = KmeansParameters.from_json(json)
# print the JSON string representation of the object
print(KmeansParameters.to_json())

# convert the object into a dict
kmeans_parameters_dict = kmeans_parameters_instance.to_dict()
# create an instance of KmeansParameters from a dict
kmeans_parameters_from_dict = KmeansParameters.from_dict(kmeans_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


