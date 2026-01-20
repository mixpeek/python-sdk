# StageParamsApiCall

Configuration for API call enrichment stage.  **Stage Category**: ENRICH (1-1 Enrichment)  **⚠️ CRITICAL SECURITY WARNINGS ⚠️**:  1. **SSRF Risk**: This stage makes external HTTP requests which can be exploited    for Server-Side Request Forgery attacks. ALWAYS use `allowed_domains` allowlist.  2. **Data Exfiltration**: Malicious configurations could send internal data to    external endpoints. Audit all configurations before deployment.  3. **Credential Safety**: NEVER store credentials directly in configuration.    Always use `auth.secret_ref` to reference vault-stored credentials.  4. **Rate Limiting**: Set rate limits to prevent abuse and excessive costs.  5. **Domain Allowlist**: REQUIRED. Explicitly list allowed domains. Never use \"*\".  **Transformation**: N documents → N documents (same count, expanded schema)  **Purpose**: Enriches documents by calling external HTTP APIs. Enables integration with third-party services (Stripe, GitHub, weather APIs, etc.) to augment documents with real-time data. Due to security risks, this stage implements strict controls including domain allowlisting, SSRF protection, rate limiting, and secure credential management.  **When to Use**:     - Enrich documents with data from external APIs     - Integrate third-party services (Stripe, GitHub, Salesforce)     - Fetch real-time data (weather, stocks, currency rates)     - Validate data against external systems     - Lookup additional context from APIs  **When NOT to Use**:     - For untrusted/user-provided URLs (major security risk)     - When API credentials can't be securely stored     - For high-volume enrichment (rate limits apply)     - When response time is critical (network latency)     - For internal-only APIs behind firewalls  Requirements:     - url: REQUIRED, API endpoint URL (supports templates)     - allowed_domains: REQUIRED, domain allowlist (NEVER use \"*\")     - method: OPTIONAL, HTTP method (default: GET)     - auth: OPTIONAL, authentication configuration     - headers: OPTIONAL, additional headers     - body: OPTIONAL, request body (for POST/PUT)     - output_field: REQUIRED, where to store response     - timeout: OPTIONAL, request timeout (default: 10s)     - max_response_size: OPTIONAL, max response size (default: 10MB)     - when: OPTIONAL, conditional enrichment filter     - on_error: OPTIONAL, error handling (skip/remove/raise)  Use Cases:     - Stripe customer lookup: Enrich with billing data     - GitHub repo info: Fetch commit stats     - Weather API: Add location-based weather     - Currency conversion: Real-time exchange rates     - Address validation: Verify and standardize addresses

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | API endpoint URL to call. Supports template variables: {INPUT.field}, {DOC.field}. Must be HTTP/HTTPS. Domain must be in allowed_domains list. Default uses httpbin.org for testing. Examples: &#39;https://api.stripe.com/v1/customers/{DOC.metadata.customer_id}&#39; | [optional] [default to 'https://httpbin.org/get']
**allowed_domains** | **List[str]** | Allowlist of domains that can be called. CRITICAL FOR SECURITY - prevents SSRF attacks. Supports wildcards: &#39;*.example.com&#39; matches subdomains. NEVER use &#39;*&#39; (all domains) in production. Default allows httpbin.org for testing. Examples: [&#39;api.stripe.com&#39;, &#39;*.github.com&#39;, &#39;api.weatherapi.com&#39;] | [optional] [default to ["httpbin.org"]]
**method** | **str** | HTTP method: GET, POST, PUT, PATCH, DELETE. Default: GET. | [optional] [default to 'GET']
**auth** | [**AuthConfig**](AuthConfig.md) | OPTIONAL. Authentication configuration. Uses organization vault for credential storage. See AuthConfig for details. | [optional] 
**headers** | **Dict[str, str]** | OPTIONAL. Additional HTTP headers to include. Do NOT include authentication headers here - use &#39;auth&#39; field. Supports template variables in values. Example: {&#39;Content-Type&#39;: &#39;application/json&#39;, &#39;X-Custom&#39;: &#39;{{INPUT.value}}&#39;} | [optional] 
**body** | **object** | OPTIONAL. Request body (for POST/PUT/PATCH). Serialized as JSON. Supports template variables in values. Only used for non-GET requests. | [optional] 
**output_field** | **str** | Dot-path where API response should be stored. Creates nested structure if needed. Response stored as-is (JSON object/array/primitive). Example: &#39;metadata.api_data&#39; | [optional] [default to 'metadata.api_response']
**timeout** | **int** | Request timeout in seconds. Range: 1-60. Default: 10. | [optional] [default to 10]
**max_response_size** | **int** | Maximum response size in bytes. Prevents memory exhaustion. Default: 10MB. | [optional] [default to 10485760]
**rate_limit** | [**RateLimitConfig**](RateLimitConfig.md) | OPTIONAL. Rate limiting configuration per domain. | [optional] 
**response_path** | **str** | OPTIONAL. JSONPath expression to extract specific field from response. If not specified, stores entire response. Examples: &#39;$.data&#39;, &#39;$.results[0]&#39;, &#39;$.customer.email&#39; | [optional] [default to 'null']
**when** | [**LogicalOperator**](LogicalOperator.md) | OPTIONAL. Conditional filter for selective enrichment. Only documents matching condition will call API. RECOMMENDED for cost/performance optimization. | [optional] 
**on_error** | [**ErrorHandling**](ErrorHandling.md) | Error handling strategy: &#39;skip&#39;: Pass document through unchanged. &#39;remove&#39;: Remove failed documents. &#39;raise&#39;: Halt pipeline on error. Default: &#39;skip&#39;. | [optional] 

## Example

```python
from mixpeek.models.stage_params_api_call import StageParamsApiCall

# TODO update the JSON string below
json = "{}"
# create an instance of StageParamsApiCall from a JSON string
stage_params_api_call_instance = StageParamsApiCall.from_json(json)
# print the JSON string representation of the object
print(StageParamsApiCall.to_json())

# convert the object into a dict
stage_params_api_call_dict = stage_params_api_call_instance.to_dict()
# create an instance of StageParamsApiCall from a dict
stage_params_api_call_from_dict = StageParamsApiCall.from_dict(stage_params_api_call_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


