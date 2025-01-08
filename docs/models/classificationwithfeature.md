# ClassificationWithFeature

Classification entry with optional full feature and node data


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `feature_id`                                                             | *str*                                                                    | :heavy_check_mark:                                                       | ID of the classified feature                                             |
| `classification_id`                                                      | *str*                                                                    | :heavy_check_mark:                                                       | ID of the classification run                                             |
| `taxonomy_id`                                                            | *str*                                                                    | :heavy_check_mark:                                                       | ID of the taxonomy used                                                  |
| `matches`                                                                | List[[models.ClassificationMatch](../models/classificationmatch.md)]     | :heavy_check_mark:                                                       | List of node matches with scores                                         |
| `feature`                                                                | [OptionalNullable[models.FeatureResponse]](../models/featureresponse.md) | :heavy_minus_sign:                                                       | Full feature object if requested                                         |