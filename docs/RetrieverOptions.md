# RetrieverOptions

Options for retriever migration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preserve_retriever_ids** | **bool** | Keep same retriever IDs (avoid conflicts) | [optional] [default to False]
**migrate_interactions** | **bool** | Migrate user interaction data | [optional] [default to False]
**migrate_execution_history** | **bool** | Migrate past execution history | [optional] [default to False]
**validate_references** | **bool** | Pre-flight check all references exist | [optional] [default to True]

## Example

```python
from mixpeek.models.retriever_options import RetrieverOptions

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieverOptions from a JSON string
retriever_options_instance = RetrieverOptions.from_json(json)
# print the JSON string representation of the object
print(RetrieverOptions.to_json())

# convert the object into a dict
retriever_options_dict = retriever_options_instance.to_dict()
# create an instance of RetrieverOptions from a dict
retriever_options_from_dict = RetrieverOptions.from_dict(retriever_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


