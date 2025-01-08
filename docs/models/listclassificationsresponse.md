# ListClassificationsResponse

Response for the list classifications endpoint


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `results`                                                                        | List[[models.ClassificationWithFeature](../models/classificationwithfeature.md)] | :heavy_check_mark:                                                               | List of classification entries with optional enriched data                       |
| `pagination`                                                                     | [models.DbModelPaginationResponse](../models/dbmodelpaginationresponse.md)       | :heavy_check_mark:                                                               | N/A                                                                              |