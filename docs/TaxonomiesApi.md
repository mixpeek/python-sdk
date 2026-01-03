# mixpeek.TaxonomiesApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clone_taxonomy_taxonomies**](TaxonomiesApi.md#clone_taxonomy_taxonomies) | **POST** /v1/taxonomies/{taxonomy_identifier}/clone | Clone Taxonomy
[**create_taxonomy_taxonomies**](TaxonomiesApi.md#create_taxonomy_taxonomies) | **POST** /v1/taxonomies | Create Taxonomy
[**create_taxonomy_version_taxonomies**](TaxonomiesApi.md#create_taxonomy_version_taxonomies) | **POST** /v1/taxonomies/{taxonomy_id}/versions | Create Taxonomy Version
[**delete_taxonomy_taxonomies**](TaxonomiesApi.md#delete_taxonomy_taxonomies) | **DELETE** /v1/taxonomies/{taxonomy_identifier} | Delete Taxonomy
[**execute_taxonomy_taxonomies**](TaxonomiesApi.md#execute_taxonomy_taxonomies) | **POST** /v1/taxonomies/execute/{taxonomy_identifier} | Test taxonomy configuration (validation only)
[**get_taxonomy_taxonomies**](TaxonomiesApi.md#get_taxonomy_taxonomies) | **GET** /v1/taxonomies/{taxonomy_identifier} | Get Taxonomy
[**list_taxonomies**](TaxonomiesApi.md#list_taxonomies) | **POST** /v1/taxonomies/list | List Taxonomies
[**list_taxonomy_versions_taxonomies**](TaxonomiesApi.md#list_taxonomy_versions_taxonomies) | **GET** /v1/taxonomies/{taxonomy_id}/versions | List Taxonomy Versions
[**patch_taxonomy_taxonomies**](TaxonomiesApi.md#patch_taxonomy_taxonomies) | **PATCH** /v1/taxonomies/{taxonomy_identifier} | Partially Update Taxonomy


# **clone_taxonomy_taxonomies**
> CloneTaxonomyResponse clone_taxonomy_taxonomies(taxonomy_identifier, clone_taxonomy_request, authorization=authorization, x_namespace=x_namespace)

Clone Taxonomy

Clone a taxonomy with optional modifications.

    **Purpose:**
    Creates a NEW taxonomy (with new ID) based on an existing one. This is the
    recommended way to iterate on taxonomy designs when you need to modify core
    logic that PATCH doesn't allow (config, retriever_id, input_mappings).

    **Clone vs PATCH vs Template:**
    - **PATCH**: Update metadata only (name, description, metadata)
    - **Clone**: Copy and modify core logic (config, retriever, collections)
    - **Template**: Start from a pre-configured pattern (for new projects)

    **Common Use Cases:**
    - Fix configuration errors without losing join history
    - Change retriever or input mappings
    - Modify enrichment fields or collection configuration
    - Test modifications before replacing production taxonomy
    - Create variants for different datasets

    **How it works:**
    1. Source taxonomy is copied
    2. You provide a new name (REQUIRED)
    3. Optionally override any other fields (description, config)
    4. A new taxonomy is created with a new ID
    5. Original taxonomy remains unchanged

### Example


```python
import mixpeek
from mixpeek.models.clone_taxonomy_request import CloneTaxonomyRequest
from mixpeek.models.clone_taxonomy_response import CloneTaxonomyResponse
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
    api_instance = mixpeek.TaxonomiesApi(api_client)
    taxonomy_identifier = 'taxonomy_identifier_example' # str | Source taxonomy ID or name to clone.
    clone_taxonomy_request = mixpeek.CloneTaxonomyRequest() # CloneTaxonomyRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Clone Taxonomy
        api_response = api_instance.clone_taxonomy_taxonomies(taxonomy_identifier, clone_taxonomy_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of TaxonomiesApi->clone_taxonomy_taxonomies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomiesApi->clone_taxonomy_taxonomies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxonomy_identifier** | **str**| Source taxonomy ID or name to clone. | 
 **clone_taxonomy_request** | [**CloneTaxonomyRequest**](CloneTaxonomyRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**CloneTaxonomyResponse**](CloneTaxonomyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
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

# **create_taxonomy_taxonomies**
> TaxonomyResponse create_taxonomy_taxonomies(create_taxonomy_request, authorization=authorization, x_namespace=x_namespace)

Create Taxonomy

Create a taxonomy and return the created resource.

### Example


```python
import mixpeek
from mixpeek.models.create_taxonomy_request import CreateTaxonomyRequest
from mixpeek.models.taxonomy_response import TaxonomyResponse
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
    api_instance = mixpeek.TaxonomiesApi(api_client)
    create_taxonomy_request = mixpeek.CreateTaxonomyRequest() # CreateTaxonomyRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Create Taxonomy
        api_response = api_instance.create_taxonomy_taxonomies(create_taxonomy_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of TaxonomiesApi->create_taxonomy_taxonomies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomiesApi->create_taxonomy_taxonomies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_taxonomy_request** | [**CreateTaxonomyRequest**](CreateTaxonomyRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**TaxonomyResponse**](TaxonomyResponse.md)

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

# **create_taxonomy_version_taxonomies**
> TaxonomyResponse create_taxonomy_version_taxonomies(taxonomy_id, request_body, authorization=authorization, x_namespace=x_namespace)

Create Taxonomy Version

Create a new version for a taxonomy with a new config snapshot.

### Example


```python
import mixpeek
from mixpeek.models.taxonomy_response import TaxonomyResponse
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
    api_instance = mixpeek.TaxonomiesApi(api_client)
    taxonomy_id = 'taxonomy_id_example' # str | Taxonomy ID (tax_...)
    request_body = None # Dict[str, object] | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Create Taxonomy Version
        api_response = api_instance.create_taxonomy_version_taxonomies(taxonomy_id, request_body, authorization=authorization, x_namespace=x_namespace)
        print("The response of TaxonomiesApi->create_taxonomy_version_taxonomies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomiesApi->create_taxonomy_version_taxonomies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxonomy_id** | **str**| Taxonomy ID (tax_...) | 
 **request_body** | [**Dict[str, object]**](object.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**TaxonomyResponse**](TaxonomyResponse.md)

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

# **delete_taxonomy_taxonomies**
> object delete_taxonomy_taxonomies(taxonomy_identifier, authorization=authorization, x_namespace=x_namespace)

Delete Taxonomy

This endpoint deletes a taxonomy and all its resources including:
    - Taxonomy versions (version snapshots)
    - Taxonomy metadata from MongoDB

    The deletion is performed synchronously and returns when complete.

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
    api_instance = mixpeek.TaxonomiesApi(api_client)
    taxonomy_identifier = 'taxonomy_identifier_example' # str | Taxonomy ID or name
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Delete Taxonomy
        api_response = api_instance.delete_taxonomy_taxonomies(taxonomy_identifier, authorization=authorization, x_namespace=x_namespace)
        print("The response of TaxonomiesApi->delete_taxonomy_taxonomies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomiesApi->delete_taxonomy_taxonomies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxonomy_identifier** | **str**| Taxonomy ID or name | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

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

# **execute_taxonomy_taxonomies**
> JoinResponse execute_taxonomy_taxonomies(taxonomy_identifier, payload, version=version, authorization=authorization, x_namespace=x_namespace)

Test taxonomy configuration (validation only)

⚠️ VALIDATION ENDPOINT ONLY - Not for production enrichment!

This endpoint validates taxonomy configuration with 1-5 sample documents.
Results are returned immediately and NOT persisted to any collection.

❌ DO NOT USE FOR:
- Enriching entire collections (use taxonomy_applications instead)
- Batch processing documents (automatic during ingestion)
- Persisting enriched documents (use retriever pipelines instead)

✅ USE THIS FOR:
- Testing taxonomy configuration is correct
- Validating retriever finds matching taxonomy nodes
- Checking enrichment fields are properly applied
- Development/debugging taxonomy setup

📚 FOR PRODUCTION ENRICHMENT:

Automatic (during ingestion):
  1. Create taxonomy: POST /taxonomies
  2. Attach to collection: PUT /collections/{id} with taxonomy_applications field
  3. Ingest documents: Documents are automatically enriched by engine

On-the-fly (during retrieval):
  1. Add taxonomy_join stage to retriever pipeline
  2. Execute retriever: GET /retrievers/{id}/execute
  3. Results include enriched documents (not persisted)

See API documentation for Collections and Retrievers for details.

### Example


```python
import mixpeek
from mixpeek.models.join_response import JoinResponse
from mixpeek.models.payload import Payload
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
    api_instance = mixpeek.TaxonomiesApi(api_client)
    taxonomy_identifier = 'tax_abc123' # str | Taxonomy ID or name to validate
    payload = mixpeek.Payload() # Payload | 
    version = 1 # int | Optional taxonomy version (defaults to latest) (optional)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Test taxonomy configuration (validation only)
        api_response = api_instance.execute_taxonomy_taxonomies(taxonomy_identifier, payload, version=version, authorization=authorization, x_namespace=x_namespace)
        print("The response of TaxonomiesApi->execute_taxonomy_taxonomies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomiesApi->execute_taxonomy_taxonomies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxonomy_identifier** | **str**| Taxonomy ID or name to validate | 
 **payload** | [**Payload**](Payload.md)|  | 
 **version** | **int**| Optional taxonomy version (defaults to latest) | [optional] 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**JoinResponse**](JoinResponse.md)

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

# **get_taxonomy_taxonomies**
> TaxonomyResponse get_taxonomy_taxonomies(taxonomy_identifier, version=version, authorization=authorization, x_namespace=x_namespace)

Get Taxonomy

Get a taxonomy by ID or name.

### Example


```python
import mixpeek
from mixpeek.models.taxonomy_response import TaxonomyResponse
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
    api_instance = mixpeek.TaxonomiesApi(api_client)
    taxonomy_identifier = 'taxonomy_identifier_example' # str | Taxonomy ID or name
    version = 56 # int | Optional taxonomy version to fetch (optional)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Taxonomy
        api_response = api_instance.get_taxonomy_taxonomies(taxonomy_identifier, version=version, authorization=authorization, x_namespace=x_namespace)
        print("The response of TaxonomiesApi->get_taxonomy_taxonomies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomiesApi->get_taxonomy_taxonomies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxonomy_identifier** | **str**| Taxonomy ID or name | 
 **version** | **int**| Optional taxonomy version to fetch | [optional] 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**TaxonomyResponse**](TaxonomyResponse.md)

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

# **list_taxonomies**
> ListTaxonomiesResponse list_taxonomies(limit=limit, offset=offset, cursor=cursor, include_total=include_total, authorization=authorization, x_namespace=x_namespace, list_taxonomies_request=list_taxonomies_request)

List Taxonomies

List taxonomies with optional filters and pagination.

### Example


```python
import mixpeek
from mixpeek.models.list_taxonomies_request import ListTaxonomiesRequest
from mixpeek.models.list_taxonomies_response import ListTaxonomiesResponse
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
    api_instance = mixpeek.TaxonomiesApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    cursor = 'cursor_example' # str |  (optional)
    include_total = False # bool |  (optional) (default to False)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)
    list_taxonomies_request = mixpeek.ListTaxonomiesRequest() # ListTaxonomiesRequest |  (optional)

    try:
        # List Taxonomies
        api_response = api_instance.list_taxonomies(limit=limit, offset=offset, cursor=cursor, include_total=include_total, authorization=authorization, x_namespace=x_namespace, list_taxonomies_request=list_taxonomies_request)
        print("The response of TaxonomiesApi->list_taxonomies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomiesApi->list_taxonomies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **cursor** | **str**|  | [optional] 
 **include_total** | **bool**|  | [optional] [default to False]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 
 **list_taxonomies_request** | [**ListTaxonomiesRequest**](ListTaxonomiesRequest.md)|  | [optional] 

### Return type

[**ListTaxonomiesResponse**](ListTaxonomiesResponse.md)

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

# **list_taxonomy_versions_taxonomies**
> ListTaxonomiesResponse list_taxonomy_versions_taxonomies(taxonomy_id, authorization=authorization, x_namespace=x_namespace)

List Taxonomy Versions

List all versions for a taxonomy (head included as latest).

### Example


```python
import mixpeek
from mixpeek.models.list_taxonomies_response import ListTaxonomiesResponse
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
    api_instance = mixpeek.TaxonomiesApi(api_client)
    taxonomy_id = 'taxonomy_id_example' # str | Taxonomy ID (tax_...)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # List Taxonomy Versions
        api_response = api_instance.list_taxonomy_versions_taxonomies(taxonomy_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of TaxonomiesApi->list_taxonomy_versions_taxonomies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomiesApi->list_taxonomy_versions_taxonomies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxonomy_id** | **str**| Taxonomy ID (tax_...) | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**ListTaxonomiesResponse**](ListTaxonomiesResponse.md)

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

# **patch_taxonomy_taxonomies**
> TaxonomyResponse patch_taxonomy_taxonomies(taxonomy_identifier, patch_taxonomy_request, authorization=authorization, x_namespace=x_namespace)

Partially Update Taxonomy

Update a taxonomy's metadata.

    **Metadata Only Updates:**
    This endpoint allows updating ONLY metadata fields. Core taxonomy logic is immutable
    to ensure consistency for join history and dependent resources.

    **Fields You CAN Update:**
    - taxonomy_name: Rename the taxonomy
    - description: Update documentation
    - metadata: Update custom metadata

    **Fields You CANNOT Update:**
    - config: Taxonomy configuration (retriever_id, input_mappings, collections)
    - taxonomy_type: Type (flat vs hierarchical)

    **Need to Modify Core Logic?**
    Use POST /{taxonomy_identifier}/clone instead to modify configuration,
    retriever_id, input_mappings, or collections.

### Example


```python
import mixpeek
from mixpeek.models.patch_taxonomy_request import PatchTaxonomyRequest
from mixpeek.models.taxonomy_response import TaxonomyResponse
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
    api_instance = mixpeek.TaxonomiesApi(api_client)
    taxonomy_identifier = 'taxonomy_identifier_example' # str | Taxonomy ID or name
    patch_taxonomy_request = mixpeek.PatchTaxonomyRequest() # PatchTaxonomyRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Partially Update Taxonomy
        api_response = api_instance.patch_taxonomy_taxonomies(taxonomy_identifier, patch_taxonomy_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of TaxonomiesApi->patch_taxonomy_taxonomies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomiesApi->patch_taxonomy_taxonomies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxonomy_identifier** | **str**| Taxonomy ID or name | 
 **patch_taxonomy_request** | [**PatchTaxonomyRequest**](PatchTaxonomyRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**TaxonomyResponse**](TaxonomyResponse.md)

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

