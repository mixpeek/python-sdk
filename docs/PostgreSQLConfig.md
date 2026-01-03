# PostgreSQLConfig

PostgreSQL database configuration for table-based sync and SQL queries.  Enables syncing PostgreSQL table rows as JSON objects and running SQL queries via the SQL Lookup retriever stage. Each row becomes one object, with incremental sync via watermark columns.  Authentication:     - Username/Password: Standard PostgreSQL authentication  Requirements:     - PostgreSQL 12+ recommended     - Read access to target tables     - Network connectivity to PostgreSQL server  Use Cases:     - Sync customer data tables for AI/ML pipelines     - Run SQL lookups to enrich documents in retriever pipelines     - Ingest product catalog for search/recommendations     - Process transaction logs for analytics  Example:     ```python     config = {         \"provider_type\": \"postgresql\",         \"credentials\": {             \"type\": \"username_password\",             \"username\": \"mixpeek_sync\",             \"password\": \"secure_password\",         },         \"host\": \"db.example.com\",         \"port\": 5432,         \"database\": \"production\",         \"schema\": \"public\",         \"ssl_mode\": \"require\",     }     ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_type** | **str** |  | [optional] [default to 'postgresql']
**credentials** | [**PostgreSQLCredentials**](PostgreSQLCredentials.md) | REQUIRED. PostgreSQL authentication credentials. Currently supports username/password authentication. | 
**host** | **str** | REQUIRED. PostgreSQL server hostname or IP address. Examples: &#39;localhost&#39;, &#39;db.example.com&#39;, &#39;192.168.1.100&#39; | 
**port** | **int** | PostgreSQL server port. Default: 5432 (standard PostgreSQL port) | [optional] [default to 5432]
**database** | **str** | REQUIRED. Database name to connect to. User must have CONNECT privilege on this database. | 
**var_schema** | **str** | Schema name for default context. Default: &#39;public&#39;. User must have USAGE privilege on this schema. | [optional] [default to 'public']
**ssl_mode** | **str** | SSL/TLS connection mode. Options: &#39;disable&#39;, &#39;allow&#39;, &#39;prefer&#39;, &#39;require&#39;, &#39;verify-ca&#39;, &#39;verify-full&#39;. Default: &#39;prefer&#39;. RECOMMENDED: Use &#39;require&#39; or stricter for production environments. | [optional] [default to 'prefer']
**incremental_column** | **str** | NOT REQUIRED. Column name for incremental sync watermark. Should be a TIMESTAMP or DATE column that tracks row modifications. Common values: updated_at, modified_at, last_updated. If omitted, full table scan on every sync. | [optional] 
**primary_key_columns** | **List[str]** | NOT REQUIRED. Column names forming the primary key for stable object IDs. Used to generate deterministic file_id for deduplication. If omitted, uses hash of entire row content. | [optional] 
**query_timeout_seconds** | **int** | Query timeout in seconds. Default: 300 seconds (5 minutes). Increase for large tables or complex queries. | [optional] [default to 300]
**fetch_size** | **int** | Number of rows to fetch per batch. Higher values reduce network overhead but increase memory usage. Default: 1000 rows. | [optional] [default to 1000]

## Example

```python
from mixpeek.models.postgre_sql_config import PostgreSQLConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PostgreSQLConfig from a JSON string
postgre_sql_config_instance = PostgreSQLConfig.from_json(json)
# print the JSON string representation of the object
print(PostgreSQLConfig.to_json())

# convert the object into a dict
postgre_sql_config_dict = postgre_sql_config_instance.to_dict()
# create an instance of PostgreSQLConfig from a dict
postgre_sql_config_from_dict = PostgreSQLConfig.from_dict(postgre_sql_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


