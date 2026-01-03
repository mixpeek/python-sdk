# SEOConfig

SEO configuration for public retriever discoverability.  Auto-generated during publishing with sensible defaults inferred from the retriever's display_config. All fields can be overridden manually.  This configuration controls how the public retriever appears in: - Search engine results (Google, Bing, etc.) - Social media shares (Twitter, Facebook, LinkedIn) - Link previews in messaging apps

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta_title** | **str** | SEO-optimized page title (50-60 chars recommended). Auto-generated from display_config.title + site_name if not provided. | [optional] 
**meta_description** | **str** | Meta description for search engine snippets (max 160 chars). Auto-generated from display_config.description if not provided. | [optional] 
**keywords** | **List[str]** | Relevant keywords for search engines. Auto-inferred from title, description, and retriever tags. | [optional] 
**og_image_url** | **str** | URL to OG image for social previews (1200x630px recommended). Auto-generated and uploaded to public S3 bucket during publishing. | [optional] 
**og_image_alt** | **str** | Alt text for OG image (accessibility and SEO) | [optional] 
**og_type** | **str** | Open Graph content type | [optional] [default to 'website']
**twitter_card** | **str** | Twitter card display style | [optional] [default to 'summary_large_image']
**twitter_site** | **str** | Twitter @handle for the site | [optional] [default to '@mixpeek']
**twitter_creator** | **str** | Twitter @handle for content creator (optional) | [optional] 
**robots** | **str** | Robots meta directive for search engine crawlers. Use &#39;noindex, nofollow&#39; to hide from search engines. | [optional] [default to 'index, follow']
**canonical_url** | **str** | Canonical URL if different from default. Auto-set to https://apps.mixpeek.com/r/{public_name} if not provided. | [optional] 
**site_name** | **str** | Site name for OG tags and branding | [optional] [default to 'Mixpeek']
**author** | **str** | Content author/creator name | [optional] 
**locale** | **str** | Content language/locale | [optional] [default to 'en_US']
**logo_url** | **str** | URL to organization/brand logo for SEO and branding. Used in structured data and can be displayed in search results. | [optional] 
**favicon_url** | **str** | URL to favicon/icon for the public retriever page. Recommended sizes: 32x32, 48x48, or 180x180 for Apple touch icon. | [optional] 
**structured_data** | [**StructuredDataConfig**](StructuredDataConfig.md) | Schema.org structured data for rich search results | [optional] 

## Example

```python
from mixpeek.models.seo_config import SEOConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SEOConfig from a JSON string
seo_config_instance = SEOConfig.from_json(json)
# print the JSON string representation of the object
print(SEOConfig.to_json())

# convert the object into a dict
seo_config_dict = seo_config_instance.to_dict()
# create an instance of SEOConfig from a dict
seo_config_from_dict = SEOConfig.from_dict(seo_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


