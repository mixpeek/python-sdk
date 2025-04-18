# CacheStats

Statistics about cache usage


## Fields

| Field                       | Type                        | Required                    | Description                 |
| --------------------------- | --------------------------- | --------------------------- | --------------------------- |
| `hits`                      | *Optional[int]*             | :heavy_minus_sign:          | Number of cache hits        |
| `misses`                    | *Optional[int]*             | :heavy_minus_sign:          | Number of cache misses      |
| `size`                      | *Optional[int]*             | :heavy_minus_sign:          | Number of entries in cache  |
| `hit_ratio`                 | *Optional[float]*           | :heavy_minus_sign:          | Cache hit ratio             |
| `retriever_stats`           | Dict[str, Dict[str, *int*]] | :heavy_minus_sign:          | Statistics per retriever    |