# UploadPerformanceResponse

Upload performance analytics response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_id** | **str** | Bucket identifier | 
**time_range** | [**ApiAnalyticsBucketsModelsTimeRange**](ApiAnalyticsBucketsModelsTimeRange.md) | Query time range | 
**metrics** | [**List[UploadPerformanceMetric]**](UploadPerformanceMetric.md) | Upload performance metrics | 
**summary** | **Dict[str, object]** | Summary statistics | [optional] 

## Example

```python
from mixpeek.models.upload_performance_response import UploadPerformanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UploadPerformanceResponse from a JSON string
upload_performance_response_instance = UploadPerformanceResponse.from_json(json)
# print the JSON string representation of the object
print(UploadPerformanceResponse.to_json())

# convert the object into a dict
upload_performance_response_dict = upload_performance_response_instance.to_dict()
# create an instance of UploadPerformanceResponse from a dict
upload_performance_response_from_dict = UploadPerformanceResponse.from_dict(upload_performance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


