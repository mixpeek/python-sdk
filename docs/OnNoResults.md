# OnNoResults

Behavior when SQL query returns no rows.  Values:     SKIP: Keep document unchanged, do not set output_field         - Document passes through without enrichment         - Best for optional lookups      NULL: Set output_field to null         - Explicitly marks no result found         - Useful for downstream conditional logic      ERROR: Raise error and fail enrichment         - Strict mode for mandatory data         - Use with on_error to control pipeline behavior

## Enum

* `SKIP` (value: `'skip'`)

* `NULL` (value: `'null'`)

* `ERROR` (value: `'error'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


