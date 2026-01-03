# CollectionDiagnostic

Diagnostic information for a collection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_id** | **str** | Collection ID | 
**collection_name** | **str** | Collection name | 
**document_count** | **int** | Number of documents in collection | [optional] [default to 0]
**expected_documents** | **int** | Expected document count | [optional] 
**status** | **str** | Collection status (ready, processing, empty) | 

## Example

```python
from mixpeek.models.collection_diagnostic import CollectionDiagnostic

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionDiagnostic from a JSON string
collection_diagnostic_instance = CollectionDiagnostic.from_json(json)
# print the JSON string representation of the object
print(CollectionDiagnostic.to_json())

# convert the object into a dict
collection_diagnostic_dict = collection_diagnostic_instance.to_dict()
# create an instance of CollectionDiagnostic from a dict
collection_diagnostic_from_dict = CollectionDiagnostic.from_dict(collection_diagnostic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


