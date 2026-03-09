# PageTabOutput

A single tab in a Page.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tab_id** | **str** | Unique identifier for this tab | 
**label** | **str** | Display label for the tab | 
**retriever_id** | **str** | Internal retriever ID (use for private retrievers) | [optional] 
**public_name** | **str** | Marketplace catalog public_name (proxies execution via public API) | [optional] 
**description** | **str** | Optional tab description shown as subtitle | [optional] 
**display_config** | [**DisplayConfigOutput**](DisplayConfigOutput.md) | Display configuration for this tab&#39;s search UI | 

## Example

```python
from mixpeek.models.page_tab_output import PageTabOutput

# TODO update the JSON string below
json = "{}"
# create an instance of PageTabOutput from a JSON string
page_tab_output_instance = PageTabOutput.from_json(json)
# print the JSON string representation of the object
print(PageTabOutput.to_json())

# convert the object into a dict
page_tab_output_dict = page_tab_output_instance.to_dict()
# create an instance of PageTabOutput from a dict
page_tab_output_from_dict = PageTabOutput.from_dict(page_tab_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


