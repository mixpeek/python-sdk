# ResponseSyncCollectionSchemaV1CollectionsCollectionIdSyncSchemaPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Request succeeded | [default to True]
**collection_id** | **str** | Collection ID | 
**schema_version** | **int** | Current schema version | 
**previous_version** | **int** | Previous schema version | 
**fields_added** | **List[str]** | List of new fields discovered | [optional] 
**fields_total** | **int** | Total fields in output_schema | 
**documents_sampled** | **int** | Number of documents sampled | 
**downstream_collections_updated** | **List[str]** | Downstream collections that were updated | [optional] 
**message** | **str** | Additional message or error | [optional] 
**skipped** | **bool** | Schema sync was skipped | [optional] [default to True]
**reason** | **str** | Why sync was skipped | 
**last_sync** | **str** | Last sync timestamp | [optional] 

## Example

```python
from mixpeek.models.response_sync_collection_schema_v1_collections_collection_id_sync_schema_post import ResponseSyncCollectionSchemaV1CollectionsCollectionIdSyncSchemaPost

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseSyncCollectionSchemaV1CollectionsCollectionIdSyncSchemaPost from a JSON string
response_sync_collection_schema_v1_collections_collection_id_sync_schema_post_instance = ResponseSyncCollectionSchemaV1CollectionsCollectionIdSyncSchemaPost.from_json(json)
# print the JSON string representation of the object
print(ResponseSyncCollectionSchemaV1CollectionsCollectionIdSyncSchemaPost.to_json())

# convert the object into a dict
response_sync_collection_schema_v1_collections_collection_id_sync_schema_post_dict = response_sync_collection_schema_v1_collections_collection_id_sync_schema_post_instance.to_dict()
# create an instance of ResponseSyncCollectionSchemaV1CollectionsCollectionIdSyncSchemaPost from a dict
response_sync_collection_schema_v1_collections_collection_id_sync_schema_post_from_dict = ResponseSyncCollectionSchemaV1CollectionsCollectionIdSyncSchemaPost.from_dict(response_sync_collection_schema_v1_collections_collection_id_sync_schema_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


