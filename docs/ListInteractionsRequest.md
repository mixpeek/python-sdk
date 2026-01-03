# ListInteractionsRequest

Request for listing interactions with filters.  Supports both simple field filters (for common queries) and advanced LogicalOperator filters (for complex analytics). This hybrid approach follows the same pattern as the Tasks module.  Common Queries (Simple Fields):     - Filter by execution: {\"execution_id\": \"exec_abc\"}     - Filter by session: {\"session_id\": \"sess_xyz\"}     - Filter by user: {\"user_id\": \"user_123\"}  Advanced Queries (LogicalOperator):     - Range queries: {\"filters\": {\"position\": {\"lte\": 5}}}     - Complex logic: {\"filters\": {\"AND\": [...]}}     - Time ranges: {\"filters\": {\"created_at\": {\"gte\": \"2025-01-01\"}}}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**execution_id** | **str** | Filter by retriever execution ID. Most common query: find all interactions from a specific search execution. Example: &#39;exec_abc123&#39; | [optional] 
**retriever_id** | **str** | Filter by retriever ID. Compare performance across different retriever configurations. Example: &#39;ret_product_search_v2&#39; | [optional] 
**session_id** | **str** | Filter by session ID. Track user journey across multiple searches within a session. Example: &#39;sess_xyz789&#39; | [optional] 
**user_id** | **str** | Filter by user ID. Analyze behavior of specific users for personalization insights. Example: &#39;user_456&#39; | [optional] 
**feature_id** | **str** | Filter by feature/document ID. Find all interactions with a specific document across all searches. Example: &#39;doc_abc123&#39; | [optional] 
**interaction_type** | **str** | Filter by interaction type. Use to find specific behaviors like clicks, purchases, or feedback. Example: &#39;click&#39;, &#39;positive_feedback&#39; | [optional] 
**filters** | [**LogicalOperatorInput**](LogicalOperatorInput.md) | Advanced filters using LogicalOperator for complex analytics queries. Supports shorthand syntax and complex AND/OR/NOT logic. Use this for: range queries, complex conditions, metadata filtering. Examples:   - Position range: {&#39;position&#39;: {&#39;lte&#39;: 5}}   - Time range: {&#39;timestamp&#39;: {&#39;gte&#39;: &#39;2025-01-01&#39;}}   - Complex: {&#39;AND&#39;: [{&#39;field&#39;: &#39;position&#39;, &#39;operator&#39;: &#39;lte&#39;, &#39;value&#39;: 5},                       {&#39;field&#39;: &#39;interaction_type&#39;, &#39;operator&#39;: &#39;in&#39;, &#39;value&#39;: [&#39;click&#39;, &#39;purchase&#39;]}]} See LogicalOperator documentation for full syntax. | [optional] 
**sort** | [**SortOption**](SortOption.md) | Sort options for ordering results. Default: timestamp descending (newest first). Examples:   - Sort by timestamp: {&#39;field&#39;: &#39;timestamp&#39;, &#39;direction&#39;: &#39;desc&#39;}   - Sort by position: {&#39;field&#39;: &#39;position&#39;, &#39;direction&#39;: &#39;asc&#39;} | [optional] 
**search** | **str** | Full-text search across metadata fields. NOT REQUIRED. Use to search interaction metadata content. | [optional] 

## Example

```python
from mixpeek.models.list_interactions_request import ListInteractionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListInteractionsRequest from a JSON string
list_interactions_request_instance = ListInteractionsRequest.from_json(json)
# print the JSON string representation of the object
print(ListInteractionsRequest.to_json())

# convert the object into a dict
list_interactions_request_dict = list_interactions_request_instance.to_dict()
# create an instance of ListInteractionsRequest from a dict
list_interactions_request_from_dict = ListInteractionsRequest.from_dict(list_interactions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


