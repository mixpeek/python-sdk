# ExecuteClusterRequest

Request to execute clustering on one or more collections.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_ids** | **List[str]** | IDs of the collections to cluster together | 
**config** | [**ClusteringConfig**](ClusteringConfig.md) | Clustering configuration including algorithm and parameters | 
**sample_size** | **int** | Number of documents to sample for clustering | [optional] 
**store_results** | **bool** | Whether to store clustering results | [optional] [default to True]
**include_members** | **bool** | Whether to include cluster membership in results | [optional] [default to False]
**compute_metrics** | **bool** | Whether to compute clustering quality metrics | [optional] [default to True]
**save_artifacts** | **bool** | Whether to save clustering artifacts (e.g., parquet) to S3 | [optional] [default to False]

## Example

```python
from mixpeek.models.execute_cluster_request import ExecuteClusterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExecuteClusterRequest from a JSON string
execute_cluster_request_instance = ExecuteClusterRequest.from_json(json)
# print the JSON string representation of the object
print(ExecuteClusterRequest.to_json())

# convert the object into a dict
execute_cluster_request_dict = execute_cluster_request_instance.to_dict()
# create an instance of ExecuteClusterRequest from a dict
execute_cluster_request_from_dict = ExecuteClusterRequest.from_dict(execute_cluster_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


