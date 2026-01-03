# ListClusterExecutionsRequest

Request parameters for listing and filtering cluster execution history.  Provides flexible querying of historical clustering executions with filtering, sorting, and search capabilities. Use to build execution history UIs, compare runs over time, and analyze clustering performance trends.  Use Cases:     - Display execution history table with sorting and filtering     - Find failed executions for debugging     - Compare metrics across successful runs     - Search executions by date range or status     - Build execution timeline visualization  Query Behavior:     - Empty request {} returns all executions sorted by created_at (newest first)     - Filters, sort, and search can be combined for complex queries     - Results are paginated (use page/page_size query params)  Note:     All fields are OPTIONAL. Omit for default behavior (all executions, newest first).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**LogicalOperatorInput**](LogicalOperatorInput.md) | OPTIONAL. Complex filtering conditions for execution history. NOT REQUIRED - omit to return all executions. Structure: Logical operator (AND/OR) with array of conditions. Supported filter fields:   - status: Filter by execution status (pending/processing/completed/failed).   - created_at: Filter by execution start date (use gte/lte for ranges).   - num_clusters: Filter by number of clusters found.   - metrics.silhouette_score: Filter by quality threshold. Example filters:   - Status is completed: {operator: &#39;AND&#39;, conditions: [{field: &#39;status&#39;, value: &#39;completed&#39;, operator: &#39;&#x3D;&#x3D;&#39;}]}.   - Created in last 7 days: {operator: &#39;AND&#39;, conditions: [{field: &#39;created_at&#39;, operator: &#39;gte&#39;, value: &#39;2025-11-06T00:00:00Z&#39;}]}.   - Good quality (silhouette &gt; 0.5): {operator: &#39;AND&#39;, conditions: [{field: &#39;metrics.silhouette_score&#39;, operator: &#39;&gt;&#39;, value: 0.5}]}. Combine with OR: Status completed OR failed (exclude in-progress). | [optional] 
**sort** | [**SortOption**](SortOption.md) | OPTIONAL. Sorting configuration for results. NOT REQUIRED - defaults to created_at descending (newest first). Structure: {field: &#39;field_name&#39;, direction: &#39;asc&#39; or &#39;desc&#39;}. Sortable fields:   - created_at: Sort by execution start time (default).   - completed_at: Sort by execution finish time.   - num_clusters: Sort by cluster count.   - num_points: Sort by document count.   - metrics.silhouette_score: Sort by quality score.   - status: Sort by execution status. Common use cases:   - Newest first (default): {field: &#39;created_at&#39;, direction: &#39;desc&#39;}.   - Best quality first: {field: &#39;metrics.silhouette_score&#39;, direction: &#39;desc&#39;}.   - Failed executions first: {field: &#39;status&#39;, direction: &#39;asc&#39;} (alphabetical). | [optional] 
**search** | **str** | OPTIONAL. Full-text search query across execution metadata. NOT REQUIRED - omit for no search filtering. Searches in:   - run_id: Search by execution identifier.   - error_message: Find executions with specific error text.   - centroids.label: Search by cluster label names.   - centroids.summary: Search by cluster descriptions. Behavior:   - Case-insensitive partial matching.   - Multiple terms are AND-ed together.   - Combines with filters for complex queries. Examples:   - &#39;failed&#39; → Find executions with &#39;failed&#39; in error messages.   - &#39;product review&#39; → Find executions with clusters about products/reviews.   - &#39;run_abc123&#39; → Find specific execution by ID. | [optional] 

## Example

```python
from mixpeek.models.list_cluster_executions_request import ListClusterExecutionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListClusterExecutionsRequest from a JSON string
list_cluster_executions_request_instance = ListClusterExecutionsRequest.from_json(json)
# print the JSON string representation of the object
print(ListClusterExecutionsRequest.to_json())

# convert the object into a dict
list_cluster_executions_request_dict = list_cluster_executions_request_instance.to_dict()
# create an instance of ListClusterExecutionsRequest from a dict
list_cluster_executions_request_from_dict = ListClusterExecutionsRequest.from_dict(list_cluster_executions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


