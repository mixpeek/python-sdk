# mixpeek.MarketplaceApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_subscription_marketplace**](MarketplaceApi.md#cancel_subscription_marketplace) | **DELETE** /v1/marketplace/subscriptions/{subscription_id} | Cancel Subscription
[**create_marketplace_listing**](MarketplaceApi.md#create_marketplace_listing) | **POST** /v1/marketplace/listings | Create Marketplace Listing
[**create_subscription_marketplace**](MarketplaceApi.md#create_subscription_marketplace) | **POST** /v1/marketplace/subscriptions | Subscribe to Marketplace Listing
[**delete_marketplace_listing**](MarketplaceApi.md#delete_marketplace_listing) | **DELETE** /v1/marketplace/listings/{listing_id} | Delete Marketplace Listing
[**execute_marketplace_retriever_catalog_name**](MarketplaceApi.md#execute_marketplace_retriever_catalog_name) | **POST** /v1/marketplace/catalog/{public_name}/execute | Execute Marketplace Retriever
[**get_marketplace_catalog**](MarketplaceApi.md#get_marketplace_catalog) | **GET** /v1/marketplace/catalog | Browse Marketplace Catalog
[**get_marketplace_listing_by_name_catalog**](MarketplaceApi.md#get_marketplace_listing_by_name_catalog) | **GET** /v1/marketplace/catalog/{public_name} | Get Marketplace Listing by Public Name
[**get_marketplace_listing_config_catalog_name**](MarketplaceApi.md#get_marketplace_listing_config_catalog_name) | **GET** /v1/marketplace/catalog/{public_name}/config | Get Marketplace Listing Configuration
[**get_marketplace_listing_template_catalog_name**](MarketplaceApi.md#get_marketplace_listing_template_catalog_name) | **GET** /v1/marketplace/catalog/{public_name}/template | Get Marketplace Listing as Template
[**get_subscription_marketplace**](MarketplaceApi.md#get_subscription_marketplace) | **GET** /v1/marketplace/subscriptions/{subscription_id} | Get Subscription Details
[**list_my_subscriptions_marketplace**](MarketplaceApi.md#list_my_subscriptions_marketplace) | **GET** /v1/marketplace/subscriptions | List My Subscriptions
[**publish_marketplace_listing**](MarketplaceApi.md#publish_marketplace_listing) | **PATCH** /v1/marketplace/listings/{listing_id}/publish | Publish Marketplace Listing
[**update_marketplace_listing**](MarketplaceApi.md#update_marketplace_listing) | **PATCH** /v1/marketplace/listings/{listing_id} | Update Marketplace Listing
[**verify_marketplace_listing_password_catalog_name**](MarketplaceApi.md#verify_marketplace_listing_password_catalog_name) | **POST** /v1/marketplace/catalog/{public_name}/verify | Verify Password for Marketplace Listing


# **cancel_subscription_marketplace**
> Dict[str, object] cancel_subscription_marketplace(subscription_id, authorization=authorization)

Cancel Subscription

Cancel a marketplace subscription.

Free Tier: Immediately revokes access
Paid Tiers: Cancels at end of billing period

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
    api_instance = mixpeek.MarketplaceApi(api_client)
    subscription_id = 'subscription_id_example' # str | Subscription ID to cancel
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Cancel Subscription
        api_response = api_instance.cancel_subscription_marketplace(subscription_id, authorization=authorization)
        print("The response of MarketplaceApi->cancel_subscription_marketplace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->cancel_subscription_marketplace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Subscription ID to cancel | 
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
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_marketplace_listing**
> MarketplaceListing create_marketplace_listing(request_body, authorization=authorization)

Create Marketplace Listing

Create a new marketplace listing for a retriever.

This endpoint allows retriever owners to publish their retrievers to the marketplace
with custom tiers, pricing, and display configuration.

### Example


```python
import mixpeek
from mixpeek.models.marketplace_listing import MarketplaceListing
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
    api_instance = mixpeek.MarketplaceApi(api_client)
    request_body = None # Dict[str, object] | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Create Marketplace Listing
        api_response = api_instance.create_marketplace_listing(request_body, authorization=authorization)
        print("The response of MarketplaceApi->create_marketplace_listing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->create_marketplace_listing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**MarketplaceListing**](MarketplaceListing.md)

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
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_subscription_marketplace**
> Dict[str, object] create_subscription_marketplace(body_create_subscription_v1_marketplace_subscriptions_post, authorization=authorization)

Subscribe to Marketplace Listing

Subscribe to a marketplace listing.

Free Tier:
    - Immediately active
    - Returns access_token (prk_xxx format)
    - No Stripe checkout required

Paid Tiers:
    - Creates pending subscription
    - Returns checkout_url for Stripe payment
    - Subscription activates after payment via webhook

### Example


```python
import mixpeek
from mixpeek.models.body_create_subscription_v1_marketplace_subscriptions_post import BodyCreateSubscriptionV1MarketplaceSubscriptionsPost
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
    api_instance = mixpeek.MarketplaceApi(api_client)
    body_create_subscription_v1_marketplace_subscriptions_post = mixpeek.BodyCreateSubscriptionV1MarketplaceSubscriptionsPost() # BodyCreateSubscriptionV1MarketplaceSubscriptionsPost | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Subscribe to Marketplace Listing
        api_response = api_instance.create_subscription_marketplace(body_create_subscription_v1_marketplace_subscriptions_post, authorization=authorization)
        print("The response of MarketplaceApi->create_subscription_marketplace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->create_subscription_marketplace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_create_subscription_v1_marketplace_subscriptions_post** | [**BodyCreateSubscriptionV1MarketplaceSubscriptionsPost**](BodyCreateSubscriptionV1MarketplaceSubscriptionsPost.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

**Dict[str, object]**

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
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_marketplace_listing**
> object delete_marketplace_listing(listing_id, authorization=authorization)

Delete Marketplace Listing

Delete a marketplace listing.

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
    api_instance = mixpeek.MarketplaceApi(api_client)
    listing_id = 'listing_id_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Delete Marketplace Listing
        api_response = api_instance.delete_marketplace_listing(listing_id, authorization=authorization)
        print("The response of MarketplaceApi->delete_marketplace_listing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->delete_marketplace_listing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listing_id** | **str**|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

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
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_marketplace_retriever_catalog_name**
> object execute_marketplace_retriever_catalog_name(public_name, retriever_execution_request, return_presigned_urls=return_presigned_urls, return_vectors=return_vectors, authorization=authorization)

Execute Marketplace Retriever

Execute a marketplace retriever using its public name. Free tier listings can be accessed without authentication. Paid tier access requires a subscription token.

### Example


```python
import mixpeek
from mixpeek.models.retriever_execution_request import RetrieverExecutionRequest
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
    api_instance = mixpeek.MarketplaceApi(api_client)
    public_name = 'public_name_example' # str | Public name of the marketplace listing
    retriever_execution_request = mixpeek.RetrieverExecutionRequest() # RetrieverExecutionRequest | 
    return_presigned_urls = True # bool | Generate fresh presigned download URLs for all blobs with S3 storage (optional) (default to True)
    return_vectors = False # bool | Include vector embeddings in response (optional) (default to False)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Execute Marketplace Retriever
        api_response = api_instance.execute_marketplace_retriever_catalog_name(public_name, retriever_execution_request, return_presigned_urls=return_presigned_urls, return_vectors=return_vectors, authorization=authorization)
        print("The response of MarketplaceApi->execute_marketplace_retriever_catalog_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->execute_marketplace_retriever_catalog_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_name** | **str**| Public name of the marketplace listing | 
 **retriever_execution_request** | [**RetrieverExecutionRequest**](RetrieverExecutionRequest.md)|  | 
 **return_presigned_urls** | **bool**| Generate fresh presigned download URLs for all blobs with S3 storage | [optional] [default to True]
 **return_vectors** | **bool**| Include vector embeddings in response | [optional] [default to False]
 **authorization** | **str**|  | [optional] 

### Return type

**object**

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
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_marketplace_catalog**
> List[MarketplaceListing] get_marketplace_catalog(category=category, tags=tags, search=search, skip=skip, limit=limit)

Browse Marketplace Catalog

Browse marketplace catalog with optional filters.

Returns published, listed marketplace listings only. Unlisted retrievers
are still accessible via direct link but don't appear here.

### Example


```python
import mixpeek
from mixpeek.models.marketplace_listing import MarketplaceListing
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
    api_instance = mixpeek.MarketplaceApi(api_client)
    category = 'category_example' # str | Filter by category (e.g., 'Content Moderation', 'Search') (optional)
    tags = ['tags_example'] # List[str] | Filter by tags (AND logic - listing must have all tags) (optional)
    search = 'search_example' # str | Search in title and description (optional)
    skip = 0 # int | Number of listings to skip (optional) (default to 0)
    limit = 20 # int | Number of listings to return (optional) (default to 20)

    try:
        # Browse Marketplace Catalog
        api_response = api_instance.get_marketplace_catalog(category=category, tags=tags, search=search, skip=skip, limit=limit)
        print("The response of MarketplaceApi->get_marketplace_catalog:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->get_marketplace_catalog: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**| Filter by category (e.g., &#39;Content Moderation&#39;, &#39;Search&#39;) | [optional] 
 **tags** | [**List[str]**](str.md)| Filter by tags (AND logic - listing must have all tags) | [optional] 
 **search** | **str**| Search in title and description | [optional] 
 **skip** | **int**| Number of listings to skip | [optional] [default to 0]
 **limit** | **int**| Number of listings to return | [optional] [default to 20]

### Return type

[**List[MarketplaceListing]**](MarketplaceListing.md)

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
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_marketplace_listing_by_name_catalog**
> MarketplaceListing get_marketplace_listing_by_name_catalog(public_name)

Get Marketplace Listing by Public Name

Get detailed information about a marketplace listing by its public name.

Example: /marketplace/catalog/brand-safety-api

### Example


```python
import mixpeek
from mixpeek.models.marketplace_listing import MarketplaceListing
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
    api_instance = mixpeek.MarketplaceApi(api_client)
    public_name = 'public_name_example' # str | Public URL slug for the listing

    try:
        # Get Marketplace Listing by Public Name
        api_response = api_instance.get_marketplace_listing_by_name_catalog(public_name)
        print("The response of MarketplaceApi->get_marketplace_listing_by_name_catalog:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->get_marketplace_listing_by_name_catalog: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_name** | **str**| Public URL slug for the listing | 

### Return type

[**MarketplaceListing**](MarketplaceListing.md)

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
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_marketplace_listing_config_catalog_name**
> object get_marketplace_listing_config_catalog_name(public_name)

Get Marketplace Listing Configuration

Get display configuration for rendering the marketplace listing interface

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
    api_instance = mixpeek.MarketplaceApi(api_client)
    public_name = 'public_name_example' # str | Public name of the marketplace listing

    try:
        # Get Marketplace Listing Configuration
        api_response = api_instance.get_marketplace_listing_config_catalog_name(public_name)
        print("The response of MarketplaceApi->get_marketplace_listing_config_catalog_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->get_marketplace_listing_config_catalog_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_name** | **str**| Public name of the marketplace listing | 

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
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_marketplace_listing_template_catalog_name**
> object get_marketplace_listing_template_catalog_name(public_name)

Get Marketplace Listing as Template

Get the retriever configuration from a marketplace listing as a reusable template

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
    api_instance = mixpeek.MarketplaceApi(api_client)
    public_name = 'public_name_example' # str | Public name of the marketplace listing

    try:
        # Get Marketplace Listing as Template
        api_response = api_instance.get_marketplace_listing_template_catalog_name(public_name)
        print("The response of MarketplaceApi->get_marketplace_listing_template_catalog_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->get_marketplace_listing_template_catalog_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_name** | **str**| Public name of the marketplace listing | 

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
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_marketplace**
> Dict[str, object] get_subscription_marketplace(subscription_id, authorization=authorization)

Get Subscription Details

Get detailed information about a subscription.

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
    api_instance = mixpeek.MarketplaceApi(api_client)
    subscription_id = 'subscription_id_example' # str | Subscription ID
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Get Subscription Details
        api_response = api_instance.get_subscription_marketplace(subscription_id, authorization=authorization)
        print("The response of MarketplaceApi->get_subscription_marketplace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->get_subscription_marketplace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Subscription ID | 
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
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_my_subscriptions_marketplace**
> List[Dict[str, object]] list_my_subscriptions_marketplace(status=status, authorization=authorization)

List My Subscriptions

List all subscriptions for the current organization.

### Example


```python
import mixpeek
from mixpeek.models.subscription_status import SubscriptionStatus
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
    api_instance = mixpeek.MarketplaceApi(api_client)
    status = mixpeek.SubscriptionStatus() # SubscriptionStatus | Filter by subscription status (optional)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # List My Subscriptions
        api_response = api_instance.list_my_subscriptions_marketplace(status=status, authorization=authorization)
        print("The response of MarketplaceApi->list_my_subscriptions_marketplace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->list_my_subscriptions_marketplace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | [**SubscriptionStatus**](.md)| Filter by subscription status | [optional] 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

**List[Dict[str, object]]**

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
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish_marketplace_listing**
> MarketplaceListing publish_marketplace_listing(listing_id, authorization=authorization)

Publish Marketplace Listing

Publish a marketplace listing (change status from draft to published).

### Example


```python
import mixpeek
from mixpeek.models.marketplace_listing import MarketplaceListing
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
    api_instance = mixpeek.MarketplaceApi(api_client)
    listing_id = 'listing_id_example' # str | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Publish Marketplace Listing
        api_response = api_instance.publish_marketplace_listing(listing_id, authorization=authorization)
        print("The response of MarketplaceApi->publish_marketplace_listing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->publish_marketplace_listing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listing_id** | **str**|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**MarketplaceListing**](MarketplaceListing.md)

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
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_marketplace_listing**
> MarketplaceListing update_marketplace_listing(listing_id, request_body, authorization=authorization)

Update Marketplace Listing

Update an existing marketplace listing.

### Example


```python
import mixpeek
from mixpeek.models.marketplace_listing import MarketplaceListing
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
    api_instance = mixpeek.MarketplaceApi(api_client)
    listing_id = 'listing_id_example' # str | 
    request_body = None # Dict[str, object] | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Update Marketplace Listing
        api_response = api_instance.update_marketplace_listing(listing_id, request_body, authorization=authorization)
        print("The response of MarketplaceApi->update_marketplace_listing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->update_marketplace_listing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listing_id** | **str**|  | 
 **request_body** | [**Dict[str, object]**](object.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**MarketplaceListing**](MarketplaceListing.md)

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
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_marketplace_listing_password_catalog_name**
> object verify_marketplace_listing_password_catalog_name(public_name, body_verify_marketplace_listing_password_v1_marketplace_catalog_public_name_verify_post)

Verify Password for Marketplace Listing

Verify password for a password-protected marketplace listing

### Example


```python
import mixpeek
from mixpeek.models.body_verify_marketplace_listing_password_v1_marketplace_catalog_public_name_verify_post import BodyVerifyMarketplaceListingPasswordV1MarketplaceCatalogPublicNameVerifyPost
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
    api_instance = mixpeek.MarketplaceApi(api_client)
    public_name = 'public_name_example' # str | Public name of the marketplace listing
    body_verify_marketplace_listing_password_v1_marketplace_catalog_public_name_verify_post = mixpeek.BodyVerifyMarketplaceListingPasswordV1MarketplaceCatalogPublicNameVerifyPost() # BodyVerifyMarketplaceListingPasswordV1MarketplaceCatalogPublicNameVerifyPost | 

    try:
        # Verify Password for Marketplace Listing
        api_response = api_instance.verify_marketplace_listing_password_catalog_name(public_name, body_verify_marketplace_listing_password_v1_marketplace_catalog_public_name_verify_post)
        print("The response of MarketplaceApi->verify_marketplace_listing_password_catalog_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->verify_marketplace_listing_password_catalog_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_name** | **str**| Public name of the marketplace listing | 
 **body_verify_marketplace_listing_password_v1_marketplace_catalog_public_name_verify_post** | [**BodyVerifyMarketplaceListingPasswordV1MarketplaceCatalogPublicNameVerifyPost**](BodyVerifyMarketplaceListingPasswordV1MarketplaceCatalogPublicNameVerifyPost.md)|  | 

### Return type

**object**

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
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

