# MarkdownContent

Reusable markdown content model with title and content.  This model provides a structured way to include rich markdown content anywhere in the published retriever configuration. Includes safety constraints to prevent database issues.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title for the markdown content section | 
**content** | **str** | Markdown-formatted content. Supports standard markdown syntax including headers, lists, links, images, code blocks, and emphasis. Limited to 50KB to prevent database issues. | 

## Example

```python
from mixpeek.models.markdown_content import MarkdownContent

# TODO update the JSON string below
json = "{}"
# create an instance of MarkdownContent from a JSON string
markdown_content_instance = MarkdownContent.from_json(json)
# print the JSON string representation of the object
print(MarkdownContent.to_json())

# convert the object into a dict
markdown_content_dict = markdown_content_instance.to_dict()
# create an instance of MarkdownContent from a dict
markdown_content_from_dict = MarkdownContent.from_dict(markdown_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


