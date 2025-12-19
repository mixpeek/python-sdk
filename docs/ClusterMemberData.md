# ClusterMemberData

Data for a cluster member.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | Document ID | 
**cluster_label** | **str** | Assigned cluster | 
**distance_to_centroid** | **float** | Distance to cluster center | 
**coordinates** | **List[float]** | Feature vector/coordinates in clustering space | 
**metadata** | **Dict[str, object]** | Document metadata | [optional] 

## Example

```python
from mixpeek.models.cluster_member_data import ClusterMemberData

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterMemberData from a JSON string
cluster_member_data_instance = ClusterMemberData.from_json(json)
# print the JSON string representation of the object
print(ClusterMemberData.to_json())

# convert the object into a dict
cluster_member_data_dict = cluster_member_data_instance.to_dict()
# create an instance of ClusterMemberData from a dict
cluster_member_data_from_dict = ClusterMemberData.from_dict(cluster_member_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


