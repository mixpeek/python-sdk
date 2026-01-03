# BatchUpdateDocumentsResponse

Response model for batch document update operation.  Provides detailed per-document results showing success/failure for each update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_count** | **int** | Total number of documents successfully updated | 
**failed_count** | **int** | Total number of documents that failed to update | [optional] [default to 0]
**results** | [**List[BatchDocumentUpdateResult]**](BatchDocumentUpdateResult.md) | Detailed per-document results. Each entry shows document_id, success status, and error message (if failed). Empty list when using filter mode (only counts returned). | [optional] 
**message** | **str** | Summary message of the operation | [optional] [default to 'Batch update completed']

## Example

```python
from mixpeek.models.batch_update_documents_response import BatchUpdateDocumentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BatchUpdateDocumentsResponse from a JSON string
batch_update_documents_response_instance = BatchUpdateDocumentsResponse.from_json(json)
# print the JSON string representation of the object
print(BatchUpdateDocumentsResponse.to_json())

# convert the object into a dict
batch_update_documents_response_dict = batch_update_documents_response_instance.to_dict()
# create an instance of BatchUpdateDocumentsResponse from a dict
batch_update_documents_response_from_dict = BatchUpdateDocumentsResponse.from_dict(batch_update_documents_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


