# OrganizationModelResponse

Organization Model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal_id** | **str** |  | 
**organization_name** | **str** |  | 
**organization_id** | **str** |  | 
**account_type** | [**AccountTier**](AccountTier.md) |  | 
**credit_count** | **int** |  | 
**metadata** | **Dict[str, object]** |  | 
**users** | [**List[UserModelOutput]**](UserModelOutput.md) |  | 
**rate_limits** | [**BaseRateLimits**](BaseRateLimits.md) |  | 

## Example

```python
from mixpeek.models.organization_model_response import OrganizationModelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationModelResponse from a JSON string
organization_model_response_instance = OrganizationModelResponse.from_json(json)
# print the JSON string representation of the object
print(OrganizationModelResponse.to_json())

# convert the object into a dict
organization_model_response_dict = organization_model_response_instance.to_dict()
# create an instance of OrganizationModelResponse from a dict
organization_model_response_from_dict = OrganizationModelResponse.from_dict(organization_model_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


