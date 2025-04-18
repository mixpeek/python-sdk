# TaxonomyEntities
(*taxonomy_entities*)

## Overview

### Available Operations

* [create](#create) - Create Taxonomy
* [list](#list) - List Taxonomies
* [get_node](#get_node) - Get Taxonomy Node
* [update_node](#update_node) - Update Node
* [classify_features](#classify_features) - Classify Features against Taxonomy
* [list_classifications](#list_classifications) - List Taxonomy Classifications
* [delete_classification](#delete_classification) - Delete Classifications

## create

Register new taxonomies with their descriptions

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

    res = m_client.taxonomy_entities.create(taxonomy_name="electronics", nodes=[
        {
            "node_name": "electronics_accessories",
            "node_description": "Electronics accessories and peripherals category",
            "embedding_configs": [
                {
                    "type": mixpeek.EmbeddingConfigType.URL,
                    "value": "https://example.com/image.jpg",
                    "embedding_model": mixpeek.AvailableModels.TEXT,
                },
            ],
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           | Example                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `taxonomy_name`                                                                                                                                                                       | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | Taxonomy name (must not contain spaces or special characters)                                                                                                                         | electronics                                                                                                                                                                           |
| `nodes`                                                                                                                                                                               | List[[models.TaxonomyNodeCreate](../../models/taxonomynodecreate.md)]                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | N/A                                                                                                                                                                                   |                                                                                                                                                                                       |
| `x_namespace`                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. |                                                                                                                                                                                       |
| `retries`                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                   |                                                                                                                                                                                       |

### Response

**[models.TaskResponse](../../models/taskresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404         | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorResponse       | 500                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## list

Get all taxonomies for the current namespace

### Example Usage

```python
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.taxonomy_entities.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `offset_id`                                                                                                                                                                           | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | The offset id to start returning results from. Used for pagination                                                                                                                    |
| `page_size`                                                                                                                                                                           | *Optional[int]*                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
| `x_namespace`                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. |
| `retries`                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                   |

### Response

**[models.ListTaxonomiesResponse](../../models/listtaxonomiesresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404         | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorResponse       | 500                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_node

Get the complete taxonomy that contains the specified node

### Example Usage

```python
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.taxonomy_entities.get_node(node="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `node`                                                                                                                                                                                | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | The ID or name of the node to find the taxonomy for                                                                                                                                   |
| `x_namespace`                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. |
| `retries`                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                   |

### Response

**[models.TaxonomyNode](../../models/taxonomynode.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404         | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorResponse       | 500                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## update_node

Update an existing taxonomy node

**Requirements:**
- Required permissions: write

### Example Usage

```python
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.taxonomy_entities.update_node(node="<value>", node_name="electronics_accessories", node_description="Electronics accessories and peripherals category")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           | Example                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `node`                                                                                                                                                                                | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | The ID or name of the node to update                                                                                                                                                  |                                                                                                                                                                                       |
| `node_name`                                                                                                                                                                           | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | Name of the taxonomy node (must be lowercase without spaces)                                                                                                                          | electronics_accessories                                                                                                                                                               |
| `x_namespace`                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. |                                                                                                                                                                                       |
| `node_description`                                                                                                                                                                    | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Optional description of what this node represents                                                                                                                                     | Electronics accessories and peripherals category                                                                                                                                      |
| `retries`                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                   |                                                                                                                                                                                       |

### Response

**[models.TaxonomyNode](../../models/taxonomynode.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404         | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorResponse       | 500                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## classify_features

Starts an asynchronous task to classify features within collections for a given taxonomy.

### Example Usage

```python
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.taxonomy_entities.classify_features(taxonomy="<value>", collections=[
        "<value>",
    ], filters={
        "case_sensitive": True,
        "and_": [],
        "or_": [],
        "nor": [],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `taxonomy`                                                                                                                                                                            | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | The name or id of the taxonomy to use for discovery                                                                                                                                   |
| `collections`                                                                                                                                                                         | List[*str*]                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                    | List of collection names or ids to search for features                                                                                                                                |
| `x_namespace`                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. |
| `filters`                                                                                                                                                                             | [OptionalNullable[models.LogicalOperator]](../../models/logicaloperator.md)                                                                                                           | :heavy_minus_sign:                                                                                                                                                                    | Filters to apply to the discovery task                                                                                                                                                |
| `assignment`                                                                                                                                                                          | [Optional[models.AssignmentConfig]](../../models/assignmentconfig.md)                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                    | Configuration for how classifications should be assigned to features                                                                                                                  |
| `limit`                                                                                                                                                                               | *OptionalNullable[int]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Number of feature samples to process, if None, all features that match the filters are processed                                                                                      |
| `retries`                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                   |

### Response

**[models.TaskResponse](../../models/taskresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404         | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorResponse       | 500                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## list_classifications

Retrieves a paginated list of classification entries with optional filtering.

### Example Usage

```python
import mixpeek
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.taxonomy_entities.list_classifications(taxonomy="<value>", filters={
        "case_sensitive": True,
        "and_": [],
        "or_": [],
        "nor": [],
    }, sort={
        "field": "score",
        "direction": mixpeek.Direction.DESC,
    }, feature_options={}, node_options={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           | Example                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `taxonomy`                                                                                                                                                                            | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | The ID or name of the taxonomy                                                                                                                                                        |                                                                                                                                                                                       |
| `page`                                                                                                                                                                                | *OptionalNullable[int]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | N/A                                                                                                                                                                                   |                                                                                                                                                                                       |
| `page_size`                                                                                                                                                                           | *Optional[int]*                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                    | N/A                                                                                                                                                                                   |                                                                                                                                                                                       |
| `x_namespace`                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. |                                                                                                                                                                                       |
| `filters`                                                                                                                                                                             | [OptionalNullable[models.LogicalOperator]](../../models/logicaloperator.md)                                                                                                           | :heavy_minus_sign:                                                                                                                                                                    | Complex nested query filters for classifications                                                                                                                                      |                                                                                                                                                                                       |
| `sort`                                                                                                                                                                                | [OptionalNullable[models.SortOption]](../../models/sortoption.md)                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                    | Sort options for ordering classifications                                                                                                                                             |                                                                                                                                                                                       |
| `feature_options`                                                                                                                                                                     | [OptionalNullable[models.FeatureOptions]](../../models/featureoptions.md)                                                                                                             | :heavy_minus_sign:                                                                                                                                                                    | Controls what feature data to include in the response. Note: Including additional data increases response latency.                                                                    | {<br/>"return_payload": true,<br/>"return_url": true<br/>}                                                                                                                            |
| `node_options`                                                                                                                                                                        | [OptionalNullable[models.NodeOptions]](../../models/nodeoptions.md)                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                    | Controls what node data to include in the response. Note: Including additional data increases response latency.                                                                       | {<br/>"return_payload": true<br/>}                                                                                                                                                    |
| `retries`                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                   |                                                                                                                                                                                       |

### Response

**[models.ListClassificationsResponse](../../models/listclassificationsresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404         | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorResponse       | 500                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## delete_classification

**Requirements:**
- Required permissions: write

### Example Usage

```python
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.taxonomy_entities.delete_classification(taxonomy="<value>", classification_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `taxonomy`                                                                                                                                                                            | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | The id or name of the taxonomy                                                                                                                                                        |
| `classification_id`                                                                                                                                                                   | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | The id of the classification to delete                                                                                                                                                |
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