# SearchInteractions
(*search_interactions*)

## Overview

### Available Operations

* [create](#create) - Create Interaction
* [get_interaction](#get_interaction) - Get Interaction
* [delete](#delete) - Delete Interaction

## create

Record a search interaction (view, click, feedback, etc.)

### Example Usage

```python
import mixpeek
from mixpeek import Mixpeek
import os

with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as mixpeek:

    res = mixpeek.search_interactions.create(feature_id="prod_123", interaction_type=mixpeek.InteractionType.NEGATIVE_FEEDBACK, search_request=mixpeek.SearchRequestFeaturesInput(
        queries=[

        ],
        collections=[
            "collection1",
            "collection2",
        ],
        filters={
            "case_sensitive": True,
            "and_": [

            ],
            "or_": [

            ],
            "nor": [

            ],
        },
        group_by={
            "field": "asset_id",
            "max_features": 10,
            "sort": {
                "field": "score",
                "direction": mixpeek.Direction.DESC,
            },
        },
        sort={
            "field": "score",
            "direction": mixpeek.Direction.DESC,
        },
        select=[
            "title",
            "content",
            "metadata.author",
            "metadata.publication_date",
        ],
        reranking_options={
            "weights": {
                "feedback": 0.7,
                "popularity": 0.3,
            },
            "enable_reranking": True,
        },
        session_id="sess_abc123",
        return_url=True,
    ), position=3, metadata={}, session_id="sess_abc123")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           | Example                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `feature_id`                                                                                                                                                                          | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | ID of the item that was interacted with                                                                                                                                               | prod_123                                                                                                                                                                              |
| `interaction_type`                                                                                                                                                                    | [models.InteractionType](../../models/interactiontype.md)                                                                                                                             | :heavy_check_mark:                                                                                                                                                                    | N/A                                                                                                                                                                                   |                                                                                                                                                                                       |
| `x_namespace`                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. |                                                                                                                                                                                       |
| `search_request`                                                                                                                                                                      | [OptionalNullable[models.SearchRequestFeaturesInput]](../../models/searchrequestfeaturesinput.md)                                                                                     | :heavy_minus_sign:                                                                                                                                                                    | The search request that led to this interaction                                                                                                                                       |                                                                                                                                                                                       |
| `position`                                                                                                                                                                            | *OptionalNullable[int]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Position in search results where interaction occurred                                                                                                                                 | 3                                                                                                                                                                                     |
| `metadata`                                                                                                                                                                            | [OptionalNullable[models.Metadata]](../../models/metadata.md)                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                    | Additional context about the interaction                                                                                                                                              | {<br/>"device": "mobile",<br/>"duration_ms": 5000,<br/>"interaction_reason": "not_relevant",<br/>"page": "search_results"<br/>}                                                       |
| `session_id`                                                                                                                                                                          | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Search session identifier                                                                                                                                                             | sess_abc123                                                                                                                                                                           |
| `retries`                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                   |                                                                                                                                                                                       |

### Response

**[models.InteractionResponse](../../models/interactionresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404, 500    | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_interaction

Get a specific interaction

### Example Usage

```python
from mixpeek import Mixpeek
import os

with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as mixpeek:

    res = mixpeek.search_interactions.get_interaction(interaction_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `interaction_id`                                                                                                                                                                      | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
| `x_namespace`                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. |
| `retries`                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                   |

### Response

**[models.InteractionResponse](../../models/interactionresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404, 500    | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## delete

Delete a specific interaction

### Example Usage

```python
from mixpeek import Mixpeek
import os

with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as mixpeek:

    res = mixpeek.search_interactions.delete(interaction_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `interaction_id`                                                                                                                                                                      | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
| `x_namespace`                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. |
| `retries`                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                   |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404, 500    | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |