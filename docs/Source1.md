# Source1

Source extractor defining where to get the value. Options: tag, metadata, filename_regex, column, drive_property, folder_path, constant. The 'file' source is not valid for field mappings (use blob instead).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Source type identifier. Must be &#39;tag&#39; for S3/Tigris object tags. | [optional] [default to 'tag']
**key** | **str** | The property key to extract. Built-in: &#39;name&#39;, &#39;mimeType&#39;, &#39;description&#39;, &#39;starred&#39;, &#39;createdTime&#39;, &#39;modifiedTime&#39;, &#39;size&#39;, &#39;webViewLink&#39;, &#39;parents&#39;. Custom: Any key set in the file&#39;s appProperties. Case-sensitive. | 
**pattern** | **str** | Python regex pattern with exactly one capture group. The captured group becomes the extracted value. Pattern is applied to the filename only (not full path). Use non-capturing groups (?:...) for grouping without capturing. Remember to escape backslashes in JSON (\\\\d instead of \\d). | 
**default** | **str** | Default value if regex doesn&#39;t match the filename. If None and regex doesn&#39;t match, the field is omitted from the object. Useful for ensuring a field always has a value. | [optional] 
**name** | **str** | The column name to extract from. Case handling depends on the database. Snowflake: case-insensitive (defaults to uppercase). PostgreSQL: case-sensitive unless quoted. Column must exist in the source table/view. | 
**segment** | **int** | Extract a specific path segment by index. 0 &#x3D; first segment (root folder), 1 &#x3D; second segment, etc. -1 &#x3D; last segment (immediate parent), -2 &#x3D; second to last, etc. If None and full_path is False, extracts the immediate parent folder. | [optional] 
**full_path** | **bool** | If True, extracts the complete folder path (joined with &#39;/&#39;). If False, extracts only the segment specified or immediate parent. Does not include the filename. | [optional] [default to False]
**value** | **object** |  | 

## Example

```python
from mixpeek.models.source1 import Source1

# TODO update the JSON string below
json = "{}"
# create an instance of Source1 from a JSON string
source1_instance = Source1.from_json(json)
# print the JSON string representation of the object
print(Source1.to_json())

# convert the object into a dict
source1_dict = source1_instance.to_dict()
# create an instance of Source1 from a dict
source1_from_dict = Source1.from_dict(source1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


