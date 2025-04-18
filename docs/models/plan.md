# Plan

Subscription plan model


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `name`                                               | *str*                                                | :heavy_check_mark:                                   | Display name of the plan                             |
| `description`                                        | *OptionalNullable[str]*                              | :heavy_minus_sign:                                   | Plan description                                     |
| `price_monthly_usd`                                  | *OptionalNullable[float]*                            | :heavy_minus_sign:                                   | Monthly price in USD                                 |
| `price_yearly_usd`                                   | *OptionalNullable[float]*                            | :heavy_minus_sign:                                   | Yearly price in USD                                  |
| `totals`                                             | [models.ResourceTotals](../models/resourcetotals.md) | :heavy_check_mark:                                   | Resource totals for the organization                 |
| `features`                                           | List[*str*]                                          | :heavy_minus_sign:                                   | Available features for extraction                    |