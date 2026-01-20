# URLPatterns

URL pattern filters for crawling.  Used to include or exclude specific URL patterns when crawling. Patterns are Python regular expressions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **List[str]** | Regex patterns for URLs to include. If provided, URLs must match at least one pattern to be crawled. If empty, all URLs (subject to other filters) are included. Example: [&#39;/blog/.*&#39;, &#39;/docs/.*&#39;] | [optional] 
**exclude** | **List[str]** | Regex patterns for URLs to exclude. URLs matching any pattern are skipped. Applied after include patterns. Example: [&#39;/login&#39;, &#39;/admin/.*&#39;, &#39;\\\\?.*&#39;] | [optional] 

## Example

```python
from mixpeek.models.url_patterns import URLPatterns

# TODO update the JSON string below
json = "{}"
# create an instance of URLPatterns from a JSON string
url_patterns_instance = URLPatterns.from_json(json)
# print the JSON string representation of the object
print(URLPatterns.to_json())

# convert the object into a dict
url_patterns_dict = url_patterns_instance.to_dict()
# create an instance of URLPatterns from a dict
url_patterns_from_dict = URLPatterns.from_dict(url_patterns_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


