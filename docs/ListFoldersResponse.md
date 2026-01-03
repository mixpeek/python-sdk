# ListFoldersResponse

Response payload for listing Google Drive folders.  Returns a list of folders available at the specified path, enabling users to browse and select folders for sync configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[FolderItem]**](FolderItem.md) | List of folders found at the specified parent path. Only includes folders (not files). Empty list if no folders found or path doesn&#39;t exist. | 
**parent_path** | **str** | The parent folder path that was queried. This is the path specified in the request (or &#39;/&#39; for root). Use this to show breadcrumb navigation in UI. | 

## Example

```python
from mixpeek.models.list_folders_response import ListFoldersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListFoldersResponse from a JSON string
list_folders_response_instance = ListFoldersResponse.from_json(json)
# print the JSON string representation of the object
print(ListFoldersResponse.to_json())

# convert the object into a dict
list_folders_response_dict = list_folders_response_instance.to_dict()
# create an instance of ListFoldersResponse from a dict
list_folders_response_from_dict = ListFoldersResponse.from_dict(list_folders_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


