# mixpeek.ClustersApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_cluster_enrichment_enrich**](ClustersApi.md#apply_cluster_enrichment_enrich) | **POST** /v1/clusters/enrich | Apply Cluster Enrichment
[**create_cluster**](ClustersApi.md#create_cluster) | **POST** /v1/clusters | Create Cluster
[**delete_cluster**](ClustersApi.md#delete_cluster) | **DELETE** /v1/clusters/{cluster_id} | Delete Cluster
[**execute_clustering_clusters**](ClustersApi.md#execute_clustering_clusters) | **POST** /v1/clusters/{cluster_id}/execute | Execute Clustering
[**get_cluster**](ClustersApi.md#get_cluster) | **GET** /v1/clusters/{cluster_identifier} | Get Cluster
[**list_clusters**](ClustersApi.md#list_clusters) | **POST** /v1/clusters/list | List Clusters
[**patch_cluster**](ClustersApi.md#patch_cluster) | **PATCH** /v1/clusters/{cluster_identifier} | Partially Update Cluster


# **apply_cluster_enrichment_enrich**
> ClusteringEnrichmentResponse apply_cluster_enrichment_enrich(apply_cluster_enrichment_request, authorization=authorization, x_namespace=x_namespace)

Apply Cluster Enrichment

Apply clustering enrichments to a collection via engine.

### Example


```python
import mixpeek
from mixpeek.models.apply_cluster_enrichment_request import ApplyClusterEnrichmentRequest
from mixpeek.models.clustering_enrichment_response import ClusteringEnrichmentResponse
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
    api_instance = mixpeek.ClustersApi(api_client)
    apply_cluster_enrichment_request = mixpeek.ApplyClusterEnrichmentRequest() # ApplyClusterEnrichmentRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Apply Cluster Enrichment
        api_response = api_instance.apply_cluster_enrichment_enrich(apply_cluster_enrichment_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of ClustersApi->apply_cluster_enrichment_enrich:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->apply_cluster_enrichment_enrich: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apply_cluster_enrichment_request** | [**ApplyClusterEnrichmentRequest**](ApplyClusterEnrichmentRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**ClusteringEnrichmentResponse**](ClusteringEnrichmentResponse.md)

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

# **create_cluster**
> ClusterMetadata create_cluster(create_cluster_request, authorization=authorization, x_namespace=x_namespace)

Create Cluster

Create a new cluster configuration and output collection.

    This endpoint:
    1. Creates cluster metadata
    2. Creates output collection for cluster documents
    3. Returns cluster metadata with output_collection_id

    The cluster can then be executed via POST /v1/clusters/{id}/execute

### Example


```python
import mixpeek
from mixpeek.models.cluster_metadata import ClusterMetadata
from mixpeek.models.create_cluster_request import CreateClusterRequest
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
    api_instance = mixpeek.ClustersApi(api_client)
    create_cluster_request = mixpeek.CreateClusterRequest() # CreateClusterRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Create Cluster
        api_response = api_instance.create_cluster(create_cluster_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of ClustersApi->create_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->create_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_cluster_request** | [**CreateClusterRequest**](CreateClusterRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**ClusterMetadata**](ClusterMetadata.md)

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

# **delete_cluster**
> object delete_cluster(cluster_id, authorization=authorization, x_namespace=x_namespace)

Delete Cluster

This endpoint deletes a cluster and all its resources including:
    - Running Ray jobs (cancels active jobs)
    - Cluster triggers
    - Execution history (clustering_results)
    - S3 artifacts (parquet files, documents, members)
    - Related tasks
    - Clustering jobs
    - MongoDB cluster metadata

    Note: Output collections created by the cluster are NOT deleted as they
    contain user data and should persist independently.

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
    api_instance = mixpeek.ClustersApi(api_client)
    cluster_id = 'cluster_id_example' # str | Cluster ID
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Delete Cluster
        api_response = api_instance.delete_cluster(cluster_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of ClustersApi->delete_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->delete_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Cluster ID | 
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

# **execute_clustering_clusters**
> TaskResponse execute_clustering_clusters(cluster_id, authorization=authorization, x_namespace=x_namespace)

Execute Clustering

Execute clustering on a specific cluster.

    This endpoint:
    1. Validates the cluster exists
    2. Queues clustering job via Celery
    3. Returns task_id immediately (non-blocking)
    4. Celery prepares data and submits to Engine
    5. Monitor progress via GET /v1/tasks/{task_id}

    Flow:
    - API: Receives request
    - Celery: Fetches documents, creates parquet, uploads to S3
    - Engine: Runs Ray job on parquet data
    - Status: Automatically updates cluster when complete

    Use GET /v1/clusters/{id}/executions to retrieve results.

### Example


```python
import mixpeek
from mixpeek.models.task_response import TaskResponse
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
    api_instance = mixpeek.ClustersApi(api_client)
    cluster_id = 'cluster_id_example' # str | Cluster ID to execute
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Execute Clustering
        api_response = api_instance.execute_clustering_clusters(cluster_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of ClustersApi->execute_clustering_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->execute_clustering_clusters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Cluster ID to execute | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**TaskResponse**](TaskResponse.md)

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

# **get_cluster**
> ClusterMetadata get_cluster(cluster_identifier, authorization=authorization, x_namespace=x_namespace)

Get Cluster

Retrieve a cluster by ID or name.

    Returns cluster metadata including:
    - Configuration (cluster_type, algorithm, parameters)
    - Output collection information (output_collection_id, output_collection_name)
    - Execution results (num_clusters, num_documents_clustered, status)
    - Timestamps and metadata

### Example


```python
import mixpeek
from mixpeek.models.cluster_metadata import ClusterMetadata
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
    api_instance = mixpeek.ClustersApi(api_client)
    cluster_identifier = 'cluster_identifier_example' # str | Cluster ID or name
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Cluster
        api_response = api_instance.get_cluster(cluster_identifier, authorization=authorization, x_namespace=x_namespace)
        print("The response of ClustersApi->get_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->get_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_identifier** | **str**| Cluster ID or name | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**ClusterMetadata**](ClusterMetadata.md)

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

# **list_clusters**
> ListClustersResponse list_clusters(limit=limit, offset=offset, cursor=cursor, include_total=include_total, authorization=authorization, x_namespace=x_namespace, list_clusters_request=list_clusters_request)

List Clusters

This endpoint allows you to list clusters.

### Example


```python
import mixpeek
from mixpeek.models.list_clusters_request import ListClustersRequest
from mixpeek.models.list_clusters_response import ListClustersResponse
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
    api_instance = mixpeek.ClustersApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    cursor = 'cursor_example' # str |  (optional)
    include_total = False # bool |  (optional) (default to False)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)
    list_clusters_request = mixpeek.ListClustersRequest() # ListClustersRequest |  (optional)

    try:
        # List Clusters
        api_response = api_instance.list_clusters(limit=limit, offset=offset, cursor=cursor, include_total=include_total, authorization=authorization, x_namespace=x_namespace, list_clusters_request=list_clusters_request)
        print("The response of ClustersApi->list_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->list_clusters: %s\n" % e)
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
 **list_clusters_request** | [**ListClustersRequest**](ListClustersRequest.md)|  | [optional] 

### Return type

[**ListClustersResponse**](ListClustersResponse.md)

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

# **patch_cluster**
> ClusterModel patch_cluster(cluster_identifier, patch_cluster_request, authorization=authorization, x_namespace=x_namespace)

Partially Update Cluster

This endpoint partially updates a cluster (PATCH operation).
    Only provided fields will be updated. At minimum, metadata can always be updated.
    Immutable fields like cluster_id, status, and computed fields cannot be modified.

### Example


```python
import mixpeek
from mixpeek.models.cluster_model import ClusterModel
from mixpeek.models.patch_cluster_request import PatchClusterRequest
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
    api_instance = mixpeek.ClustersApi(api_client)
    cluster_identifier = 'cluster_identifier_example' # str | Cluster ID or name
    patch_cluster_request = mixpeek.PatchClusterRequest() # PatchClusterRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Partially Update Cluster
        api_response = api_instance.patch_cluster(cluster_identifier, patch_cluster_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of ClustersApi->patch_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->patch_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_identifier** | **str**| Cluster ID or name | 
 **patch_cluster_request** | [**PatchClusterRequest**](PatchClusterRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**ClusterModel**](ClusterModel.md)

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

