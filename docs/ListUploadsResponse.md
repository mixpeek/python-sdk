# ListUploadsResponse

Response model for listing uploads.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[UploadResponse]**](UploadResponse.md) | List of upload records matching the query | 
**pagination** | [**PaginationResponse**](PaginationResponse.md) | Pagination metadata including total count, limit, offset, has_more | 
**stats** | [**UploadListStats**](UploadListStats.md) | Aggregate statistics across all uploads in the result | 

## Example

```python
from mixpeek.models.list_uploads_response import ListUploadsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListUploadsResponse from a JSON string
list_uploads_response_instance = ListUploadsResponse.from_json(json)
# print the JSON string representation of the object
print(ListUploadsResponse.to_json())

# convert the object into a dict
list_uploads_response_dict = list_uploads_response_instance.to_dict()
# create an instance of ListUploadsResponse from a dict
list_uploads_response_from_dict = ListUploadsResponse.from_dict(list_uploads_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


