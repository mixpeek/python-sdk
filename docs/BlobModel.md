# BlobModel

Model for a blob within a bucket object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blob_id** | **str** | Unique identifier for the blob | [optional] 
**var_property** | **str** | Property name of the blob | 
**key_prefix** | **str** | Storage key/path of the blob, this will be used to retrieve the blob from the storage. It is similar to a file path. If not provided, it will be placed in the root of the bucket. | [optional] 
**type** | [**BucketSchemaFieldType**](BucketSchemaFieldType.md) | The schema field type this blob corresponds to (e.g., IMAGE, PDF, DOCUMENT) | 
**data** | [**Data**](Data.md) |  | 
**metadata** | **Dict[str, object]** | Metadata for the blob, this will only be applied to the documents that use this blob | [optional] 
**details** | [**BlobDetails**](BlobDetails.md) | Details of the blob | [optional] 

## Example

```python
from mixpeek.models.blob_model import BlobModel

# TODO update the JSON string below
json = "{}"
# create an instance of BlobModel from a JSON string
blob_model_instance = BlobModel.from_json(json)
# print the JSON string representation of the object
print(BlobModel.to_json())

# convert the object into a dict
blob_model_dict = blob_model_instance.to_dict()
# create an instance of BlobModel from a dict
blob_model_from_dict = BlobModel.from_dict(blob_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


