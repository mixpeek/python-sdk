# PublicRetrieverListItem

Simplified retriever information for public listing.  Provides essential details for browsing public retrievers without exposing sensitive configuration or credentials.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_name** | **str** | Public URL-safe name used in the public URL | 
**public_url** | **str** | Full public URL to the retriever page | 
**title** | **str** | Display title from display_config | 
**description** | **str** | Display description from display_config | [optional] 
**logo_url** | **str** | Logo URL from display_config | [optional] 
**icon_base64** | **str** | Base64 encoded icon/favicon from display_config | [optional] 
**og_image_url** | **str** | Social preview/OG image URL from display_config | [optional] 
**password_protected** | **bool** | Whether password authentication is required | 
**is_active** | **bool** | Whether the retriever is active | 
**external_links** | [**List[ExternalLink]**](ExternalLink.md) | External resource links (GitHub, blog posts, docs, etc.) | [optional] 
**created_at** | **datetime** | When the retriever was published | 
**updated_at** | **datetime** | When the retriever was last updated | 

## Example

```python
from mixpeek.models.public_retriever_list_item import PublicRetrieverListItem

# TODO update the JSON string below
json = "{}"
# create an instance of PublicRetrieverListItem from a JSON string
public_retriever_list_item_instance = PublicRetrieverListItem.from_json(json)
# print the JSON string representation of the object
print(PublicRetrieverListItem.to_json())

# convert the object into a dict
public_retriever_list_item_dict = public_retriever_list_item_instance.to_dict()
# create an instance of PublicRetrieverListItem from a dict
public_retriever_list_item_from_dict = PublicRetrieverListItem.from_dict(public_retriever_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


