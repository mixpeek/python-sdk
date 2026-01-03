# FolderPathSource

Extract value from the folder path structure.  Useful for deriving categories or metadata from folder organization. Can extract the full path, a specific segment, or the immediate parent.  Provider Compatibility: All providers with folder/prefix structure  Example folder structure: /Marketing/Campaigns/Q4-2024/videos/     - segment=0 -> \"Marketing\"     - segment=1 -> \"Campaigns\"     - segment=2 -> \"Q4-2024\"     - segment=-1 -> \"videos\" (last segment)     - full_path=True -> \"Marketing/Campaigns/Q4-2024/videos\"     - Neither (default) -> \"videos\" (immediate parent)  Use Cases:     - Derive category from top-level folder     - Extract project name from folder structure     - Preserve full path for hierarchical organization  Attributes:     type: Must be \"folder_path\" to identify this source type     segment: Index of path segment to extract (0-based, negative for reverse)     full_path: Whether to extract complete path

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Source type identifier. Must be &#39;folder_path&#39; for path extraction. | [optional] [default to 'folder_path']
**segment** | **int** | Extract a specific path segment by index. 0 &#x3D; first segment (root folder), 1 &#x3D; second segment, etc. -1 &#x3D; last segment (immediate parent), -2 &#x3D; second to last, etc. If None and full_path is False, extracts the immediate parent folder. | [optional] 
**full_path** | **bool** | If True, extracts the complete folder path (joined with &#39;/&#39;). If False, extracts only the segment specified or immediate parent. Does not include the filename. | [optional] [default to False]

## Example

```python
from mixpeek.models.folder_path_source import FolderPathSource

# TODO update the JSON string below
json = "{}"
# create an instance of FolderPathSource from a JSON string
folder_path_source_instance = FolderPathSource.from_json(json)
# print the JSON string representation of the object
print(FolderPathSource.to_json())

# convert the object into a dict
folder_path_source_dict = folder_path_source_instance.to_dict()
# create an instance of FolderPathSource from a dict
folder_path_source_from_dict = FolderPathSource.from_dict(folder_path_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


