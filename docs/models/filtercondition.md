# FilterCondition

Represents a single filter condition.

Attributes:
    field: The field to filter on
    operator: The comparison operator
    value: The value to compare against


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `field`                                                        | *str*                                                          | :heavy_check_mark:                                             | Field name to filter on                                        |
| `operator`                                                     | [Optional[models.FilterOperator]](../models/filteroperator.md) | :heavy_minus_sign:                                             | Supported filter operators across database implementations.    |
| `value`                                                        | *OptionalNullable[Any]*                                        | :heavy_minus_sign:                                             | Value to compare against                                       |