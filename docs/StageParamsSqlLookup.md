# StageParamsSqlLookup

Configuration for SQL Lookup enrichment stage.  **Stage Category**: APPLY (1-1 Enrichment or 0-M Document Creation)  **Transformation**: - With documents: N documents -> N documents (expanded schema) - Without documents: 0 documents -> M documents (from SQL results)  **Purpose**: Enriches documents by running SQL queries against organization connections (PostgreSQL, Snowflake). Enables joining structured database data with document pipelines.  **Security**: - Only SELECT queries allowed (no INSERT/UPDATE/DELETE/DROP) - Uses parameterized queries to prevent SQL injection - Connection credentials managed via organization connections - Query timeout enforced  **Supported Providers**: - PostgreSQL: Full SQL support with $1, $2 placeholders - Snowflake: Full SQL support (coming soon)  **When to Use**: - Lookup customer data from database by ID - Enrich products with inventory information - Join document metadata with relational data - Create documents from SQL query results  **When NOT to Use**: - Complex analytics queries (use dedicated analytics tools) - High-volume batch operations (use ETL pipelines) - Real-time streaming (use event systems)  Requirements:     - connection_id: REQUIRED, organization connection ID or name     - query: REQUIRED, SQL SELECT query     - parameters: OPTIONAL, named parameters for query     - output_field: OPTIONAL, where to store results     - result_handling: OPTIONAL, how to handle multiple rows     - timeout: OPTIONAL, query timeout (default: 30s)     - when: OPTIONAL, conditional enrichment filter     - on_error: OPTIONAL, error handling strategy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_id** | **str** | REQUIRED. Organization connection ID (conn_...) or name. Connection must be SQL-capable (PostgreSQL or Snowflake). Use POST /v1/organizations/connections to create connections. Example: &#39;conn_abc123&#39; or &#39;my_postgres_db&#39; | 
**query** | **str** | REQUIRED. SQL SELECT query to execute. Only SELECT queries allowed - mutations are blocked. Use $1, $2, etc. for PostgreSQL parameter placeholders. Supports template variables in &#39;parameters&#39; field values. Example: &#39;SELECT * FROM products WHERE sku &#x3D; $1&#39; | 
**parameters** | **object** | OPTIONAL. Named parameters for SQL query. Keys are parameter names, values support template syntax. Parameters are converted to positional args ($1, $2) in order. Template variables: {{DOC.field}}, {{INPUT.field}}, {{SECRET.name}}. Example: {&#39;sku&#39;: &#39;{{DOC.metadata.sku}}&#39;} | [optional] 
**output_field** | **str** | OPTIONAL. Dot-path where SQL results should be stored. Creates nested structure if needed. For FIRST mode: single object. For ALL mode: array of objects. Default: &#39;sql_result&#39;. Note: Avoid using &#39;metadata.*&#39; paths as the metadata field is excluded from API responses. | [optional] [default to 'sql_result']
**result_handling** | [**ResultHandling**](ResultHandling.md) | OPTIONAL. How to handle multiple result rows. &#39;first&#39;: Return only first row (default). &#39;all&#39;: Return all rows as array. &#39;error_if_empty&#39;: Error if no results. &#39;error_if_multiple&#39;: Error if more than one result.  | [optional] 
**on_no_results** | [**OnNoResults**](OnNoResults.md) | OPTIONAL. Behavior when query returns no rows. &#39;skip&#39;: Keep document unchanged. &#39;null&#39;: Set output_field to null (default). &#39;error&#39;: Raise error. | [optional] 
**timeout** | **int** | OPTIONAL. Query timeout in seconds. Range: 1-300. Default: 30. Increase for complex queries. | [optional] [default to 30]
**when** | [**LogicalOperator**](LogicalOperator.md) | OPTIONAL. Conditional filter for selective enrichment. Only documents matching condition will execute SQL lookup. RECOMMENDED for performance optimization. | [optional] 
**on_error** | [**ErrorHandling**](ErrorHandling.md) | OPTIONAL. Error handling strategy. &#39;skip&#39;: Pass document through unchanged (default). &#39;remove&#39;: Remove failed documents. &#39;raise&#39;: Halt pipeline on error. | [optional] 

## Example

```python
from mixpeek.models.stage_params_sql_lookup import StageParamsSqlLookup

# TODO update the JSON string below
json = "{}"
# create an instance of StageParamsSqlLookup from a JSON string
stage_params_sql_lookup_instance = StageParamsSqlLookup.from_json(json)
# print the JSON string representation of the object
print(StageParamsSqlLookup.to_json())

# convert the object into a dict
stage_params_sql_lookup_dict = stage_params_sql_lookup_instance.to_dict()
# create an instance of StageParamsSqlLookup from a dict
stage_params_sql_lookup_from_dict = StageParamsSqlLookup.from_dict(stage_params_sql_lookup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


