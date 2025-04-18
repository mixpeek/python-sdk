# StageResponse

Output from a retriever stage


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `results`                                          | List[[models.Results](../models/results.md)]       | :heavy_check_mark:                                 | N/A                                                |
| `execution_time`                                   | *float*                                            | :heavy_check_mark:                                 | N/A                                                |
| `total_results`                                    | *OptionalNullable[int]*                            | :heavy_minus_sign:                                 | Total number of results not filtered by pagination |