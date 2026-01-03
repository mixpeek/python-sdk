# AggregationFunction

Supported aggregation functions.  These functions can be applied to fields during aggregation operations.  Values:     COUNT: Count total number of items in each group     COUNT_DISTINCT: Count unique values in a field     SUM: Sum numeric values     AVG: Calculate average of numeric values     MIN: Find minimum value     MAX: Find maximum value     FIRST: Get first value in group     LAST: Get last value in group     PUSH: Collect all values into an array     ADD_TO_SET: Collect unique values into an array  Examples:     - Use COUNT for total items per category     - Use COUNT_DISTINCT for unique users per day     - Use SUM for total revenue     - Use AVG for average video duration

## Enum

* `COUNT` (value: `'count'`)

* `COUNT_DISTINCT` (value: `'count_distinct'`)

* `SUM` (value: `'sum'`)

* `AVG` (value: `'avg'`)

* `MIN` (value: `'min'`)

* `MAX` (value: `'max'`)

* `FIRST` (value: `'first'`)

* `LAST` (value: `'last'`)

* `PUSH` (value: `'push'`)

* `ADD_TO_SET` (value: `'add_to_set'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


