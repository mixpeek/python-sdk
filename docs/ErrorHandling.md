# ErrorHandling

Error handling strategy for API call failures.  Defines what happens when an API call fails (network error, timeout, authentication failure, etc.). Choose based on whether failed enrichment should be fatal or gracefully handled.  Values:     SKIP: Skip document enrichment, keep document in results         - Document remains unchanged in the pipeline         - Best for optional enrichment         - Use when: Enrichment is nice-to-have but not critical         - Example: Adding weather data to locations (keep doc if API fails)      REMOVE: Remove document from results entirely         - Document is filtered out of pipeline         - Best when enrichment is mandatory         - Use when: Document is useless without enrichment         - Example: Must have Stripe billing data to proceed      RAISE: Raise exception and fail entire pipeline         - Stops pipeline execution immediately         - Best for debugging or critical failures         - Use when: Want to catch and fix configuration issues         - Example: Development/testing to catch errors early  Examples:     - Optional weather enrichment: SKIP     - Mandatory Stripe billing: REMOVE     - Development/debugging: RAISE

## Enum

* `SKIP` (value: `'skip'`)

* `REMOVE` (value: `'remove'`)

* `RAISE` (value: `'raise'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


