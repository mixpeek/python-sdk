# Assets
(*assets*)

## Overview

### Available Operations

* [get](#get) - Get Asset
* [delete](#delete) - Delete Asset
* [update](#update) - Full Asset Update
* [partial_update](#partial_update) - Partial Asset Update
* [get_with_features](#get_with_features) - Get Asset With Features
* [list](#list) - List Assets
* [search](#search) - Search Assets

## get

Get basic asset details

### Example Usage

```python
from mixpeek import Mixpeek
import os

with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.assets.get(asset_id="ast_123")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           | Example                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `asset_id`                                                                                                                                                                            | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | Unique identifier of the asset                                                                                                                                                        | ast_123                                                                                                                                                                               |
| `return_url`                                                                                                                                                                          | *Optional[bool]*                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Whether to generate and return presigned S3 URLs for the asset and preview. Set to false to improve performance when URLs aren't needed                                               | true                                                                                                                                                                                  |
| `x_namespace`                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. |                                                                                                                                                                                       |
| `retries`                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                   |                                                                                                                                                                                       |

### Response

**[models.AssetResponse](../../models/assetresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404         | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorResponse       | 500                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## delete

**Requirements:**
- Required permissions: write

### Example Usage

```python
from mixpeek import Mixpeek
import os

with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.assets.delete(asset_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `asset_id`                                                                                                                                                                            | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
| `x_namespace`                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. |
| `retries`                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                   |

### Response

**[models.GenericSuccessResponse](../../models/genericsuccessresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404         | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorResponse       | 500                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## update

**Requirements:**
- Required permissions: write

### Example Usage

```python
from mixpeek import Mixpeek
import os

with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.assets.update(asset_id="<id>", propagate_features=True, metadata={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           | Example                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `asset_id`                                                                                                                                                                            | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | N/A                                                                                                                                                                                   |                                                                                                                                                                                       |
| `x_namespace`                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. |                                                                                                                                                                                       |
| `propagate_features`                                                                                                                                                                  | *OptionalNullable[bool]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                    | If True, the features will be propagated to all assets with the same asset_id                                                                                                         | true                                                                                                                                                                                  |
| `metadata`                                                                                                                                                                            | [Optional[models.UpdateAssetRequestMetadata]](../../models/updateassetrequestmetadata.md)                                                                                             | :heavy_minus_sign:                                                                                                                                                                    | Updated metadata for the asset. This can include any key-value pairs that should be updated or added to the asset's metadata.                                                         | {<br/>"description": "A new description",<br/>"title": "New Title"<br/>}                                                                                                              |
| `retries`                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                   |                                                                                                                                                                                       |

### Response

**[models.AssetResponse](../../models/assetresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404         | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorResponse       | 500                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## partial_update

**Requirements:**
- Required permissions: write

### Example Usage

```python
from mixpeek import Mixpeek
import os

with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.assets.partial_update(asset_id="<id>", propagate_features=True, metadata={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           | Example                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `asset_id`                                                                                                                                                                            | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | N/A                                                                                                                                                                                   |                                                                                                                                                                                       |
| `x_namespace`                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. |                                                                                                                                                                                       |
| `propagate_features`                                                                                                                                                                  | *OptionalNullable[bool]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                    | If True, the features will be propagated to all assets with the same asset_id                                                                                                         | true                                                                                                                                                                                  |
| `metadata`                                                                                                                                                                            | [Optional[models.UpdateAssetRequestMetadata]](../../models/updateassetrequestmetadata.md)                                                                                             | :heavy_minus_sign:                                                                                                                                                                    | Updated metadata for the asset. This can include any key-value pairs that should be updated or added to the asset's metadata.                                                         | {<br/>"description": "A new description",<br/>"title": "New Title"<br/>}                                                                                                              |
| `retries`                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                   |                                                                                                                                                                                       |

### Response

**[models.AssetResponse](../../models/assetresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404         | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorResponse       | 500                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_with_features

Get asset details including all related features

### Example Usage

```python
from mixpeek import Mixpeek
import os

with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.assets.get_with_features(asset_id="asset_123456789")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           | Example                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `asset_id`                                                                                                                                                                            | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | Unique identifier of the asset                                                                                                                                                        | asset_123456789                                                                                                                                                                       |
| `return_url`                                                                                                                                                                          | *Optional[bool]*                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Whether to generate and return presigned S3 URLs for the asset and preview. Set to false to improve performance when URLs aren't needed                                               | false                                                                                                                                                                                 |
| `x_namespace`                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. |                                                                                                                                                                                       |
| `retries`                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                   |                                                                                                                                                                                       |

### Response

**[models.GroupedAssetData](../../models/groupedassetdata.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404         | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorResponse       | 500                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## list

List Assets

### Example Usage

```python
import mixpeek
from mixpeek import Mixpeek
import os

with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.assets.list(collections=[
        "col_123",
        "my_collection",
    ], filters={
        "case_sensitive": True,
        "and_": [

        ],
        "or_": [

        ],
        "nor": [

        ],
    }, group_by={
        "field": "asset_id",
        "max_assets": 10,
        "sort": {
            "field": "score",
            "direction": mixpeek.Direction.DESC,
        },
    }, sort={
        "field": "score",
        "direction": mixpeek.Direction.DESC,
    }, select=[
        "title",
        "content",
        "metadata.author",
        "metadata.publication_date",
    ], return_url=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           | Example                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `collections`                                                                                                                                                                         | List[*str*]                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                    | List of Collection IDs or Names to search within, required                                                                                                                            | [<br/>"col_123",<br/>"my_collection"<br/>]                                                                                                                                            |
| `page`                                                                                                                                                                                | *OptionalNullable[int]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | N/A                                                                                                                                                                                   |                                                                                                                                                                                       |
| `page_size`                                                                                                                                                                           | *Optional[int]*                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                    | N/A                                                                                                                                                                                   |                                                                                                                                                                                       |
| `x_namespace`                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. |                                                                                                                                                                                       |
| `filters`                                                                                                                                                                             | [OptionalNullable[models.LogicalOperator]](../../models/logicaloperator.md)                                                                                                           | :heavy_minus_sign:                                                                                                                                                                    | Used for filtering across all indexes                                                                                                                                                 |                                                                                                                                                                                       |
| `group_by`                                                                                                                                                                            | [OptionalNullable[models.GroupByOptionsAsset]](../../models/groupbyoptionsasset.md)                                                                                                   | :heavy_minus_sign:                                                                                                                                                                    | Grouping options for search results                                                                                                                                                   |                                                                                                                                                                                       |
| `sort`                                                                                                                                                                                | [OptionalNullable[models.SortOption]](../../models/sortoption.md)                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                    | List of fields to sort by, with direction (asc or desc). Supports dot notation for nested fields.                                                                                     |                                                                                                                                                                                       |
| `select`                                                                                                                                                                              | List[*str*]                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                    | List of fields to return in results, supports dot notation. If None, all fields are returned.                                                                                         | [<br/>"title",<br/>"content",<br/>"metadata.author",<br/>"metadata.publication_date"<br/>]                                                                                            |
| `return_url`                                                                                                                                                                          | *OptionalNullable[bool]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                    | Return the presigned URL for the asset and preview asset, this will introduce additional latency                                                                                      | true                                                                                                                                                                                  |
| `retries`                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                   |                                                                                                                                                                                       |

### Response

**[models.ListAssetsResponse](../../models/listassetsresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404         | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorResponse       | 500                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## search

Search Assets

### Example Usage

```python
import mixpeek
from mixpeek import Mixpeek
import os

with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.assets.search(collections=[
        "col_123",
        "my_collection",
    ], query={
        "key": [
            "title",
            "description",
        ],
        "value": "search term",
    }, filters={
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
    }, return_url=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           | Example                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `collections`                                                                                                                                                                         | List[*str*]                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                    | List of Collection IDs or Names to search within, required                                                                                                                            | [<br/>"col_123",<br/>"my_collection"<br/>]                                                                                                                                            |
| `x_namespace`                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. |                                                                                                                                                                                       |
| `query`                                                                                                                                                                               | [OptionalNullable[models.AssetsModelSearchQuery]](../../models/assetsmodelsearchquery.md)                                                                                             | :heavy_minus_sign:                                                                                                                                                                    | Structured query object specifying which fields to search in and what to search for                                                                                                   |                                                                                                                                                                                       |
| `filters`                                                                                                                                                                             | [OptionalNullable[models.LogicalOperator]](../../models/logicaloperator.md)                                                                                                           | :heavy_minus_sign:                                                                                                                                                                    | Complex nested query filters                                                                                                                                                          |                                                                                                                                                                                       |
| `sort`                                                                                                                                                                                | [OptionalNullable[models.SortOption]](../../models/sortoption.md)                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                    | List of fields to sort by                                                                                                                                                             |                                                                                                                                                                                       |
| `select`                                                                                                                                                                              | List[*str*]                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                    | List of fields to return in results                                                                                                                                                   |                                                                                                                                                                                       |
| `return_url`                                                                                                                                                                          | *OptionalNullable[bool]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                    | Return the presigned URL for the asset and preview asset, this will introduce additional latency                                                                                      | true                                                                                                                                                                                  |
| `retries`                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                   |                                                                                                                                                                                       |

### Response

**[models.ListAssetsResponse](../../models/listassetsresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404         | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorResponse       | 500                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |