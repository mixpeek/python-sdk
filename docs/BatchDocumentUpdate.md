# BatchDocumentUpdate

Single document update specification for batch operations.  Represents one document's update within a batch request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | REQUIRED. Document ID to update. Must exist in the collection. Format: &#39;doc_&#39; prefix + alphanumeric characters. | 
**update_data** | **object** | REQUIRED. Fields to update for this specific document. Can update any document field except vectors. Supported fields: metadata, source_blobs, document_blobs, lineage fields (root_object_id, source_type, etc.), and any custom fields. Each document in the batch can have different update_data. | 

## Example

```python
from mixpeek.models.batch_document_update import BatchDocumentUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of BatchDocumentUpdate from a JSON string
batch_document_update_instance = BatchDocumentUpdate.from_json(json)
# print the JSON string representation of the object
print(BatchDocumentUpdate.to_json())

# convert the object into a dict
batch_document_update_dict = batch_document_update_instance.to_dict()
# create an instance of BatchDocumentUpdate from a dict
batch_document_update_from_dict = BatchDocumentUpdate.from_dict(batch_document_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


