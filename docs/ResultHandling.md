# ResultHandling

How to handle multiple result rows from SQL query.  Values:     FIRST: Return only the first row (most common for lookups)         - Use when expecting single result (lookup by primary key)         - Result stored as object      ALL: Return all rows as array         - Use when query may return multiple matches         - Result stored as array of objects      ERROR_IF_EMPTY: Raise error if no rows returned         - Use when result is mandatory         - Fails enrichment if query returns nothing      ERROR_IF_MULTIPLE: Raise error if more than one row returned         - Use for strict single-result lookups         - Validates uniqueness constraint at runtime

## Enum

* `FIRST` (value: `'first'`)

* `ALL` (value: `'all'`)

* `ERROR_IF_EMPTY` (value: `'error_if_empty'`)

* `ERROR_IF_MULTIPLE` (value: `'error_if_multiple'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


