# PublicPageSearchRequest

Request to execute a search on a specific tab of a Page.  Extra top-level fields (e.g. ``query_image``, ``query_text``) are automatically merged into ``inputs`` so callers can pass retriever inputs at the top level without nesting them inside an ``inputs`` key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tab_id** | **str** | Tab ID to search within | 
**inputs** | **Dict[str, object]** | Search inputs | [optional] 
**settings** | **Dict[str, object]** | Optional execution settings | [optional] 

## Example

```python
from mixpeek.models.public_page_search_request import PublicPageSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PublicPageSearchRequest from a JSON string
public_page_search_request_instance = PublicPageSearchRequest.from_json(json)
# print the JSON string representation of the object
print(PublicPageSearchRequest.to_json())

# convert the object into a dict
public_page_search_request_dict = public_page_search_request_instance.to_dict()
# create an instance of PublicPageSearchRequest from a dict
public_page_search_request_from_dict = PublicPageSearchRequest.from_dict(public_page_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


