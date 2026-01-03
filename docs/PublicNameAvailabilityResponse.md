# PublicNameAvailabilityResponse

Response for public name availability check.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The public name that was checked | 
**available** | **bool** | Whether the name is available for use | 

## Example

```python
from mixpeek.models.public_name_availability_response import PublicNameAvailabilityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublicNameAvailabilityResponse from a JSON string
public_name_availability_response_instance = PublicNameAvailabilityResponse.from_json(json)
# print the JSON string representation of the object
print(PublicNameAvailabilityResponse.to_json())

# convert the object into a dict
public_name_availability_response_dict = public_name_availability_response_instance.to_dict()
# create an instance of PublicNameAvailabilityResponse from a dict
public_name_availability_response_from_dict = PublicNameAvailabilityResponse.from_dict(public_name_availability_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


