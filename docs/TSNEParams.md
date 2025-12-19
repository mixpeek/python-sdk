# TSNEParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** |  | [optional] [default to 'tsne']
**n_components** | **int** |  | [optional] [default to 2]
**random_state** | **int** |  | [optional] [default to 42]
**perplexity** | **float** |  | [optional] [default to 30.0]
**learning_rate** | **float** |  | [optional] [default to 200.0]

## Example

```python
from mixpeek.models.tsne_params import TSNEParams

# TODO update the JSON string below
json = "{}"
# create an instance of TSNEParams from a JSON string
tsne_params_instance = TSNEParams.from_json(json)
# print the JSON string representation of the object
print(TSNEParams.to_json())

# convert the object into a dict
tsne_params_dict = tsne_params_instance.to_dict()
# create an instance of TSNEParams from a dict
tsne_params_from_dict = TSNEParams.from_dict(tsne_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


