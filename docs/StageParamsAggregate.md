# StageParamsAggregate

Configuration for the aggregate REDUCE stage.  ┌─────────────────────────────────────────────────────────────────────────────┐ │ Stage Category: REDUCE                                                      │ │                                                                             │ │ Transformation: N documents → M aggregation results                         │ │                                                                             │ │ This stage operates on IN-MEMORY pipeline results, NOT the database.        │ │ Use this for analytics on already-retrieved documents.                      │ └─────────────────────────────────────────────────────────────────────────────┘  Purpose:     Compute aggregations (counts, sums, averages, etc.) on pipeline results.     Useful for analytics, summaries, and metadata extraction from search results.  When to Use:     - Compute statistics on retrieved documents (avg score, total count)     - Group results by a field and count per group     - Extract summary metrics for display (e.g., \"45 results in 3 categories\")     - Post-search analytics that don't need database queries  When NOT to Use:     - For faceted search (use feature_search.facets instead - queries Qdrant)     - For full-collection analytics (use aggregation API directly)     - The aggregate stage only sees pipeline results, not full filtered dataset  Performance:     - Fast: In-memory Python operations on already-fetched documents     - No database queries     - Suitable for up to ~10K documents  Common Pipeline Position:     FILTER → SORT → REDUCE (this stage)  Example Use Cases:     - \"Show average relevance score of top 100 results\"     - \"Count results per category from search results\"     - \"Get min/max prices from product search\"     - \"List unique authors in search results\"

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregations** | [**List[AggregationOperation]**](AggregationOperation.md) | List of aggregation operations to compute. At least one aggregation is required. Multiple aggregations can be computed in a single stage. | [optional] [default to [{"function":"count","field":null,"alias":"total"},{"function":"avg","field":"score","alias":"avg_score"}]]
**group_by** | [**List[GroupByFieldConfig]**](GroupByFieldConfig.md) | OPTIONAL. Fields to group by before aggregating. When specified, aggregations are computed per-group. When None, aggregations are computed across all documents (global). Multiple fields create composite groups (e.g., category + year). | [optional] [default to null]
**sort_by** | **str** | OPTIONAL. Metric alias to sort aggregation results by. Must match an alias from the aggregations list. Only applies when group_by is specified. | [optional] [default to 'null']
**sort_order** | **str** | OPTIONAL. Sort order for aggregation results. &#39;desc&#39;: Highest values first (default). &#39;asc&#39;: Lowest values first. | [optional] [default to 'desc']
**limit** | **int** | OPTIONAL. Maximum number of aggregation results to return. Only applies when group_by is specified. Useful for &#39;top N&#39; queries (e.g., top 10 categories by count). | [optional] [default to null]
**include_documents** | **bool** | OPTIONAL. Whether to include the original documents in output. False (default): Only return aggregation results in metadata. True: Pass through documents and add aggregation results to metadata. Set to True when aggregations are supplementary to search results. | [optional] [default to False]

## Example

```python
from mixpeek.models.stage_params_aggregate import StageParamsAggregate

# TODO update the JSON string below
json = "{}"
# create an instance of StageParamsAggregate from a JSON string
stage_params_aggregate_instance = StageParamsAggregate.from_json(json)
# print the JSON string representation of the object
print(StageParamsAggregate.to_json())

# convert the object into a dict
stage_params_aggregate_dict = stage_params_aggregate_instance.to_dict()
# create an instance of StageParamsAggregate from a dict
stage_params_aggregate_from_dict = StageParamsAggregate.from_dict(stage_params_aggregate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


