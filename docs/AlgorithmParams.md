# AlgorithmParams

Algorithm-specific parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**n_clusters** | **int** | Number of clusters to form | [optional] [default to 8]
**max_iter** | **int** | Maximum number of iterations per seed point before the algorithm stops | [optional] [default to 300]
**random_state** | **int** | Random seed for reproducibility | [optional] [default to 42]
**n_init** | **int** | Number of initializations to perform | [optional] [default to 1]
**tol** | **float** | Convergence threshold | [optional] [default to 0.001]
**init** | **str** | Method for initialization (&#39;k-means++&#39; or &#39;random&#39;) | [optional] [default to 'k-means++']
**verbose** | **int** | Enable verbose output | [optional] [default to 0]
**copy_x** | **bool** | If True, the original data is not modified | [optional] [default to True]
**algorithm** | **str** | Algorithm to compute pointwise distances (&#39;auto&#39;, &#39;ball_tree&#39;, &#39;kd_tree&#39;, &#39;brute&#39;) | [optional] [default to 'auto']
**eps** | **float** | Maximum distance for DBSCAN cluster extraction method | [optional] 
**min_samples** | **int** | Number of samples in a neighborhood for a point to be considered a core point | [optional] [default to 5]
**metric** | **str** | Metric to use for distance computation | [optional] [default to 'minkowski']
**metric_params** | **object** | Additional keyword arguments for the metric function | [optional] 
**leaf_size** | **int** | Leaf size passed to BallTree or KDTree | [optional] [default to 30]
**p** | **float** | Parameter for the Minkowski metric | [optional] [default to 2]
**n_jobs** | **int** | Number of parallel jobs to run (-1 means using all processors) | [optional] [default to 1]
**min_cluster_size** | **float** | Minimum number of samples in a cluster. Can be a fraction if &lt; 1.0 | [optional] 
**cluster_selection_epsilon** | **float** | A distance threshold for cluster selection. Clusters below this value will be merged | [optional] [default to 0.0]
**max_cluster_size** | **int** | Maximum number of samples in a cluster. Clusters above this size will be split | [optional] 
**alpha** | **float** | A distance scaling parameter | [optional] [default to 1.0]
**cluster_selection_method** | **str** | Method to select clusters from the condensed tree (&#39;eom&#39; or &#39;leaf&#39;) | [optional] [default to 'eom']
**allow_single_cluster** | **bool** | Allow HDBSCAN to find only a single cluster | [optional] [default to False]
**prediction_data** | **bool** | Whether to generate extra data for predicting cluster membership | [optional] [default to False]
**match_reference_implementation** | **bool** | Whether to match the reference implementation exactly | [optional] [default to False]
**affinity** | **str** | How to construct the affinity matrix (&#39;nearest_neighbors&#39;, &#39;rbf&#39;, &#39;precomputed&#39;, &#39;precomputed_nearest_neighbors&#39;) | [optional] [default to 'rbf']
**memory** | **str** | Path to the caching directory | [optional] 
**connectivity** | **object** |  | [optional] 
**compute_full_tree** | **str** | Whether to compute the full tree (&#39;auto&#39;, True, or False) | [optional] [default to 'auto']
**linkage** | **str** | Linkage criterion (&#39;ward&#39;, &#39;complete&#39;, &#39;average&#39;, &#39;single&#39;) | [optional] [default to 'ward']
**distance_threshold** | **float** | The linkage distance threshold above which clusters will not be merged | [optional] 
**compute_distances** | **bool** | Whether to compute distances between clusters | [optional] [default to False]
**eigen_solver** | **str** | The eigenvalue decomposition strategy (&#39;arpack&#39;, &#39;lobpcg&#39;, &#39;amg&#39;, or None) | [optional] 
**n_components** | **int** | Number of mixture components | [optional] [default to 1]
**gamma** | **float** | Kernel coefficient for rbf, poly, sigmoid, laplacian and chi2 kernels | [optional] [default to 1.0]
**n_neighbors** | **int** | Number of neighbors to use when constructing the affinity matrix using nearest neighbors | [optional] [default to 10]
**eigen_tol** | **float** | Stopping criterion for eigendecomposition | [optional] [default to 0.0]
**assign_labels** | **str** | Strategy to assign labels in the embedding space (&#39;kmeans&#39; or &#39;discretize&#39;) | [optional] [default to 'kmeans']
**degree** | **float** | Degree of the polynomial kernel. Ignored by other kernels | [optional] [default to 3]
**coef0** | **float** | Zero coefficient for polynomial and sigmoid kernels | [optional] [default to 1]
**kernel_params** | **object** | Parameters for the kernel function | [optional] 
**covariance_type** | **str** | Type of covariance parameters (&#39;full&#39;, &#39;tied&#39;, &#39;diag&#39;, &#39;spherical&#39;) | [optional] [default to 'full']
**reg_covar** | **float** | Regularization added to the diagonal of covariance | [optional] [default to 1.0E-6]
**init_params** | **str** | Method used to initialize weights, means and covariances (&#39;kmeans&#39; or &#39;random&#39;) | [optional] [default to 'kmeans']
**weights_init** | **List[object]** | Initial weights | [optional] 
**means_init** | **List[object]** | Initial means | [optional] 
**precisions_init** | **List[object]** | Initial precisions | [optional] 
**warm_start** | **bool** | If True, use the solution of the last fit as initialization | [optional] [default to False]
**verbose_interval** | **int** | Number of iterations between each verbose message | [optional] [default to 10]
**bandwidth** | **float** | Bandwidth used in the RBF kernel. If None, estimated using sklearn.cluster.estimate_bandwidth | [optional] 
**seeds** | **List[List[float]]** | Seeds used to initialize kernels. If None, all points are used as seeds | [optional] 
**bin_seeding** | **bool** | If true, initial kernel locations are discretized into a grid to speed up algorithm | [optional] [default to False]
**min_bin_freq** | **int** | Minimum number of seeds within a bin for the bin to be considered | [optional] [default to 1]
**cluster_all** | **bool** | If true, all points are clustered, even orphans. If false, orphans are given label -1 | [optional] [default to True]
**max_eps** | **float** | Maximum distance between two samples. Default (None) means no maximum distance | [optional] 
**cluster_method** | **str** | Method to extract clusters (&#39;xi&#39; or &#39;dbscan&#39;) | [optional] [default to 'xi']
**xi** | **float** | Minimum steepness on the reachability plot for cluster boundary (xi method) | [optional] [default to 0.05]
**predecessor_correction** | **bool** | Correct clusters based on predecessors (xi method) | [optional] [default to True]

## Example

```python
from mixpeek.models.algorithm_params import AlgorithmParams

# TODO update the JSON string below
json = "{}"
# create an instance of AlgorithmParams from a JSON string
algorithm_params_instance = AlgorithmParams.from_json(json)
# print the JSON string representation of the object
print(AlgorithmParams.to_json())

# convert the object into a dict
algorithm_params_dict = algorithm_params_instance.to_dict()
# create an instance of AlgorithmParams from a dict
algorithm_params_from_dict = AlgorithmParams.from_dict(algorithm_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


