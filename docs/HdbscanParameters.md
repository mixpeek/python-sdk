# HdbscanParameters

Parameters for HDBSCAN clustering (deprecated, use algorithm_params)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_cluster_size** | **int** | Minimum number of samples in a cluster | [optional] [default to 5]
**min_samples** | **int** | Number of samples in a neighborhood for a point to be considered a core point. Defaults to min_cluster_size if None | [optional] 
**cluster_selection_epsilon** | **float** | A distance threshold for cluster selection. Clusters below this value will be merged | [optional] [default to 0.0]
**max_cluster_size** | **int** | Maximum number of samples in a cluster. Clusters above this size will be split | [optional] 
**metric** | **str** | Metric to use for distance computation | [optional] [default to 'euclidean']
**alpha** | **float** | A distance scaling parameter | [optional] [default to 1.0]
**cluster_selection_method** | **str** | Method to select clusters from the condensed tree (&#39;eom&#39; or &#39;leaf&#39;) | [optional] [default to 'eom']
**allow_single_cluster** | **bool** | Allow HDBSCAN to find only a single cluster | [optional] [default to False]
**prediction_data** | **bool** | Whether to generate extra data for predicting cluster membership | [optional] [default to False]
**match_reference_implementation** | **bool** | Whether to match the reference implementation exactly | [optional] [default to False]

## Example

```python
from mixpeek.models.hdbscan_parameters import HdbscanParameters

# TODO update the JSON string below
json = "{}"
# create an instance of HdbscanParameters from a JSON string
hdbscan_parameters_instance = HdbscanParameters.from_json(json)
# print the JSON string representation of the object
print(HdbscanParameters.to_json())

# convert the object into a dict
hdbscan_parameters_dict = hdbscan_parameters_instance.to_dict()
# create an instance of HdbscanParameters from a dict
hdbscan_parameters_from_dict = HdbscanParameters.from_dict(hdbscan_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


