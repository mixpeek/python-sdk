# AuthConfig

Authentication configuration for API calls.  Defines how to authenticate with external APIs using credentials stored in the organization secrets vault. Credentials are NEVER stored in the stage configuration - only references to vault secrets.  **⚠️ CRITICAL SECURITY WARNINGS**: - NEVER store actual credentials in configuration - ALWAYS use secret_ref to reference vault secrets - Credentials are encrypted at rest in vault - Decrypted values never appear in logs or API responses  **How It Works**: 1. Store secret via: POST /v1/organizations/secrets 2. Reference secret via: auth.secret_ref in stage config 3. At runtime: Secret is retrieved, decrypted, and injected into request 4. Security: Original secret value never exposed or logged  **Requirements**: - type: REQUIRED, authentication method (none, api_key, bearer, basic, custom_header) - secret_ref: REQUIRED (except for type=none), name of secret in vault - key: REQUIRED (for api_key and custom_header types), header/query param name - location: OPTIONAL (for api_key type), 'header' or 'query' (default: header)  **Supported Authentication Types**: - Bearer tokens (OAuth 2.0, JWT): Most modern APIs - API keys: Weather APIs, Maps, etc. - Basic auth: Legacy systems - Custom headers: Non-standard auth schemes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**AuthType**](AuthType.md) | REQUIRED. Authentication method to use. Options: none (public API), api_key (API keys), bearer (OAuth/JWT), basic (HTTP Basic Auth), custom_header (non-standard headers). See AuthType enum for detailed description of each type. | [optional] 
**secret_ref** | **str** | REQUIRED (except for type&#x3D;none). Name of secret in organization vault. The secret must be created first via POST /v1/organizations/secrets. Format: Use the exact secret_name from vault (e.g., &#39;stripe_api_key&#39;). At runtime, the secret value is securely retrieved and decrypted. The decrypted value is then injected into the request per auth type. SECURITY: NEVER store actual credentials here - only the reference name. Examples: &#39;stripe_api_key&#39;, &#39;github_pat&#39;, &#39;weather_api_key&#39; | [optional] 
**location** | **str** | OPTIONAL (for api_key type only). Where to inject the API key. Options: &#39;header&#39; (recommended, more secure) or &#39;query&#39; (less secure). Default: &#39;header&#39; if not specified. Query parameters appear in URLs and logs - use headers when possible. Ignored for other auth types (bearer, basic, custom_header). | [optional] 
**key** | **str** | REQUIRED (for api_key and custom_header types). Header name or query parameter name for authentication. For api_key with location&#x3D;header: Header name like &#39;X-API-Key&#39;, &#39;Authorization&#39;. For api_key with location&#x3D;query: Query param like &#39;apikey&#39;, &#39;api_key&#39;, &#39;key&#39;. For custom_header: Any custom header name like &#39;X-Custom-Auth&#39;, &#39;X-Token&#39;. Ignored for bearer and basic types (use standard headers). Common patterns: &#39;X-API-Key&#39;, &#39;Authorization&#39;, &#39;X-Auth-Token&#39; | [optional] 

## Example

```python
from mixpeek.models.auth_config import AuthConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AuthConfig from a JSON string
auth_config_instance = AuthConfig.from_json(json)
# print the JSON string representation of the object
print(AuthConfig.to_json())

# convert the object into a dict
auth_config_dict = auth_config_instance.to_dict()
# create an instance of AuthConfig from a dict
auth_config_from_dict = AuthConfig.from_dict(auth_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


