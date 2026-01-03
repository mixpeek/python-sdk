# TaxonomyListStats

Aggregate statistics for a list of taxonomies.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_taxonomies** | **int** | Total number of taxonomies in the result | [optional] [default to 0]
**flat_taxonomies** | **int** | Number of flat taxonomies | [optional] [default to 0]
**hierarchical_taxonomies** | **int** | Number of hierarchical taxonomies | [optional] [default to 0]
**taxonomies_with_retrievers** | **int** | Number of taxonomies with retriever configured | [optional] [default to 0]

## Example

```python
from mixpeek.models.taxonomy_list_stats import TaxonomyListStats

# TODO update the JSON string below
json = "{}"
# create an instance of TaxonomyListStats from a JSON string
taxonomy_list_stats_instance = TaxonomyListStats.from_json(json)
# print the JSON string representation of the object
print(TaxonomyListStats.to_json())

# convert the object into a dict
taxonomy_list_stats_dict = taxonomy_list_stats_instance.to_dict()
# create an instance of TaxonomyListStats from a dict
taxonomy_list_stats_from_dict = TaxonomyListStats.from_dict(taxonomy_list_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


