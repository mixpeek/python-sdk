# APIKeyType

Type of API key determining its purpose and scope.  - STANDARD: Regular organization API key with standard permissions. - MARKETPLACE_SUBSCRIPTION: Special key generated for marketplace subscriptions,   allowing cross-org access to specific marketplace retrievers. - RETRIEVER: Per-retriever API key scoped to execute a specific retriever.   Only the retriever owner can create these keys. Prefix: ret_sk_

## Enum

* `STANDARD` (value: `'standard'`)

* `MARKETPLACE_SUBSCRIPTION` (value: `'marketplace_subscription'`)

* `RETRIEVER` (value: `'retriever'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


