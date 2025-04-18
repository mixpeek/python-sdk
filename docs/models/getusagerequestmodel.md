# GetUsageRequestModel

Request model for customizing usage data retrieval


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `time_range`                                                             | [Optional[models.UsageTimeRange]](../models/usagetimerange.md)           | :heavy_minus_sign:                                                       | Time ranges for usage data                                               |
| `custom_start_date`                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects)     | :heavy_minus_sign:                                                       | Custom start date if time_range is 'custom'                              |
| `custom_end_date`                                                        | [date](https://docs.python.org/3/library/datetime.html#date-objects)     | :heavy_minus_sign:                                                       | Custom end date if time_range is 'custom'                                |
| `include_namespace_breakdown`                                            | *Optional[bool]*                                                         | :heavy_minus_sign:                                                       | Whether to include usage breakdown by namespace                          |
| `history_aggregation`                                                    | [OptionalNullable[models.AggregationType]](../models/aggregationtype.md) | :heavy_minus_sign:                                                       | Aggregation level for historical data                                    |
| `namespaces`                                                             | List[*str*]                                                              | :heavy_minus_sign:                                                       | Filter to specific namespaces (all if not specified)                     |