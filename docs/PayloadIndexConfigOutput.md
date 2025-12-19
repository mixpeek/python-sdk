# PayloadIndexConfigOutput

Configuration for a payload index.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** |  | 
**type** | [**PayloadSchemaType**](PayloadSchemaType.md) |  | 
**field_schema** | [**FieldSchema**](FieldSchema.md) |  | [optional] 

## Example

```python
from mixpeek.models.payload_index_config_output import PayloadIndexConfigOutput

# TODO update the JSON string below
json = "{}"
# create an instance of PayloadIndexConfigOutput from a JSON string
payload_index_config_output_instance = PayloadIndexConfigOutput.from_json(json)
# print the JSON string representation of the object
print(PayloadIndexConfigOutput.to_json())

# convert the object into a dict
payload_index_config_output_dict = payload_index_config_output_instance.to_dict()
# create an instance of PayloadIndexConfigOutput from a dict
payload_index_config_output_from_dict = PayloadIndexConfigOutput.from_dict(payload_index_config_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


