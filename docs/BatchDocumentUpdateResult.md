# BatchDocumentUpdateResult

Result of a single document update in a batch operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | Document ID that was updated | 
**success** | **bool** | Whether the update succeeded | 
**error** | **str** | Error message if update failed | [optional] 

## Example

```python
from mixpeek.models.batch_document_update_result import BatchDocumentUpdateResult

# TODO update the JSON string below
json = "{}"
# create an instance of BatchDocumentUpdateResult from a JSON string
batch_document_update_result_instance = BatchDocumentUpdateResult.from_json(json)
# print the JSON string representation of the object
print(BatchDocumentUpdateResult.to_json())

# convert the object into a dict
batch_document_update_result_dict = batch_document_update_result_instance.to_dict()
# create an instance of BatchDocumentUpdateResult from a dict
batch_document_update_result_from_dict = BatchDocumentUpdateResult.from_dict(batch_document_update_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


