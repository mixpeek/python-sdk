# BucketCreateRequest

Request model for creating a new bucket.  REQUIRED: A bucket_schema must be defined to enable data processing and validation.  The bucket_schema tells the system what fields your objects will have, enabling: - Collections to map your data fields to feature extractors via input_mappings - Validation of object structure at upload time - Type-safe data pipelines from bucket → collection → retrieval  Every bucket must have a schema that defines the structure of objects it will contain.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_name** | **str** | Human-readable name for the bucket | 
**description** | **str** | Description of the bucket | [optional] 
**bucket_schema** | [**BucketSchemaInput**](BucketSchemaInput.md) | Schema definition for objects in this bucket (REQUIRED). Defines the custom fields your objects will have (blob properties, metadata structure, etc.) | 
**unique_key** | [**UniqueKeyConfig**](UniqueKeyConfig.md) | Unique key configuration for this bucket (OPTIONAL). Enables uniqueness enforcement and upsert operations on specified field(s) from the schema. Cannot be changed after bucket creation. | [optional] 
**metadata** | **object** | Additional metadata for the bucket | [optional] 

## Example

```python
from mixpeek.models.bucket_create_request import BucketCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BucketCreateRequest from a JSON string
bucket_create_request_instance = BucketCreateRequest.from_json(json)
# print the JSON string representation of the object
print(BucketCreateRequest.to_json())

# convert the object into a dict
bucket_create_request_dict = bucket_create_request_instance.to_dict()
# create an instance of BucketCreateRequest from a dict
bucket_create_request_from_dict = BucketCreateRequest.from_dict(bucket_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


