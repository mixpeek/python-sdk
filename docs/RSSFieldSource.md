# RSSFieldSource

Extract value from an RSS entry field.  Provider Compatibility: RSS only  Available fields: title, author, link, categories, summary, published  Example mapping:     {\"type\": \"rss_field\", \"field\": \"title\"} -> extracts entry title     {\"type\": \"rss_field\", \"field\": \"categories\"} -> extracts list of category terms  Attributes:     type: Must be \"rss_field\" to identify this source type     field: RSS entry field name to extract

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Source type identifier. | [optional] [default to 'rss_field']
**var_field** | **str** | RSS entry field: title, author, link, categories, summary, published | 

## Example

```python
from mixpeek.models.rss_field_source import RSSFieldSource

# TODO update the JSON string below
json = "{}"
# create an instance of RSSFieldSource from a JSON string
rss_field_source_instance = RSSFieldSource.from_json(json)
# print the JSON string representation of the object
print(RSSFieldSource.to_json())

# convert the object into a dict
rss_field_source_dict = rss_field_source_instance.to_dict()
# create an instance of RSSFieldSource from a dict
rss_field_source_from_dict = RSSFieldSource.from_dict(rss_field_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


