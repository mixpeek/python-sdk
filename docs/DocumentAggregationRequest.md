# DocumentAggregationRequest

Aggregation request for collection documents.  Extends the base AggregationRequest with document-specific context. Inherits all fields from AggregationRequest.  Requirements:     - group_by: REQUIRED, fields to group by     - aggregations: REQUIRED, aggregation operations to perform     - All other fields from AggregationRequest are available  Examples:     - Count documents by feature type     - Daily processing statistics     - User-based analytics with filtering

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_by** | [**List[GroupByField]**](GroupByField.md) | Fields to group results by. REQUIRED, at least one field. Can include field transformations (date_trunc, date_part). Results will have one row per unique combination of group_by values. | 
**aggregations** | [**List[AggregationOperation]**](AggregationOperation.md) | Aggregation operations to perform. REQUIRED, at least one operation. Each operation produces a calculated field in results. Can combine multiple functions (COUNT, SUM, AVG, etc.). | 
**filters** | **Dict[str, object]** | Pre-aggregation filters to apply to source data. OPTIONAL, filters data before grouping. Uses same syntax as standard query filters. Applied before GROUP BY. | [optional] 
**having** | [**List[HavingCondition]**](HavingCondition.md) | Post-aggregation filters to apply to results. OPTIONAL, filters groups after aggregation. Uses aggregation aliases as field names. Applied after GROUP BY and aggregation calculations. | [optional] 
**unwind** | **str** | Array field to unwind before aggregation. OPTIONAL, creates one document per array element. Useful for aggregating over array contents. Example: &#39;blobs&#39; to analyze each blob separately. | [optional] 
**range_buckets** | [**List[RangeBucket]**](RangeBucket.md) | Range-based bucketing for numeric fields. OPTIONAL, creates histogram-style buckets. Groups numeric values into defined ranges. Applied during grouping stage. | [optional] 
**sort_by** | **str** | Field to sort results by. OPTIONAL, can be group_by field or aggregation alias. Defaults to no specific order. Use with sort_direction to control order. | [optional] 
**sort_direction** | **str** | Sort direction. OPTIONAL, defaults to &#39;desc&#39; (descending). Valid values: &#39;asc&#39; (ascending), &#39;desc&#39; (descending). Used with sort_by field. | [optional] [default to 'desc']
**limit** | **int** | Maximum number of results to return. OPTIONAL, no limit if not specified. Applied after sorting. Useful for &#39;top N&#39; queries. | [optional] 

## Example

```python
from mixpeek.models.document_aggregation_request import DocumentAggregationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentAggregationRequest from a JSON string
document_aggregation_request_instance = DocumentAggregationRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentAggregationRequest.to_json())

# convert the object into a dict
document_aggregation_request_dict = document_aggregation_request_instance.to_dict()
# create an instance of DocumentAggregationRequest from a dict
document_aggregation_request_from_dict = DocumentAggregationRequest.from_dict(document_aggregation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


