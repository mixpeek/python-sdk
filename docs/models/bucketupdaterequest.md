# BucketUpdateRequest

Request model for updating an existing bucket


## Fields

| Field                              | Type                               | Required                           | Description                        |
| ---------------------------------- | ---------------------------------- | ---------------------------------- | ---------------------------------- |
| `bucket_name`                      | *OptionalNullable[str]*            | :heavy_minus_sign:                 | Human-readable name for the bucket |
| `description`                      | *OptionalNullable[str]*            | :heavy_minus_sign:                 | Description of the bucket          |
| `metadata`                         | Dict[str, *Any*]                   | :heavy_minus_sign:                 | Additional metadata for the bucket |