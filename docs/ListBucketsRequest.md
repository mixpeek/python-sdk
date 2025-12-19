# ListBucketsRequest

Request model for listing buckets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search** | **str** | Search term for wildcard search across all text fields | [optional] 
**filters** | **Dict[str, object]** | Filters to apply to the bucket list | [optional] 
**sort** | **Dict[str, object]** | Sort options for the bucket list | [optional] 
**case_sensitive** | **bool** | If True, filters and search will be case-sensitive | [optional] [default to False]
**limit** | **int** | Number of results to return | [optional] [default to 10]
**offset** | **int** | Number of results to skip | [optional] [default to 0]

## Example

```python
from mixpeek.models.list_buckets_request import ListBucketsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListBucketsRequest from a JSON string
list_buckets_request_instance = ListBucketsRequest.from_json(json)
# print the JSON string representation of the object
print(ListBucketsRequest.to_json())

# convert the object into a dict
list_buckets_request_dict = list_buckets_request_instance.to_dict()
# create an instance of ListBucketsRequest from a dict
list_buckets_request_from_dict = ListBucketsRequest.from_dict(list_buckets_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


