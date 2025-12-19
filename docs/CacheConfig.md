# CacheConfig

Configuration for retriever result caching.  Controls how retriever results are cached to improve performance and reduce redundant compute.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether caching is enabled for this retriever | [optional] [default to True]
**ttl_seconds** | **int** | Time-to-live for cached results in seconds. Default: 1 hour | [optional] [default to 3600]
**stage** | **str** | Which stage to cache: &#39;retrieval&#39;, &#39;generation&#39;, or &#39;full&#39; | [optional] [default to 'retrieval']
**exclude_fields** | **List[str]** | Fields to exclude from caching (e.g., PII fields) | [optional] 
**stats** | [**CacheStatistics**](CacheStatistics.md) | Cache performance statistics | [optional] 

## Example

```python
from mixpeek.models.cache_config import CacheConfig

# TODO update the JSON string below
json = "{}"
# create an instance of CacheConfig from a JSON string
cache_config_instance = CacheConfig.from_json(json)
# print the JSON string representation of the object
print(CacheConfig.to_json())

# convert the object into a dict
cache_config_dict = cache_config_instance.to_dict()
# create an instance of CacheConfig from a dict
cache_config_from_dict = CacheConfig.from_dict(cache_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


