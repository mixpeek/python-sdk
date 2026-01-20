# CORSConfigurationResponse

Response model for CORS configuration operations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether the CORS configuration was successful | 
**bucket** | **str** | The object storage bucket name where CORS was configured | 
**applied_configuration** | **object** | The CORS configuration that was applied to the bucket | 
**message** | **str** | Human-readable status message | 

## Example

```python
from mixpeek.models.cors_configuration_response import CORSConfigurationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CORSConfigurationResponse from a JSON string
cors_configuration_response_instance = CORSConfigurationResponse.from_json(json)
# print the JSON string representation of the object
print(CORSConfigurationResponse.to_json())

# convert the object into a dict
cors_configuration_response_dict = cors_configuration_response_instance.to_dict()
# create an instance of CORSConfigurationResponse from a dict
cors_configuration_response_from_dict = CORSConfigurationResponse.from_dict(cors_configuration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


