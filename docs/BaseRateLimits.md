# BaseRateLimits

Base rate limits.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **int** |  | [optional] [default to 10]
**search** | **int** |  | [optional] [default to 10]
**upload** | **int** |  | [optional] [default to 10]
**delete** | **int** |  | [optional] [default to 10]

## Example

```python
from mixpeek.models.base_rate_limits import BaseRateLimits

# TODO update the JSON string below
json = "{}"
# create an instance of BaseRateLimits from a JSON string
base_rate_limits_instance = BaseRateLimits.from_json(json)
# print the JSON string representation of the object
print(BaseRateLimits.to_json())

# convert the object into a dict
base_rate_limits_dict = base_rate_limits_instance.to_dict()
# create an instance of BaseRateLimits from a dict
base_rate_limits_from_dict = BaseRateLimits.from_dict(base_rate_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


