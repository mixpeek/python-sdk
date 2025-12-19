# BucketSchemaInput

Schema definition for bucket objects.  IMPORTANT: The bucket schema defines what fields your bucket objects will have. This schema is REQUIRED if you want to: 1. Create collections that use input_mappings to process your bucket data 2. Validate object structure before ingestion 3. Enable type-safe data pipelines  The schema defines the custom fields that will be used in: - Blob properties (e.g., \"content\", \"thumbnail\", \"transcript\") - Object metadata structure - Blob data structures  Example workflow: 1. Create bucket WITH schema defining your data structure 2. Upload objects that conform to that schema 3. Create collections that map schema fields to feature extractors  Without a bucket_schema, collections cannot use input_mappings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**Dict[str, BucketSchemaFieldInput]**](BucketSchemaFieldInput.md) |  | 

## Example

```python
from mixpeek.models.bucket_schema_input import BucketSchemaInput

# TODO update the JSON string below
json = "{}"
# create an instance of BucketSchemaInput from a JSON string
bucket_schema_input_instance = BucketSchemaInput.from_json(json)
# print the JSON string representation of the object
print(BucketSchemaInput.to_json())

# convert the object into a dict
bucket_schema_input_dict = bucket_schema_input_instance.to_dict()
# create an instance of BucketSchemaInput from a dict
bucket_schema_input_from_dict = BucketSchemaInput.from_dict(bucket_schema_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


