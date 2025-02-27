# FeatureExtractors
(*feature_extractors*)

## Overview

### Available Operations

* [extract_embeddings](#extract_embeddings) - Extract Embeddings

## extract_embeddings

Extract Embeddings

### Example Usage

```python
import mixpeek
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.feature_extractors.extract_embeddings(type_=mixpeek.InputType.URL, embedding_model=mixpeek.VectorModel.TEXT, value="https://example.com/image.jpg")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   | Example                                                                                       |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `type`                                                                                        | [models.InputType](../../models/inputtype.md)                                                 | :heavy_check_mark:                                                                            | N/A                                                                                           |                                                                                               |
| `embedding_model`                                                                             | [models.VectorModel](../../models/vectormodel.md)                                             | :heavy_check_mark:                                                                            | N/A                                                                                           |                                                                                               |
| `value`                                                                                       | *OptionalNullable[str]*                                                                       | :heavy_minus_sign:                                                                            | The input content to embed. Could be a URL, text content, file path, or base64 encoded string | https://example.com/image.jpg                                                                 |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |                                                                                               |

### Response

**[models.EmbeddingResponse](../../models/embeddingresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404         | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorResponse       | 500                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |