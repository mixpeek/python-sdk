# EmbeddingResponse


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `embedding`                                                        | [models.Embedding](../models/embedding.md)                         | :heavy_check_mark:                                                 | The embedding of the processed data, either dense or sparse format |
| `elapsed_time`                                                     | *OptionalNullable[float]*                                          | :heavy_minus_sign:                                                 | The time taken to process the data.                                |