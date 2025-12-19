# ClusterCentroid

Represents a cluster centroid with its feature vector and labels.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** | Unique identifier for the cluster | 
**centroid_vector** | **List[float]** | Feature vector representing the cluster center | 
**feature_name** | **str** | Name of the feature this centroid represents | 
**feature_dimensions** | **int** | Dimensionality of the feature vector | 
**num_members** | **int** | Number of points in this cluster | [optional] [default to 0]
**variance** | **float** | Variance/spread of the cluster | [optional] 
**label** | **str** | Human-readable label for the cluster | [optional] 
**summary** | **str** | Brief summary of cluster contents | [optional] 
**keywords** | **List[str]** | Keywords describing the cluster | [optional] 
**effective_features** | **Dict[str, object]** | Aggregated features from cluster members | [optional] 
**feature_statistics** | **Dict[str, Dict[str, float]]** | Statistics for each feature (mean, std, min, max) | [optional] 
**parent_cluster_id** | **str** | Parent cluster for hierarchical clustering | [optional] 
**child_cluster_ids** | **List[str]** | Child clusters | [optional] 
**hierarchy_level** | **int** | Level in hierarchy (0 &#x3D; root) | [optional] [default to 0]
**metadata** | **Dict[str, object]** | Additional cluster metadata | [optional] 

## Example

```python
from mixpeek.models.cluster_centroid import ClusterCentroid

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterCentroid from a JSON string
cluster_centroid_instance = ClusterCentroid.from_json(json)
# print the JSON string representation of the object
print(ClusterCentroid.to_json())

# convert the object into a dict
cluster_centroid_dict = cluster_centroid_instance.to_dict()
# create an instance of ClusterCentroid from a dict
cluster_centroid_from_dict = ClusterCentroid.from_dict(cluster_centroid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


