# SchemaSyncRequest

Request to sync a collection's schema by sampling documents.  Used by: - Manual API calls from users - Automatic triggers from BatchJobPoller

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sample_size** | **int** | Number of documents to sample for schema discovery | [optional] [default to 1000]
**force** | **bool** | Force schema sync even if within debounce window. Default: false (respects 5-minute debounce) | [optional] [default to False]
**cascade_to_downstream** | **bool** | Automatically update downstream collections that use this collection as source. Default: true | [optional] [default to True]

## Example

```python
from mixpeek.models.schema_sync_request import SchemaSyncRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaSyncRequest from a JSON string
schema_sync_request_instance = SchemaSyncRequest.from_json(json)
# print the JSON string representation of the object
print(SchemaSyncRequest.to_json())

# convert the object into a dict
schema_sync_request_dict = schema_sync_request_instance.to_dict()
# create an instance of SchemaSyncRequest from a dict
schema_sync_request_from_dict = SchemaSyncRequest.from_dict(schema_sync_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


