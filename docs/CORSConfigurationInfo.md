# CORSConfigurationInfo

Current CORS configuration information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | **str** | The object storage bucket name | 
**has_cors** | **bool** | Whether CORS is currently configured on the bucket | 
**cors_rules** | **List[object]** | The current CORS rules (if configured) | [optional] 

## Example

```python
from mixpeek.models.cors_configuration_info import CORSConfigurationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CORSConfigurationInfo from a JSON string
cors_configuration_info_instance = CORSConfigurationInfo.from_json(json)
# print the JSON string representation of the object
print(CORSConfigurationInfo.to_json())

# convert the object into a dict
cors_configuration_info_dict = cors_configuration_info_instance.to_dict()
# create an instance of CORSConfigurationInfo from a dict
cors_configuration_info_from_dict = CORSConfigurationInfo.from_dict(cors_configuration_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


