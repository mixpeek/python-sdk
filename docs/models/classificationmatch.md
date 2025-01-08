# ClassificationMatch

Individual node match with score


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        | Example                                                            |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `node_id`                                                          | *str*                                                              | :heavy_check_mark:                                                 | ID of the matched taxonomy node                                    |                                                                    |
| `score`                                                            | *float*                                                            | :heavy_check_mark:                                                 | Confidence score of the match                                      |                                                                    |
| `depth`                                                            | *int*                                                              | :heavy_check_mark:                                                 | Depth of the node in the taxonomy                                  | 1                                                                  |
| `order`                                                            | List[*int*]                                                        | :heavy_check_mark:                                                 | Order of the node in the taxonomy                                  | [<br/>1,<br/>2,<br/>3<br/>]                                        |
| `node`                                                             | [OptionalNullable[models.TaxonomyNode]](../models/taxonomynode.md) | :heavy_minus_sign:                                                 | Full node object if requested                                      |                                                                    |