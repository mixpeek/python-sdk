# mixpeek.CollectionsApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clone_collection**](CollectionsApi.md#clone_collection) | **POST** /v1/collections/{collection_identifier}/clone | Clone Collection
[**create_collection**](CollectionsApi.md#create_collection) | **POST** /v1/collections | Create Collection
[**delete_collection**](CollectionsApi.md#delete_collection) | **DELETE** /v1/collections/{collection_identifier} | Delete Collection
[**describe_collection_features**](CollectionsApi.md#describe_collection_features) | **GET** /v1/collections/{collection_identifier}/features | Describe collection features
[**get_collection**](CollectionsApi.md#get_collection) | **GET** /v1/collections/{collection_identifier} | Get Collection
[**list_collections**](CollectionsApi.md#list_collections) | **POST** /v1/collections/list | List Collections
[**trigger_collection**](CollectionsApi.md#trigger_collection) | **POST** /v1/collections/{collection_identifier}/trigger | Trigger Collection Processing
[**update_collection**](CollectionsApi.md#update_collection) | **PATCH** /v1/collections/{collection_identifier} | Update Collection


# **clone_collection**
> CloneCollectionResponse clone_collection(collection_identifier, clone_collection_request, authorization=authorization, x_namespace=x_namespace)

Clone Collection

Clone a collection with optional modifications.

    **Purpose:**
    Creates a NEW collection (with new ID) based on an existing one. This is the
    recommended way to iterate on collection designs when you need to modify core
    configuration that PATCH doesn't allow (source, feature_extractor, field_passthrough).

    **Clone vs PATCH vs Template:**
    - **PATCH**: Update metadata only (enabled, metadata, taxonomy_applications)
    - **Clone**: Copy and modify core configuration (source, feature_extractor)
    - **Template**: Start from a pre-configured pattern (for new projects)

    **Common Use Cases:**
    - Change feature extractor configuration (model, parameters)
    - Modify field_passthrough to include/exclude fields
    - Switch to different source (bucket or collection)
    - Test modifications before replacing production collection
    - Create variants (e.g., different embedding models)

    **How it works:**
    1. Source collection is copied
    2. You provide a new name (REQUIRED)
    3. Optionally override any other fields
    4. A new collection is created with a new ID
    5. Original collection remains unchanged

### Example


```python
import mixpeek
from mixpeek.models.clone_collection_request import CloneCollectionRequest
from mixpeek.models.clone_collection_response import CloneCollectionResponse
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
    api_instance = mixpeek.CollectionsApi(api_client)
    collection_identifier = 'collection_identifier_example' # str | Source collection ID or name to clone.
    clone_collection_request = mixpeek.CloneCollectionRequest() # CloneCollectionRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Clone Collection
        api_response = api_instance.clone_collection(collection_identifier, clone_collection_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of CollectionsApi->clone_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->clone_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_identifier** | **str**| Source collection ID or name to clone. | 
 **clone_collection_request** | [**CloneCollectionRequest**](CloneCollectionRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**CloneCollectionResponse**](CloneCollectionResponse.md)

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

# **create_collection**
> CollectionResponse create_collection(create_collection_request, authorization=authorization, x_namespace=x_namespace)

Create Collection

This endpoint allows you to create a new collection.

### Example


```python
import mixpeek
from mixpeek.models.collection_response import CollectionResponse
from mixpeek.models.create_collection_request import CreateCollectionRequest
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
    api_instance = mixpeek.CollectionsApi(api_client)
    create_collection_request = mixpeek.CreateCollectionRequest() # CreateCollectionRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Create Collection
        api_response = api_instance.create_collection(create_collection_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of CollectionsApi->create_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->create_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_collection_request** | [**CreateCollectionRequest**](CreateCollectionRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**CollectionResponse**](CollectionResponse.md)

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

# **delete_collection**
> object delete_collection(collection_identifier, authorization=authorization, x_namespace=x_namespace)

Delete Collection

This endpoint deletes a collection and all its resources including:
    - Qdrant points (documents) with this collection_id
    - Cache entries
    - MongoDB collection metadata

    Note: Collections are payload IDs within the namespace's Qdrant collection,
    not separate Qdrant collections.

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
    api_instance = mixpeek.CollectionsApi(api_client)
    collection_identifier = 'collection_identifier_example' # str | The ID or name of the collection to delete
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Delete Collection
        api_response = api_instance.delete_collection(collection_identifier, authorization=authorization, x_namespace=x_namespace)
        print("The response of CollectionsApi->delete_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->delete_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_identifier** | **str**| The ID or name of the collection to delete | 
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

# **describe_collection_features**
> DescribeCollectionFeaturesResponse describe_collection_features(collection_identifier, authorization=authorization, x_namespace=x_namespace)

Describe collection features

List feature addresses and metadata available in this collection

### Example


```python
import mixpeek
from mixpeek.models.describe_collection_features_response import DescribeCollectionFeaturesResponse
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
    api_instance = mixpeek.CollectionsApi(api_client)
    collection_identifier = 'collection_identifier_example' # str | The ID or name of the collection to describe
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Describe collection features
        api_response = api_instance.describe_collection_features(collection_identifier, authorization=authorization, x_namespace=x_namespace)
        print("The response of CollectionsApi->describe_collection_features:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->describe_collection_features: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_identifier** | **str**| The ID or name of the collection to describe | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**DescribeCollectionFeaturesResponse**](DescribeCollectionFeaturesResponse.md)

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

# **get_collection**
> CollectionResponse get_collection(collection_identifier, authorization=authorization, x_namespace=x_namespace)

Get Collection

This endpoint allows you to retrieve a collection by ID or name.

### Example


```python
import mixpeek
from mixpeek.models.collection_response import CollectionResponse
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
    api_instance = mixpeek.CollectionsApi(api_client)
    collection_identifier = 'collection_identifier_example' # str | The ID or name of the collection to retrieve
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Collection
        api_response = api_instance.get_collection(collection_identifier, authorization=authorization, x_namespace=x_namespace)
        print("The response of CollectionsApi->get_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->get_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_identifier** | **str**| The ID or name of the collection to retrieve | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**CollectionResponse**](CollectionResponse.md)

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

# **list_collections**
> ListCollectionsResponse list_collections(limit=limit, offset=offset, cursor=cursor, include_total=include_total, authorization=authorization, x_namespace=x_namespace, list_collections_request=list_collections_request)

List Collections

This endpoint allows you to list collections.

### Example


```python
import mixpeek
from mixpeek.models.list_collections_request import ListCollectionsRequest
from mixpeek.models.list_collections_response import ListCollectionsResponse
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
    api_instance = mixpeek.CollectionsApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    cursor = 'cursor_example' # str |  (optional)
    include_total = False # bool |  (optional) (default to False)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)
    list_collections_request = mixpeek.ListCollectionsRequest() # ListCollectionsRequest |  (optional)

    try:
        # List Collections
        api_response = api_instance.list_collections(limit=limit, offset=offset, cursor=cursor, include_total=include_total, authorization=authorization, x_namespace=x_namespace, list_collections_request=list_collections_request)
        print("The response of CollectionsApi->list_collections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->list_collections: %s\n" % e)
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
 **list_collections_request** | [**ListCollectionsRequest**](ListCollectionsRequest.md)|  | [optional] 

### Return type

[**ListCollectionsResponse**](ListCollectionsResponse.md)

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

# **trigger_collection**
> TriggerCollectionResponse trigger_collection(collection_identifier, authorization=authorization, x_namespace=x_namespace, trigger_collection_request=trigger_collection_request)

Trigger Collection Processing

Process data through a collection - works for both bucket-sourced and collection-sourced collections.

    **For bucket-sourced collections:**
    Discovers objects from source bucket(s), creates a batch, and submits for processing.
    Use `include_buckets` to limit which source buckets to process from.

    **For collection-sourced collections:**
    Processes existing documents from upstream collection(s).
    Use `include_collections` to limit which source collections to process from.

    **Filtering:**
    - `source_filters`: Field-level filters using LogicalOperator format
    - Example: `{"AND": [{"field": "status", "operator": "eq", "value": "pending"}]}`
    - For specific objects: `{"AND": [{"field": "object_id", "operator": "in", "value": ["obj_1", "obj_2"]}]}`

    **Returns:**
    - batch_id: Track progress via GET /batches/{batch_id}
    - task_id: Monitor via GET /tasks/{task_id}

### Example


```python
import mixpeek
from mixpeek.models.trigger_collection_request import TriggerCollectionRequest
from mixpeek.models.trigger_collection_response import TriggerCollectionResponse
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
    api_instance = mixpeek.CollectionsApi(api_client)
    collection_identifier = 'collection_identifier_example' # str | The ID or name of the collection to trigger
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)
    trigger_collection_request = mixpeek.TriggerCollectionRequest() # TriggerCollectionRequest |  (optional)

    try:
        # Trigger Collection Processing
        api_response = api_instance.trigger_collection(collection_identifier, authorization=authorization, x_namespace=x_namespace, trigger_collection_request=trigger_collection_request)
        print("The response of CollectionsApi->trigger_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->trigger_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_identifier** | **str**| The ID or name of the collection to trigger | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 
 **trigger_collection_request** | [**TriggerCollectionRequest**](TriggerCollectionRequest.md)|  | [optional] 

### Return type

[**TriggerCollectionResponse**](TriggerCollectionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_collection**
> CollectionResponse update_collection(collection_identifier, request_body, authorization=authorization, x_namespace=x_namespace)

Update Collection

Update mutable collection fields (collection_name, description, taxonomy_applications, enabled)

### Example


```python
import mixpeek
from mixpeek.models.collection_response import CollectionResponse
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
    api_instance = mixpeek.CollectionsApi(api_client)
    collection_identifier = 'collection_identifier_example' # str | The ID or name of the collection to update
    request_body = None # Dict[str, object] | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Update Collection
        api_response = api_instance.update_collection(collection_identifier, request_body, authorization=authorization, x_namespace=x_namespace)
        print("The response of CollectionsApi->update_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->update_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_identifier** | **str**| The ID or name of the collection to update | 
 **request_body** | [**Dict[str, object]**](object.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**CollectionResponse**](CollectionResponse.md)

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

