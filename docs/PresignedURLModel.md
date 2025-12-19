# PresignedURLModel

Typed presigned URL entry for a related S3 object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_name** | **str** | Logical name or filename, e.g., &#39;thumb.jpg&#39; | 
**object_key** | **str** | Full S3 object key | 
**presigned_url** | **str** | Time-limited HTTPS URL | 

## Example

```python
from mixpeek.models.presigned_url_model import PresignedURLModel

# TODO update the JSON string below
json = "{}"
# create an instance of PresignedURLModel from a JSON string
presigned_url_model_instance = PresignedURLModel.from_json(json)
# print the JSON string representation of the object
print(PresignedURLModel.to_json())

# convert the object into a dict
presigned_url_model_dict = presigned_url_model_instance.to_dict()
# create an instance of PresignedURLModel from a dict
presigned_url_model_from_dict = PresignedURLModel.from_dict(presigned_url_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


