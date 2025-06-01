# BucketCreateRequest

Request model for creating a new bucket


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `bucket_name`                                              | *str*                                                      | :heavy_check_mark:                                         | Human-readable name for the bucket                         |
| `description`                                              | *OptionalNullable[str]*                                    | :heavy_minus_sign:                                         | Description of the bucket                                  |
| `bucket_schema`                                            | [models.BucketSchemaInput](../models/bucketschemainput.md) | :heavy_check_mark:                                         | Schema definition for bucket objects                       |
| `metadata`                                                 | Dict[str, *Any*]                                           | :heavy_minus_sign:                                         | Additional metadata for the bucket                         |