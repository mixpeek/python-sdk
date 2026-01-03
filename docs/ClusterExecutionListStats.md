# ClusterExecutionListStats

Aggregate statistics calculated across all executions in the current result set.  Provides summary metrics for the filtered/searched execution history, useful for dashboards, monitoring, and trend analysis. Statistics are calculated only for the executions returned in the current query (respects filters and pagination).  Use Cases:     - Display execution summary cards (\"5 completed, 2 failed, 3 pending\")     - Show average execution time trend     - Monitor clustering performance over time     - Build execution health dashboard     - Compare stats across different time periods (via filters)  Important:     Stats reflect only the current result set, not all historical executions.     Apply filters to calculate stats for specific time ranges or statuses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_executions** | **int** | OPTIONAL (always provided). Total number of executions in current result set. Equals length of results array. Use for:   - Display total count in UI (&#39;Showing 10 of 100 executions&#39;).   - Validate pagination (total should match page_size × pages).   - Check if filters returned any results (0 &#x3D; no matches). Note: This is the count in the current page, not all executions. | [optional] [default to 0]
**executions_by_status** | **Dict[str, int]** | OPTIONAL (always provided). Count of executions grouped by status. Keys: &#39;pending&#39;, &#39;processing&#39;, &#39;completed&#39;, &#39;failed&#39;. Values: Number of executions in each status. Use for:   - Status distribution chart (pie/bar chart).   - Health monitoring (high failed count &#x3D; problem).   - Progress tracking (pending + processing &#x3D; in-flight jobs). Example: {&#39;completed&#39;: 45, &#39;failed&#39;: 3, &#39;processing&#39;: 2, &#39;pending&#39;: 0}. Empty dict {} if no executions in result set. | [optional] 
**avg_execution_time_ms** | **float** | OPTIONAL (always provided). Average execution duration in milliseconds. Calculated as: mean(completed_at - created_at) for completed/failed executions. Excludes pending/processing executions (no completed_at yet). Use for:   - Performance monitoring (&#39;Average: 5.2 seconds&#39;).   - Trend analysis (is clustering getting slower over time?).   - Capacity planning (estimate time for future runs). 0.0 if: No completed/failed executions in result set. Typical values:   - Small datasets (&lt; 100 docs): 1000-5000ms (1-5 seconds).   - Medium datasets (100-1000 docs): 5000-30000ms (5-30 seconds).   - Large datasets (1000+ docs): 30000-300000ms (30 seconds - 5 minutes). | [optional] [default to 0.0]
**total_documents_clustered** | **int** | OPTIONAL (always provided). Total documents processed across all executions. Calculated as: sum(num_points) for all executions in result set. Use for:   - Volume tracking (&#39;Processed 10,000 documents&#39;).   - Cost estimation (larger datasets &#x3D; more compute).   - Data growth monitoring (compare over time). 0 if: No executions in result set. Note: Same document may be counted multiple times if re-clustered. | [optional] [default to 0]
**avg_num_clusters** | **float** | OPTIONAL (always provided). Average number of clusters found per execution. Calculated as: mean(num_clusters) for all executions in result set. Use for:   - Clustering consistency check (stable avg &#x3D; consistent results).   - Algorithm tuning (avg too high/low may need parameter adjustment).   - Trend analysis (is clustering finding more/fewer clusters over time?). 0.0 if: No executions in result set. Typical values:   - Under-clustering: &lt; 3 clusters (data may be too diverse).   - Good clustering: 3-20 clusters (manageable, meaningful groups).   - Over-clustering: &gt; 20 clusters (too granular, hard to interpret). | [optional] [default to 0.0]

## Example

```python
from mixpeek.models.cluster_execution_list_stats import ClusterExecutionListStats

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterExecutionListStats from a JSON string
cluster_execution_list_stats_instance = ClusterExecutionListStats.from_json(json)
# print the JSON string representation of the object
print(ClusterExecutionListStats.to_json())

# convert the object into a dict
cluster_execution_list_stats_dict = cluster_execution_list_stats_instance.to_dict()
# create an instance of ClusterExecutionListStats from a dict
cluster_execution_list_stats_from_dict = ClusterExecutionListStats.from_dict(cluster_execution_list_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


