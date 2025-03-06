# IngestAssets
(*ingest_assets*)

## Overview

### Available Operations

* [ingest_text](#ingest_text) - Ingest Text
* [ingest_video_url](#ingest_video_url) - Ingest Video Url
* [ingest_image_url](#ingest_image_url) - Ingest Image Url

## ingest_text

**Requirements:**
- Required permissions: write

### Example Usage

```python
import mixpeek
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.ingest_assets.ingest_text(collection="col_1234567890", metadata={}, feature_extractors={
        "embed": [
            {
                "type": mixpeek.InputType.TEXT,
                "embedding_model": mixpeek.VectorModel.MULTIMODAL,
                "value": "a dog",
            },
        ],
        "json_output": {},
        "entities": {
            "taxonomy_extraction": {
                "taxonomy": "tax_123",
            },
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           | Example                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `collection`                                                                                                                                                                          | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | Unique identifier for the collection where the processed asset will be stored, can be the collection name or collection ID. If neither exist, the collection will be created.         | col_1234567890                                                                                                                                                                        |
| `x_namespace`                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. |                                                                                                                                                                                       |
| `asset_update`                                                                                                                                                                        | [OptionalNullable[models.AssetUpdate]](../../models/assetupdate.md)                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                    | Controls how processing results are stored - either creating a new asset or updating an existing one.                                                                                 |                                                                                                                                                                                       |
| `metadata`                                                                                                                                                                            | [Optional[models.ProcessTextInputMetadata]](../../models/processtextinputmetadata.md)                                                                                                 | :heavy_minus_sign:                                                                                                                                                                    | Additional metadata associated with the file. Can include any key-value pairs relevant to the file.                                                                                   | {<br/>"author": "John Doe",<br/>"category": "Research Paper",<br/>"tags": [<br/>"AI",<br/>"Machine Learning"<br/>]<br/>}                                                              |
| `feature_extractors`                                                                                                                                                                  | [OptionalNullable[models.TextSettings]](../../models/textsettings.md)                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                    | Settings for text processing.                                                                                                                                                         |                                                                                                                                                                                       |
| `skip_duplicate`                                                                                                                                                                      | *OptionalNullable[bool]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                    | Skips processing when a duplicate hash is found and stores an error by the task_id with the existing asset_id                                                                         |                                                                                                                                                                                       |
| `retries`                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                   |                                                                                                                                                                                       |

### Response

**[models.TaskResponse](../../models/taskresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404         | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorResponse       | 500                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## ingest_video_url

**Requirements:**
- Required permissions: write

### Example Usage

```python
import mixpeek
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.ingest_assets.ingest_video_url(url="https://example.com/sample-video.mp4", collection="col_1234567890", metadata={}, feature_extractors=[
        mixpeek.VideoSettings(
            read=mixpeek.VideoReadSettings(),
            embed=[
                mixpeek.EmbeddingRequest(
                    type=mixpeek.InputType.TEXT,
                    embedding_model=mixpeek.VectorModel.VERTEX_MULTIMODAL,
                    value="a dog",
                ),
            ],
            transcribe=mixpeek.VideoTranscriptionSettings(),
            describe=mixpeek.VideoDescribeSettings(),
            detect=mixpeek.VideoDetectSettings(),
            json_output=mixpeek.JSONVideoOutputSettings(),
            entities=mixpeek.EntitySettings(
                taxonomy_extraction=mixpeek.TaxonomyExtractionConfig(
                    taxonomy="tax_123",
                ),
            ),
        ),
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                            | Type                                                                                                                                                                                                                                                                 | Required                                                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                                                          | Example                                                                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `url`                                                                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                                                   | The URL of the asset to be processed. Must be a valid HTTP or HTTPS URL.                                                                                                                                                                                             | https://example.com/sample-video.mp4                                                                                                                                                                                                                                 |
| `collection`                                                                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                                                   | Unique identifier for the collection where the processed asset will be stored, can be the collection name or collection ID. If neither exist, the collection will be created.                                                                                        | col_1234567890                                                                                                                                                                                                                                                       |
| `x_namespace`                                                                                                                                                                                                                                                        | *OptionalNullable[str]*                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                   | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint.                                                                                |                                                                                                                                                                                                                                                                      |
| `asset_update`                                                                                                                                                                                                                                                       | [OptionalNullable[models.AssetUpdate]](../../models/assetupdate.md)                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                   | Controls how processing results are stored - either creating a new asset or updating an existing one.                                                                                                                                                                |                                                                                                                                                                                                                                                                      |
| `metadata`                                                                                                                                                                                                                                                           | [Optional[models.ProcessVideoURLInputMetadata]](../../models/processvideourlinputmetadata.md)                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                   | Additional metadata associated with the asset. Can include any key-value pairs relevant to the asset.                                                                                                                                                                | {<br/>"author": "John Doe",<br/>"category": "Research Paper",<br/>"tags": [<br/>"AI",<br/>"Machine Learning"<br/>]<br/>}                                                                                                                                             |
| `skip_duplicate`                                                                                                                                                                                                                                                     | *OptionalNullable[bool]*                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                   | Makes feature extraction idempotent. When True and a duplicate file hash is found, copies features from the existing asset instead of reprocessing. This allows the same file to be used multiple times with different metadata while avoiding redundant processing. |                                                                                                                                                                                                                                                                      |
| `feature_extractors`                                                                                                                                                                                                                                                 | List[[models.VideoSettings](../../models/videosettings.md)]                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                   | Settings for video processing. Only applicable if the URL points to a video file.                                                                                                                                                                                    |                                                                                                                                                                                                                                                                      |
| `retries`                                                                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                      |

### Response

**[models.TaskResponse](../../models/taskresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404         | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorResponse       | 500                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## ingest_image_url

**Requirements:**
- Required permissions: write

### Example Usage

```python
import mixpeek
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.ingest_assets.ingest_image_url(url="https://example.com/sample-video.mp4", collection="col_1234567890", metadata={}, feature_extractors=mixpeek.ImageSettings(
        read=mixpeek.ImageReadSettings(),
        embed=[
            mixpeek.EmbeddingRequest(
                type=mixpeek.InputType.TEXT,
                embedding_model=mixpeek.VectorModel.BAAI_BGE_M3,
                value="a dog",
            ),
        ],
        describe=mixpeek.ImageDescribeSettings(
            max_length=1000,
        ),
        detect=mixpeek.ImageDetectSettings(),
        json_output=mixpeek.JSONImageOutputSettings(),
        entities=mixpeek.EntitySettings(
            taxonomy_extraction=mixpeek.TaxonomyExtractionConfig(
                taxonomy="tax_123",
            ),
        ),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                            | Type                                                                                                                                                                                                                                                                 | Required                                                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                                                          | Example                                                                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `url`                                                                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                                                   | The URL of the asset to be processed. Must be a valid HTTP or HTTPS URL.                                                                                                                                                                                             | https://example.com/sample-video.mp4                                                                                                                                                                                                                                 |
| `collection`                                                                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                                                   | Unique identifier for the collection where the processed asset will be stored, can be the collection name or collection ID. If neither exist, the collection will be created.                                                                                        | col_1234567890                                                                                                                                                                                                                                                       |
| `x_namespace`                                                                                                                                                                                                                                                        | *OptionalNullable[str]*                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                   | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint.                                                                                |                                                                                                                                                                                                                                                                      |
| `asset_update`                                                                                                                                                                                                                                                       | [OptionalNullable[models.AssetUpdate]](../../models/assetupdate.md)                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                   | Controls how processing results are stored - either creating a new asset or updating an existing one.                                                                                                                                                                |                                                                                                                                                                                                                                                                      |
| `metadata`                                                                                                                                                                                                                                                           | [Optional[models.ProcessImageURLInputMetadata]](../../models/processimageurlinputmetadata.md)                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                   | Additional metadata associated with the asset. Can include any key-value pairs relevant to the asset.                                                                                                                                                                | {<br/>"author": "John Doe",<br/>"category": "Research Paper",<br/>"tags": [<br/>"AI",<br/>"Machine Learning"<br/>]<br/>}                                                                                                                                             |
| `skip_duplicate`                                                                                                                                                                                                                                                     | *OptionalNullable[bool]*                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                   | Makes feature extraction idempotent. When True and a duplicate file hash is found, copies features from the existing asset instead of reprocessing. This allows the same file to be used multiple times with different metadata while avoiding redundant processing. |                                                                                                                                                                                                                                                                      |
| `feature_extractors`                                                                                                                                                                                                                                                 | [OptionalNullable[models.ImageSettings]](../../models/imagesettings.md)                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                   | Settings for image processing. Only applicable if the URL points to an image file.                                                                                                                                                                                   |                                                                                                                                                                                                                                                                      |
| `retries`                                                                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                      |

### Response

**[models.TaskResponse](../../models/taskresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404         | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorResponse       | 500                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |