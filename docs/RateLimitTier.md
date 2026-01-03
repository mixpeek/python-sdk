# RateLimitTier

Rate limit tier for public retrievers.  Defines preset rate limit configurations for different use cases.  Tiers:     STANDARD: Default tier for most public retrievers         - 10 requests/minute         - 100 requests/hour         - 1,000 requests/day         - Suitable for demos, prototypes, and low-traffic public applications      ELEVATED: Higher limits for trusted public applications         - 30 requests/minute (3x standard)         - 500 requests/hour (5x standard)         - 5,000 requests/day (5x standard)         - Suitable for production public apps with moderate traffic      ENTERPRISE: High limits for enterprise public deployments         - 100 requests/minute (10x standard)         - 2,000 requests/hour (20x standard)         - 20,000 requests/day (20x standard)         - Suitable for high-traffic public applications with monitoring      UNLIMITED: No rate limiting         - Use with extreme caution - only for fully trusted deployments         - Still respects max_results_per_query and IP limits if enabled

## Enum

* `STANDARD` (value: `'standard'`)

* `ELEVATED` (value: `'elevated'`)

* `ENTERPRISE` (value: `'enterprise'`)

* `UNLIMITED` (value: `'unlimited'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


