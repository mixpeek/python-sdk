# DrivePropertySource

Extract value from Google Drive file properties.  Google Drive files have built-in properties (name, mimeType, etc.) and custom properties (appProperties). This source extracts from either.  Provider Compatibility: Google Drive, Google Workspace Shared Drives  Built-in properties:     - name: File name     - mimeType: MIME type     - description: File description     - starred: Boolean star status     - trashed: Boolean trash status     - createdTime: Creation timestamp     - modifiedTime: Last modified timestamp     - size: File size in bytes  Custom properties: Set via Drive API appProperties field  Example mapping:     {\"type\": \"drive_property\", \"key\": \"description\"} -> extracts file description  Attributes:     type: Must be \"drive_property\" to identify this source type     key: The property key to extract (case-sensitive)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Source type identifier. Must be &#39;drive_property&#39; for Google Drive. | [optional] [default to 'drive_property']
**key** | **str** | The property key to extract. Built-in: &#39;name&#39;, &#39;mimeType&#39;, &#39;description&#39;, &#39;starred&#39;, &#39;createdTime&#39;, &#39;modifiedTime&#39;, &#39;size&#39;, &#39;webViewLink&#39;, &#39;parents&#39;. Custom: Any key set in the file&#39;s appProperties. Case-sensitive. | 

## Example

```python
from mixpeek.models.drive_property_source import DrivePropertySource

# TODO update the JSON string below
json = "{}"
# create an instance of DrivePropertySource from a JSON string
drive_property_source_instance = DrivePropertySource.from_json(json)
# print the JSON string representation of the object
print(DrivePropertySource.to_json())

# convert the object into a dict
drive_property_source_dict = drive_property_source_instance.to_dict()
# create an instance of DrivePropertySource from a dict
drive_property_source_from_dict = DrivePropertySource.from_dict(drive_property_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


