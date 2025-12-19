# GaussianMixtureParams

Parameters for Gaussian Mixture Model clustering.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**n_components** | **int** | Number of mixture components | [optional] [default to 1]
**covariance_type** | **str** | Type of covariance parameters (&#39;full&#39;, &#39;tied&#39;, &#39;diag&#39;, &#39;spherical&#39;) | [optional] [default to 'full']
**tol** | **float** | Convergence threshold | [optional] [default to 0.001]
**reg_covar** | **float** | Regularization added to the diagonal of covariance | [optional] [default to 1.0E-6]
**max_iter** | **int** | Maximum number of EM iterations | [optional] [default to 100]
**n_init** | **int** | Number of initializations to perform | [optional] [default to 1]
**init_params** | **str** | Method used to initialize weights, means and covariances (&#39;kmeans&#39; or &#39;random&#39;) | [optional] [default to 'kmeans']
**weights_init** | **List[object]** | Initial weights | [optional] 
**means_init** | **List[object]** | Initial means | [optional] 
**precisions_init** | **List[object]** | Initial precisions | [optional] 
**random_state** | **int** | Random seed for reproducibility | [optional] [default to 42]
**warm_start** | **bool** | If True, use the solution of the last fit as initialization | [optional] [default to False]
**verbose** | **int** | Enable verbose output | [optional] [default to 0]
**verbose_interval** | **int** | Number of iterations between each verbose message | [optional] [default to 10]

## Example

```python
from mixpeek.models.gaussian_mixture_params import GaussianMixtureParams

# TODO update the JSON string below
json = "{}"
# create an instance of GaussianMixtureParams from a JSON string
gaussian_mixture_params_instance = GaussianMixtureParams.from_json(json)
# print the JSON string representation of the object
print(GaussianMixtureParams.to_json())

# convert the object into a dict
gaussian_mixture_params_dict = gaussian_mixture_params_instance.to_dict()
# create an instance of GaussianMixtureParams from a dict
gaussian_mixture_params_from_dict = GaussianMixtureParams.from_dict(gaussian_mixture_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


