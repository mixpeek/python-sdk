# BucketSchemaFieldOutput

Schema field definition for bucket objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**BucketSchemaFieldType**](BucketSchemaFieldType.md) |  | 
**default** | **object** |  | [optional] 
**items** | [**BucketSchemaFieldOutput**](BucketSchemaFieldOutput.md) |  | [optional] 
**properties** | [**Dict[str, BucketSchemaFieldOutput]**](BucketSchemaFieldOutput.md) |  | [optional] 
**examples** | **List[object]** | OPTIONAL. List of example values for this field. Used by Apps to show example inputs in the UI. Provide multiple diverse examples when possible. | [optional] 
**description** | **str** |  | [optional] 
**enum** | **List[object]** |  | [optional] 
**required** | **bool** |  | [optional] [default to False]

## Example

```python
from mixpeek.models.bucket_schema_field_output import BucketSchemaFieldOutput

# TODO update the JSON string below
json = "{}"
# create an instance of BucketSchemaFieldOutput from a JSON string
bucket_schema_field_output_instance = BucketSchemaFieldOutput.from_json(json)
# print the JSON string representation of the object
print(BucketSchemaFieldOutput.to_json())

# convert the object into a dict
bucket_schema_field_output_dict = bucket_schema_field_output_instance.to_dict()
# create an instance of BucketSchemaFieldOutput from a dict
bucket_schema_field_output_from_dict = BucketSchemaFieldOutput.from_dict(bucket_schema_field_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


