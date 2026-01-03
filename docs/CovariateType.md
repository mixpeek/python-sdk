# CovariateType

Type of covariate/predictor variable for conversion analysis.  Different types enable different analysis strategies: - CATEGORICAL: String values, analyzed via grouping (e.g., sender_domain, priority) - NUMERIC: Continuous values, binned into quartiles/deciles (e.g., word_count, price) - EMBEDDING: Dense vectors, clustered for semantic analysis (e.g., CLIP embeddings) - CLUSTER_ID: Pre-computed cluster identifiers (e.g., topic_cluster, visual_cluster)  Examples:     ```python     # Categorical: Which email domains convert better?     CovariateConfig(field_path=\"sender_domain\", covariate_type=\"categorical\")      # Numeric: Do longer emails convert faster?     CovariateConfig(field_path=\"word_count\", covariate_type=\"numeric\")      # Embedding: Do visually similar images follow similar paths?     CovariateConfig(field_path=\"features.clip\", covariate_type=\"embedding\")      # Cluster: Which topic clusters have highest conversion?     CovariateConfig(field_path=\"metadata.topic_id\", covariate_type=\"cluster_id\")     ```

## Enum

* `CATEGORICAL` (value: `'categorical'`)

* `NUMERIC` (value: `'numeric'`)

* `EMBEDDING` (value: `'embedding'`)

* `CLUSTER_ID` (value: `'cluster_id'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


