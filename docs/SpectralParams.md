# SpectralParams

Parameters for Spectral clustering algorithm.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**n_clusters** | **int** | Number of clusters to form | [optional] [default to 8]
**eigen_solver** | **str** | The eigenvalue decomposition strategy (&#39;arpack&#39;, &#39;lobpcg&#39;, &#39;amg&#39;, or None) | [optional] 
**n_components** | **int** | Number of eigenvectors to use for spectral embedding | [optional] 
**random_state** | **int** | Random seed for reproducibility | [optional] [default to 42]
**n_init** | **int** | Number of times k-means will run with different centroid seeds | [optional] [default to 10]
**gamma** | **float** | Kernel coefficient for rbf, poly, sigmoid, laplacian and chi2 kernels | [optional] [default to 1.0]
**affinity** | **str** | How to construct the affinity matrix (&#39;nearest_neighbors&#39;, &#39;rbf&#39;, &#39;precomputed&#39;, &#39;precomputed_nearest_neighbors&#39;) | [optional] [default to 'rbf']
**n_neighbors** | **int** | Number of neighbors to use when constructing the affinity matrix using nearest neighbors | [optional] [default to 10]
**eigen_tol** | **float** | Stopping criterion for eigendecomposition | [optional] [default to 0.0]
**assign_labels** | **str** | Strategy to assign labels in the embedding space (&#39;kmeans&#39; or &#39;discretize&#39;) | [optional] [default to 'kmeans']
**degree** | **float** | Degree of the polynomial kernel. Ignored by other kernels | [optional] [default to 3]
**coef0** | **float** | Zero coefficient for polynomial and sigmoid kernels | [optional] [default to 1]
**kernel_params** | **object** | Parameters for the kernel function | [optional] 
**n_jobs** | **int** | Number of parallel jobs to run (-1 means using all processors) | [optional] [default to 1]
**verbose** | **bool** | Verbosity mode | [optional] [default to False]

## Example

```python
from mixpeek.models.spectral_params import SpectralParams

# TODO update the JSON string below
json = "{}"
# create an instance of SpectralParams from a JSON string
spectral_params_instance = SpectralParams.from_json(json)
# print the JSON string representation of the object
print(SpectralParams.to_json())

# convert the object into a dict
spectral_params_dict = spectral_params_instance.to_dict()
# create an instance of SpectralParams from a dict
spectral_params_from_dict = SpectralParams.from_dict(spectral_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


