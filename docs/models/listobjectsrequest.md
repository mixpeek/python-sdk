# ListObjectsRequest

Request model for listing objects in a bucket


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `filters`                                                                          | [OptionalNullable[models.LogicalOperatorInput]](../models/logicaloperatorinput.md) | :heavy_minus_sign:                                                                 | Filters to apply to the object list                                                |
| `sort`                                                                             | [OptionalNullable[models.SortOption]](../models/sortoption.md)                     | :heavy_minus_sign:                                                                 | Sort options for the object list                                                   |
| `search`                                                                           | *OptionalNullable[str]*                                                            | :heavy_minus_sign:                                                                 | Search term to filter objects by key or metadata                                   |