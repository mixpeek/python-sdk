# SnowflakeConfig

Snowflake data warehouse configuration for table-based sync.  Enables syncing Snowflake table rows as JSON objects in Mixpeek buckets. Each row becomes one object, with incremental sync via watermark columns.  Authentication Options:     - Key Pair: Recommended for production (secure, password-less)     - Username/Password: Fallback option (simpler setup)  Requirements:     - Snowflake account with read access to target tables     - Warehouse with compute resources     - SELECT permissions on target tables/schemas     - USAGE permissions on database, schema, warehouse  Use Cases:     - Sync customer data tables for AI/ML pipelines     - Ingest product catalog for search/recommendations     - Process transaction logs for analytics     - Mirror metadata tables for vector search  Example:     Production setup with key pair auth:     ```python     config = {         \"provider_type\": \"snowflake\",         \"credentials\": {             \"type\": \"key_pair\",             \"username\": \"MIXPEEK_SYNC\",             \"private_key\": \"-----BEGIN PRIVATE KEY-----\\n...\\n-----END PRIVATE KEY-----\\n\",         },         \"account\": \"xy12345.us-east-1\",         \"warehouse\": \"MIXPEEK_SYNC_WH\",         \"database\": \"PRODUCTION\",         \"schema\": \"PUBLIC\",         \"role\": \"SYNC_ROLE\",         \"incremental_column\": \"updated_at\",         \"primary_key_columns\": [\"id\"],     }     ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_type** | **str** |  | [optional] [default to 'snowflake']
**credentials** | [**Credentials3**](Credentials3.md) |  | 
**account** | **str** | REQUIRED. Snowflake account identifier. Format: {account_locator}.{cloud_region} or {org_name}-{account_name} Find in: Snowflake UI &gt; Account dropdown &gt; Account URL | 
**warehouse** | **str** | REQUIRED. Warehouse name for compute resources. Must have USAGE privilege on this warehouse. Warehouse will be used for all sync queries. Consider: Use dedicated warehouse for sync operations to isolate costs. | 
**database** | **str** | NOT REQUIRED if fully qualified table name used in source_path. Database name for default context. Can be omitted if source_path uses {DATABASE}.{SCHEMA}.{TABLE} format. Must have USAGE privilege if specified. | [optional] 
**var_schema** | **str** | NOT REQUIRED if fully qualified table name used in source_path. Schema name for default context. Can be omitted if source_path uses {SCHEMA}.{TABLE} or {DATABASE}.{SCHEMA}.{TABLE}. Must have USAGE privilege if specified. | [optional] 
**role** | **str** | NOT REQUIRED. Snowflake role to use for operations. If omitted, uses user&#39;s default role. Role must have SELECT on target tables and USAGE on database/schema/warehouse. Best practice: Create dedicated read-only role for sync operations. | [optional] 
**incremental_column** | **str** | NOT REQUIRED. Column name for incremental sync watermark. Should be a TIMESTAMP, TIMESTAMP_NTZ, or DATE column that tracks row modifications. When set, only rows with {incremental_column} &gt; last_sync_watermark are synced. Common values: updated_at, modified_at, last_updated, ingestion_timestamp. If omitted, full table scan on every sync (not recommended for large tables). | [optional] 
**primary_key_columns** | **List[str]** | NOT REQUIRED. Column names forming the primary key for stable object IDs. Used to generate deterministic file_id for deduplication. If omitted, uses hash of entire row content (less stable). Recommendation: Always specify for production to ensure idempotent syncs. | [optional] 
**query_timeout_seconds** | **int** | Query timeout in seconds. Prevents long-running queries from blocking sync operations. Default: 300 seconds (5 minutes). Increase for large tables or complex queries. | [optional] [default to 300]
**fetch_size** | **int** | Number of rows to fetch per network round-trip. Higher values reduce network overhead but increase memory usage. Default: 1000 rows. Tune based on row size and available memory. | [optional] [default to 1000]

## Example

```python
from mixpeek.models.snowflake_config import SnowflakeConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SnowflakeConfig from a JSON string
snowflake_config_instance = SnowflakeConfig.from_json(json)
# print the JSON string representation of the object
print(SnowflakeConfig.to_json())

# convert the object into a dict
snowflake_config_dict = snowflake_config_instance.to_dict()
# create an instance of SnowflakeConfig from a dict
snowflake_config_from_dict = SnowflakeConfig.from_dict(snowflake_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


