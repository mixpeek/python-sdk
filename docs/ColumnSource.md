# ColumnSource

Extract value from a database column (Snowflake, PostgreSQL, etc.).  For database sync sources, maps a column from the source table/view to a bucket schema field. Column handling varies by database.  Provider Compatibility: Snowflake, PostgreSQL (future), BigQuery (future)  Example Snowflake table:     CREATE TABLE CUSTOMERS (         ID VARCHAR, NAME VARCHAR, CATEGORY VARCHAR,         CREATED_AT TIMESTAMP, PROFILE_IMAGE_URL VARCHAR     );  Example mapping:     {\"type\": \"column\", \"name\": \"CATEGORY\"} -> extracts the CATEGORY column value  Database-Specific Notes:     - Snowflake: Case-insensitive (internally uppercase), use unquoted names     - PostgreSQL: Case-sensitive if quoted, defaults to lowercase     - BigQuery: Case-sensitive  Attributes:     type: Must be \"column\" to identify this source type     name: The column name to extract from

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Source type identifier. Must be &#39;column&#39; for database columns. | [optional] [default to 'column']
**name** | **str** | The column name to extract from. Case handling depends on the database. Snowflake: case-insensitive (defaults to uppercase). PostgreSQL: case-sensitive unless quoted. Column must exist in the source table/view. | 

## Example

```python
from mixpeek.models.column_source import ColumnSource

# TODO update the JSON string below
json = "{}"
# create an instance of ColumnSource from a JSON string
column_source_instance = ColumnSource.from_json(json)
# print the JSON string representation of the object
print(ColumnSource.to_json())

# convert the object into a dict
column_source_dict = column_source_instance.to_dict()
# create an instance of ColumnSource from a dict
column_source_from_dict = ColumnSource.from_dict(column_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


