# ListMigrationsRequest

Request to list migrations with filters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**MigrationStatus**](MigrationStatus.md) | Filter by status | [optional] 
**migration_type** | [**MigrationType**](MigrationType.md) | Filter by type | [optional] 
**source_namespace_id** | **str** | Filter by source namespace | [optional] 
**limit** | **int** | Maximum results | [optional] [default to 20]
**offset** | **int** | Result offset for pagination | [optional] [default to 0]

## Example

```python
from mixpeek.models.list_migrations_request import ListMigrationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListMigrationsRequest from a JSON string
list_migrations_request_instance = ListMigrationsRequest.from_json(json)
# print the JSON string representation of the object
print(ListMigrationsRequest.to_json())

# convert the object into a dict
list_migrations_request_dict = list_migrations_request_instance.to_dict()
# create an instance of ListMigrationsRequest from a dict
list_migrations_request_from_dict = ListMigrationsRequest.from_dict(list_migrations_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


