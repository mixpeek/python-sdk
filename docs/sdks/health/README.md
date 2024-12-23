# Health
(*health*)

## Overview

### Available Operations

* [check](#check) - Healthcheck

## check

Healthcheck

### Example Usage

```python
from mixpeek import Mixpeek
import os

with Mixpeek(
    bearer_auth=os.getenv("MIXPEEK_BEARER_AUTH", ""),
) as mixpeek:

    res = mixpeek.health.check()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.HealthCheckResponse](../../models/healthcheckresponse.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.ErrorResponse    | 400, 401, 403, 404, 500 | application/json        |
| models.APIError         | 4XX, 5XX                | \*/\*                   |