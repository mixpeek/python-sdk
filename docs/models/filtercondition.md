# FilterCondition


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `key`                                              | *str*                                              | :heavy_check_mark:                                 | Field name to filter on                            |
| `value`                                            | *OptionalNullable[Any]*                            | :heavy_minus_sign:                                 | Value to compare against                           |
| `operator`                                         | [Optional[models.Operator]](../models/operator.md) | :heavy_minus_sign:                                 | Comparison operator                                |