# CloneCollectionResponse

Response after cloning a collection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection** | [**CollectionModel**](CollectionModel.md) | Cloned collection configuration with new collection_id. | 
**source_collection_id** | **str** | ID of the source collection that was cloned. | 

## Example

```python
from mixpeek.models.clone_collection_response import CloneCollectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CloneCollectionResponse from a JSON string
clone_collection_response_instance = CloneCollectionResponse.from_json(json)
# print the JSON string representation of the object
print(CloneCollectionResponse.to_json())

# convert the object into a dict
clone_collection_response_dict = clone_collection_response_instance.to_dict()
# create an instance of CloneCollectionResponse from a dict
clone_collection_response_from_dict = CloneCollectionResponse.from_dict(clone_collection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


