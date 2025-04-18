# RetrieverCacheConfig

Configuration for retriever-specific caching


## Fields

| Field                                         | Type                                          | Required                                      | Description                                   |
| --------------------------------------------- | --------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| `enabled`                                     | *Optional[bool]*                              | :heavy_minus_sign:                            | Whether caching is enabled for this retriever |
| `ttl_seconds`                                 | *OptionalNullable[int]*                       | :heavy_minus_sign:                            | Optional retriever-specific TTL override      |
| `score_threshold`                             | *OptionalNullable[float]*                     | :heavy_minus_sign:                            | Optional retriever-specific score threshold   |