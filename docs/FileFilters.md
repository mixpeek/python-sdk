# FileFilters

Filter rules controlling which files are synced from storage providers.  All filters are optional and combined with AND logic. Files must pass ALL specified filters to be synced.  **Pattern Matching:** Uses glob patterns (*, ?, [abc], etc.) **Size Filtering:** Bytes-based, inclusive bounds **Time Filtering:** ISO 8601 datetime, based on provider's modified timestamp

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_patterns** | **List[str]** | Glob patterns to include (e.g. [&#39;*.mp4&#39;, &#39;*.mov&#39;]). | [optional] 
**exclude_patterns** | **List[str]** | Glob patterns to exclude (e.g. [&#39;*/drafts/*&#39;, &#39;*_temp.*&#39;]). | [optional] 
**min_size_bytes** | **int** | Minimum file size (bytes). Files smaller are skipped. | [optional] 
**max_size_bytes** | **int** | Maximum file size (bytes). Files larger are skipped. | [optional] 
**modified_after** | **datetime** | Only sync files modified after this timestamp. | [optional] 
**modified_before** | **datetime** | Only sync files modified before this timestamp. | [optional] 
**mime_types** | **List[str]** | Optional list of MIME types to include. | [optional] 

## Example

```python
from mixpeek.models.file_filters import FileFilters

# TODO update the JSON string below
json = "{}"
# create an instance of FileFilters from a JSON string
file_filters_instance = FileFilters.from_json(json)
# print the JSON string representation of the object
print(FileFilters.to_json())

# convert the object into a dict
file_filters_dict = file_filters_instance.to_dict()
# create an instance of FileFilters from a dict
file_filters_from_dict = FileFilters.from_dict(file_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


