# UpdateObjectRequest

Request model for updating an existing bucket object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_prefix** | **str** | Updated storage key/path prefix of the object, this will be used to retrieve the object from the storage. It&#39;s at the root of the object. | [optional] 
**blobs** | [**List[CreateBlobRequest]**](CreateBlobRequest.md) | List of new or updated blobs for this object | [optional] 
**metadata** | **Dict[str, object]** | Updated metadata for the object, this will be merged with existing metadata. | [optional] 
**skip_duplicates** | **bool** | Skip duplicate blobs, if a blob with the same hash already exists, it will be skipped. | [optional] 

## Example

```python
from mixpeek.models.update_object_request import UpdateObjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateObjectRequest from a JSON string
update_object_request_instance = UpdateObjectRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateObjectRequest.to_json())

# convert the object into a dict
update_object_request_dict = update_object_request_instance.to_dict()
# create an instance of UpdateObjectRequest from a dict
update_object_request_from_dict = UpdateObjectRequest.from_dict(update_object_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


