# BucketResponse

Response model for bucket operations


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `bucket_id`                                                  | *Optional[str]*                                              | :heavy_minus_sign:                                           | Unique identifier for the bucket                             |
| `bucket_name`                                                | *str*                                                        | :heavy_check_mark:                                           | Human-readable name for the bucket                           |
| `description`                                                | *OptionalNullable[str]*                                      | :heavy_minus_sign:                                           | Description of the bucket                                    |
| `bucket_schema`                                              | [models.BucketSchemaOutput](../models/bucketschemaoutput.md) | :heavy_check_mark:                                           | Schema definition for bucket objects                         |
| `metadata`                                                   | Dict[str, *Any*]                                             | :heavy_minus_sign:                                           | Additional metadata for the bucket                           |
| `object_count`                                               | *int*                                                        | :heavy_check_mark:                                           | Number of objects in the bucket                              |
| `total_size_bytes`                                           | *int*                                                        | :heavy_check_mark:                                           | Total size of all objects in the bucket in bytes             |