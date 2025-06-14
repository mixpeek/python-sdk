# Namespaces
(*namespaces*)

## Overview

### Available Operations

* [create](#create) - Create Namespace
* [list](#list) - List Namespaces
* [delete](#delete) - Delete Namespace
* [update](#update) - Update Namespace
* [get](#get) - Get Namespace

## create

Creates a new namespace with specified feature extractors and payload indexes.

### Example Usage

```python
import mixpeek
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.namespaces.create(namespace_name="spotify_playlists_dev", feature_extractors=[
        {
            "feature_extractor_name": "text-extractor",
            "description": "Text extractor",
            "supported_input_types": [
                "text",
            ],
            "version": "1.0.0",
        },
    ], description="This namespace contains playlists from Spotify", payload_indexes=[
        {
            "field_name": "metadata.title",
            "type": mixpeek.PayloadSchemaType.TEXT,
            "field_schema": {
                "type": "text",
                "tokenizer": mixpeek.TokenizerType.WORD,
                "min_token_len": 2,
                "max_token_len": 15,
                "lowercase": True,
            },
        },
        {
            "field_name": "metadata.description",
            "type": mixpeek.PayloadSchemaType.KEYWORD,
            "field_schema": {
                "type": "keyword",
                "is_tenant": True,
            },
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                          | Type                                                                                                                                                                                                                                                                                               | Required                                                                                                                                                                                                                                                                                           | Description                                                                                                                                                                                                                                                                                        | Example                                                                                                                                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `namespace_name`                                                                                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                                                                                                 | Name of the namespace to create                                                                                                                                                                                                                                                                    | spotify_playlists_dev                                                                                                                                                                                                                                                                              |
| `feature_extractors`                                                                                                                                                                                                                                                                               | List[[models.BasicFeatureExtractor](../../models/basicfeatureextractor.md)]                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                                                                                 | List of feature extractors to use. At least one feature extractor must be provided.                                                                                                                                                                                                                | [<br/>{<br/>"description": "Text extractor",<br/>"feature_extractor_name": "text-extractor",<br/>"supported_input_types": [<br/>"text"<br/>],<br/>"version": "1.0.0"<br/>}<br/>]                                                                                                                   |
| `description`                                                                                                                                                                                                                                                                                      | *OptionalNullable[str]*                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                 | Description of the namespace                                                                                                                                                                                                                                                                       | This namespace contains playlists from Spotify                                                                                                                                                                                                                                                     |
| `payload_indexes`                                                                                                                                                                                                                                                                                  | List[[models.PayloadIndexConfig](../../models/payloadindexconfig.md)]                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                 | Optional list of custom payload index configurations. Indexes required by selected feature extractors will be added automatically.                                                                                                                                                                 | [<br/>{<br/>"field_name": "metadata.title",<br/>"field_schema": {<br/>"lowercase": true,<br/>"max_token_len": 15,<br/>"min_token_len": 2,<br/>"tokenizer": "word",<br/>"type": "text"<br/>},<br/>"type": "text"<br/>},<br/>{<br/>"field_name": "metadata.description",<br/>"field_schema": {<br/>"is_tenant": true,<br/>"type": "keyword"<br/>},<br/>"type": "keyword"<br/>}<br/>] |
| `retries`                                                                                                                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                    |

### Response

**[models.NamespaceResponse](../../models/namespaceresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404         | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorResponse       | 500                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## list

List all namespaces for a user

### Example Usage

```python
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.namespaces.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.NamespaceResponse]](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404         | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorResponse       | 500                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## delete

Deletes an existing namespace using either its name or ID

### Example Usage

```python
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.namespaces.delete(namespace="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `namespace`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Either the namespace name or namespace ID                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TaskResponse](../../models/taskresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404         | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorResponse       | 500                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## update

Fully updates an existing namespace (all fields required)

### Example Usage

```python
import mixpeek
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.namespaces.update(namespace="my_namespace", namespace_name="spotify_playlists_dev", payload_indexes=[
        {
            "field_name": "metadata.title",
            "type": mixpeek.PayloadSchemaType.TEXT,
            "field_schema": {
                "type": "text",
                "tokenizer": mixpeek.TokenizerType.WORD,
                "min_token_len": 2,
                "max_token_len": 15,
                "lowercase": True,
            },
        },
        {
            "field_name": "metadata.description",
            "type": mixpeek.PayloadSchemaType.KEYWORD,
            "field_schema": {
                "type": "keyword",
                "is_tenant": False,
            },
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                           | Type                                                                                                                                                                                                                                                                                                | Required                                                                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                                                                         | Example                                                                                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `namespace`                                                                                                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                                                                                  | Either the namespace name or namespace ID                                                                                                                                                                                                                                                           | my_namespace                                                                                                                                                                                                                                                                                        |
| `namespace_name`                                                                                                                                                                                                                                                                                    | *OptionalNullable[str]*                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                  | Name of the namespace to update                                                                                                                                                                                                                                                                     | spotify_playlists_dev                                                                                                                                                                                                                                                                               |
| `payload_indexes`                                                                                                                                                                                                                                                                                   | List[[models.PayloadIndexConfig](../../models/payloadindexconfig.md)]                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                  | Updated list of payload index configurations                                                                                                                                                                                                                                                        | [<br/>{<br/>"field_name": "metadata.title",<br/>"field_schema": {<br/>"lowercase": true,<br/>"max_token_len": 15,<br/>"min_token_len": 2,<br/>"tokenizer": "word",<br/>"type": "text"<br/>},<br/>"type": "text"<br/>},<br/>{<br/>"field_name": "metadata.description",<br/>"field_schema": {<br/>"is_tenant": false,<br/>"type": "keyword"<br/>},<br/>"type": "keyword"<br/>}<br/>] |
| `retries`                                                                                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                     |

### Response

**[models.NamespaceResponse](../../models/namespaceresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404         | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorResponse       | 500                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get

Retrieve details of a specific namespace using either its name or ID

### Example Usage

```python
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.namespaces.get(namespace="my_namespace")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `namespace`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Either the namespace name or namespace ID                           | my_namespace                                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.NamespaceResponse](../../models/namespaceresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404         | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorResponse       | 500                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |