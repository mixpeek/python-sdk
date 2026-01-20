# mixpeek.HealthApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**healthcheck_health**](HealthApi.md#healthcheck_health) | **GET** /v1/health | Healthcheck
[**healthcheck_health_0**](HealthApi.md#healthcheck_health_0) | **GET** /v1/health | Healthcheck
[**liveness_health**](HealthApi.md#liveness_health) | **GET** /v1/health/liveness | Liveness
[**liveness_health_0**](HealthApi.md#liveness_health_0) | **GET** /v1/health/liveness | Liveness


# **healthcheck_health**
> HealthCheckResponse healthcheck_health(deep=deep, metrics=metrics)

Healthcheck

Health check endpoint.

### Example


```python
import mixpeek
from mixpeek.models.health_check_response import HealthCheckResponse
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
    api_instance = mixpeek.HealthApi(api_client)
    deep = False # bool |  (optional) (default to False)
    metrics = False # bool | Include Layer 2 protection metrics (optional) (default to False)

    try:
        # Healthcheck
        api_response = api_instance.healthcheck_health(deep=deep, metrics=metrics)
        print("The response of HealthApi->healthcheck_health:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthApi->healthcheck_health: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deep** | **bool**|  | [optional] [default to False]
 **metrics** | **bool**| Include Layer 2 protection metrics | [optional] [default to False]

### Return type

[**HealthCheckResponse**](HealthCheckResponse.md)

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

# **healthcheck_health_0**
> HealthCheckResponse healthcheck_health_0(deep=deep, metrics=metrics)

Healthcheck

Health check endpoint.

### Example


```python
import mixpeek
from mixpeek.models.health_check_response import HealthCheckResponse
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
    api_instance = mixpeek.HealthApi(api_client)
    deep = False # bool |  (optional) (default to False)
    metrics = False # bool | Include Layer 2 protection metrics (optional) (default to False)

    try:
        # Healthcheck
        api_response = api_instance.healthcheck_health_0(deep=deep, metrics=metrics)
        print("The response of HealthApi->healthcheck_health_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthApi->healthcheck_health_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deep** | **bool**|  | [optional] [default to False]
 **metrics** | **bool**| Include Layer 2 protection metrics | [optional] [default to False]

### Return type

[**HealthCheckResponse**](HealthCheckResponse.md)

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

# **liveness_health**
> object liveness_health()

Liveness

Lightweight liveness probe for container orchestration (Render, K8s).

This endpoint returns immediately without checking external services.
Use this for Render health checks to avoid timeouts when services are slow.

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
    api_instance = mixpeek.HealthApi(api_client)

    try:
        # Liveness
        api_response = api_instance.liveness_health()
        print("The response of HealthApi->liveness_health:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthApi->liveness_health: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **liveness_health_0**
> object liveness_health_0()

Liveness

Lightweight liveness probe for container orchestration (Render, K8s).

This endpoint returns immediately without checking external services.
Use this for Render health checks to avoid timeouts when services are slow.

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
    api_instance = mixpeek.HealthApi(api_client)

    try:
        # Liveness
        api_response = api_instance.liveness_health_0()
        print("The response of HealthApi->liveness_health_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthApi->liveness_health_0: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

