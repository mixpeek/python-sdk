# TaxonomyOptions

Options for taxonomy migration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preserve_taxonomy_ids** | **bool** | Keep same taxonomy IDs in target | [optional] [default to True]
**preserve_enrichment_fields** | **bool** | Keep _taxonomy_* fields in documents | [optional] [default to True]
**re_run_enrichment** | **bool** | Re-run taxonomy enrichment after migration | [optional] [default to False]
**migrate_reference_collections** | **bool** | Automatically migrate reference collections | [optional] [default to True]

## Example

```python
from mixpeek.models.taxonomy_options import TaxonomyOptions

# TODO update the JSON string below
json = "{}"
# create an instance of TaxonomyOptions from a JSON string
taxonomy_options_instance = TaxonomyOptions.from_json(json)
# print the JSON string representation of the object
print(TaxonomyOptions.to_json())

# convert the object into a dict
taxonomy_options_dict = taxonomy_options_instance.to_dict()
# create an instance of TaxonomyOptions from a dict
taxonomy_options_from_dict = TaxonomyOptions.from_dict(taxonomy_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


