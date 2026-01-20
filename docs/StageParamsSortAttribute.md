# StageParamsSortAttribute

Configuration for sorting documents by an attribute field.  **Stage Category**: SORT  **Transformation**: N documents → N documents (same docs, different order, same schema)  **Purpose**: Reorders documents in the pipeline based on any document attribute (not just relevance scores). Use this for sorting by metadata fields like dates, popularity, priority, or custom attributes.  **When to Use**:     - Sort by timestamps (created_at, updated_at, published_date)     - Sort by numeric metadata (popularity, view_count, rating, price)     - Sort by string attributes (title, category) with optional case-insensitive comparison     - Apply business logic ordering (priority, status)     - Secondary sorting after relevance-based retrieval  **When NOT to Use**:     - For sorting by relevance/similarity scores (use sort_relevance instead)     - For initial document retrieval (use FILTER stages)     - For removing documents (use FILTER stages)     - For enriching documents (use APPLY stages)  **Operational Behavior**:     - Operates on in-memory document results (no database queries)     - Maintains all documents, just changes their order     - Fast operation (simple in-memory sort)     - Does not change document count or schema     - Handles null values gracefully (configurable placement)  **Common Pipeline Position**: FILTER → SORT (this stage) → APPLY  Requirements:     - field: REQUIRED, document field path to sort on     - direction: OPTIONAL, defaults to descending     - nulls_last: OPTIONAL, defaults to true (nulls at end)  Use Cases:     - Recent content first: Sort by published_date desc     - Popular content: Sort by view_count or popularity score     - Alphabetical: Sort by title or name     - Priority-based: Sort by urgency or importance ratings     - Temporal ordering: Sort by event timestamps

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Document field path to sort on. Use dot notation for nested fields (e.g., &#39;metadata.release_date&#39;). Supports template expressions for dynamic field selection. Can sort by strings, numbers, dates, or booleans. Examples: &#39;metadata.created_at&#39;, &#39;metadata.popularity&#39;, &#39;title&#39;. | [optional] [default to 'metadata.created_at']
**direction** | [**SortDirection**](SortDirection.md) | OPTIONAL. Sort direction. &#39;desc&#39; (default): Highest/latest values first (Z-A, 100-0, newest-oldest). &#39;asc&#39;: Lowest/earliest values first (A-Z, 0-100, oldest-newest). | [optional] 
**nulls_last** | **bool** | OPTIONAL. Whether documents with null/missing field values should be placed at the end of results regardless of sort direction. true (default): Nulls always at the end. false: Nulls follow natural sort order (beginning for asc, end for desc). | [optional] [default to True]

## Example

```python
from mixpeek.models.stage_params_sort_attribute import StageParamsSortAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of StageParamsSortAttribute from a JSON string
stage_params_sort_attribute_instance = StageParamsSortAttribute.from_json(json)
# print the JSON string representation of the object
print(StageParamsSortAttribute.to_json())

# convert the object into a dict
stage_params_sort_attribute_dict = stage_params_sort_attribute_instance.to_dict()
# create an instance of StageParamsSortAttribute from a dict
stage_params_sort_attribute_from_dict = StageParamsSortAttribute.from_dict(stage_params_sort_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


