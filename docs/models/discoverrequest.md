# DiscoverRequest


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `collections`                                                            | List[*str*]                                                              | :heavy_check_mark:                                                       | List of collection names or ids to search for features                   |
| `filters`                                                                | [OptionalNullable[models.LogicalOperator]](../models/logicaloperator.md) | :heavy_minus_sign:                                                       | Filters to apply to the discovery task                                   |
| `confidence_threshold`                                                   | *Optional[float]*                                                        | :heavy_minus_sign:                                                       | Minimum confidence score required for classification                     |
| `assignment`                                                             | [Optional[models.AssignmentConfig]](../models/assignmentconfig.md)       | :heavy_minus_sign:                                                       | Configuration for how classifications should be assigned to features     |
| `sample_size`                                                            | *OptionalNullable[int]*                                                  | :heavy_minus_sign:                                                       | Number of feature samples to process                                     |