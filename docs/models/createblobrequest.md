# CreateBlobRequest

Request model for creating a new blob


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `property`                                                                           | *str*                                                                                | :heavy_check_mark:                                                                   | Property name in the schema that this blob belongs to                                |
| `key_prefix`                                                                         | *OptionalNullable[str]*                                                              | :heavy_minus_sign:                                                                   | Optional prefix for the blob key                                                     |
| `type`                                                                               | [models.BucketSchemaFieldType](../models/bucketschemafieldtype.md)                   | :heavy_check_mark:                                                                   | Enum for field types in bucket schemas                                               |
| `data`                                                                               | *Any*                                                                                | :heavy_check_mark:                                                                   | Data for the blob, this will only be applied to the documents that use this blob     |
| `metadata`                                                                           | Dict[str, *Any*]                                                                     | :heavy_minus_sign:                                                                   | Metadata for the blob, this will only be applied to the documents that use this blob |