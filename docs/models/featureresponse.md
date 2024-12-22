# FeatureResponse


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `url`                                                       | *OptionalNullable[str]*                                     | :heavy_minus_sign:                                          | The presigned URL for accessing the asset                   |
| `preview_url`                                               | *OptionalNullable[str]*                                     | :heavy_minus_sign:                                          | The presigned URL for accessing the asset preview           |
| `duplicate_of`                                              | *OptionalNullable[str]*                                     | :heavy_minus_sign:                                          | The asset_id of the asset that this asset is a duplicate of |
| `__pydantic_extra__`                                        | Dict[str, *Any*]                                            | :heavy_minus_sign:                                          | N/A                                                         |