# UploadListStats

Aggregate statistics for a list of uploads.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_uploads** | **int** | Total number of uploads in the result set | 
**total_size_bytes** | **int** | Total size of all files in bytes | 
**uploads_by_status** | **Dict[str, int]** | Count of uploads grouped by status | 
**avg_file_size_bytes** | **float** | Average file size across all uploads | 
**unique_buckets** | **int** | Number of unique buckets in the result set | 

## Example

```python
from mixpeek.models.upload_list_stats import UploadListStats

# TODO update the JSON string below
json = "{}"
# create an instance of UploadListStats from a JSON string
upload_list_stats_instance = UploadListStats.from_json(json)
# print the JSON string representation of the object
print(UploadListStats.to_json())

# convert the object into a dict
upload_list_stats_dict = upload_list_stats_instance.to_dict()
# create an instance of UploadListStats from a dict
upload_list_stats_from_dict = UploadListStats.from_dict(upload_list_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


