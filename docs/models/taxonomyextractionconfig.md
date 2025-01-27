# TaxonomyExtractionConfig

Configuration for taxonomy-based entity extraction during ingestion


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `taxonomy`                                                           | *str*                                                                | :heavy_check_mark:                                                   | Taxonomy name or ID to use for classification                        | tax_123                                                              |
| `assignment`                                                         | [Optional[models.AssignmentConfig]](../models/assignmentconfig.md)   | :heavy_minus_sign:                                                   | Configuration for how classifications should be assigned to features |                                                                      |