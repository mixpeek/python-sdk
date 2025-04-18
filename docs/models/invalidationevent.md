# InvalidationEvent

Event that triggers cache invalidation


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `collection`                                                         | *str*                                                                | :heavy_check_mark:                                                   | Collection ID to monitor                                             |
| `action`                                                             | *str*                                                                | :heavy_check_mark:                                                   | Action that triggers invalidation (create, update, delete)           |
| `recompute_strategy`                                                 | [Optional[models.RecomputeStrategy]](../models/recomputestrategy.md) | :heavy_minus_sign:                                                   | Strategies for recomputing cache entries                             |
| `retriever_id`                                                       | *OptionalNullable[str]*                                              | :heavy_minus_sign:                                                   | Optional retriever ID for retriever-specific invalidation            |