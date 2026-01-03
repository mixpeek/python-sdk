# DocumentListStats

Aggregate statistics for a list of documents.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_documents** | **int** | Total number of documents in the result | [optional] [default to 0]
**avg_blobs_per_document** | **float** | Average number of source blobs per document | [optional] [default to 0.0]
**total_groups** | **int** | Total number of groups when group_by is used. None for non-grouped results. | [optional] 
**avg_documents_per_group** | **float** | Average number of documents per group when group_by is used. None for non-grouped results. | [optional] 

## Example

```python
from mixpeek.models.document_list_stats import DocumentListStats

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentListStats from a JSON string
document_list_stats_instance = DocumentListStats.from_json(json)
# print the JSON string representation of the object
print(DocumentListStats.to_json())

# convert the object into a dict
document_list_stats_dict = document_list_stats_instance.to_dict()
# create an instance of DocumentListStats from a dict
document_list_stats_from_dict = DocumentListStats.from_dict(document_list_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


