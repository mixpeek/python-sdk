# CreateTaxonomyRequest

Request to create a new taxonomy


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `taxonomy_name`                                      | *str*                                                | :heavy_check_mark:                                   | N/A                                                  |
| `description`                                        | *OptionalNullable[str]*                              | :heavy_minus_sign:                                   | N/A                                                  |
| `config`                                             | [models.TaxonomyConfig](../models/taxonomyconfig.md) | :heavy_check_mark:                                   | Base configuration for all taxonomy types            |