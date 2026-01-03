# BucketSchemaFieldInput

Schema field definition for bucket objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**BucketSchemaFieldType**](BucketSchemaFieldType.md) |  | 
**default** | **object** |  | [optional] 
**items** | [**BucketSchemaFieldInput**](BucketSchemaFieldInput.md) |  | [optional] 
**properties** | [**Dict[str, BucketSchemaFieldInput]**](BucketSchemaFieldInput.md) |  | [optional] 
**examples** | **List[object]** | OPTIONAL. List of example values for this field. Used by Apps to show example inputs in the UI. Provide multiple diverse examples when possible. | [optional] 
**description** | **str** |  | [optional] 
**enum** | **List[object]** |  | [optional] 
**required** | **bool** |  | [optional] [default to False]

## Example

```python
from mixpeek.models.bucket_schema_field_input import BucketSchemaFieldInput

# TODO update the JSON string below
json = "{}"
# create an instance of BucketSchemaFieldInput from a JSON string
bucket_schema_field_input_instance = BucketSchemaFieldInput.from_json(json)
# print the JSON string representation of the object
print(BucketSchemaFieldInput.to_json())

# convert the object into a dict
bucket_schema_field_input_dict = bucket_schema_field_input_instance.to_dict()
# create an instance of BucketSchemaFieldInput from a dict
bucket_schema_field_input_from_dict = BucketSchemaFieldInput.from_dict(bucket_schema_field_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


