# Features
(*features*)

## Overview

### Available Operations

* [get_feature_v1_features_feature_id_get](#get_feature_v1_features_feature_id_get) - Get Feature
* [delete_feature_v1_features_feature_id_delete](#delete_feature_v1_features_feature_id_delete) - Delete Feature
* [full_feature_update_v1_features_feature_id_put](#full_feature_update_v1_features_feature_id_put) - Full Feature Update
* [list_features_v1_features_post](#list_features_v1_features_post) - List Features

## get_feature_v1_features_feature_id_get

Get Feature

### Example Usage

```python
from mixpeek import Mixpeek
import os

with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as mixpeek:

    res = mixpeek.features.get_feature_v1_features_feature_id_get(feature_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `feature_id`                                                                                                                                                                          | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
| `return_vectors`                                                                                                                                                                      | *OptionalNullable[bool]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                    | When true, includes the feature's vector embeddings in the response                                                                                                                   |
| `x_namespace`                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. |
| `retries`                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                   |

### Response

**[models.FeatureResponse](../../models/featureresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404, 500    | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## delete_feature_v1_features_feature_id_delete

**Requirements:**
- Required permissions: write

### Example Usage

```python
from mixpeek import Mixpeek
import os

with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as mixpeek:

    res = mixpeek.features.delete_feature_v1_features_feature_id_delete(feature_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `feature_id`                                                                                                                                                                          | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
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

## full_feature_update_v1_features_feature_id_put

**Requirements:**
- Required permissions: write

### Example Usage

```python
from mixpeek import Mixpeek
import os

with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as mixpeek:

    res = mixpeek.features.full_feature_update_v1_features_feature_id_put(feature_id="<id>", metadata={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `feature_id`                                                                                                                                                                          | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
| `metadata`                                                                                                                                                                            | [models.FeatureUpdateRequestMetadata](../../models/featureupdaterequestmetadata.md)                                                                                                   | :heavy_check_mark:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
| `x_namespace`                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. |
| `retries`                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                   |

### Response

**[models.FeatureResponse](../../models/featureresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404, 500    | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## list_features_v1_features_post

Retrieves a list of features based on
    the provided filters and sorting criteria. 
    If you provide a sort, then pagination isn't supported.

### Example Usage

```python
import mixpeek
from mixpeek import Mixpeek
import os

with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as mixpeek:

    res = mixpeek.features.list_features_v1_features_post(collections=[
        "collection_123",
        "my_collection_name",
    ], filters={
        "case_sensitive": True,
        "and_": [

        ],
        "or_": [

        ],
        "nor": [

        ],
    }, sort={
        "field": "score",
        "direction": mixpeek.Direction.DESC,
    }, select=[
        "metadata.tags",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           | Example                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `collections`                                                                                                                                                                         | List[*str*]                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                    | Collection identifiers - can be either collection IDs or collection names                                                                                                             | [<br/>"collection_123",<br/>"my_collection_name"<br/>]                                                                                                                                |
| `offset_feature_id`                                                                                                                                                                   | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | The offset id to start returning results from. Used for pagination                                                                                                                    |                                                                                                                                                                                       |
| `page_size`                                                                                                                                                                           | *Optional[int]*                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                    | N/A                                                                                                                                                                                   |                                                                                                                                                                                       |
| `x_namespace`                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. |                                                                                                                                                                                       |
| `filters`                                                                                                                                                                             | [OptionalNullable[models.LogicalOperator]](../../models/logicaloperator.md)                                                                                                           | :heavy_minus_sign:                                                                                                                                                                    | Complex nested query filters                                                                                                                                                          |                                                                                                                                                                                       |
| `sort`                                                                                                                                                                                | [OptionalNullable[models.SortOption]](../../models/sortoption.md)                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                    | <br/>        List of fields to sort by, with direction (asc or desc).<br/>        NOTE: fields will require a specialty index to use this, consult with the team.<br/>                |                                                                                                                                                                                       |
| `select`                                                                                                                                                                              | List[*Any*]                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                    | List of fields to return in results, supports dot notation. Everything else is excluded.                                                                                              | [<br/>"metadata.tags"<br/>]                                                                                                                                                           |
| `return_urls`                                                                                                                                                                         | *Optional[bool]*                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | When true, generates presigned URLs for assets                                                                                                                                        |                                                                                                                                                                                       |
| `retries`                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                   |                                                                                                                                                                                       |

### Response

**[models.ListFeaturesResponse](../../models/listfeaturesresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404, 500    | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |