# AddCreditsResponse

Response after adding credits.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**previous_balance** | **int** | Credit balance before addition | 
**credits_added** | **int** | Number of credits added | 
**new_balance** | **int** | Credit balance after addition | 
**previous_tier** | [**AccountTier**](AccountTier.md) | Account tier before addition | 
**new_tier** | [**AccountTier**](AccountTier.md) | Account tier after addition (may auto-upgrade) | 
**tier_upgraded** | **bool** | Whether tier was automatically upgraded | 

## Example

```python
from mixpeek.models.add_credits_response import AddCreditsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddCreditsResponse from a JSON string
add_credits_response_instance = AddCreditsResponse.from_json(json)
# print the JSON string representation of the object
print(AddCreditsResponse.to_json())

# convert the object into a dict
add_credits_response_dict = add_credits_response_instance.to_dict()
# create an instance of AddCreditsResponse from a dict
add_credits_response_from_dict = AddCreditsResponse.from_dict(add_credits_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


