# PageTabInput

A single tab in a Page.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tab_id** | **str** | Unique identifier for this tab | 
**label** | **str** | Display label for the tab | 
**retriever_id** | **str** | Internal retriever ID (use for private retrievers) | [optional] 
**public_name** | **str** | Marketplace catalog public_name (proxies execution via public API) | [optional] 
**description** | **str** | Optional tab description shown as subtitle | [optional] 
**display_config** | [**DisplayConfigInput**](DisplayConfigInput.md) | Display configuration for this tab&#39;s search UI | 

## Example

```python
from mixpeek.models.page_tab_input import PageTabInput

# TODO update the JSON string below
json = "{}"
# create an instance of PageTabInput from a JSON string
page_tab_input_instance = PageTabInput.from_json(json)
# print the JSON string representation of the object
print(PageTabInput.to_json())

# convert the object into a dict
page_tab_input_dict = page_tab_input_instance.to_dict()
# create an instance of PageTabInput from a dict
page_tab_input_from_dict = PageTabInput.from_dict(page_tab_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


