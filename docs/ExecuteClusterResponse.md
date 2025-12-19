# ExecuteClusterResponse

Response from cluster execution.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether clustering was successful | 
**run_id** | **str** | Unique identifier for this clustering run | [optional] 
**algorithm** | [**ClusteringAlgorithm**](ClusteringAlgorithm.md) | Algorithm used for clustering | 
**num_clusters** | **int** | Number of clusters found | 
**num_documents** | **int** | Number of documents clustered | 
**centroids** | [**List[ClusterCentroid]**](ClusterCentroid.md) | Cluster centroids with features | 
**metrics** | **Dict[str, float]** | Clustering quality metrics | [optional] 
**parquet_path** | **str** | S3 key path to parquet file with full results | [optional] 
**members_key** | **str** | S3 key to members.parquet (if saved) | [optional] 
**execution_time_ms** | **int** | Total execution time in milliseconds | 
**created_at** | **datetime** | Timestamp of clustering | [optional] 

## Example

```python
from mixpeek.models.execute_cluster_response import ExecuteClusterResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExecuteClusterResponse from a JSON string
execute_cluster_response_instance = ExecuteClusterResponse.from_json(json)
# print the JSON string representation of the object
print(ExecuteClusterResponse.to_json())

# convert the object into a dict
execute_cluster_response_dict = execute_cluster_response_instance.to_dict()
# create an instance of ExecuteClusterResponse from a dict
execute_cluster_response_from_dict = ExecuteClusterResponse.from_dict(execute_cluster_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


