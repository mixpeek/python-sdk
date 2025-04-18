# CollectionCacheConfigOutput

Configuration for collection-level caching


## Fields

| Field                                                                       | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `enabled`                                                                   | *Optional[bool]*                                                            | :heavy_minus_sign:                                                          | Whether caching is enabled                                                  |
| `ttl_seconds`                                                               | *Optional[int]*                                                             | :heavy_minus_sign:                                                          | Time-to-live for cache entries in seconds                                   |
| `invalidation_strategy`                                                     | [Optional[models.InvalidationStrategy]](../models/invalidationstrategy.md)  | :heavy_minus_sign:                                                          | Strategies for cache invalidation                                           |
| `max_entries_per_key`                                                       | *Optional[int]*                                                             | :heavy_minus_sign:                                                          | Maximum number of results to cache per key                                  |
| `score_threshold`                                                           | *OptionalNullable[float]*                                                   | :heavy_minus_sign:                                                          | Minimum score threshold for caching results                                 |
| `invalidation_events`                                                       | List[[models.InvalidationEvent](../models/invalidationevent.md)]            | :heavy_minus_sign:                                                          | Events that trigger cache invalidation                                      |
| `retriever_configs`                                                         | Dict[str, [models.RetrieverCacheConfig](../models/retrievercacheconfig.md)] | :heavy_minus_sign:                                                          | Retriever-specific cache configurations                                     |