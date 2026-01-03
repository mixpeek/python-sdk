# AddCreditsRequest

Request to add credits to an organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credits** | **int** | Number of credits to add. Must be positive. | 

## Example

```python
from mixpeek.models.add_credits_request import AddCreditsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddCreditsRequest from a JSON string
add_credits_request_instance = AddCreditsRequest.from_json(json)
# print the JSON string representation of the object
print(AddCreditsRequest.to_json())

# convert the object into a dict
add_credits_request_dict = add_credits_request_instance.to_dict()
# create an instance of AddCreditsRequest from a dict
add_credits_request_from_dict = AddCreditsRequest.from_dict(add_credits_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


