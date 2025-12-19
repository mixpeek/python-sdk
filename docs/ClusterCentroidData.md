# ClusterCentroidData

Data for a single cluster centroid.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_label** | **str** | Cluster identifier/label | 
**centroid_vector** | **List[float]** | Centroid feature vector | 
**num_members** | **int** | Number of members in cluster | 
**metadata** | **Dict[str, object]** | Additional metadata | [optional] 

## Example

```python
from mixpeek.models.cluster_centroid_data import ClusterCentroidData

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterCentroidData from a JSON string
cluster_centroid_data_instance = ClusterCentroidData.from_json(json)
# print the JSON string representation of the object
print(ClusterCentroidData.to_json())

# convert the object into a dict
cluster_centroid_data_dict = cluster_centroid_data_instance.to_dict()
# create an instance of ClusterCentroidData from a dict
cluster_centroid_data_from_dict = ClusterCentroidData.from_dict(cluster_centroid_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


