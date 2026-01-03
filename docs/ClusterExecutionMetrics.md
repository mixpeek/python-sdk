# ClusterExecutionMetrics

Quality metrics for evaluating clustering execution performance.  Provides statistical measures to assess the quality of the clustering results. Higher quality clusters have better cohesion (documents within clusters are similar) and separation (clusters are distinct from each other).  Use Cases:     - Compare quality across multiple clustering executions     - Determine optimal number of clusters for a dataset     - Validate clustering algorithm performance     - Track clustering quality over time     - Debug clustering issues (poor metrics indicate problems)  Interpretation:     - Use silhouette_score as primary quality indicator (0.5+ = good, 0.7+ = excellent)     - Lower davies_bouldin_index indicates better-separated clusters     - Higher calinski_harabasz_score indicates denser, better-separated clusters  Note:     All metrics are OPTIONAL and only present if clustering completed successfully.     Failed executions return null for all metrics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**silhouette_score** | **float** | OPTIONAL. Silhouette score measuring cluster cohesion and separation. Range: -1 to +1. Interpretation:   +1.0 &#x3D; Perfect clustering (documents far from other clusters, close to own cluster).   0.0 &#x3D; Overlapping clusters (documents on cluster boundaries).   -1.0 &#x3D; Poor clustering (documents assigned to wrong clusters). Practical thresholds:   0.7 to 1.0 &#x3D; Excellent clustering.   0.5 to 0.7 &#x3D; Good clustering.   0.25 to 0.5 &#x3D; Weak clustering, consider different parameters.   Below 0.25 &#x3D; Poor clustering, reconfigure or more data needed. null &#x3D; metric not calculated (too few points or clustering failed). | [optional] 
**davies_bouldin_index** | **float** | OPTIONAL. Davies-Bouldin index measuring cluster separation. Range: 0 to +∞ (lower is better, no upper bound). Interpretation:   0.0 &#x3D; Perfect separation (impossible in practice).   0.0 to 1.0 &#x3D; Excellent separation.   1.0 to 2.0 &#x3D; Good separation.   Above 2.0 &#x3D; Poor separation, clusters overlap. Formula: Average ratio of intra-cluster to inter-cluster distances. Use when: Validating that clusters are distinct and well-separated. null &#x3D; metric not calculated (too few points or clustering failed). | [optional] 
**calinski_harabasz_score** | **float** | OPTIONAL. Calinski-Harabasz score (also called Variance Ratio Criterion). Range: 0 to +∞ (higher is better, no strict upper bound). Interpretation:   Higher values indicate denser, more compact clusters.   No universal threshold - compare relative values across runs.   Typical good values: 100-1000+ (dataset dependent). Formula: Ratio of between-cluster to within-cluster dispersion. Use when: Comparing different numbers of clusters for the same dataset. Note: Biased toward algorithms that produce spherical, equally-sized clusters. null &#x3D; metric not calculated (too few points or clustering failed). | [optional] 

## Example

```python
from mixpeek.models.cluster_execution_metrics import ClusterExecutionMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterExecutionMetrics from a JSON string
cluster_execution_metrics_instance = ClusterExecutionMetrics.from_json(json)
# print the JSON string representation of the object
print(ClusterExecutionMetrics.to_json())

# convert the object into a dict
cluster_execution_metrics_dict = cluster_execution_metrics_instance.to_dict()
# create an instance of ClusterExecutionMetrics from a dict
cluster_execution_metrics_from_dict = ClusterExecutionMetrics.from_dict(cluster_execution_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


