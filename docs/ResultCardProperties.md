# ResultCardProperties

Properties for result card display configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**layout** | **str** | Card layout orientation | [optional] [default to 'vertical']
**show_thumbnail** | **bool** | Whether to show thumbnail image in results | [optional] [default to True]
**thumbnail_aspect_ratio** | **str** | Aspect ratio for thumbnail images | [optional] [default to '16/9']
**thumbnail_fit** | **str** | How thumbnail should fit in container | [optional] [default to 'cover']
**show_score** | **bool** | Whether to display relevance score | [optional] [default to False]
**truncate_title** | **int** | Maximum characters for title before truncation | [optional] 
**truncate_description** | **int** | Maximum characters for description before truncation | [optional] 
**field_order** | **List[str]** | Order of fields to display in result card. Fields not in this list won&#39;t be shown. Must be subset of exposed_fields. | [optional] 
**show_find_similar** | **bool** | Whether to show a &#39;Find Similar&#39; button on result cards | [optional] [default to False]
**card_click_action** | **str** | Action when card is clicked: none (no action), findSimilar (trigger similar search), viewDetails (open detail modal) | [optional] [default to 'viewDetails']
**thumbnail_field** | **str** | Field name to use as thumbnail image source | [optional] 
**title_field** | **str** | Field name to use as card title | [optional] 
**card_fields** | **List[str]** | Fields to display on the card (alternative to field_order for template compatibility) | [optional] 
**modal_fields** | **List[str]** | Fields to display in the detail modal when card is clicked | [optional] 
**card_style** | **str** | Card style preset: default, portrait-discovery, media-search, document-search, or custom template-specific styles | [optional] [default to 'default']

## Example

```python
from mixpeek.models.result_card_properties import ResultCardProperties

# TODO update the JSON string below
json = "{}"
# create an instance of ResultCardProperties from a JSON string
result_card_properties_instance = ResultCardProperties.from_json(json)
# print the JSON string representation of the object
print(ResultCardProperties.to_json())

# convert the object into a dict
result_card_properties_dict = result_card_properties_instance.to_dict()
# create an instance of ResultCardProperties from a dict
result_card_properties_from_dict = ResultCardProperties.from_dict(result_card_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


