# CollectionListStats

Aggregate statistics for a list of collections.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_documents** | **int** | Total number of documents across all collections | [optional] [default to 0]
**avg_documents_per_collection** | **float** | Average number of documents per collection | [optional] [default to 0.0]
**collections_with_taxonomies** | **int** | Number of collections with taxonomy applications | [optional] [default to 0]
**total_feature_extractors** | **int** | Total number of feature extractors across all collections | [optional] [default to 0]
**total_taxonomies** | **int** | Total number of taxonomy connections across all collections | [optional] [default to 0]
**total_retrievers** | **int** | Total number of retriever connections across all collections | [optional] [default to 0]

## Example

```python
from mixpeek.models.collection_list_stats import CollectionListStats

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionListStats from a JSON string
collection_list_stats_instance = CollectionListStats.from_json(json)
# print the JSON string representation of the object
print(CollectionListStats.to_json())

# convert the object into a dict
collection_list_stats_dict = collection_list_stats_instance.to_dict()
# create an instance of CollectionListStats from a dict
collection_list_stats_from_dict = CollectionListStats.from_dict(collection_list_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


