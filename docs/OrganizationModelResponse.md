# OrganizationModelResponse

Response model for organization endpoints.  SECURITY: Does NOT expose internal_id to prevent leakage of high-entropy secrets. Only organization_id (public identifier) is included in API responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** |  | 
**organization_name** | **str** |  | 
**logo_url** | **str** |  | [optional] 
**account_type** | [**AccountTier**](AccountTier.md) |  | 
**credit_count** | **int** |  | 
**metadata** | **object** |  | [optional] 
**billing_email** | **str** |  | [optional] 
**rate_limits** | [**BaseRateLimits**](BaseRateLimits.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**users** | **List[object]** |  | [optional] 

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


