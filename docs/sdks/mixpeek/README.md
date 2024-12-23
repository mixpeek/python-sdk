# Mixpeek SDK

## Overview

Mixpeek API: This is the Mixpeek API, providing access to various endpoints for data processing and retrieval.

### Available Operations

* [debug_openapi_debug_openapi_get](#debug_openapi_debug_openapi_get) - Debug Openapi

## debug_openapi_debug_openapi_get

Debug Openapi

### Example Usage

```python
from mixpeek import Mixpeek

with Mixpeek() as mixpeek:

    res = mixpeek.debug_openapi_debug_openapi_get()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |