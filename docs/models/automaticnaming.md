# AutomaticNaming


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `enabled`                                                          | *Optional[bool]*                                                   | :heavy_minus_sign:                                                 | Automatically assign cluster labels to documents                   |
| `generative_model`                                                 | [Optional[models.GenerativeModels]](../models/generativemodels.md) | :heavy_minus_sign:                                                 | N/A                                                                |
| `method`                                                           | [Optional[models.NamingMethod]](../models/namingmethod.md)         | :heavy_minus_sign:                                                 | N/A                                                                |
| `num_nearest_points`                                               | *Optional[int]*                                                    | :heavy_minus_sign:                                                 | Features used to generate name                                     |