# SectionConfig

A single section/block in a page layout.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**section_id** | **str** | Auto-generated section identifier | [optional] 
**type** | **str** | Section type: &#39;hero&#39;, &#39;stats-bar&#39;, &#39;featured-gallery&#39;, &#39;search-tabs&#39;, &#39;results-grid&#39;, &#39;results-list&#39;, &#39;markdown-content&#39;, &#39;iframe-embed&#39; | 
**props** | **Dict[str, object]** | Section-specific configuration properties | [optional] 
**order** | **int** | Explicit render order; falls back to array position if omitted | [optional] 

## Example

```python
from mixpeek.models.section_config import SectionConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SectionConfig from a JSON string
section_config_instance = SectionConfig.from_json(json)
# print the JSON string representation of the object
print(SectionConfig.to_json())

# convert the object into a dict
section_config_dict = section_config_instance.to_dict()
# create an instance of SectionConfig from a dict
section_config_from_dict = SectionConfig.from_dict(section_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


