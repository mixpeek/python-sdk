# RSSConfig

RSS/Atom feed configuration. source_path = feed URL.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_type** | **str** |  | [optional] [default to 'rss']
**credentials** | [**RSSHttpHeaderCredentials**](RSSHttpHeaderCredentials.md) | Optional HTTP headers for private feeds. | [optional] 
**user_agent** | **str** | User-Agent header for feed requests. | [optional] [default to 'Mixpeek RSS Sync/1.0']
**request_timeout** | **int** | HTTP request timeout in seconds. | [optional] [default to 30]

## Example

```python
from mixpeek.models.rss_config import RSSConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RSSConfig from a JSON string
rss_config_instance = RSSConfig.from_json(json)
# print the JSON string representation of the object
print(RSSConfig.to_json())

# convert the object into a dict
rss_config_dict = rss_config_instance.to_dict()
# create an instance of RSSConfig from a dict
rss_config_from_dict = RSSConfig.from_dict(rss_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


