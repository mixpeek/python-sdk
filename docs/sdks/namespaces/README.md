# Namespaces
(*namespaces*)

## Overview

### Available Operations

* [create](#create) - Create Namespace
* [list](#list) - List Namespaces
* [delete](#delete) - Delete Namespace
* [patch_namespace_v1_namespaces_namespace_patch](#patch_namespace_v1_namespaces_namespace_patch) - Partially Update Namespace
* [update](#update) - Update Namespace
* [get](#get) - Get Namespace
* [list_models](#list_models) - List Available Models

## create

Creates a new namespace with the specified configuration

### Example Usage

```python
import mixpeek
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.namespaces.create(namespace_name="spotify_playlists_dev", embedding_models=[
        "image",
        "multimodal",
        "text",
        "keyword",
    ], payload_indexes=[
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
| `namespace_name`                                                                                                                                                                                                                                                                                    | *str*                                                                                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                                                                                  | Name of the namespace to create                                                                                                                                                                                                                                                                     | spotify_playlists_dev                                                                                                                                                                                                                                                                               |
| `embedding_models`                                                                                                                                                                                                                                                                                  | List[*str*]                                                                                                                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                                                                                                                                  | List of vector indexes to be used within this namespace. Must be one of: 'image', 'openai-clip-vit-base-patch32', 'multimodal', 'vertex-multimodal', 'text', 'baai-bge-m3', 'keyword', 'naver-splade-v3'                                                                                            | [<br/>"image",<br/>"multimodal",<br/>"text",<br/>"keyword"<br/>]                                                                                                                                                                                                                                    |
| `payload_indexes`                                                                                                                                                                                                                                                                                   | List[[models.PayloadIndexConfig](../../models/payloadindexconfig.md)]                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                  | List of payload index configurations                                                                                                                                                                                                                                                                | [<br/>{<br/>"field_name": "metadata.title",<br/>"field_schema": {<br/>"lowercase": true,<br/>"max_token_len": 15,<br/>"min_token_len": 2,<br/>"tokenizer": "word",<br/>"type": "text"<br/>},<br/>"type": "text"<br/>},<br/>{<br/>"field_name": "metadata.description",<br/>"field_schema": {<br/>"is_tenant": false,<br/>"type": "keyword"<br/>},<br/>"type": "keyword"<br/>}<br/>] |
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

    res = m_client.namespaces.delete(namespace="ns_1234567890")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `namespace`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Either the namespace name or namespace ID                           | my_namespace                                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.TaskResponse](../../models/taskresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404         | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorResponse       | 500                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## patch_namespace_v1_namespaces_namespace_patch

Updates specific fields of an existing namespace

### Example Usage

```python
import mixpeek
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.namespaces.patch_namespace_v1_namespaces_namespace_patch(namespace="ns_1234567890", namespace_name="spotify_playlists_dev", payload_indexes=[
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

    res = m_client.namespaces.update(namespace="ns_1234567890", namespace_name="spotify_playlists_dev", payload_indexes=[
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

    res = m_client.namespaces.get(namespace="ns_1234567890")

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

## list_models

Returns all available models and their configurations, scoped to the organization

### Example Usage

```python
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.namespaces.list_models()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AvailableModelsResponse](../../models/availablemodelsresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404         | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorResponse       | 500                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |