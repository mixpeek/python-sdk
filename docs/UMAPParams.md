# UMAPParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** |  | [optional] [default to 'umap']
**n_components** | **int** |  | [optional] [default to 2]
**random_state** | **int** |  | [optional] [default to 42]
**n_neighbors** | **int** |  | [optional] [default to 15]
**min_dist** | **float** |  | [optional] [default to 0.1]

## Example

```python
from mixpeek.models.umap_params import UMAPParams

# TODO update the JSON string below
json = "{}"
# create an instance of UMAPParams from a JSON string
umap_params_instance = UMAPParams.from_json(json)
# print the JSON string representation of the object
print(UMAPParams.to_json())

# convert the object into a dict
umap_params_dict = umap_params_instance.to_dict()
# create an instance of UMAPParams from a dict
umap_params_from_dict = UMAPParams.from_dict(umap_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


