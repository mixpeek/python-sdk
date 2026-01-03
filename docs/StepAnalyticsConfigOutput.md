# StepAnalyticsConfigOutput

Configuration for step-by-step transition analytics on taxonomy assignments.  Enables analysis of how documents progress through taxonomy labels as a temporal sequence, answering questions like: - How long from \"inquiry\" to \"closed_won\"? - What % of \"inquiry\" emails reach \"proposal\"? - Which sender domains correlate with faster progression?  Use Cases:     1. Email Thread Analysis:        - Track progression: inquiry → followup → proposal → closed_won        - Identify which subject lines correlate with faster closure      2. Content Workflow Tracking:        - Monitor: draft → review → approved → published        - Find bottlenecks and optimization opportunities      3. Safety Compliance Monitoring:        - Trace: violation_detected → investigated → resolved        - Track resolution times and success rates  Attributes:     timestamp_field: Document field containing event timestamp     sequence_id_field: Field that groups related documents into sequences     step_key_source: How to extract the step identifier (label/node_id/custom field)     step_key_field_path: Required if step_key_source='field_path'     covariates: List of predictor variables to analyze for conversion lift     max_sequence_duration_days: Filter out sequences longer than this (data quality)  Example:     ```python     # Email thread analysis configuration     StepAnalyticsConfig(         timestamp_field=\"Date\",  # Email timestamp         sequence_id_field=\"Thread-Index\",  # Groups emails in same thread         step_key_source=\"assignment_label\",  # Use taxonomy label as step         covariates=[             CovariateConfig(                 field_path=\"sender_domain\",                 covariate_type=\"categorical\",                 name=\"Sender Domain\"             ),             CovariateConfig(                 field_path=\"word_count\",                 covariate_type=\"numeric\",                 name=\"Email Length\"             )         ],         max_sequence_duration_days=90  # Ignore threads >90 days     )     ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp_field** | **str** | Document field containing event timestamp (e.g., &#39;Date&#39;, &#39;created_at&#39;, &#39;metadata.timestamp&#39;) | 
**sequence_id_field** | **str** | Document field that groups related items into a sequence (e.g., &#39;Thread-Index&#39;, &#39;session_id&#39;, &#39;user_id&#39;) | 
**step_key_source** | [**StepKeySource**](StepKeySource.md) | How to determine the &#39;step&#39; for each document (label, node_id, or custom field) | [optional] 
**step_key_field_path** | **str** | Required if step_key_source&#x3D;&#39;field_path&#39;. Dot-notation path to step value in document. | [optional] 
**covariates** | [**List[CovariateConfig]**](CovariateConfig.md) | Predictor fields to analyze for conversion lift (categorical, numeric, embedding, cluster) | [optional] 
**max_sequence_duration_days** | **int** | Maximum allowed duration for a sequence. Sequences beyond this are flagged as data quality issues. | [optional] 

## Example

```python
from mixpeek.models.step_analytics_config_output import StepAnalyticsConfigOutput

# TODO update the JSON string below
json = "{}"
# create an instance of StepAnalyticsConfigOutput from a JSON string
step_analytics_config_output_instance = StepAnalyticsConfigOutput.from_json(json)
# print the JSON string representation of the object
print(StepAnalyticsConfigOutput.to_json())

# convert the object into a dict
step_analytics_config_output_dict = step_analytics_config_output_instance.to_dict()
# create an instance of StepAnalyticsConfigOutput from a dict
step_analytics_config_output_from_dict = StepAnalyticsConfigOutput.from_dict(step_analytics_config_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


