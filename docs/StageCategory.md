# StageCategory

Retriever stage categories organized by transformation pattern.  Values:     FILTER: Subset of input documents (N → ≤N, same schema)         - Removes documents that don't match criteria         - Examples: attribute_filter, feature_filter, llm_filter         - Use for: Removing irrelevant results, applying business rules         - Performance: Fast (attribute) to slow (LLM)      SORT: Reorders documents (N → N, same schema, different order)         - Changes document ordering based on criteria         - Examples: sort_relevance, sort_attribute         - Use for: Ordering by relevance, recency, custom fields         - Performance: Fast (in-memory sort)      REDUCE: Aggregates to summary (N → 1, new schema)         - Combines multiple documents into one summary         - Examples: aggregate_stats, group_by         - Use for: Summaries, statistics, reports         - Performance: Varies by aggregation logic      APPLY: Enrichment or expansion (N → N or N*M)         - 1-1: Enriches each doc (N → N, expanded schema)         - 1-N: Expands each doc (N → N*M, new/same schema)         - Examples: document_enrich, taxonomy_enrich, llm_enrich         - Use for: Adding related data, tagging, recursive lookups         - Performance: Moderate (DB) to slow (LLM)      ENRICH: Document enrichment (N → N, potentially expanded schema)         - Adds computed fields to each document         - Examples: code_execution, llm_enrich, taxonomy_enrich         - Use for: Custom transformations, data extraction, LLM processing         - Performance: Varies (fast for code, slow for LLM)  Pipeline Patterns:     - Basic: FILTER → SORT     - Enriched: FILTER → SORT → APPLY     - Tag expansion: FILTER → APPLY (1-N)     - Summary: FILTER → SORT → REDUCE

## Enum

* `FILTER` (value: `'filter'`)

* `SORT` (value: `'sort'`)

* `REDUCE` (value: `'reduce'`)

* `APPLY` (value: `'apply'`)

* `ENRICH` (value: `'enrich'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


