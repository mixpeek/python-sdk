# TaxonomyExtractionConfig

Configuration for taxonomy-based entity extraction during ingestion


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  | Example                                                      |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `taxonomy_ids`                                               | List[*str*]                                                  | :heavy_check_mark:                                           | List of taxonomy IDs to use for classification               | [<br/>"tax_123"<br/>]                                        |
| `embedding_models`                                           | List[[models.AvailableModels](../models/availablemodels.md)] | :heavy_check_mark:                                           | Vector indexes to use for classification                     | [<br/>"multimodal",<br/>"text"<br/>]                         |
| `confidence_threshold`                                       | *Optional[float]*                                            | :heavy_minus_sign:                                           | Minimum confidence score required for classification         |                                                              |