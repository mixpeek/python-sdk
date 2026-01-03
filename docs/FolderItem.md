# FolderItem

Represents a folder in Google Drive for folder selection in sync configuration.  Used by the list folders endpoint to help users browse and select folders for sync operations. Only available for Google Drive connections.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | REQUIRED. Folder ID in Google Drive. Use this ID when configuring sync operations. Format: Google Drive folder identifier (e.g., &#39;0AH-Xabc123&#39;). | 
**name** | **str** | REQUIRED. Display name of the folder. Human-readable name shown in the Google Drive UI. | 
**path** | **str** | REQUIRED. Full path from root to this folder. Format: &#39;/&#39; for root, &#39;/FolderName&#39; for first level, &#39;/Parent/Child&#39; for nested folders. | 
**mime_type** | **str** | REQUIRED. MIME type identifier for folders. Always &#39;application/vnd.google-apps.folder&#39; for folders. | 

## Example

```python
from mixpeek.models.folder_item import FolderItem

# TODO update the JSON string below
json = "{}"
# create an instance of FolderItem from a JSON string
folder_item_instance = FolderItem.from_json(json)
# print the JSON string representation of the object
print(FolderItem.to_json())

# convert the object into a dict
folder_item_dict = folder_item_instance.to_dict()
# create an instance of FolderItem from a dict
folder_item_from_dict = FolderItem.from_dict(folder_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


