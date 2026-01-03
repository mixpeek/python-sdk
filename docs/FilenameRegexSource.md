# FilenameRegexSource

Extract value from filename using a regex pattern with capture groups.  Useful when metadata is encoded in filenames following a naming convention. The regex must contain exactly one capture group to extract the value.  Provider Compatibility: All providers (works on any filename)  Example filenames and patterns:     - \"marketing_Q4_2024_final.mp4\" with pattern \"^(\\w+)_Q\\d+_\" -> \"marketing\"     - \"user_12345_avatar.jpg\" with pattern \"user_(\\d+)_\" -> \"12345\"     - \"2024-01-15_meeting_notes.pdf\" with pattern \"^(\\d{4}-\\d{2}-\\d{2})\" -> \"2024-01-15\"     - \"IMG_20240115_143022.jpg\" with pattern \"IMG_(\\d{8})_\" -> \"20240115\"  Note: Use raw strings in Python or double-escape backslashes in JSON.  Attributes:     type: Must be \"filename_regex\" to identify this source type     pattern: Python regex with exactly one capture group     default: Optional default value if regex doesn't match

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Source type identifier. Must be &#39;filename_regex&#39; for regex extraction. | [optional] [default to 'filename_regex']
**pattern** | **str** | Python regex pattern with exactly one capture group. The captured group becomes the extracted value. Pattern is applied to the filename only (not full path). Use non-capturing groups (?:...) for grouping without capturing. Remember to escape backslashes in JSON (\\\\d instead of \\d). | 
**default** | **str** | Default value if regex doesn&#39;t match the filename. If None and regex doesn&#39;t match, the field is omitted from the object. Useful for ensuring a field always has a value. | [optional] 

## Example

```python
from mixpeek.models.filename_regex_source import FilenameRegexSource

# TODO update the JSON string below
json = "{}"
# create an instance of FilenameRegexSource from a JSON string
filename_regex_source_instance = FilenameRegexSource.from_json(json)
# print the JSON string representation of the object
print(FilenameRegexSource.to_json())

# convert the object into a dict
filename_regex_source_dict = filename_regex_source_instance.to_dict()
# create an instance of FilenameRegexSource from a dict
filename_regex_source_from_dict = FilenameRegexSource.from_dict(filename_regex_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


