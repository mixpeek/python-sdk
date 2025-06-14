# RetrieverInteractions
(*retriever_interactions*)

## Overview

### Available Operations

* [create](#create) - Create Interaction
* [list](#list) - List Interactions
* [get](#get) - Get Interaction
* [delete](#delete) - Delete Interaction

## create

Record a search interaction (view, click, feedback, etc.)

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

    res = m_client.retriever_interactions.create(feature_id="prod_123", interaction_type=[
        mixpeek.InteractionType.POSITIVE_FEEDBACK,
        mixpeek.InteractionType.CLICK,
        mixpeek.InteractionType.LONG_VIEW,
    ], position=3, metadata={
        "device": "mobile",
        "duration_ms": 5000,
        "interaction_reason": "not_relevant",
        "page": "search_results",
        "page_number": 1,
        "results_count": 50,
        "search_latency_ms": 150,
        "viewport_position": 0.75,
    }, user_id="customer_user_456", session_id="sess_abc123")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                               | Type                                                                                                                                                                                                    | Required                                                                                                                                                                                                | Description                                                                                                                                                                                             | Example                                                                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `feature_id`                                                                                                                                                                                            | *str*                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                      | ID of the item that was interacted with                                                                                                                                                                 | prod_123                                                                                                                                                                                                |
| `interaction_type`                                                                                                                                                                                      | List[[models.InteractionType](../../models/interactiontype.md)]                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                                      | Type of interaction or feedback                                                                                                                                                                         | [<br/>"positive_feedback",<br/>"click",<br/>"long_view"<br/>]                                                                                                                                           |
| `x_namespace`                                                                                                                                                                                           | *OptionalNullable[str]*                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                      | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint.                   |                                                                                                                                                                                                         |
| `position`                                                                                                                                                                                              | *OptionalNullable[int]*                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                      | Position in search results where interaction occurred                                                                                                                                                   | 3                                                                                                                                                                                                       |
| `metadata`                                                                                                                                                                                              | Dict[str, *Any*]                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                      | Additional context about the interaction                                                                                                                                                                | {<br/>"device": "mobile",<br/>"duration_ms": 5000,<br/>"interaction_reason": "not_relevant",<br/>"page": "search_results",<br/>"page_number": 1,<br/>"results_count": 50,<br/>"search_latency_ms": 150,<br/>"viewport_position": 0.75<br/>} |
| `user_id`                                                                                                                                                                                               | *OptionalNullable[str]*                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                      | Customer's authenticated user identifier - persists across sessions                                                                                                                                     | customer_user_456                                                                                                                                                                                       |
| `session_id`                                                                                                                                                                                            | *OptionalNullable[str]*                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                      | Temporary identifier for a single search journey/session (typically 30min-1hr) - tracks anonymous and authenticated users                                                                               | sess_abc123                                                                                                                                                                                             |
| `retries`                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                     |                                                                                                                                                                                                         |

### Response

**[models.InteractionResponse](../../models/interactionresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404         | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorResponse       | 500                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## list

List interactions with optional filters and pagination

**Requirements:**
- Required permissions: read

### Example Usage

```python
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.retriever_interactions.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `feature_id`                                                                                                                                                                          | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
| `interaction_type`                                                                                                                                                                    | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
| `session_id`                                                                                                                                                                          | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
| `page`                                                                                                                                                                                | *OptionalNullable[int]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
| `page_size`                                                                                                                                                                           | *Optional[int]*                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
| `x_namespace`                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. |
| `retries`                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                   |

### Response

**[List[models.InteractionResponse]](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404         | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorResponse       | 500                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get

Get a specific interaction

**Requirements:**
- Required permissions: read

### Example Usage

```python
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.retriever_interactions.get(interaction_id="<id>")

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
| models.ErrorResponse       | 400, 401, 403, 404         | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorResponse       | 500                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## delete

Delete a specific interaction

**Requirements:**
- Required permissions: write

### Example Usage

```python
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.retriever_interactions.delete(interaction_id="<id>")

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
| models.ErrorResponse       | 400, 401, 403, 404         | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorResponse       | 500                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |