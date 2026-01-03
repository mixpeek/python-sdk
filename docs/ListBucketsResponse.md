# ListBucketsResponse

Response model for listing buckets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[BucketResponse]**](BucketResponse.md) |  | 
**total_count** | **int** | Total number of buckets matching the query | 
**pagination** | [**PaginationResponse**](PaginationResponse.md) |  | 
**stats** | [**BucketListStats**](BucketListStats.md) | Aggregate statistics across all buckets in the result | [optional] 

## Example

```python
from mixpeek.models.list_buckets_response import ListBucketsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListBucketsResponse from a JSON string
list_buckets_response_instance = ListBucketsResponse.from_json(json)
# print the JSON string representation of the object
print(ListBucketsResponse.to_json())

# convert the object into a dict
list_buckets_response_dict = list_buckets_response_instance.to_dict()
# create an instance of ListBucketsResponse from a dict
list_buckets_response_from_dict = ListBucketsResponse.from_dict(list_buckets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


