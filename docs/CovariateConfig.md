# CovariateConfig

Configuration for a single covariate/predictor variable in step analytics.  Covariates are used to identify which features predict conversion from one step to another. The system computes \"lift\" for each covariate value, showing whether it increases or decreases conversion likelihood.  Attributes:     field_path: JSONPath to the field in document or metadata (e.g., \"sender_domain\")     covariate_type: How to analyze this covariate (categorical, numeric, embedding, cluster)     name: Human-readable name for analytics results     binning_strategy: For NUMERIC types, how to bin values (quartiles, deciles)     clustering_method: For EMBEDDING types, algorithm to use (kmeans, hdbscan)     n_clusters: For EMBEDDING types, number of clusters to create  Examples:     ```python     # Analyze sender domains (categorical)     CovariateConfig(         field_path=\"sender_domain\",         covariate_type=\"categorical\",         name=\"Email Domain\"     )      # Analyze email length (numeric with quartile binning)     CovariateConfig(         field_path=\"word_count\",         covariate_type=\"numeric\",         name=\"Word Count\",         binning_strategy=\"quartiles\"     )      # Analyze visual similarity (embedding clustering)     CovariateConfig(         field_path=\"features.clip_embedding\",         covariate_type=\"embedding\",         name=\"Visual Cluster\",         clustering_method=\"kmeans\",         n_clusters=10     )     ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_path** | **str** | Dot-notation path to covariate field (e.g., &#39;sender_domain&#39;, &#39;metadata.priority&#39;) | 
**covariate_type** | [**CovariateType**](CovariateType.md) | Type of covariate determines analysis strategy (categorical/numeric/embedding/cluster) | 
**name** | **str** | Human-readable name for this covariate in analytics results | 
**binning_strategy** | **str** | How to bin numeric values for lift analysis (only used for NUMERIC type) | [optional] [default to 'quartiles']
**clustering_method** | **str** | Clustering algorithm for embedding analysis (only used for EMBEDDING type) | [optional] [default to 'kmeans']
**n_clusters** | **int** | Number of clusters for embedding-based predictors (only used for EMBEDDING type) | [optional] [default to 10]

## Example

```python
from mixpeek.models.covariate_config import CovariateConfig

# TODO update the JSON string below
json = "{}"
# create an instance of CovariateConfig from a JSON string
covariate_config_instance = CovariateConfig.from_json(json)
# print the JSON string representation of the object
print(CovariateConfig.to_json())

# convert the object into a dict
covariate_config_dict = covariate_config_instance.to_dict()
# create an instance of CovariateConfig from a dict
covariate_config_from_dict = CovariateConfig.from_dict(covariate_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


