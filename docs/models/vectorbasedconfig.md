# VectorBasedConfig


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `feature_extractor_name`                                                     | *str*                                                                        | :heavy_check_mark:                                                           | Name of the feature extractor to use for vector-based clustering             |
| `clustering_method`                                                          | [models.ClusteringMethod](../models/clusteringmethod.md)                     | :heavy_check_mark:                                                           | N/A                                                                          |
| `sample_size`                                                                | *Optional[int]*                                                              | :heavy_minus_sign:                                                           | Maximum number of documents to process                                       |
| `hdbscan_parameters`                                                         | [OptionalNullable[models.HDBSCANParameters]](../models/hdbscanparameters.md) | :heavy_minus_sign:                                                           | N/A                                                                          |