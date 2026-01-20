# CollectionExportResponse

Response model for collection export.  Contains the presigned URL for downloading the exported file. The URL is valid for a limited time (typically 1 hour).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_url** | **str** | Presigned URL for downloading the exported file. Valid for 1 hour. | 
**s3_path** | **str** | Full S3 path where the export is stored (for internal reference). | 
**format** | [**ExportFormat**](ExportFormat.md) | The format of the exported file. | 
**document_count** | **int** | Number of documents included in the export. | 
**file_size_bytes** | **int** | Size of the exported file in bytes. | 
**exported_at** | **datetime** | Timestamp when the export was completed. | 
**vectors_download_url** | **str** | Presigned URL for downloading the vectors file (if include_vectors&#x3D;True). Vectors are exported separately due to their large size. | [optional] 
**vectors_s3_path** | **str** | Full S3 path for the vectors file (if include_vectors&#x3D;True). | [optional] 

## Example

```python
from mixpeek.models.collection_export_response import CollectionExportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionExportResponse from a JSON string
collection_export_response_instance = CollectionExportResponse.from_json(json)
# print the JSON string representation of the object
print(CollectionExportResponse.to_json())

# convert the object into a dict
collection_export_response_dict = collection_export_response_instance.to_dict()
# create an instance of CollectionExportResponse from a dict
collection_export_response_from_dict = CollectionExportResponse.from_dict(collection_export_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


