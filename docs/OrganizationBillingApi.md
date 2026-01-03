# mixpeek.OrganizationBillingApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**confirm_payment_method_organizations_billing**](OrganizationBillingApi.md#confirm_payment_method_organizations_billing) | **POST** /v1/organizations/billing/confirm-payment-method | Confirm Payment Method
[**disable_auto_billing_organizations**](OrganizationBillingApi.md#disable_auto_billing_organizations) | **POST** /v1/organizations/billing/disable-auto-billing | Disable Auto Billing
[**enable_auto_billing_organizations**](OrganizationBillingApi.md#enable_auto_billing_organizations) | **POST** /v1/organizations/billing/enable-auto-billing | Enable Auto Billing
[**get_current_usage_organizations_billing**](OrganizationBillingApi.md#get_current_usage_organizations_billing) | **GET** /v1/organizations/billing/usage/current | Get Current Usage
[**get_payment_method_organizations_billing**](OrganizationBillingApi.md#get_payment_method_organizations_billing) | **GET** /v1/organizations/billing/payment-method | Get Payment Method
[**get_spending_caps_organizations_billing**](OrganizationBillingApi.md#get_spending_caps_organizations_billing) | **GET** /v1/organizations/billing/spending-caps | Get Spending Caps
[**get_usage_breakdown_organizations_billing**](OrganizationBillingApi.md#get_usage_breakdown_organizations_billing) | **GET** /v1/organizations/billing/usage/breakdown | Get Usage Breakdown
[**list_invoices_organizations_billing**](OrganizationBillingApi.md#list_invoices_organizations_billing) | **GET** /v1/organizations/billing/invoices | List Invoices
[**setup_payment_method_organizations_billing**](OrganizationBillingApi.md#setup_payment_method_organizations_billing) | **POST** /v1/organizations/billing/setup-payment-method | Setup Payment Method
[**update_spending_caps_organizations_billing**](OrganizationBillingApi.md#update_spending_caps_organizations_billing) | **POST** /v1/organizations/billing/spending-caps | Update Spending Caps


# **confirm_payment_method_organizations_billing**
> ConfirmPaymentMethodResponse confirm_payment_method_organizations_billing(confirm_payment_method_request, authorization=authorization)

Confirm Payment Method

Confirm payment method after frontend collects it.

After Stripe Elements confirms the SetupIntent, call this endpoint
to attach the payment method to the customer and enable auto-billing.

**Requirements:**
- Admin permission
- Must have called setup-payment-method first

**Example:**
```python
# After Stripe Elements confirms setup
response = await client.post(
    "/v1/organizations/billing/confirm-payment-method",
    json={"payment_method_id": "pm_1ABC2DEF3GHI"}
)
```

### Example


```python
import mixpeek
from mixpeek.models.confirm_payment_method_request import ConfirmPaymentMethodRequest
from mixpeek.models.confirm_payment_method_response import ConfirmPaymentMethodResponse
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
    api_instance = mixpeek.OrganizationBillingApi(api_client)
    confirm_payment_method_request = mixpeek.ConfirmPaymentMethodRequest() # ConfirmPaymentMethodRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Confirm Payment Method
        api_response = api_instance.confirm_payment_method_organizations_billing(confirm_payment_method_request, authorization=authorization)
        print("The response of OrganizationBillingApi->confirm_payment_method_organizations_billing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationBillingApi->confirm_payment_method_organizations_billing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **confirm_payment_method_request** | [**ConfirmPaymentMethodRequest**](ConfirmPaymentMethodRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**ConfirmPaymentMethodResponse**](ConfirmPaymentMethodResponse.md)

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

# **disable_auto_billing_organizations**
> AutoBillingToggleResponse disable_auto_billing_organizations(authorization=authorization)

Disable Auto Billing

Disable automatic monthly billing.

Disables automatic billing but keeps payment method saved.
Organization can re-enable later or pay invoices manually.

**Requirements:**
- Admin permission

**Example:**
```python
response = await client.post("/v1/organizations/billing/disable-auto-billing")
```

### Example


```python
import mixpeek
from mixpeek.models.auto_billing_toggle_response import AutoBillingToggleResponse
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
    api_instance = mixpeek.OrganizationBillingApi(api_client)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Disable Auto Billing
        api_response = api_instance.disable_auto_billing_organizations(authorization=authorization)
        print("The response of OrganizationBillingApi->disable_auto_billing_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationBillingApi->disable_auto_billing_organizations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**AutoBillingToggleResponse**](AutoBillingToggleResponse.md)

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

# **enable_auto_billing_organizations**
> AutoBillingToggleResponse enable_auto_billing_organizations(authorization=authorization)

Enable Auto Billing

Enable automatic monthly billing.

Re-enables automatic billing if it was previously disabled.
Payment method must already be saved.

**Requirements:**
- Admin permission
- Must have payment method saved

**Example:**
```python
response = await client.post("/v1/organizations/billing/enable-auto-billing")
```

### Example


```python
import mixpeek
from mixpeek.models.auto_billing_toggle_response import AutoBillingToggleResponse
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
    api_instance = mixpeek.OrganizationBillingApi(api_client)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Enable Auto Billing
        api_response = api_instance.enable_auto_billing_organizations(authorization=authorization)
        print("The response of OrganizationBillingApi->enable_auto_billing_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationBillingApi->enable_auto_billing_organizations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**AutoBillingToggleResponse**](AutoBillingToggleResponse.md)

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

# **get_current_usage_organizations_billing**
> CurrentUsageResponse get_current_usage_organizations_billing(authorization=authorization)

Get Current Usage

Get current month usage.

Returns credit consumption for the current billing period,
estimated cost, and next invoice date.

**Requirements:**
- Read permission

**Example:**
```python
response = await client.get("/v1/organizations/billing/usage/current")
print(f"Usage: {response['current_month_usage']} credits")
print(f"Estimated cost: ${response['estimated_cost_usd']}")
```

### Example


```python
import mixpeek
from mixpeek.models.current_usage_response import CurrentUsageResponse
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
    api_instance = mixpeek.OrganizationBillingApi(api_client)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Get Current Usage
        api_response = api_instance.get_current_usage_organizations_billing(authorization=authorization)
        print("The response of OrganizationBillingApi->get_current_usage_organizations_billing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationBillingApi->get_current_usage_organizations_billing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**CurrentUsageResponse**](CurrentUsageResponse.md)

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

# **get_payment_method_organizations_billing**
> GetPaymentMethodResponse get_payment_method_organizations_billing(authorization=authorization)

Get Payment Method

Get current payment method.

Returns the saved payment method details (last 4 digits, brand)
and auto-billing status.

**Requirements:**
- Read permission

**Example:**
```python
response = await client.get("/v1/organizations/billing/payment-method")
if response["has_payment_method"]:
    print(f"Card: {response['payment_method']['card_brand']} ****{response['payment_method']['card_last4']}")
```

### Example


```python
import mixpeek
from mixpeek.models.get_payment_method_response import GetPaymentMethodResponse
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
    api_instance = mixpeek.OrganizationBillingApi(api_client)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Get Payment Method
        api_response = api_instance.get_payment_method_organizations_billing(authorization=authorization)
        print("The response of OrganizationBillingApi->get_payment_method_organizations_billing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationBillingApi->get_payment_method_organizations_billing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**GetPaymentMethodResponse**](GetPaymentMethodResponse.md)

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

# **get_spending_caps_organizations_billing**
> SpendingCapsResponse get_spending_caps_organizations_billing(authorization=authorization)

Get Spending Caps

Get current spending cap configuration.

Returns spending cap settings including budget limits, alert thresholds,
and current spending status.

**Requirements:**
- Read permission

**Example:**
```python
response = await client.get("/v1/organizations/billing/spending-caps")
print(f"Monthly budget: ${response['monthly_spending_budget_usd']}")
print(f"Hard cap enabled: {response['hard_cap_enabled']}")
print(f"Current spending: ${response['current_spending_usd']}")
```

### Example


```python
import mixpeek
from mixpeek.models.spending_caps_response import SpendingCapsResponse
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
    api_instance = mixpeek.OrganizationBillingApi(api_client)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Get Spending Caps
        api_response = api_instance.get_spending_caps_organizations_billing(authorization=authorization)
        print("The response of OrganizationBillingApi->get_spending_caps_organizations_billing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationBillingApi->get_spending_caps_organizations_billing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**SpendingCapsResponse**](SpendingCapsResponse.md)

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

# **get_usage_breakdown_organizations_billing**
> UsageBreakdownResponse get_usage_breakdown_organizations_billing(billing_month=billing_month, authorization=authorization)

Get Usage Breakdown

Get detailed usage breakdown.

Returns usage breakdown by operation type and extractor
for the specified billing period.

**Query Parameters:**
- `billing_month`: Month to query (YYYY-MM format, defaults to current)

**Requirements:**
- Read permission

**Example:**
```python
# Current month
response = await client.get("/v1/organizations/billing/usage/breakdown")

# Specific month
response = await client.get(
    "/v1/organizations/billing/usage/breakdown",
    params={"billing_month": "2025-11"}
)
```

### Example


```python
import mixpeek
from mixpeek.models.usage_breakdown_response import UsageBreakdownResponse
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
    api_instance = mixpeek.OrganizationBillingApi(api_client)
    billing_month = 'billing_month_example' # str | Billing month in YYYY-MM format (defaults to current month) (optional)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Get Usage Breakdown
        api_response = api_instance.get_usage_breakdown_organizations_billing(billing_month=billing_month, authorization=authorization)
        print("The response of OrganizationBillingApi->get_usage_breakdown_organizations_billing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationBillingApi->get_usage_breakdown_organizations_billing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_month** | **str**| Billing month in YYYY-MM format (defaults to current month) | [optional] 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**UsageBreakdownResponse**](UsageBreakdownResponse.md)

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

# **list_invoices_organizations_billing**
> InvoiceListResponse list_invoices_organizations_billing(limit=limit, authorization=authorization)

List Invoices

List monthly invoices.

Returns paginated list of monthly invoices with links to
Stripe-hosted invoice pages.

**Query Parameters:**
- `limit`: Number of invoices (1-100, default 10)

**Requirements:**
- Read permission

**Example:**
```python
response = await client.get("/v1/organizations/billing/invoices?limit=10")
for invoice in response["invoices"]:
    print(f"{invoice['billing_month']}: ${invoice['amount_paid']/100}")
```

### Example


```python
import mixpeek
from mixpeek.models.invoice_list_response import InvoiceListResponse
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
    api_instance = mixpeek.OrganizationBillingApi(api_client)
    limit = 10 # int | Number of invoices to return (optional) (default to 10)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # List Invoices
        api_response = api_instance.list_invoices_organizations_billing(limit=limit, authorization=authorization)
        print("The response of OrganizationBillingApi->list_invoices_organizations_billing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationBillingApi->list_invoices_organizations_billing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of invoices to return | [optional] [default to 10]
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**InvoiceListResponse**](InvoiceListResponse.md)

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

# **setup_payment_method_organizations_billing**
> SetupPaymentMethodResponse setup_payment_method_organizations_billing(authorization=authorization)

Setup Payment Method

Initialize payment method setup flow.

Creates a Stripe SetupIntent for collecting payment method without charging.
The client_secret should be used with Stripe Elements on the frontend.

**Flow:**
1. Frontend calls this endpoint
2. Backend creates Stripe Customer (if needed) and SetupIntent
3. Frontend uses client_secret with Stripe Elements
4. User enters card details
5. Frontend calls confirm-payment-method endpoint

**Requirements:**
- Admin permission (only org admins can set up payment methods)

**Example:**
```python
response = await client.post("/v1/organizations/billing/setup-payment-method")
client_secret = response["client_secret"]
# Use client_secret with Stripe Elements
```

### Example


```python
import mixpeek
from mixpeek.models.setup_payment_method_response import SetupPaymentMethodResponse
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
    api_instance = mixpeek.OrganizationBillingApi(api_client)
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Setup Payment Method
        api_response = api_instance.setup_payment_method_organizations_billing(authorization=authorization)
        print("The response of OrganizationBillingApi->setup_payment_method_organizations_billing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationBillingApi->setup_payment_method_organizations_billing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**SetupPaymentMethodResponse**](SetupPaymentMethodResponse.md)

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

# **update_spending_caps_organizations_billing**
> SpendingCapsResponse update_spending_caps_organizations_billing(update_spending_caps_request, authorization=authorization)

Update Spending Caps

Update spending cap configuration.

Configure spending limits and alert thresholds to control costs.

**Features:**
- **Soft Limit (Budget)**: Triggers alerts but doesn't block API access
- **Hard Cap**: Blocks API access when reached (requires explicit enable)
- **Alert Thresholds**: Customize when to receive spending notifications

**Requirements:**
- Admin permission
- Only applies to organizations with auto-billing enabled

**Example:**
```python
# Set $100 budget with alerts at 75% and 100%
response = await client.post(
    "/v1/organizations/billing/spending-caps",
    json={
        "monthly_spending_budget": 10000,  # $100 in cents
        "spending_alert_thresholds": [75, 100],
        "spending_alerts_enabled": True,
    }
)

# Enable hard cap at $500
response = await client.post(
    "/v1/organizations/billing/spending-caps",
    json={
        "hard_spending_cap": 50000,  # $500 in cents
        "hard_cap_enabled": True,
    }
)

# Disable all spending limits
response = await client.post(
    "/v1/organizations/billing/spending-caps",
    json={
        "monthly_spending_budget": None,
        "hard_spending_cap": None,
        "hard_cap_enabled": False,
    }
)
```

### Example


```python
import mixpeek
from mixpeek.models.spending_caps_response import SpendingCapsResponse
from mixpeek.models.update_spending_caps_request import UpdateSpendingCapsRequest
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
    api_instance = mixpeek.OrganizationBillingApi(api_client)
    update_spending_caps_request = mixpeek.UpdateSpendingCapsRequest() # UpdateSpendingCapsRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)

    try:
        # Update Spending Caps
        api_response = api_instance.update_spending_caps_organizations_billing(update_spending_caps_request, authorization=authorization)
        print("The response of OrganizationBillingApi->update_spending_caps_organizations_billing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationBillingApi->update_spending_caps_organizations_billing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_spending_caps_request** | [**UpdateSpendingCapsRequest**](UpdateSpendingCapsRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 

### Return type

[**SpendingCapsResponse**](SpendingCapsResponse.md)

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

