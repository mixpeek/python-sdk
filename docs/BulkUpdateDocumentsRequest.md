# BulkUpdateDocumentsRequest

Request model for bulk updating documents by filters.  Updates ALL documents matching the provided filters with the SAME update_data. For updating specific documents by ID or different values per document, use BatchUpdateDocumentsRequest.  Use Cases:     - Update all pending documents to processed     - Update all documents from a specific date range     - Apply uniform changes across filtered document sets  Requirements:     - update_data: REQUIRED - fields to update on all matching documents     - filters: OPTIONAL - if omitted, updates ALL documents in collection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**LogicalOperatorInput**](LogicalOperatorInput.md) | OPTIONAL. Filter conditions to match documents for update. If not provided, updates ALL documents in the collection. Supports complex logical operators (AND, OR, NOT). Example: {&#39;must&#39;: [{&#39;key&#39;: &#39;metadata.status&#39;, &#39;value&#39;: &#39;pending&#39;}]} | [optional] 
**update_data** | **object** | REQUIRED. Dictionary of field-value pairs to update on ALL matching documents. Can update any document field except vectors (metadata, source_blobs, etc.). All matched documents receive the SAME updates. Example: {&#39;metadata.status&#39;: &#39;processed&#39;, &#39;metadata.reviewed&#39;: true} | 

## Example

```python
from mixpeek.models.bulk_update_documents_request import BulkUpdateDocumentsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkUpdateDocumentsRequest from a JSON string
bulk_update_documents_request_instance = BulkUpdateDocumentsRequest.from_json(json)
# print the JSON string representation of the object
print(BulkUpdateDocumentsRequest.to_json())

# convert the object into a dict
bulk_update_documents_request_dict = bulk_update_documents_request_instance.to_dict()
# create an instance of BulkUpdateDocumentsRequest from a dict
bulk_update_documents_request_from_dict = BulkUpdateDocumentsRequest.from_dict(bulk_update_documents_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


