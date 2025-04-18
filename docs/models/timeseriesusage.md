# TimeseriesUsage

Timeseries usage data for various metrics


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `api_calls`                                                          | List[[models.TimeseriesDataPoint](../models/timeseriesdatapoint.md)] | :heavy_minus_sign:                                                   | API calls over time                                                  |
| `storage_used`                                                       | List[[models.TimeseriesDataPoint](../models/timeseriesdatapoint.md)] | :heavy_minus_sign:                                                   | Storage used over time                                               |
| `documents_processed`                                                | List[[models.TimeseriesDataPoint](../models/timeseriesdatapoint.md)] | :heavy_minus_sign:                                                   | Documents processed over time                                        |
| `credits_used`                                                       | List[[models.TimeseriesDataPoint](../models/timeseriesdatapoint.md)] | :heavy_minus_sign:                                                   | Credits used over time                                               |