# BucketResponse

Response model for bucket operations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_id** | **str** | Unique identifier for the bucket | [optional] 
**bucket_name** | **str** | Human-readable name for the bucket | 
**description** | **str** | Description of the bucket | [optional] 
**bucket_schema** | [**BucketSchemaOutput**](BucketSchemaOutput.md) | Schema definition for objects in this bucket | [optional] 
**unique_key** | [**UniqueKeyConfig**](UniqueKeyConfig.md) | Unique key configuration for this bucket (if configured) | [optional] 
**metadata** | **object** | Additional metadata for the bucket | [optional] 
**object_count** | **int** | Number of objects in the bucket | 
**total_size_bytes** | **int** | Total size of all objects in the bucket in bytes | 
**created_at** | **datetime** | When the bucket was created | [optional] 
**updated_at** | **datetime** | Last modification time of bucket metadata | [optional] 
**last_upload_at** | **datetime** | When the last object was uploaded to this bucket | [optional] 
**status** | [**TaskStatusEnum**](TaskStatusEnum.md) | Bucket lifecycle status (ACTIVE, ARCHIVED, SUSPENDED, IN_PROGRESS for deleting) | [optional] 
**is_locked** | **bool** | Whether the bucket is locked (read-only) | [optional] [default to False]
**batch_stats** | [**BatchStatistics**](BatchStatistics.md) | Batch statistics for this bucket (calculated asynchronously, stored in DB) | [optional] 
**storage_stats** | [**StorageStatistics**](StorageStatistics.md) | Storage statistics for this bucket (calculated asynchronously, stored in DB) | [optional] 

## Example

```python
from mixpeek.models.bucket_response import BucketResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BucketResponse from a JSON string
bucket_response_instance = BucketResponse.from_json(json)
# print the JSON string representation of the object
print(BucketResponse.to_json())

# convert the object into a dict
bucket_response_dict = bucket_response_instance.to_dict()
# create an instance of BucketResponse from a dict
bucket_response_from_dict = BucketResponse.from_dict(bucket_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


