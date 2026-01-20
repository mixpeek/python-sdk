# StageCacheBehavior1

Cache behavior modes for retriever stages.  Controls internal caching of stage operations for performance optimization. All modes are safe and automatic with LRU eviction - no manual cache management needed.  Values:     AUTO: Smart automatic caching (default, recommended)     DISABLED: Skip internal caching completely     AGGRESSIVE: Cache even non-deterministic operations (use with caution)  Cache Architecture:     - Redis with LRU eviction policy (memory-bounded)     - Namespace-isolated per organization (multi-tenant safe)     - Stage-specific keyspaces prevent conflicts     - Cache keys hash (stage_name, inputs, parameters)     - Automatic invalidation on parameter changes  Performance Impact:     - AUTO: 50-90% latency reduction for repeated operations     - Cache lookup overhead: <5ms     - Hit rates: Typically 60-80% in production  When to Use Each Mode:     AUTO (default):         - Deterministic transformations (parsing, formatting, reshaping)         - Stable external API calls (embeddings, standard inference)         - Operations without side effects         - Most use cases - this is the recommended default      DISABLED:         - Templates with now(), random(), or time-sensitive functions         - External APIs that must be called every time (real-time data)         - Operations with side effects         - Rapidly changing data where caching would serve stale results      AGGRESSIVE:         - When you fully understand caching implications         - For debugging or testing cache behavior         - Only use if you know cache invalidation is handled elsewhere         - Generally not recommended for production  Examples:     Basic usage (auto mode, no config needed):         {\"cache_behavior\": \"auto\"}  # or omit - this is the default      Disable for time-sensitive operations:         {\"cache_behavior\": \"disabled\"}  # Template has {{now()}}      With custom TTL:         {\"cache_behavior\": \"auto\", \"cache_ttl_seconds\": 300}

## Enum

* `AUTO` (value: `'auto'`)

* `DISABLED` (value: `'disabled'`)

* `AGGRESSIVE` (value: `'aggressive'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


