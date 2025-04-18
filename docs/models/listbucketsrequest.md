# ListBucketsRequest

Request model for listing buckets


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `filters`                                                                          | [OptionalNullable[models.LogicalOperatorInput]](../models/logicaloperatorinput.md) | :heavy_minus_sign:                                                                 | Filters to apply to the bucket list                                                |
| `sort`                                                                             | [OptionalNullable[models.SortOption]](../models/sortoption.md)                     | :heavy_minus_sign:                                                                 | Sort options for the bucket list                                                   |
| `search`                                                                           | *OptionalNullable[str]*                                                            | :heavy_minus_sign:                                                                 | Search term to filter buckets by name or description                               |