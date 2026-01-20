# ErrorHandling1

Error handling strategy for SQL lookup failures.  Values:     SKIP: Skip document enrichment, keep document unchanged         - Document remains in pipeline without enrichment         - Best for optional lookups      REMOVE: Remove document from results         - Document filtered out of pipeline         - Best when enrichment is mandatory      RAISE: Raise exception and fail pipeline         - Stops execution immediately         - Best for debugging or critical failures

## Enum

* `SKIP` (value: `'skip'`)

* `REMOVE` (value: `'remove'`)

* `RAISE` (value: `'raise'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


