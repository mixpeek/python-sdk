# SourceConfigInput

Configuration for a collection source


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `type`                                                                             | [models.SourceType](../models/sourcetype.md)                                       | :heavy_check_mark:                                                                 | Types of entries in a collection lineage                                           |
| `bucket_id`                                                                        | *OptionalNullable[str]*                                                            | :heavy_minus_sign:                                                                 | ID of the source bucket                                                            |
| `prefix_key`                                                                       | *OptionalNullable[str]*                                                            | :heavy_minus_sign:                                                                 | Optional prefix to filter bucket objects                                           |
| `collection_id`                                                                    | *OptionalNullable[str]*                                                            | :heavy_minus_sign:                                                                 | ID of the source collection                                                        |
| `filters`                                                                          | [OptionalNullable[models.LogicalOperatorInput]](../models/logicaloperatorinput.md) | :heavy_minus_sign:                                                                 | Optional filters to apply to the source collection                                 |