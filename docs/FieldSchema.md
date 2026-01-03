# FieldSchema

Optional schema configuration for the index. If not provided, uses default parameters for the specified type. Different types support different parameters (e.g., KeywordIndexParams.is_tenant).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'bool']
**tokenizer** | [**TokenizerType**](TokenizerType.md) |  | [optional] 
**min_token_len** | **int** |  | [optional] [default to 2]
**max_token_len** | **int** |  | [optional] [default to 15]
**lowercase** | **bool** |  | [optional] [default to True]
**lookup** | **bool** |  | [optional] [default to True]
**range** | **bool** |  | [optional] [default to True]
**is_tenant** | **bool** |  | [optional] [default to False]

## Example

```python
from mixpeek.models.field_schema import FieldSchema

# TODO update the JSON string below
json = "{}"
# create an instance of FieldSchema from a JSON string
field_schema_instance = FieldSchema.from_json(json)
# print the JSON string representation of the object
print(FieldSchema.to_json())

# convert the object into a dict
field_schema_dict = field_schema_instance.to_dict()
# create an instance of FieldSchema from a dict
field_schema_from_dict = FieldSchema.from_dict(field_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


