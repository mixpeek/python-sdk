# BatchUpdateDocumentsRequest

Request model for batch updating multiple documents by explicit IDs or filters.  Supports TWO modes: 1. Explicit IDs mode: Provide 'updates' array with document_id + update_data for each 2. Filter mode: Provide 'filters' + 'update_data' to update all matching documents  Key difference from BulkUpdateDocumentsRequest: - Batch (this): Can apply DIFFERENT updates to SPECIFIC documents by ID - Bulk: Applies SAME update to ALL documents matching filters  Use Cases:     - Update 5 specific documents with different metadata values     - Update documents by IDs with per-document update control     - Combine with filters for targeted batch updates  Requirements:     - EITHER 'updates' (explicit mode) OR 'filters' + 'update_data' (filter mode)     - NOT BOTH modes simultaneously

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updates** | [**List[BatchDocumentUpdate]**](BatchDocumentUpdate.md) | OPTIONAL. List of document updates with explicit document IDs. Each entry specifies document_id and update_data. Use this mode when you know exact document IDs and want per-document control. Mutually exclusive with filters + update_data mode. Maximum 1000 documents per batch request. | [optional] 
**filters** | [**LogicalOperatorInput**](LogicalOperatorInput.md) | OPTIONAL. Filter conditions to match documents for update. Must be used with &#39;update_data&#39; field. Mutually exclusive with &#39;updates&#39; array. If provided, applies same update_data to all matching documents. | [optional] 
**update_data** | **object** | OPTIONAL. Update data to apply when using filters mode. Must be used with &#39;filters&#39; field. All matched documents receive the same updates. Can update any document field except vectors. | [optional] 

## Example

```python
from mixpeek.models.batch_update_documents_request import BatchUpdateDocumentsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BatchUpdateDocumentsRequest from a JSON string
batch_update_documents_request_instance = BatchUpdateDocumentsRequest.from_json(json)
# print the JSON string representation of the object
print(BatchUpdateDocumentsRequest.to_json())

# convert the object into a dict
batch_update_documents_request_dict = batch_update_documents_request_instance.to_dict()
# create an instance of BatchUpdateDocumentsRequest from a dict
batch_update_documents_request_from_dict = BatchUpdateDocumentsRequest.from_dict(batch_update_documents_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


