# Collections
(*collections*)

## Overview

### Available Operations

* [create](#create) - Create Collection
* [get](#get) - Get Collection

## create

This endpoint allows you to create a new collection.

### Example Usage

```python
import mixpeek
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.collections.create(collection_name="<value>", source={
        "type": mixpeek.SourceType.BUCKET,
        "filters": {
            "and_": [
                {
                    "field": "name",
                    "operator": mixpeek.FilterOperator.EQ,
                    "value": "John",
                },
                {
                    "field": "age",
                    "operator": mixpeek.FilterOperator.GTE,
                    "value": 30,
                },
            ],
            "or_": [
                {
                    "field": "status",
                    "operator": mixpeek.FilterOperator.EQ,
                    "value": "active",
                },
                {
                    "field": "role",
                    "operator": mixpeek.FilterOperator.EQ,
                    "value": "admin",
                },
            ],
            "not_": [
                {
                    "field": "department",
                    "operator": mixpeek.FilterOperator.EQ,
                    "value": "HR",
                },
                {
                    "field": "location",
                    "operator": mixpeek.FilterOperator.EQ,
                    "value": "remote",
                },
            ],
            "case_sensitive": True,
        },
    }, feature_extractors=[
        {
            "feature_extractor_name": "<value>",
            "version": "<value>",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                       | Type                                                                                                                                                                                                            | Required                                                                                                                                                                                                        | Description                                                                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `collection_name`                                                                                                                                                                                               | *str*                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                              | Name for the collection                                                                                                                                                                                         |
| `source`                                                                                                                                                                                                        | [models.SourceConfigInput](../../models/sourceconfiginput.md)                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                              | Configuration for a collection source                                                                                                                                                                           |
| `feature_extractors`                                                                                                                                                                                            | List[[models.FeatureExtractorConfig](../../models/featureextractorconfig.md)]                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                              | List of feature extractor configurations to use                                                                                                                                                                 |
| `x_namespace`                                                                                                                                                                                                   | *OptionalNullable[str]*                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                              | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint.                           |
| `description`                                                                                                                                                                                                   | *OptionalNullable[str]*                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                              | Description for the collection                                                                                                                                                                                  |
| `taxonomy_applications`                                                                                                                                                                                         | List[[models.TaxonomyApplicationConfig](../../models/taxonomyapplicationconfig.md)]                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                              | List of taxonomy application configurations. there are two options: on ingestion store the taxonomy application results to this collection, or on demand compute the taxonomy application results at query time |
| `enabled`                                                                                                                                                                                                       | *Optional[bool]*                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                              | Enable or disable processing of this collection                                                                                                                                                                 |
| `metadata`                                                                                                                                                                                                      | Dict[str, *Any*]                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                              | Optional metadata for the collection                                                                                                                                                                            |
| `document_handling`                                                                                                                                                                                             | [OptionalNullable[models.DocumentHandlingConfig]](../../models/documenthandlingconfig.md)                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                              | Configuration for how documents are handled by this extractor                                                                                                                                                   |
| `cache_config`                                                                                                                                                                                                  | [OptionalNullable[models.CollectionCacheConfigInput]](../../models/collectioncacheconfiginput.md)                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                              | Configuration for collection-level caching                                                                                                                                                                      |
| `retries`                                                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                                                             |

### Response

**[models.CollectionModel](../../models/collectionmodel.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404         | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorResponse       | 500                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get

This endpoint allows you to retrieve a collection by ID.

### Example Usage

```python
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.collections.get(collection_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `collection_id`                                                                                                                                                                       | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | The ID of the collection to retrieve                                                                                                                                                  |
| `x_namespace`                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. |
| `retries`                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                   |

### Response

**[models.CollectionModel](../../models/collectionmodel.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404         | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorResponse       | 500                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |