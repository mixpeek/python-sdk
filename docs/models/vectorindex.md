# VectorIndex

Base configuration for vector indexes


## Fields

| Field                                        | Type                                         | Required                                     | Description                                  |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| `name`                                       | *str*                                        | :heavy_check_mark:                           | N/A                                          |
| `description`                                | *str*                                        | :heavy_check_mark:                           | N/A                                          |
| `dimensions`                                 | *int*                                        | :heavy_check_mark:                           | N/A                                          |
| `type`                                       | [models.VectorType](../models/vectortype.md) | :heavy_check_mark:                           | Types of vectors supported                   |
| `distance`                                   | *OptionalNullable[str]*                      | :heavy_minus_sign:                           | N/A                                          |