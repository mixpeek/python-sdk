# RetrieverInputSchemaFieldOutput

Schema field definition for retriever input parameters.  Identical structure to BucketSchemaField but uses RetrieverInputSchemaFieldType which includes additional reference types like document_reference.  This allows retrievers to accept: 1. Metadata inputs (strings, numbers, dates, etc.) 2. File inputs (images, videos, documents for search) 3. Reference inputs (document_reference for \"find similar\" queries)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**RetrieverInputSchemaFieldType**](RetrieverInputSchemaFieldType.md) |  | 
**default** | **object** |  | [optional] 
**items** | [**RetrieverInputSchemaFieldOutput**](RetrieverInputSchemaFieldOutput.md) |  | [optional] 
**properties** | [**Dict[str, RetrieverInputSchemaFieldOutput]**](RetrieverInputSchemaFieldOutput.md) |  | [optional] 
**examples** | **List[object]** | OPTIONAL. List of example values for this field. Used by Apps to show example inputs in the UI. Provide multiple diverse examples when possible. | [optional] 
**description** | **str** |  | [optional] 
**enum** | **List[object]** |  | [optional] 
**required** | **bool** |  | [optional] [default to False]

## Example

```python
from mixpeek.models.retriever_input_schema_field_output import RetrieverInputSchemaFieldOutput

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieverInputSchemaFieldOutput from a JSON string
retriever_input_schema_field_output_instance = RetrieverInputSchemaFieldOutput.from_json(json)
# print the JSON string representation of the object
print(RetrieverInputSchemaFieldOutput.to_json())

# convert the object into a dict
retriever_input_schema_field_output_dict = retriever_input_schema_field_output_instance.to_dict()
# create an instance of RetrieverInputSchemaFieldOutput from a dict
retriever_input_schema_field_output_from_dict = RetrieverInputSchemaFieldOutput.from_dict(retriever_input_schema_field_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


