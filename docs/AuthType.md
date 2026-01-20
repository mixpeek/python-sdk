# AuthType

Authentication type for API calls.  Defines how credentials from the organization secrets vault should be injected into HTTP requests for authentication with external APIs.  Values:     NONE: No authentication (public APIs)      API_KEY: API key in header or query parameter         - Use for APIs that require API keys (Weather API, Maps, etc.)         - Header location recommended for security         - Requires: secret_ref, key, location         - Example: X-API-Key: abc123      BEARER: Bearer token authentication (OAuth 2.0, JWT)         - Use for APIs using Bearer tokens (GitHub, OpenAI, most modern APIs)         - Adds: Authorization: Bearer {secret_value}         - Requires: secret_ref         - Example: Authorization: Bearer ghp_abc123      BASIC: HTTP Basic authentication         - Use for APIs using Basic Auth (legacy systems)         - Secret format: \"username:password\"         - Adds: Authorization: Basic {base64(username:password)}         - Requires: secret_ref         - Example: Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=      CUSTOM_HEADER: Custom header with arbitrary name         - Use for APIs with non-standard auth headers         - Adds: {key}: {secret_value}         - Requires: secret_ref, key         - Example: X-Custom-Auth: token123  Examples:     - Bearer token for GitHub API: type=\"bearer\"     - API key for Weather API: type=\"api_key\", location=\"query\"     - Basic auth for legacy API: type=\"basic\"     - Custom header: type=\"custom_header\", key=\"X-Custom-Token\"

## Enum

* `NONE` (value: `'none'`)

* `API_KEY` (value: `'api_key'`)

* `BEARER` (value: `'bearer'`)

* `BASIC` (value: `'basic'`)

* `CUSTOM_HEADER` (value: `'custom_header'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


