# ModelDetails

Details about a model in the registry


## Fields

| Field                                               | Type                                                | Required                                            | Description                                         | Example                                             |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| `supported_modalities`                              | List[[models.Modality](../models/modality.md)]      | :heavy_check_mark:                                  | List of modalities that this model supports         | [<br/>"text",<br/>"image"<br/>]                     |
| `vector_type`                                       | [models.VectorType](../models/vectortype.md)        | :heavy_check_mark:                                  | N/A                                                 |                                                     |
| `size`                                              | *OptionalNullable[int]*                             | :heavy_minus_sign:                                  | Dimensionality of the output vector (if applicable) | 512                                                 |