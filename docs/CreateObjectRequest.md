# CreateObjectRequest

Request model for creating a bucket object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_prefix** | **str** | Storage key/path prefix of the object, this will be used to retrieve the object from the storage. It&#39;s at the root of the object. | [optional] 
**blobs** | [**List[CreateBlobRequest]**](CreateBlobRequest.md) | List of blobs to be created in this object | [optional] 
**metadata** | **Dict[str, object]** | Additional metadata for the object, this will be appended in all downstream documents of the your connected collections. | [optional] 
**skip_duplicates** | **bool** | Skip duplicate blobs, if a blob with the same hash already exists, it will be skipped. | [optional] [default to False]
**canonicalize_source** | **bool** | Mirror non-S3 sources into internal S3 and reference canonically. | [optional] [default to True]
**force_remirror** | **bool** | Force re-upload to S3 even if a blob with identical content already exists. | [optional] [default to False]

## Example

```python
from mixpeek.models.create_object_request import CreateObjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateObjectRequest from a JSON string
create_object_request_instance = CreateObjectRequest.from_json(json)
# print the JSON string representation of the object
print(CreateObjectRequest.to_json())

# convert the object into a dict
create_object_request_dict = create_object_request_instance.to_dict()
# create an instance of CreateObjectRequest from a dict
create_object_request_from_dict = CreateObjectRequest.from_dict(create_object_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


