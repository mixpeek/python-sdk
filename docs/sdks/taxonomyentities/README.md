# TaxonomyEntities
(*taxonomy_entities*)

## Overview

### Available Operations

* [create_taxonomy_v1_entities_taxonomies_post](#create_taxonomy_v1_entities_taxonomies_post) - Create Taxonomy
* [list_taxonomies_v1_entities_taxonomies_get](#list_taxonomies_v1_entities_taxonomies_get) - List Taxonomies
* [get_taxonomy_v1_entities_taxonomies_taxonomy_get](#get_taxonomy_v1_entities_taxonomies_taxonomy_get) - Get Taxonomy
* [delete_taxonomy_v1_entities_taxonomies_taxonomy_delete](#delete_taxonomy_v1_entities_taxonomies_taxonomy_delete) - Delete Taxonomy
* [update_taxonomy_v1_entities_taxonomies_taxonomy_patch](#update_taxonomy_v1_entities_taxonomies_taxonomy_patch) - Update Taxonomy
* [get_taxonomy_node_v1_entities_taxonomies_nodes_node_get](#get_taxonomy_node_v1_entities_taxonomies_nodes_node_get) - Get Taxonomy Node
* [update_node_v1_entities_taxonomies_nodes_node_patch](#update_node_v1_entities_taxonomies_nodes_node_patch) - Update Node
* [classify_features_v1_entities_taxonomies_taxonomy_classify_post](#classify_features_v1_entities_taxonomies_taxonomy_classify_post) - Classify Features against Taxonomy
* [list_classifications_v1_entities_taxonomies_taxonomy_classifications_post](#list_classifications_v1_entities_taxonomies_taxonomy_classifications_post) - List Taxonomy Classifications
* [delete_classifications_v1_entities_taxonomies_taxonomy_classifications_classification_id_delete](#delete_classifications_v1_entities_taxonomies_taxonomy_classifications_classification_id_delete) - Delete Classifications

## create_taxonomy_v1_entities_taxonomies_post

Register new taxonomies with their descriptions

**Requirements:**
- Required permissions: write

### Example Usage

```python
from mixpeek import Mixpeek
import os

with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as mixpeek:

    res = mixpeek.taxonomy_entities.create_taxonomy_v1_entities_taxonomies_post(taxonomy_name="electronics", nodes=[

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
| models.ErrorResponse       | 400, 401, 403, 404, 500    | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## list_taxonomies_v1_entities_taxonomies_get

Get all taxonomies for the current namespace

### Example Usage

```python
from mixpeek import Mixpeek
import os

with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as mixpeek:

    res = mixpeek.taxonomy_entities.list_taxonomies_v1_entities_taxonomies_get()

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
| models.ErrorResponse       | 400, 401, 403, 404, 500    | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_taxonomy_v1_entities_taxonomies_taxonomy_get

Get the complete taxonomy that contains the specified node

### Example Usage

```python
from mixpeek import Mixpeek
import os

with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as mixpeek:

    res = mixpeek.taxonomy_entities.get_taxonomy_v1_entities_taxonomies_taxonomy_get(taxonomy="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `taxonomy`                                                                                                                                                                            | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | The name or id of the taxonomy to find                                                                                                                                                |
| `x_namespace`                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. |
| `retries`                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                   |

### Response

**[models.TaxonomyModel](../../models/taxonomymodel.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404, 500    | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## delete_taxonomy_v1_entities_taxonomies_taxonomy_delete

Delete an existing taxonomy and remove all associated node classifications from features.

    This operation:
    - Deletes the taxonomy and all its nodes
    - Removes any node classifications associated with this taxonomy from all features
    - This action cannot be undone
    

**Requirements:**
- Required permissions: write

### Example Usage

```python
from mixpeek import Mixpeek
import os

with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as mixpeek:

    res = mixpeek.taxonomy_entities.delete_taxonomy_v1_entities_taxonomies_taxonomy_delete(taxonomy="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `taxonomy`                                                                                                                                                                            | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | The ID or name of the taxonomy to delete                                                                                                                                              |
| `x_namespace`                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. |
| `retries`                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                   |

### Response

**[models.GenericSuccessResponse](../../models/genericsuccessresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404, 500    | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## update_taxonomy_v1_entities_taxonomies_taxonomy_patch

Update an existing taxonomy's metadata

**Requirements:**
- Required permissions: write

### Example Usage

```python
from mixpeek import Mixpeek
import os

with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as mixpeek:

    res = mixpeek.taxonomy_entities.update_taxonomy_v1_entities_taxonomies_taxonomy_patch(taxonomy="<value>", taxonomy_name="electronics_updated", description="Updated electronics taxonomy")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           | Example                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `taxonomy`                                                                                                                                                                            | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | The ID or name of the taxonomy to update                                                                                                                                              |                                                                                                                                                                                       |
| `x_namespace`                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. |                                                                                                                                                                                       |
| `taxonomy_name`                                                                                                                                                                       | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Updated taxonomy name (must not contain spaces or special characters)                                                                                                                 | electronics_updated                                                                                                                                                                   |
| `description`                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Updated taxonomy description                                                                                                                                                          | Updated electronics taxonomy                                                                                                                                                          |
| `retries`                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                   |                                                                                                                                                                                       |

### Response

**[models.TaxonomyModel](../../models/taxonomymodel.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404, 500    | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_taxonomy_node_v1_entities_taxonomies_nodes_node_get

Get the complete taxonomy that contains the specified node

### Example Usage

```python
from mixpeek import Mixpeek
import os

with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as mixpeek:

    res = mixpeek.taxonomy_entities.get_taxonomy_node_v1_entities_taxonomies_nodes_node_get(node="<value>")

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
| models.ErrorResponse       | 400, 401, 403, 404, 500    | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## update_node_v1_entities_taxonomies_nodes_node_patch

Update an existing taxonomy node

**Requirements:**
- Required permissions: write

### Example Usage

```python
from mixpeek import Mixpeek
import os

with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as mixpeek:

    res = mixpeek.taxonomy_entities.update_node_v1_entities_taxonomies_nodes_node_patch(node="<value>", node_name="electronics_accessories", node_description="Electronics accessories and peripherals category")

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
| models.ErrorResponse       | 400, 401, 403, 404, 500    | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## classify_features_v1_entities_taxonomies_taxonomy_classify_post

Starts an asynchronous task to classify features within collections for a given taxonomy.

### Example Usage

```python
from mixpeek import Mixpeek
import os

with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as mixpeek:

    res = mixpeek.taxonomy_entities.classify_features_v1_entities_taxonomies_taxonomy_classify_post(taxonomy="<value>", collections=[
        "<value>",
        "<value>",
        "<value>",
    ], filters={
        "case_sensitive": True,
        "and_": [

        ],
        "or_": [

        ],
        "nor": [

        ],
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
| `confidence_threshold`                                                                                                                                                                | *Optional[float]*                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                    | Minimum confidence score required for classification                                                                                                                                  |
| `assignment`                                                                                                                                                                          | [Optional[models.AssignmentConfig]](../../models/assignmentconfig.md)                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                    | Configuration for how classifications should be assigned to features                                                                                                                  |
| `sample_size`                                                                                                                                                                         | *OptionalNullable[int]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Number of feature samples to process                                                                                                                                                  |
| `retries`                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                   |

### Response

**[models.TaskResponse](../../models/taskresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404, 500    | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## list_classifications_v1_entities_taxonomies_taxonomy_classifications_post

Retrieves a paginated list of classification entries with optional filtering.

### Example Usage

```python
import mixpeek
from mixpeek import Mixpeek
import os

with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as mixpeek:

    res = mixpeek.taxonomy_entities.list_classifications_v1_entities_taxonomies_taxonomy_classifications_post(taxonomy="<value>", filters={
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
    }, feature_options={
        "return_payload": True,
        "return_url": True,
    }, node_options={
        "return_payload": True,
    })

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
| models.ErrorResponse       | 400, 401, 403, 404, 500    | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## delete_classifications_v1_entities_taxonomies_taxonomy_classifications_classification_id_delete

**Requirements:**
- Required permissions: write

### Example Usage

```python
from mixpeek import Mixpeek
import os

with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as mixpeek:

    res = mixpeek.taxonomy_entities.delete_classifications_v1_entities_taxonomies_taxonomy_classifications_classification_id_delete(taxonomy="<value>", classification_id="<id>")

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
| models.ErrorResponse       | 400, 401, 403, 404, 500    | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |