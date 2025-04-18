# RetrieverResponse

Response from a retriever execution


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `execution_time`                                         | *float*                                                  | :heavy_check_mark:                                       | N/A                                                      |
| `stage_results`                                          | List[[models.StageResponse](../models/stageresponse.md)] | :heavy_minus_sign:                                       | Results from each stage execution                        |