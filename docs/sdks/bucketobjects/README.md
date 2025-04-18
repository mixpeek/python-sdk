# BucketObjects
(*bucket_objects*)

## Overview

### Available Operations

* [create_object_v1_buckets_bucket_identifier_objects_create_post](#create_object_v1_buckets_bucket_identifier_objects_create_post) - Create Object
* [get_object_v1_buckets_bucket_identifier_objects_object_identifier_get](#get_object_v1_buckets_bucket_identifier_objects_object_identifier_get) - Get Object
* [update_object_v1_buckets_bucket_identifier_objects_object_identifier_put](#update_object_v1_buckets_bucket_identifier_objects_object_identifier_put) - Update Object
* [delete_object_v1_buckets_bucket_identifier_objects_object_identifier_delete](#delete_object_v1_buckets_bucket_identifier_objects_object_identifier_delete) - Delete Object
* [list_objects_v1_buckets_bucket_identifier_objects_post](#list_objects_v1_buckets_bucket_identifier_objects_post) - List Objects

## create_object_v1_buckets_bucket_identifier_objects_create_post

This endpoint creates a new object in the specified bucket.
    The object must conform to the bucket's schema.

### Example Usage

```python
import mixpeek
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.bucket_objects.create_object_v1_buckets_bucket_identifier_objects_create_post(bucket_identifier="<value>", key_prefix="/contract-2024", blobs=[
        {
            "property": "content",
            "key_prefix": "/content.pdf",
            "type": mixpeek.BucketSchemaFieldType.STRING,
            "data": {
                "num_pages": 5,
                "title": "Service Agreement 2024",
            },
        },
    ], metadata={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                              | Type                                                                                                                                                                                                   | Required                                                                                                                                                                                               | Description                                                                                                                                                                                            | Example                                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `bucket_identifier`                                                                                                                                                                                    | *str*                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                     | Identifier of the bucket                                                                                                                                                                               |                                                                                                                                                                                                        |
| `x_namespace`                                                                                                                                                                                          | *OptionalNullable[str]*                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                     | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint.                  |                                                                                                                                                                                                        |
| `key_prefix`                                                                                                                                                                                           | *OptionalNullable[str]*                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                     | Storage key/path prefix of the object, this will be used to retrieve the object from the storage. It's at the root of the object.                                                                      | /contract-2024                                                                                                                                                                                         |
| `blobs`                                                                                                                                                                                                | List[[models.CreateBlobRequest](../../models/createblobrequest.md)]                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                     | List of blobs to be created in this object                                                                                                                                                             | [<br/>{<br/>"data": {<br/>"num_pages": 5,<br/>"title": "Service Agreement 2024"<br/>},<br/>"key_prefix": "/content.pdf",<br/>"metadata": {<br/>"author": "John Doe",<br/>"department": "Legal"<br/>},<br/>"property": "content",<br/>"type": "PDF"<br/>}<br/>] |
| `metadata`                                                                                                                                                                                             | [Optional[models.CreateObjectRequestMetadata]](../../models/createobjectrequestmetadata.md)                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                     | Additional metadata for the object, this will be appended in all downstream documents of the your connected collections.                                                                               | {<br/>"category": "contracts",<br/>"status": "draft",<br/>"year": 2024<br/>}                                                                                                                           |
| `skip_duplicates`                                                                                                                                                                                      | *Optional[bool]*                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                     | Skip duplicate blobs, if a blob with the same hash already exists, it will be skipped.                                                                                                                 |                                                                                                                                                                                                        |
| `retries`                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                    |                                                                                                                                                                                                        |

### Response

**[models.TaskResponse](../../models/taskresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404         | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorResponse       | 500                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_object_v1_buckets_bucket_identifier_objects_object_identifier_get

This endpoint retrieves an object by its ID from the specified bucket.

### Example Usage

```python
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.bucket_objects.get_object_v1_buckets_bucket_identifier_objects_object_identifier_get(bucket_identifier="<value>", object_identifier="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `bucket_identifier`                                                                                                                                                                   | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | Identifier of the bucket                                                                                                                                                              |
| `object_identifier`                                                                                                                                                                   | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | Identifier of the object                                                                                                                                                              |
| `x_namespace`                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. |
| `retries`                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                   |

### Response

**[models.ObjectResponse](../../models/objectresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404         | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorResponse       | 500                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## update_object_v1_buckets_bucket_identifier_objects_object_identifier_put

This endpoint updates an existing object in the specified bucket.
    The updated object must conform to the bucket's schema.

### Example Usage

```python
import mixpeek
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.bucket_objects.update_object_v1_buckets_bucket_identifier_objects_object_identifier_put(bucket_identifier="<value>", object_identifier="<value>", key_prefix="/updated-documents", blobs=[
        {
            "property": "content",
            "key_prefix": "/contract-2024-revised",
            "type": mixpeek.BucketSchemaFieldType.INTEGER,
            "data": {
                "num_pages": 6,
                "title": "Revised Service Agreement 2024",
            },
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `bucket_identifier`                                                                                                                                                                   | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | Identifier of the bucket                                                                                                                                                              |
| `object_identifier`                                                                                                                                                                   | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | Identifier of the object                                                                                                                                                              |
| `x_namespace`                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. |
| `key_prefix`                                                                                                                                                                          | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Updated storage key/path prefix of the object, this will be used to retrieve the object from the storage. It's at the root of the object.                                             |
| `blobs`                                                                                                                                                                               | List[[models.CreateBlobRequest](../../models/createblobrequest.md)]                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                    | List of new or updated blobs for this object                                                                                                                                          |
| `metadata`                                                                                                                                                                            | [OptionalNullable[models.UpdateObjectRequestMetadata]](../../models/updateobjectrequestmetadata.md)                                                                                   | :heavy_minus_sign:                                                                                                                                                                    | Updated metadata for the object, this will be merged with existing metadata.                                                                                                          |
| `skip_duplicates`                                                                                                                                                                     | *OptionalNullable[bool]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                    | Skip duplicate blobs, if a blob with the same hash already exists, it will be skipped.                                                                                                |
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

## delete_object_v1_buckets_bucket_identifier_objects_object_identifier_delete

This endpoint deletes an object from the specified bucket.

### Example Usage

```python
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.bucket_objects.delete_object_v1_buckets_bucket_identifier_objects_object_identifier_delete(bucket_identifier="<value>", object_identifier="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `bucket_identifier`                                                                                                                                                                   | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | Identifier of the bucket                                                                                                                                                              |
| `object_identifier`                                                                                                                                                                   | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | Identifier of the object                                                                                                                                                              |
| `x_namespace`                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. |
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

## list_objects_v1_buckets_bucket_identifier_objects_post

This endpoint lists objects in a bucket with pagination, sorting, and filtering options.

### Example Usage

```python
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.bucket_objects.list_objects_v1_buckets_bucket_identifier_objects_post(bucket_identifier="<value>", filters={
        "and_": [],
        "or_": [],
        "not_": [],
        "case_sensitive": True,
    }, sort={
        "field": "created_at",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `bucket_identifier`                                                                                                                                                                   | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | Identifier of the bucket                                                                                                                                                              |
| `limit`                                                                                                                                                                               | *OptionalNullable[int]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
| `offset`                                                                                                                                                                              | *OptionalNullable[int]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
| `x_namespace`                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. |
| `filters`                                                                                                                                                                             | [OptionalNullable[models.LogicalOperatorInput]](../../models/logicaloperatorinput.md)                                                                                                 | :heavy_minus_sign:                                                                                                                                                                    | Filters to apply to the object list                                                                                                                                                   |
| `sort`                                                                                                                                                                                | [OptionalNullable[models.SortOption]](../../models/sortoption.md)                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                    | Sort options for the object list                                                                                                                                                      |
| `search`                                                                                                                                                                              | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Search term to filter objects by key or metadata                                                                                                                                      |
| `retries`                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                   |

### Response

**[models.ListObjectsResponse](../../models/listobjectsresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404         | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorResponse       | 500                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |