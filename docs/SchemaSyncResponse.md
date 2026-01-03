# SchemaSyncResponse

Response from schema sync operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether schema sync succeeded | 
**collection_id** | **str** | Collection that was synced | 
**schema_version** | **int** | New schema version | 
**previous_version** | **int** | Previous schema version | 
**fields_added** | **List[str]** | List of new fields discovered | [optional] 
**fields_total** | **int** | Total fields in output_schema | 
**documents_sampled** | **int** | Number of documents sampled | 
**downstream_collections_updated** | **List[str]** | Downstream collections that were updated | [optional] 
**message** | **str** | Additional message or error | [optional] 

## Example

```python
from mixpeek.models.schema_sync_response import SchemaSyncResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaSyncResponse from a JSON string
schema_sync_response_instance = SchemaSyncResponse.from_json(json)
# print the JSON string representation of the object
print(SchemaSyncResponse.to_json())

# convert the object into a dict
schema_sync_response_dict = schema_sync_response_instance.to_dict()
# create an instance of SchemaSyncResponse from a dict
schema_sync_response_from_dict = SchemaSyncResponse.from_dict(schema_sync_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


