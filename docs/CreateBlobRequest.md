# CreateBlobRequest

Request model for creating a new blob.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** | Property name in the schema that this blob belongs to | 
**key_prefix** | **str** | Optional prefix for the blob key | [optional] 
**type** | [**BucketSchemaFieldType**](BucketSchemaFieldType.md) | The schema field type this blob corresponds to (e.g., IMAGE, PDF, DOCUMENT) | 
**data** | [**Data1**](Data1.md) |  | 
**metadata** | **Dict[str, object]** | Metadata for the blob, this will only be applied to the documents that use this blob | [optional] 
**canonicalize_source** | **bool** | If set, override object-level default to control source canonicalization for this blob. | [optional] 
**force_remirror** | **bool** | If set, override object-level default to force re-upload even if an identical blob exists. | [optional] 

## Example

```python
from mixpeek.models.create_blob_request import CreateBlobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBlobRequest from a JSON string
create_blob_request_instance = CreateBlobRequest.from_json(json)
# print the JSON string representation of the object
print(CreateBlobRequest.to_json())

# convert the object into a dict
create_blob_request_dict = create_blob_request_instance.to_dict()
# create an instance of CreateBlobRequest from a dict
create_blob_request_from_dict = CreateBlobRequest.from_dict(create_blob_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


