# DocsSearchOptions

Optional configuration for docs search setup.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_image_search** | **bool** | Enable SigLIP image embeddings for diagram/screenshot search. | [optional] [default to False]
**enable_code_search** | **bool** | Enable Jina Code embeddings for code-aware search. | [optional] [default to True]
**max_pages** | **int** | Maximum pages to crawl. | [optional] [default to 200]
**max_depth** | **int** | Maximum crawl depth from seed URL. | [optional] [default to 3]
**chunk_strategy** | **str** | Text chunking strategy. | [optional] [default to 'paragraphs']
**chunk_size** | **int** | Chunk size in units of chunk_strategy. | [optional] [default to 500]
**render_strategy** | **str** | Page rendering strategy: static, javascript, or auto. | [optional] [default to 'auto']

## Example

```python
from mixpeek.models.docs_search_options import DocsSearchOptions

# TODO update the JSON string below
json = "{}"
# create an instance of DocsSearchOptions from a JSON string
docs_search_options_instance = DocsSearchOptions.from_json(json)
# print the JSON string representation of the object
print(DocsSearchOptions.to_json())

# convert the object into a dict
docs_search_options_dict = docs_search_options_instance.to_dict()
# create an instance of DocsSearchOptions from a dict
docs_search_options_from_dict = DocsSearchOptions.from_dict(docs_search_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


