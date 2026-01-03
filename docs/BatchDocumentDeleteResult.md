# BatchDocumentDeleteResult

Result of a single document deletion in a batch operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | Document ID that was deleted | 
**success** | **bool** | Whether the deletion succeeded | 
**error** | **str** | Error message if deletion failed | [optional] 

## Example

```python
from mixpeek.models.batch_document_delete_result import BatchDocumentDeleteResult

# TODO update the JSON string below
json = "{}"
# create an instance of BatchDocumentDeleteResult from a JSON string
batch_document_delete_result_instance = BatchDocumentDeleteResult.from_json(json)
# print the JSON string representation of the object
print(BatchDocumentDeleteResult.to_json())

# convert the object into a dict
batch_document_delete_result_dict = batch_document_delete_result_instance.to_dict()
# create an instance of BatchDocumentDeleteResult from a dict
batch_document_delete_result_from_dict = BatchDocumentDeleteResult.from_dict(batch_document_delete_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


