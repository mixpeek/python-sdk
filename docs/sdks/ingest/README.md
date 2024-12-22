# Ingest
(*ingest*)

## Overview

### Available Operations

* [text](#text) - Ingest Text
* [video_from_url](#video_from_url) - Ingest Video Url
* [image_url](#image_url) - Ingest Image Url

## text

Ingest Text

### Example Usage

```python
import mixpeek
from mixpeek import Mixpeek

with Mixpeek() as mixpeek:

    res = mixpeek.ingest.text(collection="col_1234567890", metadata={}, feature_extractors={
        "embed": [
            {
                "type": mixpeek.InputType.TEXT,
                "vector_index": mixpeek.VectorModel.MULTIMODAL,
                "value": "https://example.com/image.jpg",
            },
            {
                "type": mixpeek.InputType.TEXT,
                "vector_index": mixpeek.VectorModel.KEYWORD,
                "value": "https://example.com/image.jpg",
            },
            {
                "type": mixpeek.InputType.TEXT,
                "vector_index": mixpeek.VectorModel.TEXT,
                "value": "https://example.com/image.jpg",
            },
        ],
        "json_output": {},
    }, percolate={})

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
| `percolate`                                                                                                                                                                           | [OptionalNullable[models.PercolateRequest]](../../models/percolaterequest.md)                                                                                                         | :heavy_minus_sign:                                                                                                                                                                    | Settings for percolating the asset against stored queries.                                                                                                                            | {<br/>"min_relevance": 0.8<br/>}                                                                                                                                                      |
| `skip_duplicate`                                                                                                                                                                      | *OptionalNullable[bool]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                    | Skips processing when a duplicate hash is found and stores an error by the task_id with the existing asset_id                                                                         |                                                                                                                                                                                       |
| `retries`                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                   |                                                                                                                                                                                       |

### Response

**[models.DbModelTaskResponse](../../models/dbmodeltaskresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404, 500    | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## video_from_url

Ingest Video Url

### Example Usage

```python
import mixpeek
from mixpeek import Mixpeek

with Mixpeek() as mixpeek:

    res = mixpeek.ingest.video_from_url(url="https://example.com/sample-video.mp4", collection="col_1234567890", metadata={}, percolate={}, feature_extractors=[
        mixpeek.VideoSettings(
            interval_sec=15,
            read={
                "enabled": True,
            },
            embed=[
                {
                    "type": mixpeek.InputType.URL,
                    "vector_index": mixpeek.VectorModel.MULTIMODAL,
                },
                {
                    "type": mixpeek.InputType.TEXT,
                    "vector_index": mixpeek.VectorModel.TEXT,
                    "value": "https://example.com/image.jpg",
                },
            ],
            transcribe={
                "enabled": True,
            },
            describe={
                "enabled": True,
            },
            detect={
                "faces": {
                    "enabled": True,
                    "confidence_threshold": 0.8,
                },
            },
            json_output={},
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
| `percolate`                                                                                                                                                                                                                                                          | [OptionalNullable[models.PercolateRequest]](../../models/percolaterequest.md)                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                   | Settings for percolating the asset against stored queries.                                                                                                                                                                                                           | {<br/>"min_relevance": 0.8<br/>}                                                                                                                                                                                                                                     |
| `skip_duplicate`                                                                                                                                                                                                                                                     | *OptionalNullable[bool]*                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                   | Makes feature extraction idempotent. When True and a duplicate file hash is found, copies features from the existing asset instead of reprocessing. This allows the same file to be used multiple times with different metadata while avoiding redundant processing. |                                                                                                                                                                                                                                                                      |
| `feature_extractors`                                                                                                                                                                                                                                                 | List[[models.VideoSettings](../../models/videosettings.md)]                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                   | Settings for video processing. Only applicable if the URL points to a video file.                                                                                                                                                                                    |                                                                                                                                                                                                                                                                      |
| `retries`                                                                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                      |

### Response

**[models.DbModelTaskResponse](../../models/dbmodeltaskresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404, 500    | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## image_url

Ingest Image Url

### Example Usage

```python
import mixpeek
from mixpeek import Mixpeek

with Mixpeek() as mixpeek:

    res = mixpeek.ingest.image_url(url="https://example.com/sample-video.mp4", collection="col_1234567890", metadata={}, percolate={}, feature_extractors=mixpeek.ImageSettings(
        read={
            "enabled": True,
        },
        embed=[
            {
                "type": mixpeek.InputType.URL,
                "vector_index": mixpeek.VectorModel.MULTIMODAL,
            },
            {
                "type": mixpeek.InputType.URL,
                "vector_index": mixpeek.VectorModel.IMAGE,
            },
        ],
        describe={
            "enabled": True,
            "max_length": 1000,
        },
        detect={
            "faces": {
                "enabled": True,
                "confidence_threshold": 0.8,
            },
        },
        json_output={},
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
| `percolate`                                                                                                                                                                                                                                                          | [OptionalNullable[models.PercolateRequest]](../../models/percolaterequest.md)                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                   | Settings for percolating the asset against stored queries.                                                                                                                                                                                                           | {<br/>"min_relevance": 0.8<br/>}                                                                                                                                                                                                                                     |
| `skip_duplicate`                                                                                                                                                                                                                                                     | *OptionalNullable[bool]*                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                   | Makes feature extraction idempotent. When True and a duplicate file hash is found, copies features from the existing asset instead of reprocessing. This allows the same file to be used multiple times with different metadata while avoiding redundant processing. |                                                                                                                                                                                                                                                                      |
| `feature_extractors`                                                                                                                                                                                                                                                 | [OptionalNullable[models.ImageSettings]](../../models/imagesettings.md)                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                   | Settings for image processing. Only applicable if the URL points to an image file.                                                                                                                                                                                   |                                                                                                                                                                                                                                                                      |
| `retries`                                                                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                      |

### Response

**[models.DbModelTaskResponse](../../models/dbmodeltaskresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404, 500    | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |