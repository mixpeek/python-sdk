# mixpeek.RetrieverBenchmarksApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_benchmark_retrievers**](RetrieverBenchmarksApi.md#create_benchmark_retrievers) | **POST** /v1/retrievers/benchmarks | Create benchmark
[**create_benchmark_retrievers_0**](RetrieverBenchmarksApi.md#create_benchmark_retrievers_0) | **POST** /v1/retrievers/benchmarks | Create benchmark
[**delete_benchmark_retrievers**](RetrieverBenchmarksApi.md#delete_benchmark_retrievers) | **DELETE** /v1/retrievers/benchmarks/{benchmark_id} | Delete benchmark
[**delete_benchmark_retrievers_0**](RetrieverBenchmarksApi.md#delete_benchmark_retrievers_0) | **DELETE** /v1/retrievers/benchmarks/{benchmark_id} | Delete benchmark
[**get_benchmark_retrievers**](RetrieverBenchmarksApi.md#get_benchmark_retrievers) | **GET** /v1/retrievers/benchmarks/{benchmark_id} | Get benchmark
[**get_benchmark_retrievers_0**](RetrieverBenchmarksApi.md#get_benchmark_retrievers_0) | **GET** /v1/retrievers/benchmarks/{benchmark_id} | Get benchmark
[**list_benchmarks_retrievers**](RetrieverBenchmarksApi.md#list_benchmarks_retrievers) | **GET** /v1/retrievers/benchmarks | List benchmarks
[**list_benchmarks_retrievers_0**](RetrieverBenchmarksApi.md#list_benchmarks_retrievers_0) | **GET** /v1/retrievers/benchmarks | List benchmarks


# **create_benchmark_retrievers**
> BenchmarkResponse create_benchmark_retrievers(create_benchmark_request, authorization=authorization, x_namespace=x_namespace)

Create benchmark

Create a new benchmark run to compare retriever pipelines. The benchmark will replay historical sessions and measure alignment with observed user behavior.

### Example


```python
import mixpeek
from mixpeek.models.benchmark_response import BenchmarkResponse
from mixpeek.models.create_benchmark_request import CreateBenchmarkRequest
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
    api_instance = mixpeek.RetrieverBenchmarksApi(api_client)
    create_benchmark_request = mixpeek.CreateBenchmarkRequest() # CreateBenchmarkRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Create benchmark
        api_response = api_instance.create_benchmark_retrievers(create_benchmark_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of RetrieverBenchmarksApi->create_benchmark_retrievers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrieverBenchmarksApi->create_benchmark_retrievers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_benchmark_request** | [**CreateBenchmarkRequest**](CreateBenchmarkRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**BenchmarkResponse**](BenchmarkResponse.md)

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

# **create_benchmark_retrievers_0**
> BenchmarkResponse create_benchmark_retrievers_0(create_benchmark_request, authorization=authorization, x_namespace=x_namespace)

Create benchmark

Create a new benchmark run to compare retriever pipelines. The benchmark will replay historical sessions and measure alignment with observed user behavior.

### Example


```python
import mixpeek
from mixpeek.models.benchmark_response import BenchmarkResponse
from mixpeek.models.create_benchmark_request import CreateBenchmarkRequest
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
    api_instance = mixpeek.RetrieverBenchmarksApi(api_client)
    create_benchmark_request = mixpeek.CreateBenchmarkRequest() # CreateBenchmarkRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Create benchmark
        api_response = api_instance.create_benchmark_retrievers_0(create_benchmark_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of RetrieverBenchmarksApi->create_benchmark_retrievers_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrieverBenchmarksApi->create_benchmark_retrievers_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_benchmark_request** | [**CreateBenchmarkRequest**](CreateBenchmarkRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**BenchmarkResponse**](BenchmarkResponse.md)

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

# **delete_benchmark_retrievers**
> delete_benchmark_retrievers(benchmark_id, authorization=authorization, x_namespace=x_namespace)

Delete benchmark

Delete a benchmark and its results

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
    api_instance = mixpeek.RetrieverBenchmarksApi(api_client)
    benchmark_id = 'benchmark_id_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Delete benchmark
        api_instance.delete_benchmark_retrievers(benchmark_id, authorization=authorization, x_namespace=x_namespace)
    except Exception as e:
        print("Exception when calling RetrieverBenchmarksApi->delete_benchmark_retrievers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **benchmark_id** | **str**|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_benchmark_retrievers_0**
> delete_benchmark_retrievers_0(benchmark_id, authorization=authorization, x_namespace=x_namespace)

Delete benchmark

Delete a benchmark and its results

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
    api_instance = mixpeek.RetrieverBenchmarksApi(api_client)
    benchmark_id = 'benchmark_id_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Delete benchmark
        api_instance.delete_benchmark_retrievers_0(benchmark_id, authorization=authorization, x_namespace=x_namespace)
    except Exception as e:
        print("Exception when calling RetrieverBenchmarksApi->delete_benchmark_retrievers_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **benchmark_id** | **str**|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_benchmark_retrievers**
> BenchmarkResponse get_benchmark_retrievers(benchmark_id, authorization=authorization, x_namespace=x_namespace)

Get benchmark

Get benchmark status and results by ID

### Example


```python
import mixpeek
from mixpeek.models.benchmark_response import BenchmarkResponse
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
    api_instance = mixpeek.RetrieverBenchmarksApi(api_client)
    benchmark_id = 'benchmark_id_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get benchmark
        api_response = api_instance.get_benchmark_retrievers(benchmark_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of RetrieverBenchmarksApi->get_benchmark_retrievers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrieverBenchmarksApi->get_benchmark_retrievers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **benchmark_id** | **str**|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**BenchmarkResponse**](BenchmarkResponse.md)

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

# **get_benchmark_retrievers_0**
> BenchmarkResponse get_benchmark_retrievers_0(benchmark_id, authorization=authorization, x_namespace=x_namespace)

Get benchmark

Get benchmark status and results by ID

### Example


```python
import mixpeek
from mixpeek.models.benchmark_response import BenchmarkResponse
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
    api_instance = mixpeek.RetrieverBenchmarksApi(api_client)
    benchmark_id = 'benchmark_id_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get benchmark
        api_response = api_instance.get_benchmark_retrievers_0(benchmark_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of RetrieverBenchmarksApi->get_benchmark_retrievers_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrieverBenchmarksApi->get_benchmark_retrievers_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **benchmark_id** | **str**|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**BenchmarkResponse**](BenchmarkResponse.md)

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

# **list_benchmarks_retrievers**
> BenchmarkListResponse list_benchmarks_retrievers(retriever_id=retriever_id, status=status, page=page, page_size=page_size, authorization=authorization, x_namespace=x_namespace)

List benchmarks

List benchmarks with optional filtering

### Example


```python
import mixpeek
from mixpeek.models.benchmark_list_response import BenchmarkListResponse
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
    api_instance = mixpeek.RetrieverBenchmarksApi(api_client)
    retriever_id = 'retriever_id_example' # str | Filter to benchmarks involving this retriever (as baseline or candidate) (optional)
    status = 'status_example' # str | Filter by status (pending, building_sessions, replaying, completed, failed) (optional)
    page = 1 # int | Page number (optional) (default to 1)
    page_size = 20 # int | Items per page (optional) (default to 20)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # List benchmarks
        api_response = api_instance.list_benchmarks_retrievers(retriever_id=retriever_id, status=status, page=page, page_size=page_size, authorization=authorization, x_namespace=x_namespace)
        print("The response of RetrieverBenchmarksApi->list_benchmarks_retrievers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrieverBenchmarksApi->list_benchmarks_retrievers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retriever_id** | **str**| Filter to benchmarks involving this retriever (as baseline or candidate) | [optional] 
 **status** | **str**| Filter by status (pending, building_sessions, replaying, completed, failed) | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **page_size** | **int**| Items per page | [optional] [default to 20]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**BenchmarkListResponse**](BenchmarkListResponse.md)

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

# **list_benchmarks_retrievers_0**
> BenchmarkListResponse list_benchmarks_retrievers_0(retriever_id=retriever_id, status=status, page=page, page_size=page_size, authorization=authorization, x_namespace=x_namespace)

List benchmarks

List benchmarks with optional filtering

### Example


```python
import mixpeek
from mixpeek.models.benchmark_list_response import BenchmarkListResponse
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
    api_instance = mixpeek.RetrieverBenchmarksApi(api_client)
    retriever_id = 'retriever_id_example' # str | Filter to benchmarks involving this retriever (as baseline or candidate) (optional)
    status = 'status_example' # str | Filter by status (pending, building_sessions, replaying, completed, failed) (optional)
    page = 1 # int | Page number (optional) (default to 1)
    page_size = 20 # int | Items per page (optional) (default to 20)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # List benchmarks
        api_response = api_instance.list_benchmarks_retrievers_0(retriever_id=retriever_id, status=status, page=page, page_size=page_size, authorization=authorization, x_namespace=x_namespace)
        print("The response of RetrieverBenchmarksApi->list_benchmarks_retrievers_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrieverBenchmarksApi->list_benchmarks_retrievers_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retriever_id** | **str**| Filter to benchmarks involving this retriever (as baseline or candidate) | [optional] 
 **status** | **str**| Filter by status (pending, building_sessions, replaying, completed, failed) | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **page_size** | **int**| Items per page | [optional] [default to 20]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**BenchmarkListResponse**](BenchmarkListResponse.md)

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

