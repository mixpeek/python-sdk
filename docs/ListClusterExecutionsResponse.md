# ListClusterExecutionsResponse

Complete response for cluster execution history listing endpoint.  Returns paginated execution history with filtering, sorting, and aggregate statistics. Use to build execution history UIs, monitoring dashboards, and performance analytics.  Response Structure:     - results: Array of execution details (paginated)     - pagination: Page navigation info (current page, total pages, etc.)     - total_count: Total matching executions (across all pages)     - stats: Aggregated metrics for current result set  Use Cases:     - Build execution history table with pagination     - Display execution status dashboard with charts     - Monitor clustering performance trends     - Debug failed executions     - Compare quality metrics across runs  Pagination Behavior:     - Default: 10 executions per page     - Use query params: ?page=1&page_size=20     - results contains current page only     - total_count shows all matching executions     - pagination provides navigation links  Example Workflow:     1. Request: POST /clusters/{id}/executions/list with filters     2. Response: 50 total executions, showing page 1 (10 results)     3. Display: Show 10 results + \"Page 1 of 5\" + aggregate stats     4. Navigate: Use pagination.next_page for next 10 results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ClusterExecutionResult]**](ClusterExecutionResult.md) | REQUIRED. Array of cluster execution results for the current page. Length: 0 to page_size (default 10, max typically 100). Empty array [] if:   - No executions exist for this cluster.   - Filters matched no results.   - Requested page beyond available pages. Sorted by: created_at descending (newest first) by default. Override with sort parameter in request. Each item contains:   - run_id: Unique execution identifier.   - status: pending/processing/completed/failed.   - num_clusters: Clusters found.   - metrics: Quality scores (if available).   - centroids: Cluster labels and summaries (if available).   - created_at/completed_at: Timestamps.   - error_message: Error details (if failed). Use for: Rendering execution history table rows. | 
**pagination** | [**PaginationResponse**](PaginationResponse.md) | REQUIRED. Pagination metadata for navigating result pages. Contains:   - total: Total items across all pages (same as total_count).   - page: Current page number (1-indexed).   - page_size: Items per page.   - total_pages: Total number of pages.   - next_page: URL for next page (null if last page).   - previous_page: URL for previous page (null if first page). Use for:   - Pagination controls (&#39;Page 2 of 5&#39;).   - Next/Previous buttons (check null for disabled state).   - Showing X-Y of Z results calculations. | 
**total_count** | **int** | REQUIRED. Total number of executions matching the query across ALL pages. Use for:   - Display total count (&#39;Found 127 executions&#39;).   - Calculate pagination (&#39;Showing 1-10 of 127&#39;).   - Validate filters (0 &#x3D; no matches, refine query). Behavior:   - Includes all filtered results, not just current page.   - Changes when filters are applied.   - Equals len(results) only if all results fit on one page. Example:   - Query returns 127 executions total.   - Page size &#x3D; 10.   - Current page (1) shows results[0:10].   - total_count &#x3D; 127 (not 10). | 
**stats** | [**ClusterExecutionListStats**](ClusterExecutionListStats.md) | OPTIONAL. Aggregate statistics for executions in current result set. NOT REQUIRED - may be null if stats calculation disabled. Typically always provided for execution listing. Contains:   - total_executions: Count in current page.   - executions_by_status: Status distribution {&#39;completed&#39;: 45, &#39;failed&#39;: 3}.   - avg_execution_time_ms: Mean duration.   - total_documents_clustered: Sum of all processed documents.   - avg_num_clusters: Mean clusters per execution. Use for:   - Summary cards above table.   - Status pie chart.   - Performance metrics dashboard. Note:   - Stats calculated for current page only (or all if no pagination).   - Respects filters (stats for filtered subset). | [optional] 

## Example

```python
from mixpeek.models.list_cluster_executions_response import ListClusterExecutionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListClusterExecutionsResponse from a JSON string
list_cluster_executions_response_instance = ListClusterExecutionsResponse.from_json(json)
# print the JSON string representation of the object
print(ListClusterExecutionsResponse.to_json())

# convert the object into a dict
list_cluster_executions_response_dict = list_cluster_executions_response_instance.to_dict()
# create an instance of ListClusterExecutionsResponse from a dict
list_cluster_executions_response_from_dict = ListClusterExecutionsResponse.from_dict(list_cluster_executions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


