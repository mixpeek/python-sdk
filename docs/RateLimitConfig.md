# RateLimitConfig

Rate limiting configuration for public retriever API.  Controls how many requests can be made to the public endpoint to prevent abuse and manage infrastructure costs.  You can either use a preset tier or specify custom limits. If both tier and custom limits are provided, custom limits override the tier defaults.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Enable rate limiting for this published retriever. Set to False to disable all rate limiting (not recommended for public retrievers). | [optional] [default to True]
**tier** | [**RateLimitTier**](RateLimitTier.md) | Rate limit tier preset. STANDARD (default): 60/min, 1k/hour, 10k/day. ELEVATED: 300/min, 10k/hour, 100k/day. ENTERPRISE: 1000/min, 50k/hour, 500k/day. UNLIMITED: No limits. Custom limits override tier defaults. | [optional] 
**requests_per_minute** | **int** | Maximum requests per minute (OPTIONAL). If not specified, uses tier default. If specified, overrides tier default. | [optional] 
**requests_per_hour** | **int** | Maximum requests per hour (OPTIONAL). If not specified, uses tier default. If specified, overrides tier default. | [optional] 
**requests_per_day** | **int** | Maximum requests per day (OPTIONAL). If not specified, uses tier default. If specified, overrides tier default. | [optional] 
**max_results_per_query** | **int** | Maximum number of results per search query (1-1000) | [optional] [default to 100]
**enable_ip_limits** | **bool** | Enable IP-based rate limiting in addition to retriever-level limits. Useful for preventing individual IPs from monopolizing the retriever. | [optional] [default to False]
**max_requests_per_ip_hour** | **int** | Maximum requests per IP address per hour (OPTIONAL). Only enforced if enable_ip_limits&#x3D;True. Recommended: 100-500 for standard tier, 1000+ for elevated/enterprise. | [optional] 

## Example

```python
from mixpeek.models.rate_limit_config import RateLimitConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RateLimitConfig from a JSON string
rate_limit_config_instance = RateLimitConfig.from_json(json)
# print the JSON string representation of the object
print(RateLimitConfig.to_json())

# convert the object into a dict
rate_limit_config_dict = rate_limit_config_instance.to_dict()
# create an instance of RateLimitConfig from a dict
rate_limit_config_from_dict = RateLimitConfig.from_dict(rate_limit_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


