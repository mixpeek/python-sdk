# StageDefsDocumentQueryInput

Document reference query input for similarity search.  Use existing document's pre-computed features without re-processing. Perfect for \"find similar documents\" functionality. No inference is performed.  Use Cases:     - Find similar documents     - Reverse image search using indexed images     - Document-to-document similarity     - Multi-hop similarity chains  Examples:     Simple document reference:         ```json         {             \"input_mode\": \"document\",             \"document_ref\": {                 \"collection_id\": \"col_products\",                 \"document_id\": \"doc_item_123\"             }         }         ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_mode** | **str** | Discriminator field. Always &#39;document&#39; for document reference queries. | [optional] [default to 'document']
**document_ref** | [**StageDefsDocumentReference**](StageDefsDocumentReference.md) | Reference to existing document&#39;s pre-computed features. The system fetches the document&#39;s feature vectors for the specified feature_uri and uses them directly without re-processing. Document must exist and have features for the specified feature_uri. | 

## Example

```python
from mixpeek.models.stage_defs_document_query_input import StageDefsDocumentQueryInput

# TODO update the JSON string below
json = "{}"
# create an instance of StageDefsDocumentQueryInput from a JSON string
stage_defs_document_query_input_instance = StageDefsDocumentQueryInput.from_json(json)
# print the JSON string representation of the object
print(StageDefsDocumentQueryInput.to_json())

# convert the object into a dict
stage_defs_document_query_input_dict = stage_defs_document_query_input_instance.to_dict()
# create an instance of StageDefsDocumentQueryInput from a dict
stage_defs_document_query_input_from_dict = StageDefsDocumentQueryInput.from_dict(stage_defs_document_query_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


