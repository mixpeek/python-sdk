# CollectionDocuments
(*collection_documents*)

## Overview

### Available Operations

* [get_document_v1_collections_collection_identifier_documents_document_id_get](#get_document_v1_collections_collection_identifier_documents_document_id_get) - Get Document
* [update_document_v1_collections_collection_identifier_documents_document_id_put](#update_document_v1_collections_collection_identifier_documents_document_id_put) - Update Document
* [delete_document_v1_collections_collection_identifier_documents_document_id_delete](#delete_document_v1_collections_collection_identifier_documents_document_id_delete) - Delete Document
* [list_documents_v1_collections_collection_identifier_documents_get](#list_documents_v1_collections_collection_identifier_documents_get) - List Documents
* [batch_update_documents_v1_collections_collection_identifier_documents_batch_put](#batch_update_documents_v1_collections_collection_identifier_documents_batch_put) - Batch Update Documents
* [batch_delete_documents_v1_collections_collection_identifier_documents_batch_delete](#batch_delete_documents_v1_collections_collection_identifier_documents_batch_delete) - Batch Delete Documents

## get_document_v1_collections_collection_identifier_documents_document_id_get

Get a document by ID.
    

**Requirements:**
- Required permissions: read

### Example Usage

```python
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.collection_documents.get_document_v1_collections_collection_identifier_documents_document_id_get(collection_identifier="<value>", document_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `collection_identifier`                                                                                                                                                               | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | The ID of the collection                                                                                                                                                              |
| `document_id`                                                                                                                                                                         | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | The ID of the document to retrieve                                                                                                                                                    |
| `x_namespace`                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. |
| `retries`                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                   |

### Response

**[models.DocumentResponse](../../models/documentresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404         | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorResponse       | 500                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## update_document_v1_collections_collection_identifier_documents_document_id_put

Update an existing document.
    

**Requirements:**
- Required permissions: write

### Example Usage

```python
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.collection_documents.update_document_v1_collections_collection_identifier_documents_document_id_put(collection_identifier="<value>", document_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `collection_identifier`                                                                                                                                                               | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | The ID of the collection                                                                                                                                                              |
| `document_id`                                                                                                                                                                         | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | The ID of the document to update                                                                                                                                                      |
| `x_namespace`                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. |
| `metadata`                                                                                                                                                                            | [OptionalNullable[models.DocumentUpdateMetadata]](../../models/documentupdatemetadata.md)                                                                                             | :heavy_minus_sign:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
| `vectors`                                                                                                                                                                             | Dict[str, List[*float*]]                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
| `retries`                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                   |

### Response

**[models.DocumentResponse](../../models/documentresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404         | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorResponse       | 500                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## delete_document_v1_collections_collection_identifier_documents_document_id_delete

Delete a document.
    

**Requirements:**
- Required permissions: write

### Example Usage

```python
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.collection_documents.delete_document_v1_collections_collection_identifier_documents_document_id_delete(collection_identifier="<value>", document_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `collection_identifier`                                                                                                                                                               | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | The ID of the collection                                                                                                                                                              |
| `document_id`                                                                                                                                                                         | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | The ID of the document to delete                                                                                                                                                      |
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

## list_documents_v1_collections_collection_identifier_documents_get

List documents with pagination and filtering.
    

**Requirements:**
- Required permissions: read

### Example Usage

```python
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.collection_documents.list_documents_v1_collections_collection_identifier_documents_get(collection_identifier="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `collection_identifier`                                                                                                                                                               | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | The ID of the collection                                                                                                                                                              |
| `limit`                                                                                                                                                                               | *Optional[int]*                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                    | Number of documents to return per page                                                                                                                                                |
| `offset_id`                                                                                                                                                                           | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | ID of the document to start pagination from                                                                                                                                           |
| `sort`                                                                                                                                                                                | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Field to sort by                                                                                                                                                                      |
| `filters`                                                                                                                                                                             | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Filter criteria                                                                                                                                                                       |
| `select`                                                                                                                                                                              | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Fields to select                                                                                                                                                                      |
| `x_namespace`                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. |
| `retries`                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                   |

### Response

**[models.DocumentListResponse](../../models/documentlistresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404         | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorResponse       | 500                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## batch_update_documents_v1_collections_collection_identifier_documents_batch_put

Update multiple documents in a batch.
    

**Requirements:**
- Required permissions: write

### Example Usage

```python
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.collection_documents.batch_update_documents_v1_collections_collection_identifier_documents_batch_put(collection_identifier="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `collection_identifier`                                                                                                                                                               | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | The ID of the collection                                                                                                                                                              |
| `x_namespace`                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. |
| `request_body`                                                                                                                                                                        | List[List[[models.RequestBody](../../models/requestbody.md)]]                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
| `retries`                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                   |

### Response

**[List[Nullable[models.DocumentResponse]]](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorResponse       | 400, 401, 403, 404         | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.ErrorResponse       | 500                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## batch_delete_documents_v1_collections_collection_identifier_documents_batch_delete

Delete multiple documents in a batch.
    

**Requirements:**
- Required permissions: write

### Example Usage

```python
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.collection_documents.batch_delete_documents_v1_collections_collection_identifier_documents_batch_delete(collection_identifier="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `collection_identifier`                                                                                                                                                               | *str*                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                    | The ID of the collection                                                                                                                                                              |
| `x_namespace`                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint. |
| `request_body`                                                                                                                                                                        | List[*str*]                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                    | N/A                                                                                                                                                                                   |
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