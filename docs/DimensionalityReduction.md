# DimensionalityReduction

Optional dimensionality reduction prior to clustering

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** |  | [optional] [default to 'none']
**n_components** | **int** |  | [optional] [default to 2]
**random_state** | **int** |  | [optional] [default to 42]
**perplexity** | **float** |  | [optional] [default to 30.0]
**learning_rate** | **float** |  | [optional] [default to 200.0]
**n_neighbors** | **int** |  | [optional] [default to 15]
**min_dist** | **float** |  | [optional] [default to 0.1]

## Example

```python
from mixpeek.models.dimensionality_reduction import DimensionalityReduction

# TODO update the JSON string below
json = "{}"
# create an instance of DimensionalityReduction from a JSON string
dimensionality_reduction_instance = DimensionalityReduction.from_json(json)
# print the JSON string representation of the object
print(DimensionalityReduction.to_json())

# convert the object into a dict
dimensionality_reduction_dict = dimensionality_reduction_instance.to_dict()
# create an instance of DimensionalityReduction from a dict
dimensionality_reduction_from_dict = DimensionalityReduction.from_dict(dimensionality_reduction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


