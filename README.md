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
  * [Debugging](#debugging)
* [Development](#development)
  * [Maturity](#maturity)
  * [Contributions](#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

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
) as mixpeek:

    res = mixpeek.health.check()

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
    ) as mixpeek:

        res = await mixpeek.health.check_async()

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
) as mixpeek:

    res = mixpeek.health.check()

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [assets](docs/sdks/assets/README.md)

* [get_asset_v1_assets_asset_id_get](docs/sdks/assets/README.md#get_asset_v1_assets_asset_id_get) - Get Asset
* [delete_asset_v1_assets_asset_id_delete](docs/sdks/assets/README.md#delete_asset_v1_assets_asset_id_delete) - Delete Asset
* [full_asset_update_v1_assets_asset_id_put](docs/sdks/assets/README.md#full_asset_update_v1_assets_asset_id_put) - Full Asset Update
* [partial_asset_update_v1_assets_asset_id_patch](docs/sdks/assets/README.md#partial_asset_update_v1_assets_asset_id_patch) - Partial Asset Update
* [get_asset_with_features_v1_assets_asset_id_features_get](docs/sdks/assets/README.md#get_asset_with_features_v1_assets_asset_id_features_get) - Get Asset With Features
* [list_assets_v1_assets_post](docs/sdks/assets/README.md#list_assets_v1_assets_post) - List Assets
* [search_assets_v1_assets_search_post](docs/sdks/assets/README.md#search_assets_v1_assets_search_post) - Search Assets

### [collections](docs/sdks/collections/README.md)

* [list_collections_v1_collections_get](docs/sdks/collections/README.md#list_collections_v1_collections_get) - List Collections
* [create_collection_v1_collections_post](docs/sdks/collections/README.md#create_collection_v1_collections_post) - Create Collection
* [delete_collection_v1_collections_collection_delete](docs/sdks/collections/README.md#delete_collection_v1_collections_collection_delete) - Delete Collection
* [update_collection_v1_collections_collection_put](docs/sdks/collections/README.md#update_collection_v1_collections_collection_put) - Update Collection
* [get_collection_v1_collections_collection_get](docs/sdks/collections/README.md#get_collection_v1_collections_collection_get) - Get Collection

### [feature_extractors](docs/sdks/featureextractors/README.md)

* [extract_embeddings_v1_features_extractors_embed_post](docs/sdks/featureextractors/README.md#extract_embeddings_v1_features_extractors_embed_post) - Extract Embeddings

### [feature_search](docs/sdks/featuresearch/README.md)

* [search_features_v1_features_search_post](docs/sdks/featuresearch/README.md#search_features_v1_features_search_post) - Search Features

### [features](docs/sdks/features/README.md)

* [get_feature_v1_features_feature_id_get](docs/sdks/features/README.md#get_feature_v1_features_feature_id_get) - Get Feature
* [delete_feature_v1_features_feature_id_delete](docs/sdks/features/README.md#delete_feature_v1_features_feature_id_delete) - Delete Feature
* [full_feature_update_v1_features_feature_id_put](docs/sdks/features/README.md#full_feature_update_v1_features_feature_id_put) - Full Feature Update
* [list_features_v1_features_post](docs/sdks/features/README.md#list_features_v1_features_post) - List Features

### [health](docs/sdks/health/README.md)

* [check](docs/sdks/health/README.md#check) - Healthcheck

### [ingest_assets](docs/sdks/ingestassets/README.md)

* [ingest_text_v1_ingest_text_post](docs/sdks/ingestassets/README.md#ingest_text_v1_ingest_text_post) - Ingest Text
* [ingest_video_url_v1_ingest_videos_url_post](docs/sdks/ingestassets/README.md#ingest_video_url_v1_ingest_videos_url_post) - Ingest Video Url
* [ingest_image_url_v1_ingest_images_url_post](docs/sdks/ingestassets/README.md#ingest_image_url_v1_ingest_images_url_post) - Ingest Image Url


### [namespaces](docs/sdks/namespaces/README.md)

* [create_namespace_v1_namespaces_post](docs/sdks/namespaces/README.md#create_namespace_v1_namespaces_post) - Create Namespace
* [list_namespaces_v1_namespaces_get](docs/sdks/namespaces/README.md#list_namespaces_v1_namespaces_get) - List Namespaces
* [delete_namespace_v1_namespaces_namespace_delete](docs/sdks/namespaces/README.md#delete_namespace_v1_namespaces_namespace_delete) - Delete Namespace
* [update_namespace_v1_namespaces_namespace_put](docs/sdks/namespaces/README.md#update_namespace_v1_namespaces_namespace_put) - Update Namespace
* [get_namespace_v1_namespaces_namespace_get](docs/sdks/namespaces/README.md#get_namespace_v1_namespaces_namespace_get) - Get Namespace
* [list_available_models_v1_namespaces_models_get](docs/sdks/namespaces/README.md#list_available_models_v1_namespaces_models_get) - List Available Models

### [organizations](docs/sdks/organizations/README.md)

* [get_organization_v1_organizations_get](docs/sdks/organizations/README.md#get_organization_v1_organizations_get) - Get Organization
* [get_usage_v1_organizations_usage_get](docs/sdks/organizations/README.md#get_usage_v1_organizations_usage_get) - Get Usage
* [get_user_v1_organizations_users_user_email_get](docs/sdks/organizations/README.md#get_user_v1_organizations_users_user_email_get) - Get User
* [delete_user_v1_organizations_users_user_email_delete](docs/sdks/organizations/README.md#delete_user_v1_organizations_users_user_email_delete) - Delete User
* [add_user_v1_organizations_users_post](docs/sdks/organizations/README.md#add_user_v1_organizations_users_post) - Add User
* [create_api_key_v1_organizations_users_user_email_api_keys_post](docs/sdks/organizations/README.md#create_api_key_v1_organizations_users_user_email_api_keys_post) - Create Api Key
* [delete_api_key_v1_organizations_users_user_email_api_keys_key_name_delete](docs/sdks/organizations/README.md#delete_api_key_v1_organizations_users_user_email_api_keys_key_name_delete) - Delete Api Key
* [update_api_key_v1_organizations_users_user_email_api_keys_key_name_patch](docs/sdks/organizations/README.md#update_api_key_v1_organizations_users_user_email_api_keys_key_name_patch) - Update Api Key

### [tasks](docs/sdks/tasks/README.md)

* [kill_task_v1_tasks_task_id_delete](docs/sdks/tasks/README.md#kill_task_v1_tasks_task_id_delete) - Kill Task
* [get_task_v1_tasks_task_id_get](docs/sdks/tasks/README.md#get_task_v1_tasks_task_id_get) - Get Task Information
* [list_active_tasks_v1_tasks_get](docs/sdks/tasks/README.md#list_active_tasks_v1_tasks_get) - List Active Tasks

### [taxonomy_entities](docs/sdks/taxonomyentities/README.md)

* [create_taxonomy_v1_entities_taxonomies_post](docs/sdks/taxonomyentities/README.md#create_taxonomy_v1_entities_taxonomies_post) - Create Taxonomy
* [list_taxonomies_v1_entities_taxonomies_get](docs/sdks/taxonomyentities/README.md#list_taxonomies_v1_entities_taxonomies_get) - List Taxonomies
* [get_taxonomy_v1_entities_taxonomies_taxonomy_get](docs/sdks/taxonomyentities/README.md#get_taxonomy_v1_entities_taxonomies_taxonomy_get) - Get Taxonomy
* [delete_taxonomy_v1_entities_taxonomies_taxonomy_delete](docs/sdks/taxonomyentities/README.md#delete_taxonomy_v1_entities_taxonomies_taxonomy_delete) - Delete Taxonomy
* [update_taxonomy_v1_entities_taxonomies_taxonomy_patch](docs/sdks/taxonomyentities/README.md#update_taxonomy_v1_entities_taxonomies_taxonomy_patch) - Update Taxonomy
* [get_taxonomy_node_v1_entities_taxonomies_nodes_node_get](docs/sdks/taxonomyentities/README.md#get_taxonomy_node_v1_entities_taxonomies_nodes_node_get) - Get Taxonomy Node
* [update_node_v1_entities_taxonomies_nodes_node_patch](docs/sdks/taxonomyentities/README.md#update_node_v1_entities_taxonomies_nodes_node_patch) - Update Node
* [classify_features_v1_entities_taxonomies_taxonomy_classify_post](docs/sdks/taxonomyentities/README.md#classify_features_v1_entities_taxonomies_taxonomy_classify_post) - Classify Features against Taxonomy
* [list_classifications_v1_entities_taxonomies_taxonomy_classifications_post](docs/sdks/taxonomyentities/README.md#list_classifications_v1_entities_taxonomies_taxonomy_classifications_post) - List Taxonomy Classifications
* [delete_classifications_v1_entities_taxonomies_taxonomy_classifications_classification_id_delete](docs/sdks/taxonomyentities/README.md#delete_classifications_v1_entities_taxonomies_taxonomy_classifications_classification_id_delete) - Delete Classifications

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
) as mixpeek:

    res = mixpeek.health.check(,
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
) as mixpeek:

    res = mixpeek.health.check()

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

When custom error responses are specified for an operation, the SDK may also raise their associated exceptions. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `get_organization_v1_organizations_get_async` method may raise the following exceptions:

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
) as mixpeek:
    res = None
    try:

        res = mixpeek.organizations.get_organization_v1_organizations_get()

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

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from mixpeek import Mixpeek
import os

with Mixpeek(
    server_url="https://api.mixpeek.com",
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as mixpeek:

    res = mixpeek.health.check()

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
