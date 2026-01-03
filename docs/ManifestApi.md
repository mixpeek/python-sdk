# mixpeek.ManifestApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_manifest**](ManifestApi.md#apply_manifest) | **POST** /v1/manifest/apply | Apply Manifest
[**diff_manifest**](ManifestApi.md#diff_manifest) | **POST** /v1/manifest/diff | Diff Manifest
[**export_manifest_get**](ManifestApi.md#export_manifest_get) | **GET** /v1/manifest/export | Export Manifest Get
[**export_manifest_post**](ManifestApi.md#export_manifest_post) | **POST** /v1/manifest/export | Export Manifest Post
[**generate_manifest**](ManifestApi.md#generate_manifest) | **POST** /v1/manifest/generate | Generate Manifest
[**validate_manifest**](ManifestApi.md#validate_manifest) | **POST** /v1/manifest/validate | Validate Manifest


# **apply_manifest**
> ApplyResult apply_manifest(manifest_file, dry_run=dry_run, authorization=authorization)

Apply Manifest

Apply a YAML manifest to create resources.

Creates all resources defined in the manifest file in dependency order.
Fails if any resource already exists (create-only mode).
Performs automatic rollback if any resource creation fails.

**Features:**
- Topological sorting ensures resources are created in correct dependency order
- Secret references (`${{ secrets.NAME }}`) are resolved from organization secrets
- Atomic operation: rolls back all created resources if any creation fails
- Dry run mode validates the manifest without making changes

**Example:**
```bash
curl -X POST /v1/manifest/apply \
  -H "Authorization: Bearer $API_KEY" \
  -H "X-Namespace-Id: ns_xxx" \
  -F "manifest_file=@mixpeek.yaml"
```

**Example manifest:**
```yaml
version: "1.0"
metadata:
  name: "my-environment"

namespaces:
  - name: video_search
    feature_extractors:
      - name: multimodal_extractor
        version: v1

buckets:
  - name: raw_videos
    namespace: video_search
    schema:
      properties:
        video: { type: video }
```

### Example


```python
import mixpeek
from mixpeek.models.apply_result import ApplyResult
from mixpeek.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mixpeek.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mixpeek.Configuration(
    host = "https://api.mixpeek.com"
)


# Enter a context with an instance of the API client
with mixpeek.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mixpeek.ManifestApi(api_client)
    manifest_file = None # bytearray | YAML manifest file
    dry_run = False # bool | Validate only, don't create resources (optional) (default to False)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Apply Manifest
        api_response = api_instance.apply_manifest(manifest_file, dry_run=dry_run, authorization=authorization)
        print("The response of ManifestApi->apply_manifest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManifestApi->apply_manifest: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manifest_file** | **bytearray**| YAML manifest file | 
 **dry_run** | **bool**| Validate only, don&#39;t create resources | [optional] [default to False]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**ApplyResult**](ApplyResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **diff_manifest**
> DiffResult diff_manifest(manifest_file, authorization=authorization)

Diff Manifest

Compare a manifest file with current state.

Shows resources that would be:
- **Created**: In manifest but not in system
- **In system only**: In system but not in manifest
- **Different**: In both but with configuration differences

This is useful for understanding what changes would occur
before applying a manifest.

**Example:**
```bash
curl -X POST /v1/manifest/diff \
  -H "Authorization: Bearer $API_KEY" \
  -F "manifest_file=@mixpeek.yaml"
```

### Example


```python
import mixpeek
from mixpeek.models.diff_result import DiffResult
from mixpeek.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mixpeek.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mixpeek.Configuration(
    host = "https://api.mixpeek.com"
)


# Enter a context with an instance of the API client
with mixpeek.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mixpeek.ManifestApi(api_client)
    manifest_file = None # bytearray | YAML manifest file
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Diff Manifest
        api_response = api_instance.diff_manifest(manifest_file, authorization=authorization)
        print("The response of ManifestApi->diff_manifest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManifestApi->diff_manifest: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manifest_file** | **bytearray**| YAML manifest file | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**DiffResult**](DiffResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_manifest_get**
> object export_manifest_get(namespace_id=namespace_id, format=format, manifest_name=manifest_name, authorization=authorization)

Export Manifest Get

Export current resources to a YAML manifest.

Exports all resources (or a specific namespace) to a YAML file
that can be version-controlled and re-applied to another environment.

**Features:**
- Resource IDs are converted to human-readable names
- Secret values are replaced with placeholder references (`${{ secrets.NAME }}`)
- Output is formatted for readability and git-friendliness

**Note:** You must configure actual secrets before applying the exported
manifest to a new environment.

**Example:**
```bash
# Export all resources
curl /v1/manifest/export \
  -H "Authorization: Bearer $API_KEY" \
  -o mixpeek.yaml

# Export specific namespace
curl "/v1/manifest/export?namespace_id=ns_abc123" \
  -H "Authorization: Bearer $API_KEY" \
  -o namespace.yaml
```

### Example


```python
import mixpeek
from mixpeek.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mixpeek.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mixpeek.Configuration(
    host = "https://api.mixpeek.com"
)


# Enter a context with an instance of the API client
with mixpeek.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mixpeek.ManifestApi(api_client)
    namespace_id = 'namespace_id_example' # str | Export specific namespace (None = all) (optional)
    format = 'yaml' # str | Output format (yaml) (optional) (default to 'yaml')
    manifest_name = 'exported-manifest' # str | Name for the manifest (optional) (default to 'exported-manifest')
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Export Manifest Get
        api_response = api_instance.export_manifest_get(namespace_id=namespace_id, format=format, manifest_name=manifest_name, authorization=authorization)
        print("The response of ManifestApi->export_manifest_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManifestApi->export_manifest_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_id** | **str**| Export specific namespace (None &#x3D; all) | [optional] 
 **format** | **str**| Output format (yaml) | [optional] [default to &#39;yaml&#39;]
 **manifest_name** | **str**| Name for the manifest | [optional] [default to &#39;exported-manifest&#39;]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_manifest_post**
> object export_manifest_post(manifest_name=manifest_name, authorization=authorization, request_body=request_body)

Export Manifest Post

Export current resources to a YAML manifest (POST version for agent tools).

Same as GET /export but accepts parameters in JSON body instead of query params.
Used by agent tools and programmatic API clients.

**Example:**
```bash
curl -X POST /v1/manifest/export \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"namespace_ids": ["ns_abc123"], "manifest_name": "my-setup"}'
```

### Example


```python
import mixpeek
from mixpeek.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mixpeek.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mixpeek.Configuration(
    host = "https://api.mixpeek.com"
)


# Enter a context with an instance of the API client
with mixpeek.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mixpeek.ManifestApi(api_client)
    manifest_name = 'exported-manifest' # str |  (optional) (default to 'exported-manifest')
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    request_body = ['request_body_example'] # List[str] |  (optional)

    try:
        # Export Manifest Post
        api_response = api_instance.export_manifest_post(manifest_name=manifest_name, authorization=authorization, request_body=request_body)
        print("The response of ManifestApi->export_manifest_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManifestApi->export_manifest_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manifest_name** | **str**|  | [optional] [default to &#39;exported-manifest&#39;]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **request_body** | [**List[str]**](str.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_manifest**
> object generate_manifest(description, manifest_name=manifest_name, authorization=authorization)

Generate Manifest

Generate a manifest from natural language description.

    Uses AI to create a valid YAML manifest from a natural language description
    of desired resources. The generated manifest can be reviewed and applied.

    **Example:**
    ```bash
    curl -X POST /v1/manifest/generate \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "description": "I need a bucket of images that feeds into a multimodal extractor and a retriever",
        "manifest_name": "image-search-setup"
      }'
    ```

    **Response:**
    ```json
    {
      "manifest": "version: '1.0'
metadata:
  name: image-search-setup
...",
      "format": "yaml",
      "manifest_name": "image-search-setup",
      "description": "I need a bucket of images..."
    }
    ```

    **Next Steps:**
    1. Review the generated manifest
    2. Apply it using POST /v1/manifest/apply

### Example


```python
import mixpeek
from mixpeek.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mixpeek.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mixpeek.Configuration(
    host = "https://api.mixpeek.com"
)


# Enter a context with an instance of the API client
with mixpeek.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mixpeek.ManifestApi(api_client)
    description = 'description_example' # str | 
    manifest_name = 'generated-manifest' # str |  (optional) (default to 'generated-manifest')
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Generate Manifest
        api_response = api_instance.generate_manifest(description, manifest_name=manifest_name, authorization=authorization)
        print("The response of ManifestApi->generate_manifest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManifestApi->generate_manifest: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str**|  | 
 **manifest_name** | **str**|  | [optional] [default to &#39;generated-manifest&#39;]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_manifest**
> ValidateResult validate_manifest(manifest_file, authorization=authorization)

Validate Manifest

Validate a YAML manifest without applying.

Checks:
- YAML syntax validity
- Schema validation against manifest models
- Cross-resource reference validation
- Dependency resolution (no circular dependencies)
- Secret reference existence

Returns detailed validation results including:
- Resource counts by type
- Missing secrets that need to be configured
- Validation errors and warnings

**Example:**
```bash
curl -X POST /v1/manifest/validate \
  -H "Authorization: Bearer $API_KEY" \
  -F "manifest_file=@mixpeek.yaml"
```

### Example


```python
import mixpeek
from mixpeek.models.validate_result import ValidateResult
from mixpeek.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mixpeek.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mixpeek.Configuration(
    host = "https://api.mixpeek.com"
)


# Enter a context with an instance of the API client
with mixpeek.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mixpeek.ManifestApi(api_client)
    manifest_file = None # bytearray | YAML manifest file
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Validate Manifest
        api_response = api_instance.validate_manifest(manifest_file, authorization=authorization)
        print("The response of ManifestApi->validate_manifest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManifestApi->validate_manifest: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manifest_file** | **bytearray**| YAML manifest file | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**ValidateResult**](ValidateResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

