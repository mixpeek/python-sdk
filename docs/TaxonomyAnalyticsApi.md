# mixpeek.TaxonomyAnalyticsApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyze_transition_paths_taxonomies_taxonomy_id_analytics**](TaxonomyAnalyticsApi.md#analyze_transition_paths_taxonomies_taxonomy_id_analytics) | **POST** /v1/taxonomies/{taxonomy_id}/analytics/paths | Analyze multi-step transition paths
[**analyze_transition_paths_taxonomies_taxonomy_id_analytics_0**](TaxonomyAnalyticsApi.md#analyze_transition_paths_taxonomies_taxonomy_id_analytics_0) | **POST** /v1/taxonomies/{taxonomy_id}/analytics/paths | Analyze multi-step transition paths
[**compute_step_transitions_taxonomies_taxonomy_id_analytics**](TaxonomyAnalyticsApi.md#compute_step_transitions_taxonomies_taxonomy_id_analytics) | **POST** /v1/taxonomies/{taxonomy_id}/analytics/transitions | Compute step transition analytics
[**compute_step_transitions_taxonomies_taxonomy_id_analytics_0**](TaxonomyAnalyticsApi.md#compute_step_transitions_taxonomies_taxonomy_id_analytics_0) | **POST** /v1/taxonomies/{taxonomy_id}/analytics/transitions | Compute step transition analytics
[**get_available_steps_taxonomies_taxonomy_id_analytics**](TaxonomyAnalyticsApi.md#get_available_steps_taxonomies_taxonomy_id_analytics) | **GET** /v1/taxonomies/{taxonomy_id}/analytics/available-steps | Get Available Steps
[**get_available_steps_taxonomies_taxonomy_id_analytics_0**](TaxonomyAnalyticsApi.md#get_available_steps_taxonomies_taxonomy_id_analytics_0) | **GET** /v1/taxonomies/{taxonomy_id}/analytics/available-steps | Get Available Steps


# **analyze_transition_paths_taxonomies_taxonomy_id_analytics**
> PathAnalysisResponse analyze_transition_paths_taxonomies_taxonomy_id_analytics(taxonomy_id, path_analysis_request, authorization=authorization, x_namespace=x_namespace)

Analyze multi-step transition paths

Discover the most common multi-step paths documents take between two taxonomy steps.

Unlike the `/transitions` endpoint which only analyzes direct A→B transitions,
this endpoint reveals the intermediate steps documents actually take.

## Use Cases

**Email Thread Analysis:**
- Question: What paths do emails take from "inquiry" to "closed_won"?
- Discover: Some go inquiry → followup → proposal → closed_won
- Discover: Others skip steps: inquiry → proposal → closed_won
- Discover: Fast track: inquiry → closed_won

**Content Editorial Paths:**
- Question: Common paths from "draft" to "published"?
- Discover: draft → review → edit → review → published
- Discover: draft → review → published (expedited)
- Discover: Paths that loop back (draft → review → draft → review)

**Compliance Resolution Paths:**
- Question: How do violations get resolved?
- Discover: violation → investigated → remediated → resolved
- Discover: violation → false_positive → closed
- Discover: Escalation paths: violation → escalated → legal_review → resolved

## Requirements

- Taxonomy must have `step_analytics` configured
- Collection must contain documents with timestamp and sequence_id fields

## Returns

**Completion Metrics:**
- `total_sequences`: Sequences starting at from_step
- `completed_sequences`: Number reaching to_step
- `completion_rate`: Percentage that completed

**Paths (sorted by frequency):**
- `path`: Ordered sequence of steps
- `count`: Number of sequences following this path
- `percentage`: Percentage of completing sequences
- `avg_duration_sec`: Average time for this path

## Example Request

```json
{
    "collection_id": "col_emails",
    "taxonomy_id": "tax_sales_stages",
    "from_step": "inquiry",
    "to_step": "closed_won",
    "max_path_length": 10,
    "min_support": 5
}
```

## Example Response

```json
{
    "from_step": "inquiry",
    "to_step": "closed_won",
    "total_sequences": 1000,
    "completed_sequences": 350,
    "completion_rate": 0.35,
    "paths": [
        {
            "path": ["inquiry", "followup", "proposal", "closed_won"],
            "count": 120,
            "percentage": 34.3,
            "avg_duration_sec": 604800.0
        },
        {
            "path": ["inquiry", "proposal", "closed_won"],
            "count": 90,
            "percentage": 25.7,
            "avg_duration_sec": 432000.0
        },
        {
            "path": ["inquiry", "closed_won"],
            "count": 70,
            "percentage": 20.0,
            "avg_duration_sec": 172800.0
        }
    ]
}
```

## Path Interpretation

**Length Analysis:**
- Shorter paths indicate efficient progression
- Longer paths may indicate complexity or bottlenecks
- Loops (repeated steps) indicate rework or revisions

**Duration Analysis:**
- Compare avg_duration_sec across paths
- Shorter paths may not always be faster
- Identify optimization opportunities

**Frequency Analysis:**
- High-percentage paths are "happy paths"
- Low-percentage paths may be edge cases or exceptions
- Missing expected paths indicate drop-off points

### Example


```python
import mixpeek
from mixpeek.models.path_analysis_request import PathAnalysisRequest
from mixpeek.models.path_analysis_response import PathAnalysisResponse
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
    api_instance = mixpeek.TaxonomyAnalyticsApi(api_client)
    taxonomy_id = 'taxonomy_id_example' # str | 
    path_analysis_request = mixpeek.PathAnalysisRequest() # PathAnalysisRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Analyze multi-step transition paths
        api_response = api_instance.analyze_transition_paths_taxonomies_taxonomy_id_analytics(taxonomy_id, path_analysis_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of TaxonomyAnalyticsApi->analyze_transition_paths_taxonomies_taxonomy_id_analytics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomyAnalyticsApi->analyze_transition_paths_taxonomies_taxonomy_id_analytics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxonomy_id** | **str**|  | 
 **path_analysis_request** | [**PathAnalysisRequest**](PathAnalysisRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**PathAnalysisResponse**](PathAnalysisResponse.md)

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

# **analyze_transition_paths_taxonomies_taxonomy_id_analytics_0**
> PathAnalysisResponse analyze_transition_paths_taxonomies_taxonomy_id_analytics_0(taxonomy_id, path_analysis_request, authorization=authorization, x_namespace=x_namespace)

Analyze multi-step transition paths

Discover the most common multi-step paths documents take between two taxonomy steps.

Unlike the `/transitions` endpoint which only analyzes direct A→B transitions,
this endpoint reveals the intermediate steps documents actually take.

## Use Cases

**Email Thread Analysis:**
- Question: What paths do emails take from "inquiry" to "closed_won"?
- Discover: Some go inquiry → followup → proposal → closed_won
- Discover: Others skip steps: inquiry → proposal → closed_won
- Discover: Fast track: inquiry → closed_won

**Content Editorial Paths:**
- Question: Common paths from "draft" to "published"?
- Discover: draft → review → edit → review → published
- Discover: draft → review → published (expedited)
- Discover: Paths that loop back (draft → review → draft → review)

**Compliance Resolution Paths:**
- Question: How do violations get resolved?
- Discover: violation → investigated → remediated → resolved
- Discover: violation → false_positive → closed
- Discover: Escalation paths: violation → escalated → legal_review → resolved

## Requirements

- Taxonomy must have `step_analytics` configured
- Collection must contain documents with timestamp and sequence_id fields

## Returns

**Completion Metrics:**
- `total_sequences`: Sequences starting at from_step
- `completed_sequences`: Number reaching to_step
- `completion_rate`: Percentage that completed

**Paths (sorted by frequency):**
- `path`: Ordered sequence of steps
- `count`: Number of sequences following this path
- `percentage`: Percentage of completing sequences
- `avg_duration_sec`: Average time for this path

## Example Request

```json
{
    "collection_id": "col_emails",
    "taxonomy_id": "tax_sales_stages",
    "from_step": "inquiry",
    "to_step": "closed_won",
    "max_path_length": 10,
    "min_support": 5
}
```

## Example Response

```json
{
    "from_step": "inquiry",
    "to_step": "closed_won",
    "total_sequences": 1000,
    "completed_sequences": 350,
    "completion_rate": 0.35,
    "paths": [
        {
            "path": ["inquiry", "followup", "proposal", "closed_won"],
            "count": 120,
            "percentage": 34.3,
            "avg_duration_sec": 604800.0
        },
        {
            "path": ["inquiry", "proposal", "closed_won"],
            "count": 90,
            "percentage": 25.7,
            "avg_duration_sec": 432000.0
        },
        {
            "path": ["inquiry", "closed_won"],
            "count": 70,
            "percentage": 20.0,
            "avg_duration_sec": 172800.0
        }
    ]
}
```

## Path Interpretation

**Length Analysis:**
- Shorter paths indicate efficient progression
- Longer paths may indicate complexity or bottlenecks
- Loops (repeated steps) indicate rework or revisions

**Duration Analysis:**
- Compare avg_duration_sec across paths
- Shorter paths may not always be faster
- Identify optimization opportunities

**Frequency Analysis:**
- High-percentage paths are "happy paths"
- Low-percentage paths may be edge cases or exceptions
- Missing expected paths indicate drop-off points

### Example


```python
import mixpeek
from mixpeek.models.path_analysis_request import PathAnalysisRequest
from mixpeek.models.path_analysis_response import PathAnalysisResponse
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
    api_instance = mixpeek.TaxonomyAnalyticsApi(api_client)
    taxonomy_id = 'taxonomy_id_example' # str | 
    path_analysis_request = mixpeek.PathAnalysisRequest() # PathAnalysisRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Analyze multi-step transition paths
        api_response = api_instance.analyze_transition_paths_taxonomies_taxonomy_id_analytics_0(taxonomy_id, path_analysis_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of TaxonomyAnalyticsApi->analyze_transition_paths_taxonomies_taxonomy_id_analytics_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomyAnalyticsApi->analyze_transition_paths_taxonomies_taxonomy_id_analytics_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxonomy_id** | **str**|  | 
 **path_analysis_request** | [**PathAnalysisRequest**](PathAnalysisRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**PathAnalysisResponse**](PathAnalysisResponse.md)

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

# **compute_step_transitions_taxonomies_taxonomy_id_analytics**
> StepTransitionResponse compute_step_transitions_taxonomies_taxonomy_id_analytics(taxonomy_id, step_transition_request, authorization=authorization, x_namespace=x_namespace)

Compute step transition analytics

Analyze how documents progress from one taxonomy step to another.

This endpoint computes conversion rates, duration statistics, and predictor lifts
for documents transitioning between taxonomy labels.

## Use Cases

**Email Thread Analysis:**
- Question: How long from "inquiry" to "closed_won"?
- Question: What % of inquiries result in sales?
- Question: Which sender domains have highest conversion?

**Content Workflow Tracking:**
- Question: Conversion rate from "draft" to "published"?
- Question: How long does content stay in review?
- Question: Which authors publish fastest?

**Safety Compliance Monitoring:**
- Question: Time from violation detection to resolution?
- Question: Success rate for remediation efforts?

## Requirements

- Taxonomy must have `step_analytics` configured (or provide `override_step_analytics`)
- Collection must contain documents enriched with this taxonomy
- Documents must have timestamp and sequence grouping fields configured

## Returns

**Conversion Metrics:**
- `count`: Total sequences starting at from_step
- `converted`: Number reaching to_step
- `conversion_rate`: Percentage that converted

**Duration Statistics (if converted > 0):**
- `mean`, `median`: Average and middle duration
- `p90`, `p95`: 90th and 95th percentile durations
- `std_dev`, `min`, `max`: Distribution statistics

**Top Predictors:**
- Covariates with highest impact on conversion
- Lift values (>1.0 = increases conversion, <1.0 = decreases)
- Statistical significance via minimum support threshold

## Example Request

```json
{
    "collection_id": "col_emails",
    "taxonomy_id": "tax_sales_stages",
    "from_step": "inquiry",
    "to_step": "closed_won",
    "max_window_days": 90,
    "min_support": 10
}
```

## Example Response

```json
{
    "from_step": "inquiry",
    "to_step": "closed_won",
    "count": 1000,
    "converted": 350,
    "conversion_rate": 0.35,
    "durations_sec": {
        "mean": 432000.0,
        "median": 345600.0,
        "p50": 345600.0,
        "p90": 691200.0,
        "p95": 864000.0
    },
    "top_predictors": [
        {
            "field": "Sender Domain",
            "value": "enterprise.com",
            "count": 150,
            "conversion_rate": 0.75,
            "lift": 2.14
        }
    ]
}
```

### Example


```python
import mixpeek
from mixpeek.models.step_transition_request import StepTransitionRequest
from mixpeek.models.step_transition_response import StepTransitionResponse
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
    api_instance = mixpeek.TaxonomyAnalyticsApi(api_client)
    taxonomy_id = 'taxonomy_id_example' # str | 
    step_transition_request = mixpeek.StepTransitionRequest() # StepTransitionRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Compute step transition analytics
        api_response = api_instance.compute_step_transitions_taxonomies_taxonomy_id_analytics(taxonomy_id, step_transition_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of TaxonomyAnalyticsApi->compute_step_transitions_taxonomies_taxonomy_id_analytics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomyAnalyticsApi->compute_step_transitions_taxonomies_taxonomy_id_analytics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxonomy_id** | **str**|  | 
 **step_transition_request** | [**StepTransitionRequest**](StepTransitionRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**StepTransitionResponse**](StepTransitionResponse.md)

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

# **compute_step_transitions_taxonomies_taxonomy_id_analytics_0**
> StepTransitionResponse compute_step_transitions_taxonomies_taxonomy_id_analytics_0(taxonomy_id, step_transition_request, authorization=authorization, x_namespace=x_namespace)

Compute step transition analytics

Analyze how documents progress from one taxonomy step to another.

This endpoint computes conversion rates, duration statistics, and predictor lifts
for documents transitioning between taxonomy labels.

## Use Cases

**Email Thread Analysis:**
- Question: How long from "inquiry" to "closed_won"?
- Question: What % of inquiries result in sales?
- Question: Which sender domains have highest conversion?

**Content Workflow Tracking:**
- Question: Conversion rate from "draft" to "published"?
- Question: How long does content stay in review?
- Question: Which authors publish fastest?

**Safety Compliance Monitoring:**
- Question: Time from violation detection to resolution?
- Question: Success rate for remediation efforts?

## Requirements

- Taxonomy must have `step_analytics` configured (or provide `override_step_analytics`)
- Collection must contain documents enriched with this taxonomy
- Documents must have timestamp and sequence grouping fields configured

## Returns

**Conversion Metrics:**
- `count`: Total sequences starting at from_step
- `converted`: Number reaching to_step
- `conversion_rate`: Percentage that converted

**Duration Statistics (if converted > 0):**
- `mean`, `median`: Average and middle duration
- `p90`, `p95`: 90th and 95th percentile durations
- `std_dev`, `min`, `max`: Distribution statistics

**Top Predictors:**
- Covariates with highest impact on conversion
- Lift values (>1.0 = increases conversion, <1.0 = decreases)
- Statistical significance via minimum support threshold

## Example Request

```json
{
    "collection_id": "col_emails",
    "taxonomy_id": "tax_sales_stages",
    "from_step": "inquiry",
    "to_step": "closed_won",
    "max_window_days": 90,
    "min_support": 10
}
```

## Example Response

```json
{
    "from_step": "inquiry",
    "to_step": "closed_won",
    "count": 1000,
    "converted": 350,
    "conversion_rate": 0.35,
    "durations_sec": {
        "mean": 432000.0,
        "median": 345600.0,
        "p50": 345600.0,
        "p90": 691200.0,
        "p95": 864000.0
    },
    "top_predictors": [
        {
            "field": "Sender Domain",
            "value": "enterprise.com",
            "count": 150,
            "conversion_rate": 0.75,
            "lift": 2.14
        }
    ]
}
```

### Example


```python
import mixpeek
from mixpeek.models.step_transition_request import StepTransitionRequest
from mixpeek.models.step_transition_response import StepTransitionResponse
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
    api_instance = mixpeek.TaxonomyAnalyticsApi(api_client)
    taxonomy_id = 'taxonomy_id_example' # str | 
    step_transition_request = mixpeek.StepTransitionRequest() # StepTransitionRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Compute step transition analytics
        api_response = api_instance.compute_step_transitions_taxonomies_taxonomy_id_analytics_0(taxonomy_id, step_transition_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of TaxonomyAnalyticsApi->compute_step_transitions_taxonomies_taxonomy_id_analytics_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomyAnalyticsApi->compute_step_transitions_taxonomies_taxonomy_id_analytics_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxonomy_id** | **str**|  | 
 **step_transition_request** | [**StepTransitionRequest**](StepTransitionRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**StepTransitionResponse**](StepTransitionResponse.md)

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

# **get_available_steps_taxonomies_taxonomy_id_analytics**
> AvailableStepsResponse get_available_steps_taxonomies_taxonomy_id_analytics(taxonomy_id, collection_id, authorization=authorization, x_namespace=x_namespace)

Get Available Steps

Get all available steps for a taxonomy and collection.

This endpoint discovers what steps exist in your analytics data by querying
the ClickHouse taxonomy_events table. Use this before querying transitions
or paths to understand what step values you can use.

**Use Cases:**
- Discover available steps before querying analytics
- Validate step names (avoid typos in from_step/to_step)
- See which steps have the most events
- Check data freshness (first_seen/last_seen timestamps)

**Example Usage:**
```python
# 1. Get available steps
GET /v1/taxonomies/tax_sales/analytics/available-steps?collection_id=col_emails

# Response:
{
    "taxonomy_id": "tax_sales",
    "collection_id": "col_emails",
    "total_events": 5432,
    "total_sequences": 1000,
    "steps": [
        {"step_key": "inquiry", "event_count": 1000, ...},
        {"step_key": "followup", "event_count": 450, ...},
        {"step_key": "closed_won", "event_count": 350, ...}
    ]
}

# 2. Use discovered steps in transition query
POST /v1/taxonomies/tax_sales/analytics/transitions
{
    "collection_id": "col_emails",
    "from_step": "inquiry",      # From available steps
    "to_step": "closed_won"      # From available steps
}
```

Args:
    request: FastAPI request object (contains tenant context)
    taxonomy_id: Taxonomy ID to query
    collection_id: Collection ID for filtering events

Returns:
    AvailableStepsResponse with all steps sorted by event count (descending)

Raises:
    NotFoundError: If taxonomy not found
    ValidationError: If unable to query ClickHouse

### Example


```python
import mixpeek
from mixpeek.models.available_steps_response import AvailableStepsResponse
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
    api_instance = mixpeek.TaxonomyAnalyticsApi(api_client)
    taxonomy_id = 'taxonomy_id_example' # str | 
    collection_id = 'collection_id_example' # str | Collection ID to analyze
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Available Steps
        api_response = api_instance.get_available_steps_taxonomies_taxonomy_id_analytics(taxonomy_id, collection_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of TaxonomyAnalyticsApi->get_available_steps_taxonomies_taxonomy_id_analytics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomyAnalyticsApi->get_available_steps_taxonomies_taxonomy_id_analytics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxonomy_id** | **str**|  | 
 **collection_id** | **str**| Collection ID to analyze | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**AvailableStepsResponse**](AvailableStepsResponse.md)

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

# **get_available_steps_taxonomies_taxonomy_id_analytics_0**
> AvailableStepsResponse get_available_steps_taxonomies_taxonomy_id_analytics_0(taxonomy_id, collection_id, authorization=authorization, x_namespace=x_namespace)

Get Available Steps

Get all available steps for a taxonomy and collection.

This endpoint discovers what steps exist in your analytics data by querying
the ClickHouse taxonomy_events table. Use this before querying transitions
or paths to understand what step values you can use.

**Use Cases:**
- Discover available steps before querying analytics
- Validate step names (avoid typos in from_step/to_step)
- See which steps have the most events
- Check data freshness (first_seen/last_seen timestamps)

**Example Usage:**
```python
# 1. Get available steps
GET /v1/taxonomies/tax_sales/analytics/available-steps?collection_id=col_emails

# Response:
{
    "taxonomy_id": "tax_sales",
    "collection_id": "col_emails",
    "total_events": 5432,
    "total_sequences": 1000,
    "steps": [
        {"step_key": "inquiry", "event_count": 1000, ...},
        {"step_key": "followup", "event_count": 450, ...},
        {"step_key": "closed_won", "event_count": 350, ...}
    ]
}

# 2. Use discovered steps in transition query
POST /v1/taxonomies/tax_sales/analytics/transitions
{
    "collection_id": "col_emails",
    "from_step": "inquiry",      # From available steps
    "to_step": "closed_won"      # From available steps
}
```

Args:
    request: FastAPI request object (contains tenant context)
    taxonomy_id: Taxonomy ID to query
    collection_id: Collection ID for filtering events

Returns:
    AvailableStepsResponse with all steps sorted by event count (descending)

Raises:
    NotFoundError: If taxonomy not found
    ValidationError: If unable to query ClickHouse

### Example


```python
import mixpeek
from mixpeek.models.available_steps_response import AvailableStepsResponse
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
    api_instance = mixpeek.TaxonomyAnalyticsApi(api_client)
    taxonomy_id = 'taxonomy_id_example' # str | 
    collection_id = 'collection_id_example' # str | Collection ID to analyze
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Get Available Steps
        api_response = api_instance.get_available_steps_taxonomies_taxonomy_id_analytics_0(taxonomy_id, collection_id, authorization=authorization, x_namespace=x_namespace)
        print("The response of TaxonomyAnalyticsApi->get_available_steps_taxonomies_taxonomy_id_analytics_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxonomyAnalyticsApi->get_available_steps_taxonomies_taxonomy_id_analytics_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxonomy_id** | **str**|  | 
 **collection_id** | **str**| Collection ID to analyze | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**AvailableStepsResponse**](AvailableStepsResponse.md)

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

