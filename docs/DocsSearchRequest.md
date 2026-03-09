# DocsSearchRequest

Request to provision a docs search pipeline.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**site_url** | **str** | Root URL of the documentation site to crawl. | 
**site_name** | **str** | Human-readable name for the docs site. | 
**include_patterns** | **List[str]** | URL patterns to include (regex). Empty means include all. | [optional] 
**exclude_patterns** | **List[str]** | URL patterns to exclude (regex). | [optional] 
**namespace_id** | **str** | Existing namespace ID. If not provided, one will be created. | [optional] 
**options** | [**DocsSearchOptions**](DocsSearchOptions.md) | Optional configuration overrides. | [optional] 

## Example

```python
from mixpeek.models.docs_search_request import DocsSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocsSearchRequest from a JSON string
docs_search_request_instance = DocsSearchRequest.from_json(json)
# print the JSON string representation of the object
print(DocsSearchRequest.to_json())

# convert the object into a dict
docs_search_request_dict = docs_search_request_instance.to_dict()
# create an instance of DocsSearchRequest from a dict
docs_search_request_from_dict = DocsSearchRequest.from_dict(docs_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


