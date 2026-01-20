# RetrieverMetadata

Metadata explaining how the retriever works.  This is separate from DisplayConfig and provides technical information about the retriever's architecture for developers/debugging.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stages** | **List[object]** | Pipeline stages used in this retriever | [optional] 
**collections** | **List[object]** | Collections and feature extractors used | [optional] 
**capabilities** | **object** | Capabilities and features of this retriever | [optional] 

## Example

```python
from mixpeek.models.retriever_metadata import RetrieverMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieverMetadata from a JSON string
retriever_metadata_instance = RetrieverMetadata.from_json(json)
# print the JSON string representation of the object
print(RetrieverMetadata.to_json())

# convert the object into a dict
retriever_metadata_dict = retriever_metadata_instance.to_dict()
# create an instance of RetrieverMetadata from a dict
retriever_metadata_from_dict = RetrieverMetadata.from_dict(retriever_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


