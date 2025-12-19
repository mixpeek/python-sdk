# RetrieverSchemaOutput

Schema definition for retriever inputs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**Dict[str, BucketSchemaFieldOutput]**](BucketSchemaFieldOutput.md) |  | 

## Example

```python
from mixpeek.models.retriever_schema_output import RetrieverSchemaOutput

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieverSchemaOutput from a JSON string
retriever_schema_output_instance = RetrieverSchemaOutput.from_json(json)
# print the JSON string representation of the object
print(RetrieverSchemaOutput.to_json())

# convert the object into a dict
retriever_schema_output_dict = retriever_schema_output_instance.to_dict()
# create an instance of RetrieverSchemaOutput from a dict
retriever_schema_output_from_dict = RetrieverSchemaOutput.from_dict(retriever_schema_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


