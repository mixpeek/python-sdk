# PayloadIndexConfigInput

Configuration for a payload index.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** |  | 
**type** | [**PayloadSchemaType**](PayloadSchemaType.md) |  | 
**field_schema** | [**FieldSchema**](FieldSchema.md) |  | [optional] 

## Example

```python
from mixpeek.models.payload_index_config_input import PayloadIndexConfigInput

# TODO update the JSON string below
json = "{}"
# create an instance of PayloadIndexConfigInput from a JSON string
payload_index_config_input_instance = PayloadIndexConfigInput.from_json(json)
# print the JSON string representation of the object
print(PayloadIndexConfigInput.to_json())

# convert the object into a dict
payload_index_config_input_dict = payload_index_config_input_instance.to_dict()
# create an instance of PayloadIndexConfigInput from a dict
payload_index_config_input_from_dict = PayloadIndexConfigInput.from_dict(payload_index_config_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


