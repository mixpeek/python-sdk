# CollectionConfig

Configuration for a collection in the taxonomy


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `collection_id`                                              | *str*                                                        | :heavy_check_mark:                                           | ID of the collection                                         |
| `enrichment_fields`                                          | List[[models.EnrichmentField](../models/enrichmentfield.md)] | :heavy_minus_sign:                                           | Fields to enrich with taxonomy metadata                      |
| `retriever`                                                  | [models.RetrieverBinding](../models/retrieverbinding.md)     | :heavy_check_mark:                                           | How a retriever should be used in a taxonomy                 |