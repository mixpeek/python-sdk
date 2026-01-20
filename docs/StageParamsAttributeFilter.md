# StageParamsAttributeFilter

Configuration for filtering documents by attribute conditions.  **Stage Category**: FILTER  **Transformation**: N documents → ≤N documents (subset, same schema)  **Purpose**: Produces a subset of input documents by removing those that don't match attribute conditions. Output documents have identical schema to input.  **When to Use**:     - **As First Stage**: To retrieve and filter documents by attributes without semantic search       (e.g., \"get all active products with priority >= 5\"). Fetches up to 1000 documents       per collection from Qdrant, then applies filter conditions.     - **As Subsequent Stage**: To narrow results from previous stages by specific attributes       (status, date range, category, tags). Operates purely on in-memory results.     - When you need to apply business logic filtering (active items, published content)     - Before expensive stages (SORT, APPLY) to reduce processing overhead     - For structured/fast filtering based on document properties  **When NOT to Use**:     - For reordering results (use SORT stages: sort_relevance, sort_attribute)     - For complex semantic filtering (use llm_filter instead)     - For enriching documents with additional data (use APPLY stages)     - For aggregating to single document (use REDUCE stages)  **Operational Behavior**:     - **As First Stage**: Fetches documents directly from Qdrant (up to 1000 per collection)       using scroll API. Supports pre_filters which leverage Qdrant's native filtering       (including full-text search with TEXT operator). Results are then filtered in-memory       using the stage's filter conditions. This allows attribute_filter to be used as an       initial retrieval stage without requiring a prior search/embedding stage.     - **As Subsequent Stage**: Operates purely on in-memory results from previous stages       (no database queries). This is the typical use case for post-filtering.     - Produces subset of documents (removes non-matching)     - Fast operation (simple condition evaluation)     - Processes documents in batches for memory efficiency     - Supports complex boolean logic (AND/OR/NOT)     - Output schema = Input schema (no schema changes)  **Common Pipeline Position**: FILTER (this stage) → SORT → APPLY  **Important Limitations**:     - When used as first stage, maximum 1000 documents per collection are fetched from Qdrant     - For large collections, consider using semantic_search or other retrieval stages first     - Vectors are not fetched from Qdrant (only payloads) to optimize performance  **Two modes of operation:**  1. **Simple mode** (single condition): Specify `field`, `operator`, and `value` 2. **Boolean mode** (multiple conditions): Specify `conditions` with AND/OR/NOT logic  Both modes support template variables that are evaluated for every document.  Examples:     Simple single condition:         ```json         {             \"field\": \"metadata.status\",             \"operator\": \"eq\",             \"value\": \"active\"         }         ```      Boolean AND:         ```json         {             \"conditions\": {                 \"AND\": [                     {\"field\": \"metadata.status\", \"operator\": \"eq\", \"value\": \"active\"},                     {\"field\": \"metadata.priority\", \"operator\": \"gte\", \"value\": 5}                 ]             }         }         ```      Boolean OR:         ```json         {             \"conditions\": {                 \"OR\": [                     {\"field\": \"metadata.urgent\", \"operator\": \"eq\", \"value\": true},                     {\"field\": \"metadata.priority\", \"operator\": \"gte\", \"value\": 8}                 ]             }         }         ```      Nested boolean logic:         ```json         {             \"conditions\": {                 \"AND\": [                     {\"field\": \"metadata.status\", \"operator\": \"eq\", \"value\": \"active\"},                     {                         \"OR\": [                             {\"field\": \"metadata.category\", \"operator\": \"eq\", \"value\": \"urgent\"},                             {\"field\": \"metadata.category\", \"operator\": \"eq\", \"value\": \"critical\"}                         ]                     }                 ]             }         }         ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Dot-delimited field path to evaluate on each document. Supports template variables (e.g. &#39;{{DOC.metadata.category}}&#39;). REQUIRED for simple mode. NOT USED when &#39;conditions&#39; is specified. | [optional] [default to 'metadata.status']
**operator** | [**FilterOperator**](FilterOperator.md) | Comparison operator to apply. Supported operators: eq, ne, gt, gte, lt, lte, in, nin, contains, starts_with, ends_with, regex, exists, is_null. REQUIRED for simple mode. NOT USED when &#39;conditions&#39; is specified. | [optional] 
**value** | **object** |  | [optional] 
**conditions** | [**LogicalOperator**](LogicalOperator.md) | Complex filter conditions using boolean logic (AND/OR/NOT). Use this for combining multiple filter conditions. REQUIRED for boolean mode. Cannot be used with &#39;field&#39;/&#39;operator&#39;/&#39;value&#39;. | [optional] 
**batch_size** | **int** | Number of documents to evaluate per batch. The executor streams documents through the filter in chunks to avoid large in-memory spikes. | [optional] [default to 100]
**case_insensitive** | **bool** | When true, string comparisons are performed case-insensitively where the operator supports it. Applies to both simple and boolean modes. | [optional] [default to False]

## Example

```python
from mixpeek.models.stage_params_attribute_filter import StageParamsAttributeFilter

# TODO update the JSON string below
json = "{}"
# create an instance of StageParamsAttributeFilter from a JSON string
stage_params_attribute_filter_instance = StageParamsAttributeFilter.from_json(json)
# print the JSON string representation of the object
print(StageParamsAttributeFilter.to_json())

# convert the object into a dict
stage_params_attribute_filter_dict = stage_params_attribute_filter_instance.to_dict()
# create an instance of StageParamsAttributeFilter from a dict
stage_params_attribute_filter_from_dict = StageParamsAttributeFilter.from_dict(stage_params_attribute_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


