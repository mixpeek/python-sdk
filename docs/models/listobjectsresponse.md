# ListObjectsResponse

Response model for listing objects in a bucket


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `results`                                                    | List[[models.ObjectResponse](../models/objectresponse.md)]   | :heavy_check_mark:                                           | List of objects matching the query                           |
| `pagination`                                                 | [models.PaginationResponse](../models/paginationresponse.md) | :heavy_check_mark:                                           | N/A                                                          |