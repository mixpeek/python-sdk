# Collections
(*collections*)

## Overview

### Available Operations

* [create_collection_v1_collections_create_post](#create_collection_v1_collections_create_post) - Create Collection
* [get_collection_v1_collections_collection_id_get](#get_collection_v1_collections_collection_id_get) - Get Collection

## create_collection_v1_collections_create_post

This endpoint allows you to create a new collection.

### Example Usage

```python
import mixpeek
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.collections.create_collection_v1_collections_create_post(collection_name="<value>", source={
        "type": mixpeek.SourceType.BUCKET,
        "filters": {
            "and_": [],
            "or_": [],
            "not_": [],
            "case_sensitive": True,
        },
    }, feature_extractors=[
        {
            "feature_extractor_name": "<value>",
            "version": "<value>",
        },
        {
            "feature_extractor_name": "<value>",
            "version": "<value>",
        },
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
| `metadata`                                                                                                                                                                                                      | [OptionalNullable[models.CreateCollectionRequestMetadata]](../../models/createcollectionrequestmetadata.md)                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                              | Optional metadata for the collection                                                                                                                                                                            |
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

## get_collection_v1_collections_collection_id_get

Get Collection

### Example Usage

```python
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.collections.get_collection_v1_collections_collection_id_get(collection_id="<id>")

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