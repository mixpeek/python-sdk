# BatchDeleteDocumentsRequest

Request model for batch deleting multiple documents by explicit IDs or filters.  Supports TWO modes: 1. Explicit IDs mode: Provide 'document_ids' array 2. Filter mode: Provide 'filters' to delete all matching documents  Use Cases:     - Delete 5 specific documents in one API call     - Delete all documents matching criteria     - Bulk cleanup operations  Requirements:     - EITHER 'document_ids' OR 'filters' must be provided     - NOT BOTH modes simultaneously

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_ids** | **List[str]** | OPTIONAL. List of document IDs to delete. Use this mode when you know exact document IDs to delete. Mutually exclusive with filters mode. Maximum 1000 documents per batch request. | [optional] 
**filters** | [**LogicalOperatorInput**](LogicalOperatorInput.md) | OPTIONAL. Filter conditions to match documents for deletion. Mutually exclusive with &#39;document_ids&#39; array. If provided, deletes ALL documents matching the filters. Use with caution - can delete many documents at once. | [optional] 

## Example

```python
from mixpeek.models.batch_delete_documents_request import BatchDeleteDocumentsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BatchDeleteDocumentsRequest from a JSON string
batch_delete_documents_request_instance = BatchDeleteDocumentsRequest.from_json(json)
# print the JSON string representation of the object
print(BatchDeleteDocumentsRequest.to_json())

# convert the object into a dict
batch_delete_documents_request_dict = batch_delete_documents_request_instance.to_dict()
# create an instance of BatchDeleteDocumentsRequest from a dict
batch_delete_documents_request_from_dict = BatchDeleteDocumentsRequest.from_dict(batch_delete_documents_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


