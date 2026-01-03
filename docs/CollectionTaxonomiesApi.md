# mixpeek.CollectionTaxonomiesApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_taxonomy_to_collection**](CollectionTaxonomiesApi.md#apply_taxonomy_to_collection) | **POST** /v1/collections/{collection_identifier}/apply-taxonomy | Apply Taxonomy to Existing Documents


# **apply_taxonomy_to_collection**
> ApplyTaxonomyResponse apply_taxonomy_to_collection(collection_identifier, apply_taxonomy_request, authorization=authorization, x_namespace=x_namespace)

Apply Taxonomy to Existing Documents

Apply a taxonomy to all existing documents in a collection retroactively.

This endpoint triggers distributed Ray processing to enrich existing documents
with taxonomy data. Unlike automatic materialization (which happens during ingestion),
this endpoint allows you to:

1. **Backfill enrichment** for documents ingested before the taxonomy was created
2. **Re-apply taxonomy** after configuration changes
3. **Process specific subsets** using scroll_filters

⚙️ **Processing Details:**
- Uses Ray datasets with map_batches for parallel processing
- Scales horizontally across Ray cluster
- Non-blocking: Returns immediately with task_id
- Monitor progress via Tasks API

⚠️ **Prerequisites:**
- Taxonomy must exist and be valid
- Taxonomy must be in collection's taxonomy_applications list
- Collection must contain documents

📊 **Performance:**
- ~1000-5000 docs/second depending on cluster size
- Parallel processing across multiple Ray workers
- Batch size and parallelism configurable

🔍 **Use Cases:**
- Backfill: Apply new taxonomy to historical data
- Re-enrichment: Update after taxonomy changes
- Selective: Process filtered document subsets

See Collections API and Taxonomies API documentation for details.

### Example


```python
import mixpeek
from mixpeek.models.apply_taxonomy_request import ApplyTaxonomyRequest
from mixpeek.models.apply_taxonomy_response import ApplyTaxonomyResponse
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
    api_instance = mixpeek.CollectionTaxonomiesApi(api_client)
    collection_identifier = 'collection_identifier_example' # str | Collection ID or name to apply taxonomy to
    apply_taxonomy_request = mixpeek.ApplyTaxonomyRequest() # ApplyTaxonomyRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Apply Taxonomy to Existing Documents
        api_response = api_instance.apply_taxonomy_to_collection(collection_identifier, apply_taxonomy_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of CollectionTaxonomiesApi->apply_taxonomy_to_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionTaxonomiesApi->apply_taxonomy_to_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_identifier** | **str**| Collection ID or name to apply taxonomy to | 
 **apply_taxonomy_request** | [**ApplyTaxonomyRequest**](ApplyTaxonomyRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**ApplyTaxonomyResponse**](ApplyTaxonomyResponse.md)

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

