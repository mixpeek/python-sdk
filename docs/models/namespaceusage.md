# NamespaceUsage

Usage statistics for a single namespace


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `namespace_id`                                                       | *str*                                                                | :heavy_check_mark:                                                   | Namespace ID                                                         |
| `namespace_name`                                                     | *str*                                                                | :heavy_check_mark:                                                   | Namespace name                                                       |
| `storage_used_gb`                                                    | *float*                                                              | :heavy_check_mark:                                                   | Storage used in GB                                                   |
| `api_calls_30d`                                                      | *int*                                                                | :heavy_check_mark:                                                   | API calls in the last 30 days                                        |
| `documents_count`                                                    | *int*                                                                | :heavy_check_mark:                                                   | Number of documents                                                  |
| `last_activity`                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Timestamp of last activity                                           |