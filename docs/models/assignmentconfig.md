# AssignmentConfig

Configuration for how classifications should be assigned to features


## Fields

| Field                                                                                               | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `enabled`                                                                                           | *Optional[bool]*                                                                                    | :heavy_minus_sign:                                                                                  | Whether to assign the taxonomy to the feature                                                       |
| `append`                                                                                            | *Optional[bool]*                                                                                    | :heavy_minus_sign:                                                                                  | Whether to append the classification to the feature, if false, replaces any existing classification |