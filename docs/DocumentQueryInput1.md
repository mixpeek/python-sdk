# DocumentQueryInput1

Document reference query input for similarity search.  Use existing document's pre-computed features without re-processing. Perfect for \"find similar documents\" functionality. No inference is performed.  Use Cases:     - Find similar documents     - Reverse image search using indexed images     - Document-to-document similarity     - Multi-hop similarity chains  Examples:     Simple document reference:         ```json         {             \"input_mode\": \"document\",             \"document_ref\": {                 \"collection_id\": \"col_products\",                 \"document_id\": \"doc_item_123\"             }         }         ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_mode** | **str** | Discriminator field. Always &#39;document&#39; for document reference queries. | [optional] [default to 'document']
**document_ref** | [**DocumentReference**](DocumentReference.md) | Reference to existing document&#39;s pre-computed features. The system fetches the document&#39;s feature vectors for the specified feature_uri and uses them directly without re-processing. Document must exist and have features for the specified feature_uri. | 

## Example

```python
from mixpeek.models.document_query_input1 import DocumentQueryInput1

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentQueryInput1 from a JSON string
document_query_input1_instance = DocumentQueryInput1.from_json(json)
# print the JSON string representation of the object
print(DocumentQueryInput1.to_json())

# convert the object into a dict
document_query_input1_dict = document_query_input1_instance.to_dict()
# create an instance of DocumentQueryInput1 from a dict
document_query_input1_from_dict = DocumentQueryInput1.from_dict(document_query_input1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


