# BatchDeleteDocumentsResponse

Response model for batch document delete operation.  Provides detailed per-document results showing success/failure for each deletion.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted_count** | **int** | Total number of documents successfully deleted | 
**failed_count** | **int** | Total number of documents that failed to delete | [optional] [default to 0]
**results** | [**List[BatchDocumentDeleteResult]**](BatchDocumentDeleteResult.md) | Detailed per-document results. Each entry shows document_id, success status, and error message (if failed). Empty list when using filter mode (only counts returned). | [optional] 
**message** | **str** | Summary message of the operation | [optional] [default to 'Batch delete completed']

## Example

```python
from mixpeek.models.batch_delete_documents_response import BatchDeleteDocumentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BatchDeleteDocumentsResponse from a JSON string
batch_delete_documents_response_instance = BatchDeleteDocumentsResponse.from_json(json)
# print the JSON string representation of the object
print(BatchDeleteDocumentsResponse.to_json())

# convert the object into a dict
batch_delete_documents_response_dict = batch_delete_documents_response_instance.to_dict()
# create an instance of BatchDeleteDocumentsResponse from a dict
batch_delete_documents_response_from_dict = BatchDeleteDocumentsResponse.from_dict(batch_delete_documents_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


