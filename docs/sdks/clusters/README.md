# Clusters
(*clusters*)

## Overview

### Available Operations

* [create_cluster_v1_clusters_post](#create_cluster_v1_clusters_post) - Create Cluster

## create_cluster_v1_clusters_post

Create Cluster

### Example Usage

```python
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.clusters.create_cluster_v1_clusters_post(collection_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `collection_id`                                                                                                                                                                       | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | ID of the collection to cluster                                                                                                                                                       |
| `x_namespace`                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. |
| `cluster_name`                                                                                                                                                                        | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Name for the cluster (auto-generated if empty)                                                                                                                                        |
| `cluster_type`                                                                                                                                                                        | [Optional[models.ClusterType]](../../models/clustertype.md)                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
| `vector_config`                                                                                                                                                                       | [OptionalNullable[models.VectorBasedConfig]](../../models/vectorbasedconfig.md)                                                                                                       | :heavy_minus_sign:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
| `attribute_config`                                                                                                                                                                    | [OptionalNullable[models.AttributeBasedConfig]](../../models/attributebasedconfig.md)                                                                                                 | :heavy_minus_sign:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
| `automatic_naming`                                                                                                                                                                    | [Optional[models.AutomaticNaming]](../../models/automaticnaming.md)                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
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