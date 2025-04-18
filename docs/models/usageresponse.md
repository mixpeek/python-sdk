# UsageResponse

Complete usage response model


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `usage_summary`                                                          | [models.UsageSummary](../models/usagesummary.md)                         | :heavy_check_mark:                                                       | Summary of current resource usage                                        |
| `namespace_usage`                                                        | List[[models.NamespaceUsage](../models/namespaceusage.md)]               | :heavy_check_mark:                                                       | Usage by namespace                                                       |
| `usage_history`                                                          | [OptionalNullable[models.TimeseriesUsage]](../models/timeseriesusage.md) | :heavy_minus_sign:                                                       | Historical usage data                                                    |
| `billing_period_start`                                                   | [date](https://docs.python.org/3/library/datetime.html#date-objects)     | :heavy_minus_sign:                                                       | Start of current billing period                                          |
| `billing_period_end`                                                     | [date](https://docs.python.org/3/library/datetime.html#date-objects)     | :heavy_check_mark:                                                       | End of current billing period                                            |
| `organization_id`                                                        | *str*                                                                    | :heavy_check_mark:                                                       | Organization ID                                                          |
| `current_plan`                                                           | [OptionalNullable[models.Plan]](../models/plan.md)                       | :heavy_minus_sign:                                                       | Current subscription plan                                                |