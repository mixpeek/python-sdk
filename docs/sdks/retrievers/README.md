# Retrievers
(*retrievers*)

## Overview

### Available Operations

* [create_retriever_v1_retrievers_retrievers_post](#create_retriever_v1_retrievers_retrievers_post) - Create Retriever
* [get_retriever_v1_retrievers_retrievers_retriever_id_get](#get_retriever_v1_retrievers_retrievers_retriever_id_get) - Get Retriever
* [execute_retriever_v1_retrievers_retrievers_retriever_id_execute_post](#execute_retriever_v1_retrievers_retrievers_retriever_id_execute_post) - Execute Retriever

## create_retriever_v1_retrievers_retrievers_post

Create Retriever

### Example Usage

```python
import mixpeek
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.retrievers.create_retriever_v1_retrievers_retrievers_post(retriever_name="<value>", input_schema=mixpeek.BucketSchemaInput(
        properties={

        },
    ), collection_ids=[
        "<value>",
    ], stages=[

    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `retriever_name`                                                                                                                                                                      | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | Name of the retriever                                                                                                                                                                 |
| `input_schema`                                                                                                                                                                        | [models.BucketSchemaInput](../../models/bucketschemainput.md)                                                                                                                         | :heavy_check_mark:                                                                                                                                                                    | Schema definition for bucket objects                                                                                                                                                  |
| `collection_ids`                                                                                                                                                                      | List[*str*]                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                    | List of collection IDs to search in                                                                                                                                                   |
| `stages`                                                                                                                                                                              | List[[models.StageConfigInput](../../models/stageconfiginput.md)]                                                                                                                     | :heavy_check_mark:                                                                                                                                                                    | List of stages to execute in order                                                                                                                                                    |
| `x_namespace`                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. |
| `description`                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Description of the retriever                                                                                                                                                          |
| `metadata`                                                                                                                                                                            | [Optional[models.CreateRetrieverRequestMetadata]](../../models/createretrieverrequestmetadata.md)                                                                                     | :heavy_minus_sign:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
| `cache_config`                                                                                                                                                                        | [OptionalNullable[models.RetrieverCacheConfig]](../../models/retrievercacheconfig.md)                                                                                                 | :heavy_minus_sign:                                                                                                                                                                    | Configuration for retriever-level caching                                                                                                                                             |
| `retries`                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                   |

### Response

**[models.RetrieverModel](../../models/retrievermodel.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404         | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorResponse       | 500                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_retriever_v1_retrievers_retrievers_retriever_id_get

Get Retriever

### Example Usage

```python
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.retrievers.get_retriever_v1_retrievers_retrievers_retriever_id_get(retriever_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `retriever_id`                                                                                                                                                                        | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
| `x_namespace`                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. |
| `retries`                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                   |

### Response

**[models.RetrieverModel](../../models/retrievermodel.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404         | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorResponse       | 500                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## execute_retriever_v1_retrievers_retrievers_retriever_id_execute_post

Execute Retriever

### Example Usage

```python
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.retrievers.execute_retriever_v1_retrievers_retrievers_retriever_id_execute_post(retriever_id="<id>", inputs={}, filters={
        "and_": [

        ],
        "or_": [

        ],
        "not_": [

        ],
        "case_sensitive": True,
    }, sorts=[
        {
            "field": "created_at",
        },
        {
            "field": "created_at",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `retriever_id`                                                                                                                                                                        | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
| `inputs`                                                                                                                                                                              | [models.RetrieverQueryRequestInputs](../../models/retrieverqueryrequestinputs.md)                                                                                                     | :heavy_check_mark:                                                                                                                                                                    | Input values for the retriever query. These map to the required inputs defined in the retriever's first stage.                                                                        |
| `x_namespace`                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. |
| `filters`                                                                                                                                                                             | [OptionalNullable[models.LogicalOperatorInput]](../../models/logicaloperatorinput.md)                                                                                                 | :heavy_minus_sign:                                                                                                                                                                    | Logical operations for filtering results. Can include AND, OR, NOT conditions with field comparisons.                                                                                 |
| `sorts`                                                                                                                                                                               | List[[models.SortOption](../../models/sortoption.md)]                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                    | Controls the ordering of results. Can sort by score (default) or any other document field. This sorts the results from the last stage.                                                |
| `limit`                                                                                                                                                                               | *Optional[int]*                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                    | Maximum number of results to return. Overrides the default pagination limit in the retriever definition.                                                                              |
| `offset`                                                                                                                                                                              | *Optional[int]*                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                    | Number of results to skip. Use with limit for pagination. For large offsets, consider using session_id for cursor-based pagination.                                                   |
| `select`                                                                                                                                                                              | List[*str*]                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                    | Specific fields to include in the response. If not specified, returns all fields.                                                                                                     |
| `session_id`                                                                                                                                                                          | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Session identifier for interaction tracking.                                                                                                                                          |
| `return_urls`                                                                                                                                                                         | *Optional[bool]*                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | When true, generates pre-signed URLs for any media assets in the results. May increase response time slightly.                                                                        |
| `retries`                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                   |

### Response

**[models.RetrieverResponse](../../models/retrieverresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404         | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorResponse       | 500                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |