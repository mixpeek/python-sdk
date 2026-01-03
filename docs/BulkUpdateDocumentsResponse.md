# BulkUpdateDocumentsResponse

Response model for bulk document update operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_count** | **int** | Number of documents that were updated. | 
**message** | **str** |  | [optional] [default to 'Documents updated successfully']

## Example

```python
from mixpeek.models.bulk_update_documents_response import BulkUpdateDocumentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkUpdateDocumentsResponse from a JSON string
bulk_update_documents_response_instance = BulkUpdateDocumentsResponse.from_json(json)
# print the JSON string representation of the object
print(BulkUpdateDocumentsResponse.to_json())

# convert the object into a dict
bulk_update_documents_response_dict = bulk_update_documents_response_instance.to_dict()
# create an instance of BulkUpdateDocumentsResponse from a dict
bulk_update_documents_response_from_dict = BulkUpdateDocumentsResponse.from_dict(bulk_update_documents_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


