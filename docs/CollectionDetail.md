# CollectionDetail

Detailed information about a collection referenced by a retriever.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_id** | **str** | Collection identifier | 
**collection_name** | **str** | Human-readable collection name | 
**document_count** | **int** | Number of documents in the collection | [optional] 
**enabled** | **bool** | Whether the collection is active | [optional] 
**last_indexed_at** | **datetime** | When the collection was last indexed | [optional] 

## Example

```python
from mixpeek.models.collection_detail import CollectionDetail

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionDetail from a JSON string
collection_detail_instance = CollectionDetail.from_json(json)
# print the JSON string representation of the object
print(CollectionDetail.to_json())

# convert the object into a dict
collection_detail_dict = collection_detail_instance.to_dict()
# create an instance of CollectionDetail from a dict
collection_detail_from_dict = CollectionDetail.from_dict(collection_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


