# Retrievers
(*retrievers*)

## Overview

### Available Operations

* [create](#create) - Create Retriever
* [get](#get) - Get Retriever
* [execute](#execute) - Execute Retriever

## create

Create Retriever

### Example Usage

```python
import mixpeek
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.retrievers.create(retriever_name="<value>", input_schema=mixpeek.RetrieverSchemaInput(
        properties={
            "key": mixpeek.RetrieverSchemaFieldInput(
                type=mixpeek.BucketSchemaFieldType.IMAGE,
            ),
            "key1": mixpeek.RetrieverSchemaFieldInput(
                type=mixpeek.BucketSchemaFieldType.IMAGE,
            ),
        },
    ), collection_ids=[], stages=[
        mixpeek.StageConfigInput(
            stage_id="<id>",
            stage_name="<value>",
            version="<value>",
            pre_filters=mixpeek.LogicalOperatorInput(
                and_=[
                    mixpeek.FilterCondition(
                        field="name",
                        operator=mixpeek.FilterOperator.EQ,
                        value="John",
                    ),
                    mixpeek.FilterCondition(
                        field="age",
                        operator=mixpeek.FilterOperator.GTE,
                        value=30,
                    ),
                ],
                or_=[
                    mixpeek.FilterCondition(
                        field="status",
                        operator=mixpeek.FilterOperator.EQ,
                        value="active",
                    ),
                    mixpeek.FilterCondition(
                        field="role",
                        operator=mixpeek.FilterOperator.EQ,
                        value="admin",
                    ),
                ],
                not_=[
                    mixpeek.FilterCondition(
                        field="department",
                        operator=mixpeek.FilterOperator.EQ,
                        value="HR",
                    ),
                    mixpeek.FilterCondition(
                        field="location",
                        operator=mixpeek.FilterOperator.EQ,
                        value="remote",
                    ),
                ],
                case_sensitive=True,
            ),
            post_filters=mixpeek.LogicalOperatorInput(
                and_=[
                    mixpeek.FilterCondition(
                        field="name",
                        operator=mixpeek.FilterOperator.EQ,
                        value="John",
                    ),
                    mixpeek.FilterCondition(
                        field="age",
                        operator=mixpeek.FilterOperator.GTE,
                        value=30,
                    ),
                ],
                or_=[
                    mixpeek.FilterCondition(
                        field="status",
                        operator=mixpeek.FilterOperator.EQ,
                        value="active",
                    ),
                    mixpeek.FilterCondition(
                        field="role",
                        operator=mixpeek.FilterOperator.EQ,
                        value="admin",
                    ),
                ],
                not_=[
                    mixpeek.FilterCondition(
                        field="department",
                        operator=mixpeek.FilterOperator.EQ,
                        value="HR",
                    ),
                    mixpeek.FilterCondition(
                        field="location",
                        operator=mixpeek.FilterOperator.EQ,
                        value="remote",
                    ),
                ],
                case_sensitive=True,
            ),
        ),
        mixpeek.StageConfigInput(
            stage_id="<id>",
            stage_name="<value>",
            version="<value>",
            pre_filters=mixpeek.LogicalOperatorInput(
                and_=[
                    mixpeek.FilterCondition(
                        field="name",
                        operator=mixpeek.FilterOperator.EQ,
                        value="John",
                    ),
                    mixpeek.FilterCondition(
                        field="age",
                        operator=mixpeek.FilterOperator.GTE,
                        value=30,
                    ),
                ],
                or_=[
                    mixpeek.FilterCondition(
                        field="status",
                        operator=mixpeek.FilterOperator.EQ,
                        value="active",
                    ),
                    mixpeek.FilterCondition(
                        field="role",
                        operator=mixpeek.FilterOperator.EQ,
                        value="admin",
                    ),
                ],
                not_=[
                    mixpeek.FilterCondition(
                        field="department",
                        operator=mixpeek.FilterOperator.EQ,
                        value="HR",
                    ),
                    mixpeek.FilterCondition(
                        field="location",
                        operator=mixpeek.FilterOperator.EQ,
                        value="remote",
                    ),
                ],
                case_sensitive=True,
            ),
            post_filters=mixpeek.LogicalOperatorInput(
                and_=[
                    mixpeek.FilterCondition(
                        field="name",
                        operator=mixpeek.FilterOperator.EQ,
                        value="John",
                    ),
                    mixpeek.FilterCondition(
                        field="age",
                        operator=mixpeek.FilterOperator.GTE,
                        value=30,
                    ),
                ],
                or_=[
                    mixpeek.FilterCondition(
                        field="status",
                        operator=mixpeek.FilterOperator.EQ,
                        value="active",
                    ),
                    mixpeek.FilterCondition(
                        field="role",
                        operator=mixpeek.FilterOperator.EQ,
                        value="admin",
                    ),
                ],
                not_=[
                    mixpeek.FilterCondition(
                        field="department",
                        operator=mixpeek.FilterOperator.EQ,
                        value="HR",
                    ),
                    mixpeek.FilterCondition(
                        field="location",
                        operator=mixpeek.FilterOperator.EQ,
                        value="remote",
                    ),
                ],
                case_sensitive=True,
            ),
        ),
        mixpeek.StageConfigInput(
            stage_id="<id>",
            stage_name="<value>",
            version="<value>",
            pre_filters=mixpeek.LogicalOperatorInput(
                and_=[
                    mixpeek.FilterCondition(
                        field="name",
                        operator=mixpeek.FilterOperator.EQ,
                        value="John",
                    ),
                    mixpeek.FilterCondition(
                        field="age",
                        operator=mixpeek.FilterOperator.GTE,
                        value=30,
                    ),
                ],
                or_=[
                    mixpeek.FilterCondition(
                        field="status",
                        operator=mixpeek.FilterOperator.EQ,
                        value="active",
                    ),
                    mixpeek.FilterCondition(
                        field="role",
                        operator=mixpeek.FilterOperator.EQ,
                        value="admin",
                    ),
                ],
                not_=[
                    mixpeek.FilterCondition(
                        field="department",
                        operator=mixpeek.FilterOperator.EQ,
                        value="HR",
                    ),
                    mixpeek.FilterCondition(
                        field="location",
                        operator=mixpeek.FilterOperator.EQ,
                        value="remote",
                    ),
                ],
                case_sensitive=True,
            ),
            post_filters=mixpeek.LogicalOperatorInput(
                and_=[
                    mixpeek.FilterCondition(
                        field="name",
                        operator=mixpeek.FilterOperator.EQ,
                        value="John",
                    ),
                    mixpeek.FilterCondition(
                        field="age",
                        operator=mixpeek.FilterOperator.GTE,
                        value=30,
                    ),
                ],
                or_=[
                    mixpeek.FilterCondition(
                        field="status",
                        operator=mixpeek.FilterOperator.EQ,
                        value="active",
                    ),
                    mixpeek.FilterCondition(
                        field="role",
                        operator=mixpeek.FilterOperator.EQ,
                        value="admin",
                    ),
                ],
                not_=[
                    mixpeek.FilterCondition(
                        field="department",
                        operator=mixpeek.FilterOperator.EQ,
                        value="HR",
                    ),
                    mixpeek.FilterCondition(
                        field="location",
                        operator=mixpeek.FilterOperator.EQ,
                        value="remote",
                    ),
                ],
                case_sensitive=True,
            ),
        ),
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `retriever_name`                                                                                                                                                                      | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | Name of the retriever                                                                                                                                                                 |
| `input_schema`                                                                                                                                                                        | [models.RetrieverSchemaInput](../../models/retrieverschemainput.md)                                                                                                                   | :heavy_check_mark:                                                                                                                                                                    | Schema definition for retriever inputs                                                                                                                                                |
| `collection_ids`                                                                                                                                                                      | List[*str*]                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                    | List of collection IDs to search in                                                                                                                                                   |
| `stages`                                                                                                                                                                              | List[[models.StageConfigInput](../../models/stageconfiginput.md)]                                                                                                                     | :heavy_check_mark:                                                                                                                                                                    | List of stages to execute in order                                                                                                                                                    |
| `x_namespace`                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. |
| `description`                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Description of the retriever                                                                                                                                                          |
| `metadata`                                                                                                                                                                            | Dict[str, *Any*]                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
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

## get

Get Retriever

### Example Usage

```python
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.retrievers.get(retriever_id="<id>")

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

## execute

Execute Retriever

### Example Usage

```python
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.retrievers.execute(retriever_id="<id>", inputs={
        "key": "<value>",
        "key1": "<value>",
        "key2": "<value>",
    }, filters=None, sorts=[
        {
            "field": "created_at",
        },
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
| `inputs`                                                                                                                                                                              | Dict[str, *Any*]                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                    | Input values for the retriever query. These map to the required inputs defined in the retriever's first stage.                                                                        |
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