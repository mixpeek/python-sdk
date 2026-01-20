# DocumentReference

Reference to an existing document to use its pre-computed features.  Use this to perform similarity search using a document's existing embeddings without re-processing the document. The system will fetch the document's feature vectors and use them directly for the search.  Use Cases:     - \"Find documents similar to this one\"     - Reverse image search using indexed images     - Document-to-document similarity     - Multi-hop similarity chains  Examples:     Find similar documents:         ```json         {             \"collection_id\": \"col_abc123\",             \"document_id\": \"doc_xyz789\"         }         ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_id** | **str** | Collection ID containing the reference document. Can be the same or different from the target search collection. Must be accessible within the current namespace. None values are handled by on_empty behavior (skip/random/error). | [optional] 
**document_id** | **str** | Document ID to use as similarity reference. The document must exist and have feature vectors for the specified feature_uri. If the document doesn&#39;t have the required feature, the search will fail. None values are handled by on_empty behavior (skip/random/error). | [optional] 

## Example

```python
from mixpeek.models.document_reference import DocumentReference

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentReference from a JSON string
document_reference_instance = DocumentReference.from_json(json)
# print the JSON string representation of the object
print(DocumentReference.to_json())

# convert the object into a dict
document_reference_dict = document_reference_instance.to_dict()
# create an instance of DocumentReference from a dict
document_reference_from_dict = DocumentReference.from_dict(document_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


