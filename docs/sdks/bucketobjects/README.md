# BucketObjects
(*bucket_objects*)

## Overview

### Available Operations

* [create](#create) - Create Object
* [get](#get) - Get Object
* [update](#update) - Update Object
* [delete](#delete) - Delete Object
* [list](#list) - List Objects

## create

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

    res = m_client.bucket_objects.create(bucket_identifier="<value>", key_prefix="/documents", blobs=[
        {
            "property": "content",
            "key_prefix": "/contract-2024/content.pdf",
            "type": mixpeek.BucketSchemaFieldType.JSON,
            "data": {
                "num_pages": 5,
                "title": "Service Agreement 2024",
            },
            "metadata": {
                "author": "John Doe",
                "department": "Legal",
            },
        },
        {
            "property": "thumbnail",
            "key_prefix": "/contract-2024/thumbnail.jpg",
            "type": mixpeek.BucketSchemaFieldType.IMAGE,
            "data": {
                "filename": "https://example.com/images/smartphone-x1.jpg",
                "mime_type": "image/jpeg",
            },
            "metadata": {
                "height": 300,
                "width": 200,
            },
        },
    ], metadata={
        "category": "contracts",
        "status": "draft",
        "year": 2024,
    })

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
| `metadata`                                                                                                                                                                                             | Dict[str, *Any*]                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                     | Additional metadata for the object, this will be appended in all downstream documents of the your connected collections.                                                                               | {<br/>"category": "contracts",<br/>"status": "draft",<br/>"year": 2024<br/>}                                                                                                                           |
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

## get

This endpoint retrieves an object by its ID from the specified bucket.

### Example Usage

```python
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.bucket_objects.get(bucket_identifier="<value>", object_identifier="<value>")

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

## update

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

    res = m_client.bucket_objects.update(bucket_identifier="<value>", object_identifier="<value>", key_prefix="/updated-documents", blobs=[
        {
            "property": "content",
            "key_prefix": "/contract-2024-revised",
            "type": mixpeek.BucketSchemaFieldType.SPREADSHEET,
            "data": {
                "num_pages": 6,
                "title": "Revised Service Agreement 2024",
            },
            "metadata": {
                "author": "Jane Smith",
                "department": "Legal",
                "version": "2.0",
            },
        },
    ], metadata={
        "category": "contracts",
        "reviewed": True,
        "status": "final",
        "year": 2024,
    })

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
| `metadata`                                                                                                                                                                            | Dict[str, *Any*]                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Updated metadata for the object, this will be merged with existing metadata.                                                                                                          |
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

## delete

This endpoint deletes an object from the specified bucket.

### Example Usage

```python
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.bucket_objects.delete(bucket_identifier="<value>", object_identifier="<value>")

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

## list

This endpoint lists objects in a bucket with pagination, sorting, and filtering options.

### Example Usage

```python
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.bucket_objects.list(bucket_identifier="<value>", filters=None, sort={
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