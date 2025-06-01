# LogicalOperatorBaseOutput

Base logical operation without nesting, used to prevent infinite recursion.


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `and_`                                                       | List[[models.FilterCondition](../models/filtercondition.md)] | :heavy_minus_sign:                                           | Logical AND operation - all conditions must be true          |
| `or_`                                                        | List[[models.FilterCondition](../models/filtercondition.md)] | :heavy_minus_sign:                                           | Logical OR operation - at least one condition must be true   |
| `not_`                                                       | List[[models.FilterCondition](../models/filtercondition.md)] | :heavy_minus_sign:                                           | Logical NOT operation - all conditions must be false         |
| `case_sensitive`                                             | *OptionalNullable[bool]*                                     | :heavy_minus_sign:                                           | Whether to perform case-sensitive matching                   |