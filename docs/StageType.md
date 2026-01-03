# StageType

Categorisation of stage behaviour within a retrieval flow.  These functional categories describe how stages transform the document stream:  - FILTER: N → ≤N documents (subset, same schema) - SORT: N → N documents (same docs, different order, same schema) - REDUCE: N → 1 document (aggregation, new schema) - APPLY: N → N or N*M documents (enrichment/expansion, expanded/new schema) - ENRICH: N → N documents (enrichment with computed fields)

## Enum

* `FILTER` (value: `'filter'`)

* `SORT` (value: `'sort'`)

* `REDUCE` (value: `'reduce'`)

* `APPLY` (value: `'apply'`)

* `ENRICH` (value: `'enrich'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


