# Permission

Simplified API key permissions.  This four-value enum replaces the legacy 16-permission model. Keep usage simple: prefer the least privileged option that satisfies the workflow.  Hierarchy (strongest -> weakest): ADMIN > DELETE > WRITE > READ.

## Enum

* `READ` (value: `'read'`)

* `WRITE` (value: `'write'`)

* `DELETE` (value: `'delete'`)

* `ADMIN` (value: `'admin'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


