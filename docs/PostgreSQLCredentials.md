# PostgreSQLCredentials

PostgreSQL username/password authentication.  Standard username/password authentication for PostgreSQL databases. Password is encrypted at rest using MongoDB CSFLE.  Security:     - password field is encrypted at rest via CSFLE     - Consider using SSL mode 'require' for production     - Use dedicated read-only database user for sync operations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'username_password']
**username** | **str** | REQUIRED. PostgreSQL username for authentication. | 
**password** | **str** | REQUIRED. PostgreSQL password for authentication. SECURITY: This field is encrypted at rest via CSFLE. Never log or expose. | 

## Example

```python
from mixpeek.models.postgre_sql_credentials import PostgreSQLCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of PostgreSQLCredentials from a JSON string
postgre_sql_credentials_instance = PostgreSQLCredentials.from_json(json)
# print the JSON string representation of the object
print(PostgreSQLCredentials.to_json())

# convert the object into a dict
postgre_sql_credentials_dict = postgre_sql_credentials_instance.to_dict()
# create an instance of PostgreSQLCredentials from a dict
postgre_sql_credentials_from_dict = PostgreSQLCredentials.from_dict(postgre_sql_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


