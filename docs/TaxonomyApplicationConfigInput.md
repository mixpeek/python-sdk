# TaxonomyApplicationConfigInput

Configuration block that attaches a taxonomy to a collection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taxonomy_id** | **str** | ID of the &#x60;TaxonomyModel&#x60; to execute. | 
**execution_mode** | [**TaxonomyExecutionMode**](TaxonomyExecutionMode.md) | Execution mode for taxonomy enrichment. Materializes results during ingestion. | [optional] 
**target_collection_id** | **str** | Optional collection to persist results into when &#x60;execution_mode&#x60; is &#39;materialize&#39;. If omitted, the source collection is updated in-place. | [optional] 
**scroll_filters** | [**LogicalOperatorInput**](LogicalOperatorInput.md) | Additional filters applied when scrolling the source collection before enrichment. | [optional] 

## Example

```python
from mixpeek.models.taxonomy_application_config_input import TaxonomyApplicationConfigInput

# TODO update the JSON string below
json = "{}"
# create an instance of TaxonomyApplicationConfigInput from a JSON string
taxonomy_application_config_input_instance = TaxonomyApplicationConfigInput.from_json(json)
# print the JSON string representation of the object
print(TaxonomyApplicationConfigInput.to_json())

# convert the object into a dict
taxonomy_application_config_input_dict = taxonomy_application_config_input_instance.to_dict()
# create an instance of TaxonomyApplicationConfigInput from a dict
taxonomy_application_config_input_from_dict = TaxonomyApplicationConfigInput.from_dict(taxonomy_application_config_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


