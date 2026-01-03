# FileSource

Use the synced file itself as the source (for blob mappings).  This is the primary source for blob-type mappings where the synced file content becomes the blob. The mime_type is automatically detected from the file unless explicitly overridden in the BlobMappingEntry.  Provider Compatibility: All providers (works on any synced file)  Example usage:     {\"type\": \"file\"} -> The synced file becomes the blob content  This source type has no additional configuration - it simply indicates that the synced file content should be used as the blob data.  Attributes:     type: Must be \"file\" to identify this source type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Source type identifier. Must be &#39;file&#39; for the synced file itself. | [optional] [default to 'file']

## Example

```python
from mixpeek.models.file_source import FileSource

# TODO update the JSON string below
json = "{}"
# create an instance of FileSource from a JSON string
file_source_instance = FileSource.from_json(json)
# print the JSON string representation of the object
print(FileSource.to_json())

# convert the object into a dict
file_source_dict = file_source_instance.to_dict()
# create an instance of FileSource from a dict
file_source_from_dict = FileSource.from_dict(file_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


