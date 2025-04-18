# CollectionCache
(*collection_cache*)

## Overview

### Available Operations

* [invalidate](#invalidate) - Invalidate Cache
* [get_stats](#get_stats) - Get Cache Stats
* [cleanup](#cleanup) - Cleanup Cache

## invalidate

Invalidate cache entries for a collection.

Args:
    collection_id: ID of the collection to invalidate
    action: Action that triggered invalidation (create, update, delete)
    document_ids: Optional list of specific document IDs to invalidate
    retriever_id: Optional retriever ID for retriever-specific invalidation
    recompute_strategy: Strategy for recomputing invalidated entries
    cache_service: Cache service instance

Returns:
    Success status

### Example Usage

```python
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.collection_cache.invalidate(collection_id="<id>", action="<value>", internal_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `collection_id`                                                                                                                                                                       | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
| `action`                                                                                                                                                                              | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
| `internal_id`                                                                                                                                                                         | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
| `retriever_id`                                                                                                                                                                        | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
| `recompute_strategy`                                                                                                                                                                  | [Optional[models.RecomputeStrategy]](../../models/recomputestrategy.md)                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Strategies for recomputing cache entries                                                                                                                                              |
| `redis_url`                                                                                                                                                                           | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
| `prefix`                                                                                                                                                                              | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
| `x_namespace`                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. |
| `request_body`                                                                                                                                                                        | List[*str*]                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
| `retries`                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                   |

### Response

**[Dict[str, bool]](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404         | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorResponse       | 500                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_stats

Get cache statistics.

Args:
    cache_service: Cache service instance

Returns:
    Cache statistics

### Example Usage

```python
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.collection_cache.get_stats(internal_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `internal_id`                                                                                                                                                                         | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
| `redis_url`                                                                                                                                                                           | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
| `prefix`                                                                                                                                                                              | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
| `x_namespace`                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. |
| `retries`                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                   |

### Response

**[models.CacheStats](../../models/cachestats.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404         | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorResponse       | 500                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## cleanup

Cleanup expired cache entries.

Args:
    batch_size: Number of keys to process per batch
    cache_service: Cache service instance

Returns:
    Number of keys deleted

### Example Usage

```python
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.collection_cache.cleanup(internal_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `internal_id`                                                                                                                                                                         | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
| `batch_size`                                                                                                                                                                          | *Optional[int]*                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
| `redis_url`                                                                                                                                                                           | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
| `prefix`                                                                                                                                                                              | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
| `x_namespace`                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. |
| `retries`                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                   |

### Response

**[Dict[str, int]](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404         | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorResponse       | 500                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |