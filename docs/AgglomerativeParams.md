# AgglomerativeParams

Parameters for Agglomerative clustering algorithm.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**n_clusters** | **int** | Number of clusters to find. Can be None if distance_threshold is not None | [optional] [default to 2]
**affinity** | **str** | Metric used to compute linkage. Can be &#39;euclidean&#39;, &#39;l1&#39;, &#39;l2&#39;, &#39;manhattan&#39;, &#39;cosine&#39;, or &#39;precomputed&#39; | [optional] [default to 'euclidean']
**memory** | **str** | Path to the caching directory | [optional] 
**connectivity** | **object** |  | [optional] 
**compute_full_tree** | **str** | Whether to compute the full tree (&#39;auto&#39;, True, or False) | [optional] [default to 'auto']
**linkage** | **str** | Linkage criterion (&#39;ward&#39;, &#39;complete&#39;, &#39;average&#39;, &#39;single&#39;) | [optional] [default to 'ward']
**distance_threshold** | **float** | The linkage distance threshold above which clusters will not be merged | [optional] 
**compute_distances** | **bool** | Whether to compute distances between clusters | [optional] [default to False]

## Example

```python
from mixpeek.models.agglomerative_params import AgglomerativeParams

# TODO update the JSON string below
json = "{}"
# create an instance of AgglomerativeParams from a JSON string
agglomerative_params_instance = AgglomerativeParams.from_json(json)
# print the JSON string representation of the object
print(AgglomerativeParams.to_json())

# convert the object into a dict
agglomerative_params_dict = agglomerative_params_instance.to_dict()
# create an instance of AgglomerativeParams from a dict
agglomerative_params_from_dict = AgglomerativeParams.from_dict(agglomerative_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


