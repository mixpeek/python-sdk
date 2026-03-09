# RSSHttpHeaderCredentials

Optional HTTP credentials for private RSS feeds.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'http_headers']
**headers** | **Dict[str, str]** | HTTP headers for feed requests (e.g., Authorization). | [optional] 

## Example

```python
from mixpeek.models.rss_http_header_credentials import RSSHttpHeaderCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of RSSHttpHeaderCredentials from a JSON string
rss_http_header_credentials_instance = RSSHttpHeaderCredentials.from_json(json)
# print the JSON string representation of the object
print(RSSHttpHeaderCredentials.to_json())

# convert the object into a dict
rss_http_header_credentials_dict = rss_http_header_credentials_instance.to_dict()
# create an instance of RSSHttpHeaderCredentials from a dict
rss_http_header_credentials_from_dict = RSSHttpHeaderCredentials.from_dict(rss_http_header_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


