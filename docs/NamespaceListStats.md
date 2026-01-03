# NamespaceListStats

Aggregate statistics for a list of namespaces.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_feature_extractors** | **int** | Total number of feature extractors across all namespaces | [optional] [default to 0]
**total_payload_indexes** | **int** | Total number of payload indexes across all namespaces | [optional] [default to 0]
**total_documents** | **int** | Total number of documents across all namespaces | [optional] [default to 0]
**total_buckets** | **int** | Total number of buckets across all namespaces | [optional] [default to 0]
**total_collections** | **int** | Total number of collections across all namespaces | [optional] [default to 0]
**total_objects** | **int** | Total number of objects across all namespaces | [optional] [default to 0]
**avg_feature_extractors_per_namespace** | **float** | Average number of feature extractors per namespace | [optional] [default to 0.0]
**avg_payload_indexes_per_namespace** | **float** | Average number of payload indexes per namespace | [optional] [default to 0.0]
**avg_documents_per_namespace** | **float** | Average number of documents per namespace | [optional] [default to 0.0]
**avg_buckets_per_namespace** | **float** | Average number of buckets per namespace | [optional] [default to 0.0]
**avg_collections_per_namespace** | **float** | Average number of collections per namespace | [optional] [default to 0.0]
**avg_objects_per_namespace** | **float** | Average number of objects per namespace | [optional] [default to 0.0]

## Example

```python
from mixpeek.models.namespace_list_stats import NamespaceListStats

# TODO update the JSON string below
json = "{}"
# create an instance of NamespaceListStats from a JSON string
namespace_list_stats_instance = NamespaceListStats.from_json(json)
# print the JSON string representation of the object
print(NamespaceListStats.to_json())

# convert the object into a dict
namespace_list_stats_dict = namespace_list_stats_instance.to_dict()
# create an instance of NamespaceListStats from a dict
namespace_list_stats_from_dict = NamespaceListStats.from_dict(namespace_list_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


