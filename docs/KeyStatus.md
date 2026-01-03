# KeyStatus

Lifecycle state of an API key.  Status determines whether an API key can be used for authentication:  - ACTIVE: Key is valid and can be used for API requests. Last_used_at timestamp   is updated on each successful authentication. - REVOKED: Key has been manually revoked by an admin or user. Cannot be   reactivated. A new key must be created instead. - EXPIRED: Key has passed its expires_at timestamp. Automatically set by the   authentication system. Cannot be reactivated.

## Enum

* `ACTIVE` (value: `'active'`)

* `REVOKED` (value: `'revoked'`)

* `EXPIRED` (value: `'expired'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


