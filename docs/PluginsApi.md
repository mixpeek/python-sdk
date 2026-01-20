# mixpeek.PluginsApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**confirm_upload_plugins**](PluginsApi.md#confirm_upload_plugins) | **POST** /v1/plugins/uploads/{upload_id}/confirm | Confirm plugin upload
[**delete_plugin**](PluginsApi.md#delete_plugin) | **DELETE** /v1/plugins/{plugin_id} | Delete a plugin
[**generate_upload_url_plugins**](PluginsApi.md#generate_upload_url_plugins) | **POST** /v1/plugins/uploads | Generate presigned URL for plugin upload
[**get_plugin**](PluginsApi.md#get_plugin) | **GET** /v1/plugins/{plugin_id} | Get plugin details
[**list_plugins**](PluginsApi.md#list_plugins) | **GET** /v1/plugins | List plugins in organization


# **confirm_upload_plugins**
> ConfirmPluginUploadResponse confirm_upload_plugins(upload_id, authorization=authorization, confirm_plugin_upload_request=confirm_plugin_upload_request)

Confirm plugin upload

Confirm a plugin upload after the archive has been uploaded to S3.

**IMPORTANT:** This endpoint MUST be called after uploading to the presigned URL.
S3 presigned URLs have no callback mechanism, so the API cannot detect when
your upload completes. You must explicitly confirm to:
- Verify the file exists in S3
- Validate archive structure (manifest.py, pipeline.py required)
- Run security scan (see POST /plugins/uploads for security requirements)
- Create the plugin record

**Optional integrity checks:**
- `etag`: S3 ETag from upload response header (recommended)
- `file_size_bytes`: Expected file size for validation

**On Success:**
- Plugin is created with organization scope
- Returns plugin_id and feature_uri for use in collections

**On Security Violation:**
- Returns 400 with list of violations (file, line, column, message)
- Common issues: forbidden imports (subprocess, ctypes), forbidden builtins (eval, exec, open)
- See POST /plugins/uploads documentation for full list of security requirements

### Example


```python
import mixpeek
from mixpeek.models.confirm_plugin_upload_request import ConfirmPluginUploadRequest
from mixpeek.models.confirm_plugin_upload_response import ConfirmPluginUploadResponse
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
    api_instance = mixpeek.PluginsApi(api_client)
    upload_id = 'upload_id_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    confirm_plugin_upload_request = mixpeek.ConfirmPluginUploadRequest() # ConfirmPluginUploadRequest |  (optional)

    try:
        # Confirm plugin upload
        api_response = api_instance.confirm_upload_plugins(upload_id, authorization=authorization, confirm_plugin_upload_request=confirm_plugin_upload_request)
        print("The response of PluginsApi->confirm_upload_plugins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->confirm_upload_plugins: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_id** | **str**|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **confirm_plugin_upload_request** | [**ConfirmPluginUploadRequest**](ConfirmPluginUploadRequest.md)|  | [optional] 

### Return type

[**ConfirmPluginUploadResponse**](ConfirmPluginUploadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Upload confirmed and plugin created |  -  |
**400** | Validation failed or upload expired |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Upload not found or S3 object missing |  -  |
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_plugin**
> ApiPluginsModelsPluginDeleteResponse delete_plugin(plugin_id, authorization=authorization)

Delete a plugin

Delete a custom plugin from the organization.

This will:
1. Delete the plugin archive from S3
2. Remove the plugin metadata from MongoDB

Note: If the plugin is deployed to any namespaces, you should undeploy it first.

### Example


```python
import mixpeek
from mixpeek.models.api_plugins_models_plugin_delete_response import ApiPluginsModelsPluginDeleteResponse
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
    api_instance = mixpeek.PluginsApi(api_client)
    plugin_id = 'plugin_id_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Delete a plugin
        api_response = api_instance.delete_plugin(plugin_id, authorization=authorization)
        print("The response of PluginsApi->delete_plugin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->delete_plugin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_id** | **str**|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**ApiPluginsModelsPluginDeleteResponse**](ApiPluginsModelsPluginDeleteResponse.md)

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
**404** | Plugin not found |  -  |
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_upload_url_plugins**
> ApiPluginsModelsPluginPresignedURLResponse generate_upload_url_plugins(api_plugins_models_create_plugin_upload_request, authorization=authorization)

Generate presigned URL for plugin upload

Generate a presigned URL for uploading a plugin archive directly to S3.

**This is the recommended upload method** - it avoids streaming large files
through the API server.

**Workflow:**
1. Call this endpoint with plugin metadata → Returns presigned_url + upload_id
2. PUT the plugin archive to presigned_url (Content-Type: application/zip)
3. Call POST /plugins/uploads/{upload_id}/confirm to validate and create plugin

**Requirements:**
- Plugin name+version must not already exist in the organization
- Archive must be .zip format containing manifest.py and pipeline.py
  (Ray Serve working_dir only supports .zip for remote URIs)

**Response:**
- `upload_id`: Use this when confirming the upload
- `presigned_url`: PUT your .zip archive to this URL
- `expires_at`: URL expires after this time (default: 1 hour)

---

## Plugin Security Requirements

Plugins are scanned for security violations before upload is confirmed.
The following restrictions apply to all Python code in your plugin.

### Allowed Imports (Recommended)

These libraries are safe to use in your plugins:

| Category | Libraries |
|----------|-----------|
| **Data Processing** | `numpy`, `pandas`, `polars`, `pyarrow` |
| **ML/AI** | `torch`, `transformers`, `sentence_transformers`, `onnxruntime`, `safetensors` |
| **Image Processing** | `PIL`/`pillow`, `cv2`/`opencv-python`, `imageio` |
| **Audio/Video** | `librosa`, `soundfile`, `ffmpeg-python` |
| **HTTP Clients** | `requests`, `httpx`, `aiohttp` |
| **Utilities** | `json`, `re`, `typing`, `dataclasses`, `pydantic`, `logging` |
| **Mixpeek SDK** | `shared.models.loader.load_namespace_model` |

### Forbidden Imports (Will Fail Validation)

These imports are blocked for security reasons:

| Category | Blocked |
|----------|---------|
| **Process Execution** | `subprocess`, `os.system`, `os.popen`, `os.spawn*`, `os.exec*` |
| **Low-level Access** | `ctypes`, `pty`, `fcntl`, `resource` |
| **Concurrency** | `multiprocessing`, `threading` (use Ray instead) |
| **Network** | `socket` (use `requests`/`httpx` instead) |
| **Legacy** | `commands`, `popen2` |

### Forbidden Builtins (Will Fail Validation)

These built-in functions cannot be used:

- `eval()`, `exec()`, `compile()` - Dynamic code execution
- `open()` - Direct file access (use provided APIs)
- `__import__()` - Dynamic imports
- `globals()`, `locals()`, `vars()` - Namespace manipulation
- `getattr()`, `setattr()`, `delattr()`, `hasattr()` - Attribute manipulation

### Forbidden Module Functions

| Module | Blocked Functions |
|--------|-------------------|
| `os` | `system`, `popen`, `spawn`, `exec`, `fork`, `kill`, `killpg` |
| `importlib` | `import_module`, `__import__` |
| `pickle` | `loads`, `load` (arbitrary code execution risk) |
| `marshal` | `loads`, `load` |

### Warning Patterns (May Fail in Strict Mode)

These patterns generate warnings:
- `pickle`, `marshal`, `shelve` usage
- Dunder attribute access: `__builtins__`, `__class__`, `__bases__`, `__subclasses__`, `__mro__`, `__code__`, `__globals__`

### Example


```python
import mixpeek
from mixpeek.models.api_plugins_models_create_plugin_upload_request import ApiPluginsModelsCreatePluginUploadRequest
from mixpeek.models.api_plugins_models_plugin_presigned_url_response import ApiPluginsModelsPluginPresignedURLResponse
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
    api_instance = mixpeek.PluginsApi(api_client)
    api_plugins_models_create_plugin_upload_request = mixpeek.ApiPluginsModelsCreatePluginUploadRequest() # ApiPluginsModelsCreatePluginUploadRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Generate presigned URL for plugin upload
        api_response = api_instance.generate_upload_url_plugins(api_plugins_models_create_plugin_upload_request, authorization=authorization)
        print("The response of PluginsApi->generate_upload_url_plugins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->generate_upload_url_plugins: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_plugins_models_create_plugin_upload_request** | [**ApiPluginsModelsCreatePluginUploadRequest**](ApiPluginsModelsCreatePluginUploadRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**ApiPluginsModelsPluginPresignedURLResponse**](ApiPluginsModelsPluginPresignedURLResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Presigned URL generated successfully |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**409** | Plugin already exists |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plugin**
> ApiPluginsModelsPluginDetailResponse get_plugin(plugin_id, authorization=authorization)

Get plugin details

Get detailed information about a specific plugin.

### Example


```python
import mixpeek
from mixpeek.models.api_plugins_models_plugin_detail_response import ApiPluginsModelsPluginDetailResponse
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
    api_instance = mixpeek.PluginsApi(api_client)
    plugin_id = 'plugin_id_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Get plugin details
        api_response = api_instance.get_plugin(plugin_id, authorization=authorization)
        print("The response of PluginsApi->get_plugin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->get_plugin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_id** | **str**|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**ApiPluginsModelsPluginDetailResponse**](ApiPluginsModelsPluginDetailResponse.md)

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
**404** | Plugin not found |  -  |
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_plugins**
> ApiPluginsModelsPluginListResponse list_plugins(authorization=authorization)

List plugins in organization

List all custom plugins uploaded to the organization.

These plugins are available to all namespaces within the organization.

### Example


```python
import mixpeek
from mixpeek.models.api_plugins_models_plugin_list_response import ApiPluginsModelsPluginListResponse
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
    api_instance = mixpeek.PluginsApi(api_client)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # List plugins in organization
        api_response = api_instance.list_plugins(authorization=authorization)
        print("The response of PluginsApi->list_plugins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->list_plugins: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**ApiPluginsModelsPluginListResponse**](ApiPluginsModelsPluginListResponse.md)

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

