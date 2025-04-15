# EmbeddingRequest


            Request model for embedding generation.
            
            When multiple EmbeddingRequests use the same embedding_model:
            - All inputs will be embedded in the same vector space
            - The final embedding will be the average of all individual embeddings
            - Original values will be stored with a ' | ' separator
            
            Example:
                Two requests with same model "clip":
                1. type: "text", value: "a dog", embedding_model: "clip"
                2. type: "url", value: "https://example.com/image.jpg", embedding_model: "clip"
                
                Result:
                - vectors["clip"] = average of both embeddings
                - embedding_configs["clip"] = "a dog | https://example.com/image.jpg"
            


## Fields

| Field                                                                                         | Type                                                                                          | Required                                                                                      | Description                                                                                   | Example                                                                                       |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `type`                                                                                        | [models.InputType](../models/inputtype.md)                                                    | :heavy_check_mark:                                                                            | N/A                                                                                           |                                                                                               |
| `value`                                                                                       | *OptionalNullable[str]*                                                                       | :heavy_minus_sign:                                                                            | The input content to embed. Could be a URL, text content, file path, or base64 encoded string | https://example.com/image.jpg                                                                 |
| `embedding_model`                                                                             | [models.VectorModel](../models/vectormodel.md)                                                | :heavy_check_mark:                                                                            | N/A                                                                                           |                                                                                               |