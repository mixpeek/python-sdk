# StageDefsRateLimitConfig

Rate limiting configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests_per_minute** | **int** | Maximum requests per minute per domain | [optional] 
**requests_per_hour** | **int** | Maximum requests per hour per domain | [optional] 

## Example

```python
from mixpeek.models.stage_defs_rate_limit_config import StageDefsRateLimitConfig

# TODO update the JSON string below
json = "{}"
# create an instance of StageDefsRateLimitConfig from a JSON string
stage_defs_rate_limit_config_instance = StageDefsRateLimitConfig.from_json(json)
# print the JSON string representation of the object
print(StageDefsRateLimitConfig.to_json())

# convert the object into a dict
stage_defs_rate_limit_config_dict = stage_defs_rate_limit_config_instance.to_dict()
# create an instance of StageDefsRateLimitConfig from a dict
stage_defs_rate_limit_config_from_dict = StageDefsRateLimitConfig.from_dict(stage_defs_rate_limit_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


