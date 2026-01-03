# mixpeek.CollectionSchemaApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sync_collection_schema**](CollectionSchemaApi.md#sync_collection_schema) | **POST** /v1/collections/{collection_id}/sync-schema | Sync Collection Schema


# **sync_collection_schema**
> ResponseSyncCollectionSchemaV1CollectionsCollectionIdSyncSchemaPost sync_collection_schema(collection_id, authorization=authorization, x_namespace=x_namespace, schema_sync_request=schema_sync_request)

Sync Collection Schema

Sample documents from Qdrant and automatically discover new fields to add to the collection's output_schema.

    This endpoint:
    - Samples N documents from the collection (default: 1000)
    - Discovers all fields present in actual documents
    - Merges discovered fields into the collection's output_schema (additive only)
    - Optionally cascades schema updates to downstream collections
    - Respects debounce window (max once per 5 minutes, unless force=true)

    The sync operation is additive only - it never removes or changes existing field types.

    Use this endpoint to:
    - Manually trigger schema discovery after data ingestion
    - Force an immediate schema sync (bypassing debounce)
    - Update schemas with new fields discovered in documents

### Example


```python
import mixpeek
from mixpeek.models.response_sync_collection_schema_v1_collections_collection_id_sync_schema_post import ResponseSyncCollectionSchemaV1CollectionsCollectionIdSyncSchemaPost
from mixpeek.models.schema_sync_request import SchemaSyncRequest
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
    api_instance = mixpeek.CollectionSchemaApi(api_client)
    collection_id = 'collection_id_example' # str | Collection ID to sync schema for
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)
    schema_sync_request = mixpeek.SchemaSyncRequest() # SchemaSyncRequest |  (optional)

    try:
        # Sync Collection Schema
        api_response = api_instance.sync_collection_schema(collection_id, authorization=authorization, x_namespace=x_namespace, schema_sync_request=schema_sync_request)
        print("The response of CollectionSchemaApi->sync_collection_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionSchemaApi->sync_collection_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| Collection ID to sync schema for | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 
 **schema_sync_request** | [**SchemaSyncRequest**](SchemaSyncRequest.md)|  | [optional] 

### Return type

[**ResponseSyncCollectionSchemaV1CollectionsCollectionIdSyncSchemaPost**](ResponseSyncCollectionSchemaV1CollectionsCollectionIdSyncSchemaPost.md)

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

