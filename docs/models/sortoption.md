# SortOption

Specifies how to sort query results.

Attributes:
    field: Field to sort by
    direction: Sort direction (ascending or descending)


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  | Example                                                      |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `field`                                                      | *str*                                                        | :heavy_check_mark:                                           | Field to sort by, supports dot notation for nested fields    | created_at                                                   |
| `direction`                                                  | [Optional[models.SortDirection]](../models/sortdirection.md) | :heavy_minus_sign:                                           | Sort direction options.                                      |                                                              |