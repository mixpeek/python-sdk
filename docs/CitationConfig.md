# CitationConfig

Configuration for citation/source tracking in RAG output.  Citations help users trace information back to source documents and are essential for attribution in RAG applications.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**style** | **str** | Citation style to use: - &#39;numbered&#39;: [1], [2], [3] - &#39;bracketed&#39;: [doc_id] - &#39;footnote&#39;: Superscript numbers - &#39;none&#39;: No citations | [optional] [default to 'numbered']
**include_title** | **bool** | Include document title in citation metadata. | [optional] [default to True]
**include_url** | **bool** | Include source URL in citation metadata if available. | [optional] [default to False]

## Example

```python
from mixpeek.models.citation_config import CitationConfig

# TODO update the JSON string below
json = "{}"
# create an instance of CitationConfig from a JSON string
citation_config_instance = CitationConfig.from_json(json)
# print the JSON string representation of the object
print(CitationConfig.to_json())

# convert the object into a dict
citation_config_dict = citation_config_instance.to_dict()
# create an instance of CitationConfig from a dict
citation_config_from_dict = CitationConfig.from_dict(citation_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


