# FlatTaxonomyConfigOutput

Configuration for a *flat* taxonomy - single source collection with one retriever.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taxonomy_type** | **str** | Discriminator identifying this as a flat taxonomy. | [optional] [default to 'flat']
**retriever_id** | **str** | The retriever to use for matching against the source collection. | 
**input_mappings** | [**List[InputMapping]**](InputMapping.md) | Input mappings defining how to construct retriever inputs. | 
**source_collection** | [**SourceCollectionOutput**](SourceCollectionOutput.md) | The single source collection for this flat taxonomy. | 
**step_analytics** | [**StepAnalyticsConfigOutput**](StepAnalyticsConfigOutput.md) | Optional configuration for step transition analytics. Enables tracking how documents progress through taxonomy labels over time (e.g., email thread progression from &#39;inquiry&#39; to &#39;closed_won&#39;). If not provided, only basic assignment events are logged. | [optional] 

## Example

```python
from mixpeek.models.flat_taxonomy_config_output import FlatTaxonomyConfigOutput

# TODO update the JSON string below
json = "{}"
# create an instance of FlatTaxonomyConfigOutput from a JSON string
flat_taxonomy_config_output_instance = FlatTaxonomyConfigOutput.from_json(json)
# print the JSON string representation of the object
print(FlatTaxonomyConfigOutput.to_json())

# convert the object into a dict
flat_taxonomy_config_output_dict = flat_taxonomy_config_output_instance.to_dict()
# create an instance of FlatTaxonomyConfigOutput from a dict
flat_taxonomy_config_output_from_dict = FlatTaxonomyConfigOutput.from_dict(flat_taxonomy_config_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


