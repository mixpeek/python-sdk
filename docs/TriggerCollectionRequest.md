# TriggerCollectionRequest

Request to trigger (re)processing through a collection.  **For bucket-sourced collections (tier 0):** Discovers objects from source bucket(s) and creates a batch for processing. Use `include_buckets` to limit which source buckets to process from.  **For collection-sourced collections (tier N):** Processes existing documents from upstream collection(s). Use `include_collections` to limit which source collections to process from.  Use `source_filters` for field-level filtering on objects or documents.  **Document Overwrite Behavior:** - If source bucket has `unique_key` configured: Documents are UPSERTED (overwrites existing) - If source bucket has NO `unique_key`: New documents are CREATED (may cause duplicates)  To enable idempotent re-processing, configure `unique_key` on the source bucket.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_buckets** | **List[str]** | Limit processing to objects from these specific buckets (IDs or names). Only applies to bucket-sourced collections. If not provided, all configured source buckets are used. | [optional] 
**include_collections** | **List[str]** | Limit processing to documents from these specific collections (IDs or names). Only applies to collection-sourced collections. If not provided, all configured source collections are used. | [optional] 
**source_filters** | **object** | Field-level filters for objects (bucket-sourced) or documents (collection-sourced). Uses LogicalOperator format (AND/OR/NOT). Use this to filter by metadata fields, status, or any other object/document properties. | [optional] 

## Example

```python
from mixpeek.models.trigger_collection_request import TriggerCollectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerCollectionRequest from a JSON string
trigger_collection_request_instance = TriggerCollectionRequest.from_json(json)
# print the JSON string representation of the object
print(TriggerCollectionRequest.to_json())

# convert the object into a dict
trigger_collection_request_dict = trigger_collection_request_instance.to_dict()
# create an instance of TriggerCollectionRequest from a dict
trigger_collection_request_from_dict = TriggerCollectionRequest.from_dict(trigger_collection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


