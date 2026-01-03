# ClusterExecutionResult

Complete results from a single clustering execution.  Represents the outcome of running a clustering algorithm on a collection's documents. Each execution creates a snapshot of clustering results at a point in time, including the clusters found, quality metrics, and semantic labels.  Use Cases:     - Display clustering execution history in UI     - Compare clustering quality across multiple runs     - Track execution status for long-running jobs     - Debug failed clustering attempts     - View cluster summaries and labels for analysis  Workflow:     1. Create cluster configuration → POST /clusters     2. Execute clustering → POST /clusters/{id}/execute     3. Poll execution status → GET /clusters/{id}/executions     4. View execution history → POST /clusters/{id}/executions/list  Status Lifecycle:     pending → processing → completed (or failed)  Note:     Execution results are immutable once completed. Re-running clustering     creates a new execution result with a new run_id.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **str** | REQUIRED. Unique identifier for this specific clustering execution. Format: &#39;run_&#39; prefix followed by random alphanumeric string. Used to retrieve specific execution artifacts and results. Each re-execution of the same cluster creates a new run_id. References execution artifacts in S3 and MongoDB. | 
**cluster_id** | **str** | REQUIRED. Parent cluster configuration that was executed. Format: &#39;clust_&#39; prefix followed by random alphanumeric string. Links this execution back to the cluster definition. Multiple executions can share the same cluster_id. | 
**status** | **str** | REQUIRED. Current status of the clustering execution. Values:   &#39;pending&#39; &#x3D; Job queued, waiting to start.   &#39;processing&#39; &#x3D; Clustering algorithm running (may take minutes for large datasets).   &#39;completed&#39; &#x3D; Clustering finished successfully, results available.   &#39;failed&#39; &#x3D; Clustering failed, check error_message for details. Status changes: pending → processing → (completed OR failed). Poll this field to track job progress. | 
**num_clusters** | **int** | REQUIRED. Number of clusters found by the clustering algorithm. Range: 1 to num_points (though typically much lower). Interpretation:   Too few clusters &#x3D; overgeneralization, may need lower n_clusters param.   Too many clusters &#x3D; overfitting, may need higher n_clusters param.   Optimal value depends on dataset and use case. Available immediately upon completion, even if metrics fail. | 
**num_points** | **int** | REQUIRED. Total number of documents/points that were clustered. Equals the count of documents in the collection at execution time. Note: This may differ across executions if documents were added/removed. Used to calculate metrics and validate clustering quality. Minimum 2 points required for clustering (1 cluster per point otherwise). | 
**metrics** | [**ClusterExecutionMetrics**](ClusterExecutionMetrics.md) | OPTIONAL. Quality metrics evaluating clustering performance. NOT REQUIRED - only present for successful executions. null if:   - Execution is still pending/processing.   - Execution failed.   - Too few points to calculate metrics (need 2+ points). Contains silhouette_score, davies_bouldin_index, calinski_harabasz_score. Use to compare quality across multiple executions. | [optional] 
**centroids** | [**List[ClusterExecutionCentroid]**](ClusterExecutionCentroid.md) | OPTIONAL. List of cluster centroids with semantic labels. NOT REQUIRED - only present for completed executions with LLM labeling enabled. Length: equals num_clusters. Each centroid contains:   - cluster_id: Identifier for the cluster (e.g., &#39;cl_0&#39;).   - num_members: Count of documents in this cluster.   - label: Human-readable cluster name (e.g., &#39;Product Reviews&#39;).   - summary: Brief description of cluster content.   - keywords: Array of representative terms. null if:   - Execution pending/processing/failed.   - LLM labeling not configured. Use for: Displaying cluster summaries in UI, filtering by cluster. | [optional] 
**created_at** | **datetime** | REQUIRED. Timestamp when the clustering execution started. ISO 8601 format with timezone (UTC). Used to:   - Sort executions chronologically.   - Calculate execution duration (completed_at - created_at).   - Filter execution history by date range. Always present, even for failed executions. | 
**completed_at** | **datetime** | OPTIONAL. Timestamp when the clustering execution finished. ISO 8601 format with timezone (UTC). NOT REQUIRED - only present for completed or failed executions. null if: status is &#39;pending&#39; or &#39;processing&#39;. Use to:   - Calculate execution duration (completed_at - created_at).   - Show when results became available. Present for both successful and failed executions. | [optional] 
**error_message** | **str** | OPTIONAL. Error message if the clustering execution failed. NOT REQUIRED - only present when status is &#39;failed&#39;. null if: execution succeeded or is still in progress. Contains:   - Human-readable error description.   - Possible causes and suggested fixes.   - Stack trace details (for debugging). Common errors:   - &#39;Insufficient documents for clustering&#39; (need 2+ docs).   - &#39;Feature extractor not found&#39; (invalid collection config).   - &#39;Out of memory&#39; (dataset too large for algorithm). Use for: Debugging failed executions and user error messages. | [optional] 
**llm_labeling_errors** | **List[str]** | OPTIONAL. List of errors encountered during LLM labeling. NOT REQUIRED - only present when LLM labeling was attempted and encountered errors. null if:   - LLM labeling was not enabled.   - LLM labeling succeeded for all clusters.   - Execution is still in progress. Each error is a JSON string containing:   - &#39;error&#39;: Human-readable error message.   - &#39;clusters&#39;: List of cluster IDs affected by this error. Common errors:   - &#39;LLM API timeout for 2 clusters&#39; (network/API issues).   - &#39;OpenAI rate limit exceeded&#39; (quota exhausted).   - &#39;Invalid model name: gpt-3.5&#39; (config error).   - &#39;No representative documents for cluster cl_3&#39; (empty cluster). Use for:   - Debugging why some clusters have fallback labels.   - Identifying LLM API issues without failing entire clustering.   - Warning users about partial labeling success. | [optional] 

## Example

```python
from mixpeek.models.cluster_execution_result import ClusterExecutionResult

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterExecutionResult from a JSON string
cluster_execution_result_instance = ClusterExecutionResult.from_json(json)
# print the JSON string representation of the object
print(ClusterExecutionResult.to_json())

# convert the object into a dict
cluster_execution_result_dict = cluster_execution_result_instance.to_dict()
# create an instance of ClusterExecutionResult from a dict
cluster_execution_result_from_dict = ClusterExecutionResult.from_dict(cluster_execution_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


