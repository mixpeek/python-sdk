# DocumentGroup

A group of documents with the same field value.  Used when group_by parameter is specified in ListDocumentsRequest.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_key** | **object** |  | 
**documents** | [**List[DocumentResponse]**](DocumentResponse.md) | List of documents that share the same group_key value. Documents within each group are sorted by relevance/score if applicable. Each document contains full document data including metadata, lineage, and blobs. | 
**count** | **int** | Number of documents in this group. | 

## Example

```python
from mixpeek.models.document_group import DocumentGroup

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentGroup from a JSON string
document_group_instance = DocumentGroup.from_json(json)
# print the JSON string representation of the object
print(DocumentGroup.to_json())

# convert the object into a dict
document_group_dict = document_group_instance.to_dict()
# create an instance of DocumentGroup from a dict
document_group_from_dict = DocumentGroup.from_dict(document_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


