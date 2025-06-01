# mixpeek

Developer-friendly & type-safe Python SDK specifically catered to leverage *mixpeek* API.

<!-- Start Summary [summary] -->
## Summary

Mixpeek API: This is the Mixpeek API, providing access to various endpoints for data processing and retrieval.
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [mixpeek](#mixpeek)
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Authentication](#authentication)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)
* [Development](#development)
  * [Maturity](#maturity)
  * [Contributions](#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install mixpeek
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add mixpeek
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from mixpeek python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "mixpeek",
# ]
# ///

from mixpeek import Mixpeek

sdk = Mixpeek(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.health.check()

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from mixpeek import Mixpeek
import os

async def main():

    async with Mixpeek(
        token=os.getenv("MIXPEEK_TOKEN", ""),
    ) as m_client:

        res = await m_client.health.check_async()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name    | Type | Scheme      | Environment Variable |
| ------- | ---- | ----------- | -------------------- |
| `token` | http | HTTP Bearer | `MIXPEEK_TOKEN`      |

To authenticate with the API the `token` parameter must be set when initializing the SDK client instance. For example:
```python
from mixpeek import Mixpeek
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.health.check()

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [bucket_objects](docs/sdks/bucketobjects/README.md)

* [create](docs/sdks/bucketobjects/README.md#create) - Create Object
* [get](docs/sdks/bucketobjects/README.md#get) - Get Object
* [update](docs/sdks/bucketobjects/README.md#update) - Update Object
* [delete](docs/sdks/bucketobjects/README.md#delete) - Delete Object
* [list](docs/sdks/bucketobjects/README.md#list) - List Objects

### [buckets](docs/sdks/buckets/README.md)

* [create](docs/sdks/buckets/README.md#create) - Create Bucket
* [get](docs/sdks/buckets/README.md#get) - Get Bucket
* [update](docs/sdks/buckets/README.md#update) - Update Bucket
* [delete](docs/sdks/buckets/README.md#delete) - Delete Bucket
* [list](docs/sdks/buckets/README.md#list) - List Buckets

### [clusters](docs/sdks/clusters/README.md)

* [create](docs/sdks/clusters/README.md#create) - Create Cluster

### [collection_cache](docs/sdks/collectioncache/README.md)

* [invalidate](docs/sdks/collectioncache/README.md#invalidate) - Invalidate Cache
* [get_stats](docs/sdks/collectioncache/README.md#get_stats) - Get Cache Stats
* [cleanup](docs/sdks/collectioncache/README.md#cleanup) - Cleanup Cache

### [collections](docs/sdks/collections/README.md)

* [create](docs/sdks/collections/README.md#create) - Create Collection
* [get](docs/sdks/collections/README.md#get) - Get Collection

### [features](docs/sdks/features/README.md)

* [list_extractors](docs/sdks/features/README.md#list_extractors) - List Feature Extractors
* [get_extractor](docs/sdks/features/README.md#get_extractor) - Get Feature Extractor Details

### [health](docs/sdks/health/README.md)

* [check](docs/sdks/health/README.md#check) - Healthcheck


### [namespaces](docs/sdks/namespaces/README.md)

* [create](docs/sdks/namespaces/README.md#create) - Create Namespace
* [list](docs/sdks/namespaces/README.md#list) - List Namespaces
* [delete](docs/sdks/namespaces/README.md#delete) - Delete Namespace
* [update](docs/sdks/namespaces/README.md#update) - Update Namespace
* [get](docs/sdks/namespaces/README.md#get) - Get Namespace

### [organization_notifications](docs/sdks/organizationnotifications/README.md)

* [send](docs/sdks/organizationnotifications/README.md#send) - Send Notification

### [organizations](docs/sdks/organizations/README.md)

* [get](docs/sdks/organizations/README.md#get) - Get Organization
* [add_user](docs/sdks/organizations/README.md#add_user) - Add User
* [delete_api_key](docs/sdks/organizations/README.md#delete_api_key) - Delete Api Key
* [update_api_key](docs/sdks/organizations/README.md#update_api_key) - Update Api Key

### [organizations_usage](docs/sdks/organizationsusage/README.md)

* [get](docs/sdks/organizationsusage/README.md#get) - Get Usage

### [research](docs/sdks/research/README.md)

* [get](docs/sdks/research/README.md#get) - Get Research

### [retriever_interactions](docs/sdks/retrieverinteractions/README.md)

* [create](docs/sdks/retrieverinteractions/README.md#create) - Create Interaction
* [list](docs/sdks/retrieverinteractions/README.md#list) - List Interactions
* [get](docs/sdks/retrieverinteractions/README.md#get) - Get Interaction
* [delete](docs/sdks/retrieverinteractions/README.md#delete) - Delete Interaction

### [retriever_stages](docs/sdks/retrieverstages/README.md)

* [list](docs/sdks/retrieverstages/README.md#list) - List Retriever Stages

### [retrievers](docs/sdks/retrievers/README.md)

* [create](docs/sdks/retrievers/README.md#create) - Create Retriever
* [get](docs/sdks/retrievers/README.md#get) - Get Retriever
* [execute](docs/sdks/retrievers/README.md#execute) - Execute Retriever

### [tasks](docs/sdks/tasks/README.md)

* [delete](docs/sdks/tasks/README.md#delete) - Kill Task
* [get](docs/sdks/tasks/README.md#get) - Get Task Information
* [list_active](docs/sdks/tasks/README.md#list_active) - List Active Tasks

### [taxonomies](docs/sdks/taxonomies/README.md)

* [create](docs/sdks/taxonomies/README.md#create) - Create Taxonomy

### [users](docs/sdks/users/README.md)

* [get](docs/sdks/users/README.md#get) - Get User
* [delete](docs/sdks/users/README.md#delete) - Delete User
* [create_api_key](docs/sdks/users/README.md#create_api_key) - Create Api Key

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from mixpeek import Mixpeek
from mixpeek.utils import BackoffStrategy, RetryConfig
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.health.check(,
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from mixpeek import Mixpeek
from mixpeek.utils import BackoffStrategy, RetryConfig
import os


with Mixpeek(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.health.check()

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations. All operations return a response object or raise an exception.

By default, an API error will raise a models.APIError exception, which has the following properties:

| Property        | Type             | Description           |
|-----------------|------------------|-----------------------|
| `.status_code`  | *int*            | The HTTP status code  |
| `.message`      | *str*            | The error message     |
| `.raw_response` | *httpx.Response* | The raw HTTP response |
| `.body`         | *str*            | The response content  |

When custom error responses are specified for an operation, the SDK may also raise their associated exceptions. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `get_async` method may raise the following exceptions:

| Error Type                 | Status Code        | Content Type     |
| -------------------------- | ------------------ | ---------------- |
| models.ErrorResponse       | 400, 401, 403, 404 | application/json |
| models.HTTPValidationError | 422                | application/json |
| models.ErrorResponse       | 500                | application/json |
| models.APIError            | 4XX, 5XX           | \*/\*            |

### Example

```python
from mixpeek import Mixpeek, models
import os


with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:
    res = None
    try:

        res = m_client.organizations.get()

        # Handle response
        print(res)

    except models.ErrorResponse as e:
        # handle e.data: models.ErrorResponseData
        raise(e)
    except models.HTTPValidationError as e:
        # handle e.data: models.HTTPValidationErrorData
        raise(e)
    except models.ErrorResponse as e:
        # handle e.data: models.ErrorResponseData
        raise(e)
    except models.APIError as e:
        # handle exception
        raise(e)
```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Override Server URL Per-Client

The default server can be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from mixpeek import Mixpeek
import os


with Mixpeek(
    server_url="https://api.mixpeek.com",
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as m_client:

    res = m_client.health.check()

    # Handle response
    print(res)

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from mixpeek import Mixpeek
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Mixpeek(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from mixpeek import Mixpeek
from mixpeek.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = Mixpeek(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `Mixpeek` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from mixpeek import Mixpeek
import os
def main():

    with Mixpeek(
        token=os.getenv("MIXPEEK_TOKEN", ""),
    ) as m_client:
        # Rest of application here...


# Or when using async:
async def amain():

    async with Mixpeek(
        token=os.getenv("MIXPEEK_TOKEN", ""),
    ) as m_client:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from mixpeek import Mixpeek
import logging

logging.basicConfig(level=logging.DEBUG)
s = Mixpeek(debug_logger=logging.getLogger("mixpeek"))
```

You can also enable a default debug logger by setting an environment variable `MIXPEEK_DEBUG` to true.
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=mixpeek&utm_campaign=python)
