# RetrieverSchemaInput

Schema definition for retriever inputs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**Dict[str, BucketSchemaFieldInput]**](BucketSchemaFieldInput.md) |  | 

## Example

```python
from mixpeek.models.retriever_schema_input import RetrieverSchemaInput

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieverSchemaInput from a JSON string
retriever_schema_input_instance = RetrieverSchemaInput.from_json(json)
# print the JSON string representation of the object
print(RetrieverSchemaInput.to_json())

# convert the object into a dict
retriever_schema_input_dict = retriever_schema_input_instance.to_dict()
# create an instance of RetrieverSchemaInput from a dict
retriever_schema_input_from_dict = RetrieverSchemaInput.from_dict(retriever_schema_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


