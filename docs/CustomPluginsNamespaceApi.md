# mixpeek.CustomPluginsNamespaceApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**confirm_upload_namespaces_id_plugins**](CustomPluginsNamespaceApi.md#confirm_upload_namespaces_id_plugins) | **POST** /v1/namespaces/{namespace_id}/plugins/uploads/{upload_id}/confirm | Confirm plugin upload
[**delete_plugin_namespaces**](CustomPluginsNamespaceApi.md#delete_plugin_namespaces) | **DELETE** /v1/namespaces/{namespace_id}/plugins/{plugin_id} | Delete a plugin
[**deploy_plugin_namespaces**](CustomPluginsNamespaceApi.md#deploy_plugin_namespaces) | **POST** /v1/namespaces/{namespace_id}/plugins/{plugin_id}/deploy | Deploy or redeploy a plugin
[**disable_org_plugin_namespaces**](CustomPluginsNamespaceApi.md#disable_org_plugin_namespaces) | **POST** /v1/namespaces/{namespace_id}/plugins/org/{plugin_id}/disable | Disable org plugin for namespace
[**enable_org_plugin_namespaces**](CustomPluginsNamespaceApi.md#enable_org_plugin_namespaces) | **POST** /v1/namespaces/{namespace_id}/plugins/org/{plugin_id}/enable | Enable org plugin for namespace
[**generate_upload_url_namespaces_id_plugins**](CustomPluginsNamespaceApi.md#generate_upload_url_namespaces_id_plugins) | **POST** /v1/namespaces/{namespace_id}/plugins/uploads | Generate presigned URL for plugin upload
[**get_deployment_status_namespaces_id_plugins**](CustomPluginsNamespaceApi.md#get_deployment_status_namespaces_id_plugins) | **GET** /v1/namespaces/{namespace_id}/plugins/{plugin_id}/status | Get plugin deployment status
[**get_plugin_namespaces**](CustomPluginsNamespaceApi.md#get_plugin_namespaces) | **GET** /v1/namespaces/{namespace_id}/plugins/{plugin_id} | Get plugin details
[**list_available_org_plugins_namespaces**](CustomPluginsNamespaceApi.md#list_available_org_plugins_namespaces) | **GET** /v1/namespaces/{namespace_id}/plugins/available | List available org plugins
[**list_plugins_namespaces**](CustomPluginsNamespaceApi.md#list_plugins_namespaces) | **GET** /v1/namespaces/{namespace_id}/plugins | List plugins in namespace
[**undeploy_plugin_namespaces**](CustomPluginsNamespaceApi.md#undeploy_plugin_namespaces) | **POST** /v1/namespaces/{namespace_id}/plugins/{plugin_id}/undeploy | Undeploy a plugin
[**upload_plugin_namespaces**](CustomPluginsNamespaceApi.md#upload_plugin_namespaces) | **POST** /v1/namespaces/{namespace_id}/plugins | Upload a custom plugin


# **confirm_upload_namespaces_id_plugins**
> ConfirmPluginUploadResponse confirm_upload_namespaces_id_plugins(namespace_id, upload_id, authorization=authorization, confirm_plugin_upload_request=confirm_plugin_upload_request)

Confirm plugin upload

Confirm a plugin upload after the archive has been uploaded to S3.

**IMPORTANT:** This endpoint MUST be called after uploading to the presigned URL.
S3 presigned URLs have no callback mechanism, so the API cannot detect when
your upload completes. You must explicitly confirm to:
- Verify the file exists in S3
- Validate archive structure (manifest.py, pipeline.py required)
- Run security scan
- Create the plugin record
- Mark upload as COMPLETED

**Optional integrity checks:**
- `etag`: S3 ETag from upload response header (recommended)
- `file_size_bytes`: Expected file size for validation

**On Success:**
- Plugin is created with status "pending" deployment
- Returns plugin_id and feature_uri for use in collections

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
    api_instance = mixpeek.CustomPluginsNamespaceApi(api_client)
    namespace_id = 'namespace_id_example' # str | 
    upload_id = 'upload_id_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    confirm_plugin_upload_request = mixpeek.ConfirmPluginUploadRequest() # ConfirmPluginUploadRequest |  (optional)

    try:
        # Confirm plugin upload
        api_response = api_instance.confirm_upload_namespaces_id_plugins(namespace_id, upload_id, authorization=authorization, confirm_plugin_upload_request=confirm_plugin_upload_request)
        print("The response of CustomPluginsNamespaceApi->confirm_upload_namespaces_id_plugins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomPluginsNamespaceApi->confirm_upload_namespaces_id_plugins: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_id** | **str**|  | 
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

# **delete_plugin_namespaces**
> ApiNamespacesPluginsModelsPluginDeleteResponse delete_plugin_namespaces(namespace_id, plugin_id, authorization=authorization)

Delete a plugin

Delete a custom plugin from the namespace.

**Security:** Users can only delete plugins in their own namespace.

**What happens:**
1. If deployed (Enterprise): Queues Ray Serve deployment removal via blue-green rollout
2. Removes plugin from namespace's feature extractors
3. Deletes the plugin archive from S3
4. Removes the plugin metadata from MongoDB

**Response:**
- `deployment_removed`: True if a Ray Serve deployment was queued for removal
- Blue-green rollout completes within 5 minutes for deployed plugins

### Example


```python
import mixpeek
from mixpeek.models.api_namespaces_plugins_models_plugin_delete_response import ApiNamespacesPluginsModelsPluginDeleteResponse
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
    api_instance = mixpeek.CustomPluginsNamespaceApi(api_client)
    namespace_id = 'namespace_id_example' # str | 
    plugin_id = 'plugin_id_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Delete a plugin
        api_response = api_instance.delete_plugin_namespaces(namespace_id, plugin_id, authorization=authorization)
        print("The response of CustomPluginsNamespaceApi->delete_plugin_namespaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomPluginsNamespaceApi->delete_plugin_namespaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_id** | **str**|  | 
 **plugin_id** | **str**|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**ApiNamespacesPluginsModelsPluginDeleteResponse**](ApiNamespacesPluginsModelsPluginDeleteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plugin deleted successfully |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Plugin not found |  -  |
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deploy_plugin_namespaces**
> Dict[str, object] deploy_plugin_namespaces(namespace_id, plugin_id, authorization=authorization)

Deploy or redeploy a plugin

Deploy a plugin for use in the namespace.

**Deployment Types:**
- `batch_only`: All accounts - plugin available for batch processing
- `realtime`: Enterprise only - plugin deployed via Anyscale blue-green deployment

Plugins with `realtime.py` require dedicated infrastructure (Enterprise). They are
queued and rolled out via Anyscale's blue-green deployment. Non-enterprise accounts
can still use batch-only plugins and reference existing feature URIs.

**Response:**
- `status`: "queued", "deployed", or "batch_only"
- `deployment_type`: "batch_only" or "realtime"
- `route_prefix`: HTTP route for realtime plugins (Enterprise only)

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
    api_instance = mixpeek.CustomPluginsNamespaceApi(api_client)
    namespace_id = 'namespace_id_example' # str | 
    plugin_id = 'plugin_id_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Deploy or redeploy a plugin
        api_response = api_instance.deploy_plugin_namespaces(namespace_id, plugin_id, authorization=authorization)
        print("The response of CustomPluginsNamespaceApi->deploy_plugin_namespaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomPluginsNamespaceApi->deploy_plugin_namespaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_id** | **str**|  | 
 **plugin_id** | **str**|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plugin deployed successfully |  -  |
**400** | Plugin not validated |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Plugin not found |  -  |
**500** | Deployment failed |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_org_plugin_namespaces**
> DisableOrgPluginResponse disable_org_plugin_namespaces(namespace_id, plugin_id, authorization=authorization)

Disable org plugin for namespace

Disable an org-level plugin for this namespace.

This:
1. Removes the plugin from the namespace's feature_extractors array
2. Undeploys from Ray if deployed
3. Removes the namespace-specific plugin tracking record

**Warning:** Collections using this plugin may no longer function correctly.

### Example


```python
import mixpeek
from mixpeek.models.disable_org_plugin_response import DisableOrgPluginResponse
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
    api_instance = mixpeek.CustomPluginsNamespaceApi(api_client)
    namespace_id = 'namespace_id_example' # str | 
    plugin_id = 'plugin_id_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Disable org plugin for namespace
        api_response = api_instance.disable_org_plugin_namespaces(namespace_id, plugin_id, authorization=authorization)
        print("The response of CustomPluginsNamespaceApi->disable_org_plugin_namespaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomPluginsNamespaceApi->disable_org_plugin_namespaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_id** | **str**|  | 
 **plugin_id** | **str**|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**DisableOrgPluginResponse**](DisableOrgPluginResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plugin disabled successfully |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Org plugin not found |  -  |
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_org_plugin_namespaces**
> EnableOrgPluginResponse enable_org_plugin_namespaces(namespace_id, plugin_id, authorization=authorization, enable_org_plugin_request=enable_org_plugin_request)

Enable org plugin for namespace

Enable an org-level plugin for this namespace.

This:
1. Adds the plugin to the namespace's feature_extractors array
2. Optionally deploys the plugin to Ray (if deploy=True)

After enabling, the plugin can be used when creating collections in this namespace.

**Note:** The plugin must exist at the organization level (uploaded via POST /v1/plugins/uploads).

### Example


```python
import mixpeek
from mixpeek.models.enable_org_plugin_request import EnableOrgPluginRequest
from mixpeek.models.enable_org_plugin_response import EnableOrgPluginResponse
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
    api_instance = mixpeek.CustomPluginsNamespaceApi(api_client)
    namespace_id = 'namespace_id_example' # str | 
    plugin_id = 'plugin_id_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    enable_org_plugin_request = mixpeek.EnableOrgPluginRequest() # EnableOrgPluginRequest |  (optional)

    try:
        # Enable org plugin for namespace
        api_response = api_instance.enable_org_plugin_namespaces(namespace_id, plugin_id, authorization=authorization, enable_org_plugin_request=enable_org_plugin_request)
        print("The response of CustomPluginsNamespaceApi->enable_org_plugin_namespaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomPluginsNamespaceApi->enable_org_plugin_namespaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_id** | **str**|  | 
 **plugin_id** | **str**|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **enable_org_plugin_request** | [**EnableOrgPluginRequest**](EnableOrgPluginRequest.md)|  | [optional] 

### Return type

[**EnableOrgPluginResponse**](EnableOrgPluginResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plugin enabled successfully |  -  |
**400** | Plugin validation failed |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Org plugin not found |  -  |
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_upload_url_namespaces_id_plugins**
> ApiNamespacesPluginsModelsPluginPresignedURLResponse generate_upload_url_namespaces_id_plugins(namespace_id, api_namespaces_plugins_models_create_plugin_upload_request, authorization=authorization)

Generate presigned URL for plugin upload

Generate a presigned URL for uploading a plugin archive directly to S3.

**This is the recommended upload method** - it avoids streaming large files
through the API server.

**Availability:**
- All accounts can upload plugins for batch processing (default quota: 10 plugins)
- Enterprise accounts get higher quotas and realtime inference support

**Workflow:**
1. Call this endpoint with plugin metadata → Returns presigned_url + upload_id
2. PUT the plugin archive to presigned_url (Content-Type: application/zip)
3. Call POST /uploads/{upload_id}/confirm to validate and deploy

**Requirements:**
- Plugin name+version must not already exist
- Must be within plugin quota

**Response:**
- `upload_id`: Use this when confirming the upload
- `presigned_url`: PUT your .zip archive to this URL
- `expires_at`: URL expires after this time (default: 1 hour)

### Example


```python
import mixpeek
from mixpeek.models.api_namespaces_plugins_models_create_plugin_upload_request import ApiNamespacesPluginsModelsCreatePluginUploadRequest
from mixpeek.models.api_namespaces_plugins_models_plugin_presigned_url_response import ApiNamespacesPluginsModelsPluginPresignedURLResponse
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
    api_instance = mixpeek.CustomPluginsNamespaceApi(api_client)
    namespace_id = 'namespace_id_example' # str | 
    api_namespaces_plugins_models_create_plugin_upload_request = mixpeek.ApiNamespacesPluginsModelsCreatePluginUploadRequest() # ApiNamespacesPluginsModelsCreatePluginUploadRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Generate presigned URL for plugin upload
        api_response = api_instance.generate_upload_url_namespaces_id_plugins(namespace_id, api_namespaces_plugins_models_create_plugin_upload_request, authorization=authorization)
        print("The response of CustomPluginsNamespaceApi->generate_upload_url_namespaces_id_plugins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomPluginsNamespaceApi->generate_upload_url_namespaces_id_plugins: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_id** | **str**|  | 
 **api_namespaces_plugins_models_create_plugin_upload_request** | [**ApiNamespacesPluginsModelsCreatePluginUploadRequest**](ApiNamespacesPluginsModelsCreatePluginUploadRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**ApiNamespacesPluginsModelsPluginPresignedURLResponse**](ApiNamespacesPluginsModelsPluginPresignedURLResponse.md)

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
**403** | Plugin quota exceeded |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**409** | Plugin already exists |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployment_status_namespaces_id_plugins**
> PluginStatusResponse get_deployment_status_namespaces_id_plugins(namespace_id, plugin_id, authorization=authorization)

Get plugin deployment status

Get the current deployment status for a plugin.

**Status Values:**
- `queued`: Plugin is waiting in the deployment queue. Deployment will start within 30 seconds.
- `pending`: Deployment has been triggered, waiting for Anyscale to start.
- `in_progress`: Blue-green deployment in progress. New replicas are being created.
- `deployed`: Plugin successfully deployed and ready for realtime inference.
- `failed`: Deployment failed. Check the error field for details.
- `not_deployed`: Plugin has not been deployed for realtime inference (batch-only).

**Polling Recommendation:**
After deploying a plugin, poll this endpoint every 10-15 seconds to check status.
Deployment typically completes within 3-5 minutes.

### Example


```python
import mixpeek
from mixpeek.models.plugin_status_response import PluginStatusResponse
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
    api_instance = mixpeek.CustomPluginsNamespaceApi(api_client)
    namespace_id = 'namespace_id_example' # str | 
    plugin_id = 'plugin_id_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Get plugin deployment status
        api_response = api_instance.get_deployment_status_namespaces_id_plugins(namespace_id, plugin_id, authorization=authorization)
        print("The response of CustomPluginsNamespaceApi->get_deployment_status_namespaces_id_plugins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomPluginsNamespaceApi->get_deployment_status_namespaces_id_plugins: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_id** | **str**|  | 
 **plugin_id** | **str**|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**PluginStatusResponse**](PluginStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deployment status |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Plugin not found |  -  |
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plugin_namespaces**
> ApiNamespacesPluginsModelsPluginDetailResponse get_plugin_namespaces(namespace_id, plugin_id, return_presigned_urls=return_presigned_urls, authorization=authorization)

Get plugin details

Get detailed information about a specific plugin.

### Example


```python
import mixpeek
from mixpeek.models.api_namespaces_plugins_models_plugin_detail_response import ApiNamespacesPluginsModelsPluginDetailResponse
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
    api_instance = mixpeek.CustomPluginsNamespaceApi(api_client)
    namespace_id = 'namespace_id_example' # str | 
    plugin_id = 'plugin_id_example' # str | 
    return_presigned_urls = False # bool | Generate a presigned download URL for the plugin archive (valid for 1 hour) (optional) (default to False)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Get plugin details
        api_response = api_instance.get_plugin_namespaces(namespace_id, plugin_id, return_presigned_urls=return_presigned_urls, authorization=authorization)
        print("The response of CustomPluginsNamespaceApi->get_plugin_namespaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomPluginsNamespaceApi->get_plugin_namespaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_id** | **str**|  | 
 **plugin_id** | **str**|  | 
 **return_presigned_urls** | **bool**| Generate a presigned download URL for the plugin archive (valid for 1 hour) | [optional] [default to False]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**ApiNamespacesPluginsModelsPluginDetailResponse**](ApiNamespacesPluginsModelsPluginDetailResponse.md)

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

# **list_available_org_plugins_namespaces**
> AvailableOrgPluginsResponse list_available_org_plugins_namespaces(namespace_id, authorization=authorization)

List available org plugins

List all org-level plugins that can be enabled for this namespace.

This returns all plugins uploaded to the organization with their enable status
for the current namespace.

**Use this to:**
- See what org plugins are available to enable
- Check which plugins are already enabled for this namespace

### Example


```python
import mixpeek
from mixpeek.models.available_org_plugins_response import AvailableOrgPluginsResponse
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
    api_instance = mixpeek.CustomPluginsNamespaceApi(api_client)
    namespace_id = 'namespace_id_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # List available org plugins
        api_response = api_instance.list_available_org_plugins_namespaces(namespace_id, authorization=authorization)
        print("The response of CustomPluginsNamespaceApi->list_available_org_plugins_namespaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomPluginsNamespaceApi->list_available_org_plugins_namespaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_id** | **str**|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**AvailableOrgPluginsResponse**](AvailableOrgPluginsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of available org plugins |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_plugins_namespaces**
> ApiNamespacesPluginsModelsPluginListResponse list_plugins_namespaces(namespace_id, authorization=authorization)

List plugins in namespace

List all custom plugins uploaded to the namespace.

### Example


```python
import mixpeek
from mixpeek.models.api_namespaces_plugins_models_plugin_list_response import ApiNamespacesPluginsModelsPluginListResponse
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
    api_instance = mixpeek.CustomPluginsNamespaceApi(api_client)
    namespace_id = 'namespace_id_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # List plugins in namespace
        api_response = api_instance.list_plugins_namespaces(namespace_id, authorization=authorization)
        print("The response of CustomPluginsNamespaceApi->list_plugins_namespaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomPluginsNamespaceApi->list_plugins_namespaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_id** | **str**|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**ApiNamespacesPluginsModelsPluginListResponse**](ApiNamespacesPluginsModelsPluginListResponse.md)

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

# **undeploy_plugin_namespaces**
> Dict[str, object] undeploy_plugin_namespaces(namespace_id, plugin_id, authorization=authorization)

Undeploy a plugin

Remove a plugin deployment from the namespace's Ray cluster.

This will:
1. Remove the Ray Serve deployment (if realtime)
2. Update deployment status in MongoDB to deployed=False

The plugin archive remains in S3 and can be redeployed.

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
    api_instance = mixpeek.CustomPluginsNamespaceApi(api_client)
    namespace_id = 'namespace_id_example' # str | 
    plugin_id = 'plugin_id_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Undeploy a plugin
        api_response = api_instance.undeploy_plugin_namespaces(namespace_id, plugin_id, authorization=authorization)
        print("The response of CustomPluginsNamespaceApi->undeploy_plugin_namespaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomPluginsNamespaceApi->undeploy_plugin_namespaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_id** | **str**|  | 
 **plugin_id** | **str**|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plugin undeployed successfully |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Plugin not found |  -  |
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_plugin_namespaces**
> PluginUploadResponse upload_plugin_namespaces(namespace_id, file, name, version, authorization=authorization, description=description)

Upload a custom plugin

Upload a custom plugin to the namespace.

**Availability:**
- All accounts can upload plugins for batch processing (default quota: 10 plugins)
- Enterprise accounts get higher quotas and realtime inference support

**Requirements:**
- Plugin archive must be a valid .zip file
- Archive must contain `manifest.py` and `pipeline.py`
- Plugin code must pass security scan

**Archive Structure:**
```
my_plugin/
├── manifest.py      # Required: Feature definitions
├── pipeline.py      # Required: Pipeline orchestration
├── batch.py         # Optional: Custom batch services
├── realtime.py      # Optional: Real-time inference (Enterprise only)
└── processors/      # Optional: Custom processors
    └── *.py
```

**Response:**
- `validation_status`: "passed" or "failed"
- `deployment_status`: "deployed", "pending", or "failed"
- `feature_uri`: URI to use the plugin (e.g., "mixpeek://my_plugin@v1")

### Example


```python
import mixpeek
from mixpeek.models.plugin_upload_response import PluginUploadResponse
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
    api_instance = mixpeek.CustomPluginsNamespaceApi(api_client)
    namespace_id = 'namespace_id_example' # str | 
    file = None # bytearray | Plugin archive (.tar.gz)
    name = 'name_example' # str | Plugin name (e.g., 'my_plugin')
    version = 'version_example' # str | Plugin version (e.g., '1.0.0')
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    description = 'description_example' # str | Optional plugin description (optional)

    try:
        # Upload a custom plugin
        api_response = api_instance.upload_plugin_namespaces(namespace_id, file, name, version, authorization=authorization, description=description)
        print("The response of CustomPluginsNamespaceApi->upload_plugin_namespaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomPluginsNamespaceApi->upload_plugin_namespaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_id** | **str**|  | 
 **file** | **bytearray**| Plugin archive (.tar.gz) | 
 **name** | **str**| Plugin name (e.g., &#39;my_plugin&#39;) | 
 **version** | **str**| Plugin version (e.g., &#39;1.0.0&#39;) | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **description** | **str**| Optional plugin description | [optional] 

### Return type

[**PluginUploadResponse**](PluginUploadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plugin uploaded successfully |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Plugin quota exceeded |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**409** | Plugin already exists |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

