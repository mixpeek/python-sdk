# DisplayConfigOutput

Display configuration for public retriever UI.  This model defines how the public search interface should be rendered, including input fields, theme, layout, and result card configuration.  The frontend (apps.mixpeek.com) uses this to dynamically build the UI without hardcoded components.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title/heading for the public search page | 
**description** | **str** | Optional description/subtitle for the page | [optional] 
**logo_url** | **str** | URL to logo image | [optional] 
**icon_base64** | **str** | Base64 encoded icon/favicon (data URI format recommended). Max size: ~200KB encoded. Use for small icons that should be embedded. Example: &#39;data:image/png;base64,iVBORw0KGgo...&#39; | [optional] 
**seo** | [**SEOConfig**](SEOConfig.md) | SEO configuration for search engine and social media discoverability. Auto-generated during publishing with sensible defaults inferred from title, description, and retriever metadata. All fields can be overridden. | [optional] 
**markdowns** | [**List[MarkdownContent]**](MarkdownContent.md) | Array of markdown content sections for documentation, guides, or informational modals. Each section has a title and markdown-formatted content. Displayed in modals, expandable sections, or tabs on the public interface. Examples: &#39;How it Works&#39;, &#39;Search Guide&#39;, &#39;About&#39;, &#39;FAQ&#39;, etc. | [optional] 
**theme** | [**ThemeConfig**](ThemeConfig.md) | Theme/styling configuration | [optional] 
**inputs** | [**List[InputRenderingConfigOutput]**](InputRenderingConfigOutput.md) | List of input fields to render in the search interface. Each input maps to a field in the retriever&#39;s input_schema. Frontend uses the field_schema to render the appropriate component type. | 
**layout** | [**LayoutConfig**](LayoutConfig.md) | Layout configuration for results | [optional] 
**exposed_fields** | **List[str]** | List of document metadata fields to show in results. Only these fields are returned to end users. | 
**components** | [**ComponentsConfig**](ComponentsConfig.md) | Configuration for UI components including search inputs, filters, and result card display options. | [optional] 
**field_config** | [**Dict[str, FieldConfig]**](FieldConfig.md) | Configuration for how each field should be displayed. Keys are field names (must be subset of exposed_fields). Values are FieldConfig objects specifying format and display options. | [optional] 
**custom_cta** | [**CustomCTA**](CustomCTA.md) | Optional custom call-to-action button displayed in the header bar. Opens a markdown modal when clicked. | [optional] 
**external_links** | [**List[ExternalLink]**](ExternalLink.md) | External resource links for this retriever (GitHub repos, blog posts, docs, etc.). Displayed on homepage and retriever listing pages to provide additional context. | [optional] 
**template_type** | **str** | Template identifier for frontend rendering. Built-in templates: portrait-gallery, media-search, document-search. Custom templates can use any string identifier. | [optional] 
**field_mappings** | **Dict[str, str]** | Field mappings from collection output fields to template display slots. Maps template slot names (e.g., &#39;thumbnail&#39;, &#39;title&#39;) to actual field names in the search results. | [optional] 
**extensions** | **object** | Generic extensions for template-specific configuration. Allows templates to store custom config without schema changes. | [optional] 

## Example

```python
from mixpeek.models.display_config_output import DisplayConfigOutput

# TODO update the JSON string below
json = "{}"
# create an instance of DisplayConfigOutput from a JSON string
display_config_output_instance = DisplayConfigOutput.from_json(json)
# print the JSON string representation of the object
print(DisplayConfigOutput.to_json())

# convert the object into a dict
display_config_output_dict = display_config_output_instance.to_dict()
# create an instance of DisplayConfigOutput from a dict
display_config_output_from_dict = DisplayConfigOutput.from_dict(display_config_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


