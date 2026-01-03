# RetrieverInputSchemaFieldInput

Schema field definition for retriever input parameters.  Identical structure to BucketSchemaField but uses RetrieverInputSchemaFieldType which includes additional reference types like document_reference.  This allows retrievers to accept: 1. Metadata inputs (strings, numbers, dates, etc.) 2. File inputs (images, videos, documents for search) 3. Reference inputs (document_reference for \"find similar\" queries)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**RetrieverInputSchemaFieldType**](RetrieverInputSchemaFieldType.md) |  | 
**default** | **object** |  | [optional] 
**items** | [**RetrieverInputSchemaFieldInput**](RetrieverInputSchemaFieldInput.md) |  | [optional] 
**properties** | [**Dict[str, RetrieverInputSchemaFieldInput]**](RetrieverInputSchemaFieldInput.md) |  | [optional] 
**examples** | **List[object]** | OPTIONAL. List of example values for this field. Used by Apps to show example inputs in the UI. Provide multiple diverse examples when possible. | [optional] 
**description** | **str** |  | [optional] 
**enum** | **List[object]** |  | [optional] 
**required** | **bool** |  | [optional] [default to False]

## Example

```python
from mixpeek.models.retriever_input_schema_field_input import RetrieverInputSchemaFieldInput

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieverInputSchemaFieldInput from a JSON string
retriever_input_schema_field_input_instance = RetrieverInputSchemaFieldInput.from_json(json)
# print the JSON string representation of the object
print(RetrieverInputSchemaFieldInput.to_json())

# convert the object into a dict
retriever_input_schema_field_input_dict = retriever_input_schema_field_input_instance.to_dict()
# create an instance of RetrieverInputSchemaFieldInput from a dict
retriever_input_schema_field_input_from_dict = RetrieverInputSchemaFieldInput.from_dict(retriever_input_schema_field_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


