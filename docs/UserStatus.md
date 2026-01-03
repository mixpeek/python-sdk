# UserStatus

Lifecycle state of an organization user.  Status values control whether a user can authenticate and access resources:  - ACTIVE: User is fully operational and can authenticate with their API keys. - SUSPENDED: User access is temporarily disabled. API keys will not work but   account data is preserved. Can be reactivated by an admin. - PENDING: User invitation has been created but not yet accepted. User cannot   authenticate until they complete the onboarding flow.

## Enum

* `ACTIVE` (value: `'active'`)

* `SUSPENDED` (value: `'suspended'`)

* `PENDING` (value: `'pending'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


