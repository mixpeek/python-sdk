# ListMigrationsResponse

Response for listing migrations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[GetMigrationResponse]**](GetMigrationResponse.md) | List of migrations | 
**total** | **int** | Total count matching filters | 
**limit** | **int** | Results limit | 
**offset** | **int** | Results offset | 

## Example

```python
from mixpeek.models.list_migrations_response import ListMigrationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListMigrationsResponse from a JSON string
list_migrations_response_instance = ListMigrationsResponse.from_json(json)
# print the JSON string representation of the object
print(ListMigrationsResponse.to_json())

# convert the object into a dict
list_migrations_response_dict = list_migrations_response_instance.to_dict()
# create an instance of ListMigrationsResponse from a dict
list_migrations_response_from_dict = ListMigrationsResponse.from_dict(list_migrations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


