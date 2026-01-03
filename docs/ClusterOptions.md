# ClusterOptions

Options for cluster migration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preserve_cluster_ids** | **bool** | Keep same cluster IDs in target | [optional] [default to True]
**preserve_assignments** | **bool** | Keep cluster_id in documents | [optional] [default to True]
**migrate_artifacts** | **bool** | Copy parquet artifacts from S3 | [optional] [default to True]
**preserve_centroids** | **bool** | Keep centroid collections | [optional] [default to True]
**recompute_clusters** | **bool** | Recompute clusters instead of copying | [optional] [default to False]

## Example

```python
from mixpeek.models.cluster_options import ClusterOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterOptions from a JSON string
cluster_options_instance = ClusterOptions.from_json(json)
# print the JSON string representation of the object
print(ClusterOptions.to_json())

# convert the object into a dict
cluster_options_dict = cluster_options_instance.to_dict()
# create an instance of ClusterOptions from a dict
cluster_options_from_dict = ClusterOptions.from_dict(cluster_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


