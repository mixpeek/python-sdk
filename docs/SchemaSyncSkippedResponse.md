# SchemaSyncSkippedResponse

Response when schema sync was skipped (debounce or disabled).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Request succeeded | [optional] [default to True]
**skipped** | **bool** | Schema sync was skipped | [optional] [default to True]
**reason** | **str** | Why sync was skipped | 
**collection_id** | **str** | Collection ID | 
**schema_version** | **int** | Current schema version | 
**last_sync** | **str** | Last sync timestamp | [optional] 

## Example

```python
from mixpeek.models.schema_sync_skipped_response import SchemaSyncSkippedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaSyncSkippedResponse from a JSON string
schema_sync_skipped_response_instance = SchemaSyncSkippedResponse.from_json(json)
# print the JSON string representation of the object
print(SchemaSyncSkippedResponse.to_json())

# convert the object into a dict
schema_sync_skipped_response_dict = schema_sync_skipped_response_instance.to_dict()
# create an instance of SchemaSyncSkippedResponse from a dict
schema_sync_skipped_response_from_dict = SchemaSyncSkippedResponse.from_dict(schema_sync_skipped_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


