# ObjectResponse

Response model for bucket objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_id** | **str** | Unique identifier for the object | [optional] 
**bucket_id** | **str** | ID of the bucket this object belongs to | 
**key_prefix** | **str** | Storage key/path of the object, this will be used to retrieve the object from the storage. It is similar to a file path. If not provided, it will be placed in the root of the bucket. | [optional] 
**content_hash** | **str** | SHA256 hash of the object&#39;s content, used for de-duplication. | [optional] 
**blobs** | [**List[BlobModel]**](BlobModel.md) | List of blobs contained in this object | [optional] 
**source_details** | [**List[SourceDetails]**](SourceDetails.md) | Lineage/source details for this object; used for downstream references. | [optional] 
**metadata** | **Dict[str, object]** | Additional metadata for the object, this will be appended in all downstream documents of the your connected collections. | [optional] 
**status** | [**TaskStatusEnum**](TaskStatusEnum.md) | The current status of the object. | [optional] 
**error** | **str** | The error message if the object failed to process. | [optional] 
**skip_duplicates** | **bool** | Skip duplicate blobs, if a blob with the same hash already exists, it will be skipped. | [optional] [default to False]

## Example

```python
from mixpeek.models.object_response import ObjectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectResponse from a JSON string
object_response_instance = ObjectResponse.from_json(json)
# print the JSON string representation of the object
print(ObjectResponse.to_json())

# convert the object into a dict
object_response_dict = object_response_instance.to_dict()
# create an instance of ObjectResponse from a dict
object_response_from_dict = ObjectResponse.from_dict(object_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


