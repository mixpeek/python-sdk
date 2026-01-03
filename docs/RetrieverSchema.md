# RetrieverSchema

Schema definition for retriever inputs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**Dict[str, RetrieverInputSchemaFieldInput]**](RetrieverInputSchemaFieldInput.md) | Schema properties for retriever inputs | [optional] 

## Example

```python
from mixpeek.models.retriever_schema import RetrieverSchema

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieverSchema from a JSON string
retriever_schema_instance = RetrieverSchema.from_json(json)
# print the JSON string representation of the object
print(RetrieverSchema.to_json())

# convert the object into a dict
retriever_schema_dict = retriever_schema_instance.to_dict()
# create an instance of RetrieverSchema from a dict
retriever_schema_from_dict = RetrieverSchema.from_dict(retriever_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


