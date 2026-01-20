# CreditBalanceResponse

Response with current credit balance and tier information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization identifier | 
**credit_balance** | **int** | Current credit balance. For FREE tier without auto-billing, this is remaining free tier credits. For auto-billing accounts, this shows current month usage (negative indicates consumption). | 
**account_tier** | **str** | Current account tier: free, pro, team, enterprise | 
**next_tier** | **str** | Next available tier or null if at max tier | [optional] 
**credits_until_next_tier** | **int** | Credits needed to reach next tier (null if at max tier or N/A) | [optional] 
**estimated_days_remaining** | **int** | Estimated days until credits depleted based on 7-day burn rate. Null if no usage history or unlimited (auto-billing enabled). | [optional] 
**daily_burn_rate** | **float** | Average credits consumed per day (7-day rolling average) | [optional] [default to 0.0]

## Example

```python
from mixpeek.models.credit_balance_response import CreditBalanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreditBalanceResponse from a JSON string
credit_balance_response_instance = CreditBalanceResponse.from_json(json)
# print the JSON string representation of the object
print(CreditBalanceResponse.to_json())

# convert the object into a dict
credit_balance_response_dict = credit_balance_response_instance.to_dict()
# create an instance of CreditBalanceResponse from a dict
credit_balance_response_from_dict = CreditBalanceResponse.from_dict(credit_balance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


