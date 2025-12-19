# ClusterMember

Represents a member of a cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | ID of the document in the cluster | 
**cluster_id** | **str** | ID of the cluster this document belongs to | 
**distance_to_centroid** | **float** | Distance from document to cluster centroid | 
**coordinates** | **List[float]** | Feature vector/coordinates of this document in the clustering space | 
**source_details** | [**SourceDetails**](SourceDetails.md) | Source information for the document | 
**features** | **Dict[str, object]** | Additional features/metadata for this document | [optional] 

## Example

```python
from mixpeek.models.cluster_member import ClusterMember

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterMember from a JSON string
cluster_member_instance = ClusterMember.from_json(json)
# print the JSON string representation of the object
print(ClusterMember.to_json())

# convert the object into a dict
cluster_member_dict = cluster_member_instance.to_dict()
# create an instance of ClusterMember from a dict
cluster_member_from_dict = ClusterMember.from_dict(cluster_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


